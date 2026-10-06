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
import functools
import gzip
import json
import re
import time
from collections import deque
from io import BytesIO
from typing import Dict, Any, Callable, TypeVar, Type, Deque, Generic, Optional
from netrc import netrc, NetrcParseError  # メインスレッド以外でimportするとデッドロックするらしい https://github.com/kennethreitz/requests/issues/2925

import requests

from ..core.exception import *
from ..core.model import *
from ..core.util import timeout

T = TypeVar('T')


def _compress_body(data: Dict[str, Any]) -> bytes:
    """
    リクエストボディをgzip圧縮する
    :param data: 圧縮するデータ
    :return: gzip圧縮されたバイト列
    """
    json_str = json.dumps(data)
    buf = BytesIO()
    with gzip.GzipFile(fileobj=buf, mode='wb') as gz:
        gz.write(json_str.encode('utf-8'))
    return buf.getvalue()


def _parse_response(response: requests.Response) -> Dict[str, Any]:
    if response.status_code == 200:
        try:
            return json.loads(response.text)
        except ValueError:
            from ..core.exception import UnknownException
            raise UnknownException(response.text)
    elif response.status_code == 400:
        from ..core.exception import BadRequestException
        raise BadRequestException(response.text)
    elif response.status_code == 401:
        from ..core.exception import UnauthorizedException
        raise UnauthorizedException(response.text)
    elif response.status_code == 402:
        from ..core.exception import QuotaExceedException
        raise QuotaExceedException(response.text)
    elif response.status_code == 404:
        from ..core.exception import NotFoundException
        raise NotFoundException(response.text)
    elif response.status_code == 409:
        from ..core.exception import ConflictException
        raise ConflictException(response.text)
    elif response.status_code == 500:
        from ..core.exception import InternalServerErrorException
        raise InternalServerErrorException(response.text)
    elif response.status_code == 502:
        from ..core.exception import BadGatewayException
        raise BadGatewayException(response.text)
    elif response.status_code == 503:
        from ..core.exception import ServiceUnavailableException
        raise ServiceUnavailableException('')
    elif response.status_code == 504:
        from ..core.exception import RequestTimeoutException
        raise RequestTimeoutException(response.text)
    else:
        from ..core.exception import UnknownException
        raise UnknownException(response.text)


_CONNECT_FAILURE_CAUSE_NAMES = frozenset({
    'NewConnectionError',
    'NameResolutionError',
    'ConnectTimeoutError',
})


def _iter_cause_chain(error: BaseException):
    seen = set()
    stack = [error]
    while stack:
        current = stack.pop()
        if not isinstance(current, BaseException) or id(current) in seen:
            continue
        seen.add(id(current))
        yield current
        for nxt in (
                getattr(current, 'reason', None),
                getattr(current, '__cause__', None),
                getattr(current, '__context__', None),
        ):
            if isinstance(nxt, BaseException):
                stack.append(nxt)
        for arg in getattr(current, 'args', ()) or ():
            if isinstance(arg, BaseException):
                stack.append(arg)


def _is_connect_failure(error: Optional[BaseException]) -> bool:
    if error is None:
        return False
    if isinstance(error, requests.exceptions.ConnectTimeout):
        return True
    if isinstance(error, requests.exceptions.SSLError):
        return True
    if isinstance(error, requests.exceptions.ConnectionError):
        for cause in _iter_cause_chain(error):
            for klass in type(cause).__mro__:
                if klass.__name__ in _CONNECT_FAILURE_CAUSE_NAMES:
                    return True
        return False
    return False


_SERVICE_MARK = '\x00'


@functools.lru_cache(maxsize=None)
def _shared_cloud_url_pattern(template: str, region: str):
    filled = template.replace('{service}', _SERVICE_MARK).replace('{region}', region)
    return re.compile('^' + re.escape(filled).replace(_SERVICE_MARK, '([^/]+)') + '(?=/|$)')


def _rewrite_to_steady(steady: Optional[str], region: str, url: str) -> str:
    base = normalize_steady_endpoint(steady)
    if not base:
        return url
    template = Gs2Constant.ENDPOINT_HOST
    if '{service}' not in template:
        return url
    matched = _shared_cloud_url_pattern(template, region).match(url)
    if matched is None:
        return url
    return base + '/' + matched.group(1) + url[matched.end():]


class NetworkJob:

    def __init__(
            self,
            url: str,
            method: str,
            result_type: Type[T],
            callback: Callable[[AsyncResult[T]], None],
            headers: Dict[str, Any] = None,
            query_strings: Dict[str, Any] = None,
            body: Dict[str, Any] = None,
    ):
        if headers is None:
            headers = {}
        if query_strings is None:
            query_strings = {}
        if body is None:
            body = {}

        self._url = url
        self._method = method
        self._result_type = result_type
        self._callback = callback
        self._headers = headers
        self._query_strings = query_strings
        self._body = body

    @property
    def url(self) -> str:
        return self._url

    @property
    def method(self) -> str:
        return self._method

    @property
    def result_type(self) -> Type[T]:
        return self._result_type

    @property
    def callback(self) -> Callable[[T], None]:
        return self._callback

    @property
    def headers(self) -> Dict[str, Any]:
        return self._headers

    @property
    def query_strings(self) -> Dict[str, Any]:
        return self._query_strings

    @property
    def body(self) -> Dict[str, Any]:
        return self._body


class Gs2RestSession(ISession):

    def __init__(
            self,
            credential: IGs2Credential,
            region: str,
            enable_request_compression: bool = True,
            enable_response_decompression: bool = True,
            steady_endpoint: Optional[str] = None,
    ):
        """
        コンストラクタ
        :param credential: クレデンシャル
        :param region: リージョン
        :param enable_request_compression: リクエストボディのgzip圧縮を有効にするか（デフォルト: True）
        :param enable_response_decompression: レスポンスのgzip展開を有効にするか（デフォルト: True）
        """
        super().__init__()
        self._credential = credential
        self._project_token = None
        self._region = region
        self._connection = None
        self._connection_thread = None
        self._job_queue = deque()
        self._enable_request_compression = enable_request_compression
        self._enable_response_decompression = enable_response_decompression
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
    def connection(self) -> requests.Session:
        return self._connection

    @property
    def enable_request_compression(self) -> bool:
        return self._enable_request_compression

    @property
    def enable_response_decompression(self) -> bool:
        return self._enable_response_decompression

    @property
    def steady_endpoint(self) -> Optional[str]:
        return self._steady_endpoint

    @steady_endpoint.setter
    def steady_endpoint(self, value: Optional[str]):
        self._steady_endpoint = normalize_steady_endpoint(value) or None

    def endpoint_host(
            self,
            service: str,
    ) -> str:
        base = normalize_steady_endpoint(self._steady_endpoint)
        if not base:
            return Gs2Constant.ENDPOINT_HOST.format(
                service=service,
                region=self.region,
            )
        return base + '/' + service

    def _do_request(
            self,
            url: str,
            headers: Dict[str, Any],
            job: NetworkJob,
            steady: bool,
    ) -> requests.Response:
        kwargs = {}
        if steady:
            kwargs['timeout'] = (Gs2Constant.STEADY_CONNECT_TIMEOUT, None)

        if job.method == 'GET':
            return self.connection.get(
                url=url,
                headers=headers,
                params=job.query_strings,
                **kwargs
            )
        elif job.method == 'POST':
            if self._enable_request_compression and job.body:
                headers['Content-Encoding'] = 'gzip'
                headers['Content-Type'] = 'application/json'
                return self.connection.post(
                    url=url,
                    headers=headers,
                    data=_compress_body(job.body),
                    **kwargs
                )
            else:
                return self.connection.post(
                    url=url,
                    headers=headers,
                    json=job.body,
                    **kwargs
                )
        elif job.method == 'PUT':
            if self._enable_request_compression and job.body:
                headers['Content-Encoding'] = 'gzip'
                headers['Content-Type'] = 'application/json'
                return self.connection.put(
                    url=url,
                    headers=headers,
                    data=_compress_body(job.body),
                    **kwargs
                )
            else:
                return self.connection.put(
                    url=url,
                    headers=headers,
                    json=job.body,
                    **kwargs
                )
        elif job.method == 'DELETE':
            return self.connection.delete(
                url=url,
                headers=headers,
                params=job.query_strings,
                **kwargs
            )
        else:
            raise AttributeError()

    def _send(self, job: NetworkJob):
        if not self._connection:
            raise BrokenPipeError()

        headers = dict(job.headers)

        if self._enable_response_decompression:
            headers['Accept-Encoding'] = 'gzip'

        url = _rewrite_to_steady(self._steady_endpoint, self.region, job.url)
        steady = is_steady_url(self._steady_endpoint, url)

        try:
            try:
                response = self._do_request(url, headers, job, steady)
            except requests.exceptions.RequestException as e:
                if steady and _is_connect_failure(e):
                    response = self._do_request(url, headers, job, steady)
                else:
                    raise
        except requests.exceptions.RequestException as e:
            job.callback(
                AsyncResult(
                    error=e,
                )
            )
            return

        try:
            job.callback(
                AsyncResult(
                    result=job.result_type.from_dict(_parse_response(response)),
                )
            )
        except Gs2Exception as e:
            job.callback(
                AsyncResult(
                    error=e,
                )
            )

    def send(
            self,
            job: NetworkJob,
            is_blocking: bool = False
    ):
        if not self._connection:
            raise BrokenPipeError()
        if is_blocking:
            self._send(job)
            pass
        else:
            self._job_queue.append(job)

    def _connect(
            self,
            callback: Callable[[AsyncResult[LoginResult]], None],
            is_blocking: bool = False,
    ):
        try:
            if not self._connection:
                import threading
                self._connection = requests.Session()
                self._connection_thread = threading.Thread(target=receive_handler, args=(self, self._job_queue))
                self._connection_thread.start()

                if isinstance(self.credential, ProjectTokenGs2Credential):
                    self._project_token = self.credential.project_token
                    callback(
                        AsyncResult(
                        )
                    )
                else:
                    url = self.endpoint_host(
                        service='identifier',
                    ) + "/projectToken/login"
                    body = {
                        "client_id": self.credential.client_id,
                        "client_secret": self.credential.client_secret,
                    }

                    _job = NetworkJob(
                        url=url,
                        method='POST',
                        result_type=LoginResult,
                        callback=callback,
                        body=body,
                    )

                    self.send(
                        job=_job,
                        is_blocking=is_blocking,
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
        with timeout(30):
            self._connect(
                lambda result: async_result.append(result),
                is_blocking=True,
            )

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
            is_blocking=False,
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
            self._connection.close()
            self._connection = None
        for job in self._job_queue:
            job.callback(
                AsyncResult(
                    error=BrokenPipeError(),
                )
            )
        self._job_queue.clear()
        self._project_token = None


class AbstractGs2RestClient(object):

    def __init__(self, session):
        """
        コンストラクタ
        :param session: 認証情報
        :type session: gs2_core_client.model.RestSession.RestSession
        """
        self._session = session

    @property
    def session(self) -> Gs2RestSession:
        return self._session

    def _create_authorized_headers(self) -> Dict[str, Any]:
        return {
            'X-GS2-CLIENT-ID': self._session.credential.client_id,
            'Authorization': 'Bearer {}'.format(self._session.project_token),
        }


def receive_handler(
        session: Gs2RestSession,
        job_queue: Deque[NetworkJob],
):
    while session.connection:
        try:
            job = job_queue.popleft()
            session._send(job)
        except IndexError:
            time.sleep(0.01)

