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
import time
from collections import deque
from typing import Callable, Type, Deque, Optional
from netrc import netrc, NetrcParseError  # メインスレッド以外でimportするとデッドロックするらしい https://github.com/kennethreitz/requests/issues/2925

import websocket
import _thread as thread

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
        self._job_queue = deque()
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

    def send(self, job: NetworkJob):
        if not self._connection:
            raise BrokenPipeError()
        import simplejson as json
        self._job_queue.append(job)
        try:
            self._connection.send(json.dumps(job.body))
        except websocket._exceptions.WebSocketConnectionClosedException:
            self._connection = None
            self.connect()
            self._connection.send(json.dumps(job.body))

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
                        target_job = [
                            job
                            for job in self._job_queue
                            if job.request_id == request_id
                        ]
                        if target_job:
                            try:
                                status = response.get('status')
                                result = response.get('body')
                                target_job[0].callback(
                                    AsyncResult(
                                        result=target_job[0].result_type.from_dict(_parse_response(status, result)),
                                    )
                                )
                            except Gs2Exception as e:
                                target_job[0].callback(
                                    AsyncResult(
                                        error=e,
                                    )
                                )
                            finally:
                                self._job_queue.remove(target_job[0])

                def on_error(ws, error):
                    print(error)
                    ws.close()

                def on_open(ws):
                    opened.append(True)

                def on_close(ws, *args):
                    closed.append(True)

                websocket.enableTrace(False)
                self._connection = websocket.WebSocketApp(
                    self._web_socket_url(),
                    on_message=on_message,
                    on_error=on_error,
                    on_open=on_open,
                    on_close=on_close,
                )

                def run():
                    self._connection.run_forever(ping_interval=10)
                thread.start_new_thread(run, ())

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
        if self._connection:
            try:
                self._connection.close()
            except:
                pass
            self._connection = None
        for job in self._job_queue:
            job.callback(
                AsyncResult(
                    error=BrokenPipeError(),
                )
            )
        self._job_queue.clear()
        self._project_token = None


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
