# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
import threading
import time
from collections import deque
from typing import Callable, Type, Deque, Optional
from netrc import netrc, NetrcParseError  # メインスレッド以外でimportするとデッドロックするらしい https://github.com/kennethreitz/requests/issues/2925

import websocket

from ..core.exception import *
from ..core.model import *
from ..core.util import timeout


def _parse_response(
        status: str,
        response: Dict[str, Any],
):
    import simplejson as json
    try:
        if status == 200:
            return response
        elif status == 400:
            raise BadRequestException(json.dumps(response))
        elif status == 401:
            raise UnauthorizedException(json.dumps(response))
        elif status == 402:
            raise QuotaExceedException(json.dumps(response))
        elif status == 404:
            raise NotFoundException(json.dumps(response))
        elif status == 409:
            raise ConflictException(json.dumps(response))
        elif status == 500:
            raise InternalServerErrorException(json.dumps(response))
        elif status == 502:
            raise BadGatewayException(json.dumps(response))
        elif status == 503:
            raise ServiceUnavailableException(json.dumps(response))
        elif status == 504:
            raise RequestTimeoutException(json.dumps(response))
        else:
            raise UnknownException(json.dumps(response))
    except KeyError:
        raise UnknownException(json.dumps(response))


class NetworkJob:

    def __init__(
            self,
            request_id: str,
            result_type: Type[T],
            callback: Callable[[AsyncResult[T]], None],
            body: Dict[str, Any] = None,
    ):
        if body is None:
            body = {}

        self._request_id = request_id
        self._result_type = result_type
        self._callback = callback
        self._body = body

    @property
    def request_id(self) -> str:
        return self._request_id

    @property
    def result_type(self) -> Type[T]:
        return self._result_type

    @property
    def callback(self) -> Callable[[T], None]:
        return self._callback

    @property
    def body(self) -> Dict[str, Any]:
        return self._body


class Gs2WebSocketSession(ISession):

    def __init__(
            self,
            credential: IGs2Credential,
            region: str,
            steady_endpoint: Optional[str] = None,
    ):
        """
        コンストラクタ
        :param credential: クレデンシャル
        :param region: クレデンシャル
        :param steady_endpoint: Steady（専用フリート）の基点（https://<host>）。None なら共有クラウド（接続先は従来どおり）。
            設定すると接続先は wss://<host>/（基点が http:// なら ws://）になり、handshake に上限が付く
        """
        super().__init__()
        self._credential = credential
        self._project_token = None
        self._region = region
        self._connection = None
        # _job_queue は応答待ちの要求。★送信（呼び出し側のスレッド）と受信（run_forever のスレッド）の
        # 両方から触るので _lock で守り、応答が来たもの・接続が切れたものは必ず取り除く。
        self._job_queue = deque()
        # ★_lock は _job_queue と _connection を守る。コールバックは錠を手放してから呼ぶ
        # （コールバックは connect() 等でこのセッションへ入り直すので、持ったまま呼ぶと固まる）。
        self._lock = threading.RLock()
        # ★受信スレッド（run_forever）。接続が切れたら必ず抜ける。
        self._receive_thread = None
        self._steady_endpoint = normalize_steady_endpoint(steady_endpoint) or None

    @property
    def credential(self) -> IGs2Credential:
        return self._credential

    @property
    def project_token(self) -> str:
        return self._project_token

    @property
    def region(self) -> str:
        return self._region

    @property
    def connection(self) -> websocket.WebSocketApp:
        return self._connection

    @property
    def steady_endpoint(self) -> Optional[str]:
        """
        Steady（専用フリート）の基点（https://<host>）。未設定なら None。
        """
        return self._steady_endpoint

    @steady_endpoint.setter
    def steady_endpoint(self, value: Optional[str]):
        self._steady_endpoint = normalize_steady_endpoint(value) or None

    def _web_socket_url(self) -> str:
        """
        接続先。優先順: steady_endpoint（wss://<host>/）＞ Gs2Constant.WS_ENDPOINT_HOST。
        steady_endpoint が未設定なら従来と byte 単位で同じ文字列。
        """
        url = steady_web_socket_url(self._steady_endpoint)
        if url:
            return url
        return Gs2Constant.WS_ENDPOINT_HOST.format(
            region=self.region,
        )

    def _take_job(self, request_id: str) -> Optional[NetworkJob]:
        """
        request_id の要求を応答待ちの行列から外して返す（無ければ None）。
        ★同じ要求に二度コールバックしないための唯一の出口。
        """
        with self._lock:
            for job in self._job_queue:
                if job.request_id == request_id:
                    self._job_queue.remove(job)
                    return job
        return None

    def _drop_connection(self, connection, cause=None):
        """
        切れた接続を捨て、応答待ちの要求すべてに BrokenPipeError を返す。

        ★サーバーが応答を返さずに接続を閉じること（gateway の setUserId が自分自身の接続を切る形、
        ノードの停止、ネットワーク断）があるので、閉じたと分かった時点で待ち中の呼び出しを
        必ず終わらせる。以前は誰も終わらせず、同期呼び出しが返らなかった。
        ★既に別の接続へ差し替わっていたら（disconnect → connect の後）何もしない。
        """
        with self._lock:
            if connection is not None and self._connection is not None and self._connection is not connection:
                return
            current = self._connection if self._connection is not None else connection
            self._connection = None
            self._project_token = None
            jobs = list(self._job_queue)
            self._job_queue.clear()

        if current is not None:
            try:
                current.close()
            except Exception:
                pass

        # ★コールバックは錠の外で呼ぶ。
        for job in jobs:
            try:
                job.callback(
                    AsyncResult(
                        error=BrokenPipeError(
                            'websocket connection closed before the response arrived{}'.format(
                                '' if cause is None else ': {}'.format(cause),
                            )
                        ),
                    )
                )
            except Exception:
                pass

    def send(self, job: NetworkJob):
        import simplejson as json
        with self._lock:
            connection = self._connection
            if not connection:
                # ★切れた後の送信はその場で失敗させる（待たせない）。
                raise BrokenPipeError('websocket connection is not available')
            self._job_queue.append(job)

        try:
            payload = json.dumps(job.body)
        except Exception:
            self._take_job(job.request_id)
            raise

        try:
            # ★websocket-client の送信は enable_multithread=True で直列化されているので、ここで
            # 錠を持つ必要はない（持ったまま書くと受信側の切断処理まで止まる）。
            connection.send(payload)
        except Exception as e:
            # ★書けなかった要求は届いていない。待ち行列から外し、繋ぎ直しも再送もしない。
            # 以前はここで connect() して再送していたので、同じ要求が二度届きうる上、繋ぎ直しの
            # ログイン待ち（最大 30 秒）の間、呼び出しが止まっていた。
            self._take_job(job.request_id)
            if isinstance(e, (websocket._exceptions.WebSocketConnectionClosedException, OSError)):
                self._drop_connection(connection, e)
                raise BrokenPipeError('failed to send over websocket: {}'.format(e))
            raise

    def on_notification(self, message):
        pass

    def _connect(
            self,
            callback: Callable[[AsyncResult[LoginResult]], None],
    ):
        try:
            if not self._connection:
                import uuid
                import time
                import simplejson as json

                opened = []
                closed = []
                def on_message(ws, message):
                    response = json.loads(message)
                    request_id = response.get('requestId')
                    if request_id is None:
                        self.on_notification(
                            response.get('body')
                        )
                    else:
                        # ★行列から外してから呼ぶ（外すのは _take_job だけ。二重コールバックを作らない）。
                        target_job = self._take_job(request_id)
                        if target_job is not None:
                            try:
                                status = response.get('status')
                                result = response.get('body')
                                target_job.callback(
                                    AsyncResult(
                                        result=target_job.result_type.from_dict(_parse_response(status, result)),
                                    )
                                )
                            except Gs2Exception as e:
                                target_job.callback(
                                    AsyncResult(
                                        error=e,
                                    )
                                )

                def on_error(ws, error):
                    # ★読み書きの誤り（Close フレーム無しの切断を含む）。接続を捨て、待ち中の要求
                    # すべてに誤りを返す。run_forever はこの後 teardown して抜ける。
                    self._drop_connection(ws, error)

                def on_open(ws):
                    opened.append(True)

                def on_close(ws, *args):
                    closed.append(True)
                    # ★サーバーが応答を返さずに閉じた場合もここに来る。待ち中の要求を終わらせる。
                    self._drop_connection(ws, 'closed by peer {}'.format(args) if args else 'closed by peer')

                websocket.enableTrace(False)
                connection = websocket.WebSocketApp(
                    self._web_socket_url(),
                    on_message=on_message,
                    on_error=on_error,
                    on_open=on_open,
                    on_close=on_close,
                )
                self._connection = connection

                # ★受信は run_forever に任せる。接続が切れると run_forever は on_error / on_close を
                # 呼んでから戻るので、このスレッドはそこで終わる（残らない）。スレッドを名前付きで
                # 持つのは、終わったことを確かめられるようにするため。
                def run():
                    connection.run_forever(ping_interval=10)

                self._receive_thread = threading.Thread(
                    target=run,
                    name='gs2-websocket-receive',
                    daemon=True,
                )
                self._receive_thread.start()

                # ★Steady のときだけ handshake の待ちを有界にする（基点はフリートのノードへ直接
                # 解決されるので、手放された公開 IP に当たると open も close も来ず固まる）。
                # 共有クラウドは従来どおり connect() 側の 30 秒に任せる。繋ぎ直しは入れない。
                connect_timeout = None
                if normalize_steady_endpoint(self._steady_endpoint):
                    connect_timeout = Gs2Constant.STEADY_CONNECT_TIMEOUT

                started = time.time()
                while not opened and self._connection:
                    if connect_timeout is not None and (closed or time.time() - started > connect_timeout):
                        break
                    time.sleep(0.1)

                if connect_timeout is not None and not opened:
                    # 開けなかった: 接続を畳んで誤りを返す（別の経路へ繋ぎ直すことはしない）
                    failed = self._connection
                    self._connection = None
                    if failed is not None:
                        try:
                            failed.close()
                        except Exception:
                            pass
                    raise ConnectionError(
                        'failed to connect to {} within {} seconds'.format(
                            self._web_socket_url(),
                            connect_timeout,
                        )
                    )

                if isinstance(self.credential, ProjectTokenGs2Credential):
                    self._project_token = self.credential.project_token
                    callback(
                        AsyncResult(
                        )
                    )
                else:
                    request_id = str(uuid.uuid4())
                    body = {
                        'client_id': self._credential.client_id,
                        'client_secret': self._credential.client_secret,
                    }
                    body.update({
                        'x_gs2': {
                            'service': 'identifier',
                            'component': 'projectToken',
                            'function': 'login',
                            'contentType': 'application/json',
                            'requestId': request_id,
                        },
                    })

                    _job = NetworkJob(
                        request_id=request_id,
                        result_type=LoginResult,
                        callback=callback,
                        body=body,
                    )

                    self.send(
                        job=_job
                    )
            else:
                callback(
                    AsyncResult(
                        error=BrokenPipeError()
                    )
                )
        except Exception as e:
            callback(
                AsyncResult(
                    error=e
                )
            )

    def connect(self):
        if self._connection:
            return

        async_result = []
        self._connect(
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            self.disconnect()
            raise async_result[0].error

        if self._project_token is None:
            self._project_token = async_result[0].result.access_token

    async def connect_async(self):
        if self._connection:
            return

        async_result = []
        self._connect(
            lambda result: async_result.append(result),
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error

        if self._project_token is None:
            self._project_token = async_result[0].result.access_token

    def disconnect(self):
        """
        接続を閉じる。★応答待ちの要求には BrokenPipeError が返る（待たせたままにしない）。
        """
        with self._lock:
            connection = self._connection
        self._drop_connection(connection, 'disconnect')


class AbstractGs2WebSocketClient(object):

    def __init__(self, session):
        """
        コンストラクタ
        :param session: 認証情報
        :type session: gs2_core_client.model.WebSocketSession.GatewaySession
        """
        self._session = session

    @property
    def session(self) -> Gs2WebSocketSession:
        return self._session

    def _create_authorized_bodies(self) -> Dict[str, Any]:
        return {
            'xGs2ClientId': self._session.credential.client_id,
            'xGs2ProjectToken': '{}'.format(self._session.project_token)
        }

    def _create_metadata(
            self,
            service: str,
            component: str,
            function: str,
            request_id: str,
            private: bool = False,
    ) -> Dict[str, Any]:
        metadata = {
            'x_gs2': {
                'service': service,
                'component': component,
                'function': function,
                'contentType': 'application/json',
                'requestId': request_id,
            },
        }
        if private:
            metadata['x_gs2']['private'] = True
        metadata.update(
            self._create_authorized_bodies()
        )
        return metadata
