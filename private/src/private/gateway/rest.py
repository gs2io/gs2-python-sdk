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
from urllib.parse import quote

from core.rest import *
from gateway.rest import Gs2GatewayRestClient
from core.model import Gs2Constant
import private.gateway.request as request_model
import private.gateway.result as result_model


class Gs2GatewayPrivateRestClient(Gs2GatewayRestClient):

    def __init__(self, session: Gs2RestSession):
        super().__init__(session)

    def _describe_namespaces_by_owner_id(
        self,
        request: request_model.DescribeNamespacesByOwnerIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeNamespacesByOwnerIdResult]], None],
        is_blocking: bool,
    ):
        """
        オーナーIDを指定してネームスペースの一覧を取得
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='gateway',
            region=self.session.region,
        ) + "/system/{ownerId}".format(
            ownerId=request.owner_id if request.owner_id is not None and request.owner_id != '' else 'null',
        )
        headers = self._create_authorized_headers()
        query_strings = {
            'contextStack': request.context_stack,
        }
        if request.page_token is not None:
            query_strings["pageToken"] = request.page_token
        if request.limit is not None:
            query_strings["limit"] = request.limit

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='GET',
            result_type=result_model.DescribeNamespacesByOwnerIdResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def describe_namespaces_by_owner_id(
        self,
        request: request_model.DescribeNamespacesByOwnerIdRequest,
    ) -> result_model.DescribeNamespacesByOwnerIdResult:
        async_result = []
        with timeout(30):
            self._describe_namespaces_by_owner_id(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_namespaces_by_owner_id_async(
        self,
        request: request_model.DescribeNamespacesByOwnerIdRequest,
    ) -> result_model.DescribeNamespacesByOwnerIdResult:
        async_result = []
        self._describe_namespaces_by_owner_id(
            request,
            lambda result: async_result.append(result),
            is_blocking=False,
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _connect(
        self,
        request: request_model.ConnectRequest,
        callback: Callable[[AsyncResult[result_model.ConnectResult]], None],
        is_blocking: bool,
    ):
        """
        接続
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='gateway',
            region=self.session.region,
        ) + "/system/session"
        headers = self._create_authorized_headers()
        body = {
            'contextStack': request.context_stack,
        }

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='POST',
            result_type=result_model.ConnectResult,
            callback=callback,
            headers=headers,
            body=body,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def connect(
        self,
        request: request_model.ConnectRequest,
    ) -> result_model.ConnectResult:
        async_result = []
        with timeout(30):
            self._connect(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def connect_async(
        self,
        request: request_model.ConnectRequest,
    ) -> result_model.ConnectResult:
        async_result = []
        self._connect(
            request,
            lambda result: async_result.append(result),
            is_blocking=False,
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _disconnect(
        self,
        request: request_model.DisconnectRequest,
        callback: Callable[[AsyncResult[result_model.DisconnectResult]], None],
        is_blocking: bool,
    ):
        """
        切断
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='gateway',
            region=self.session.region,
        ) + "/system/session"
        headers = self._create_authorized_headers()
        query_strings = {
            'contextStack': request.context_stack,
        }

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='DELETE',
            result_type=result_model.DisconnectResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def disconnect(
        self,
        request: request_model.DisconnectRequest,
    ) -> result_model.DisconnectResult:
        async_result = []
        with timeout(30):
            self._disconnect(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def disconnect_async(
        self,
        request: request_model.DisconnectRequest,
    ) -> result_model.DisconnectResult:
        async_result = []
        self._disconnect(
            request,
            lambda result: async_result.append(result),
            is_blocking=False,
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result

    def _send_notification_by_owner_id(
        self,
        request: request_model.SendNotificationByOwnerIdRequest,
        callback: Callable[[AsyncResult[result_model.SendNotificationByOwnerIdResult]], None],
        is_blocking: bool,
    ):
        """
        オーナーIDを指定して通知を送信
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='gateway',
            region=self.session.region,
        ) + "/system/{ownerId}/{namespaceName}/session/notification".format(
            ownerId=request.owner_id if request.owner_id is not None and request.owner_id != '' else 'null',
            namespaceName=request.namespace_name if request.namespace_name is not None and request.namespace_name != '' else 'null',
            userId=request.user_id if request.user_id is not None and request.user_id != '' else 'null',
        )
        headers = self._create_authorized_headers()
        body = {
            "issuer": request.issuer,
            "subject": request.subject,
            "payload": request.payload,
            'contextStack': request.context_stack,
        }
        if request.enable_transfer_mobile_notification is not None:
            body["enableTransferMobileNotification"] = request.enable_transfer_mobile_notification
        if request.sound is not None:
            body["sound"] = request.sound

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id
        headers["X-GS2-DUPLICATION-AVOIDER"] = request.duplication_avoider

        _job = NetworkJob(
            url=url,
            method='POST',
            result_type=result_model.SendNotificationByOwnerIdResult,
            callback=callback,
            headers=headers,
            body=body,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def send_notification_by_owner_id(
        self,
        request: request_model.SendNotificationByOwnerIdRequest,
    ) -> result_model.SendNotificationByOwnerIdResult:
        async_result = []
        with timeout(30):
            self._send_notification_by_owner_id(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def send_notification_by_owner_id_async(
        self,
        request: request_model.SendNotificationByOwnerIdRequest,
    ) -> result_model.SendNotificationByOwnerIdResult:
        async_result = []
        self._send_notification_by_owner_id(
            request,
            lambda result: async_result.append(result),
            is_blocking=False,
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result
