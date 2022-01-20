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
from core.model import *
from core.web_socket import *
from gateway.web_socket import Gs2GatewayWebSocketClient
import private.gateway.request as request_model
import private.gateway.result as result_model


class Gs2GatewayPrivateWebSocketClient(Gs2GatewayWebSocketClient):

    SERVICE = "gateway"

    def __init__(
        self,
        session: Gs2WebSocketSession,
    ):
        super().__init__(session)

    def _describe_namespaces_by_owner_id(
        self,
        request: request_model.DescribeNamespacesByOwnerIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeNamespacesByOwnerIdResult]], None],
    ):
        """
        オーナーIDを指定してネームスペースの一覧を取得
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='namespace',
            function='describeNamespacesByOwnerId',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.DescribeNamespacesByOwnerIdResult,
                callback=callback,
                body=body,
            )
        )

    def describe_namespaces_by_owner_id(
        self,
        request: request_model.DescribeNamespacesByOwnerIdRequest,
    ) -> result_model.DescribeNamespacesByOwnerIdResult:
        async_result = []
        self._describe_namespaces_by_owner_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
    ):
        """
        接続
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='webSocketSession',
            function='connect',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.connection_id is not None:
            body["connectionId"] = request.connection_id
        if request.api_id is not None:
            body["apiId"] = request.api_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.ConnectResult,
                callback=callback,
                body=body,
            )
        )

    def connect(
        self,
        request: request_model.ConnectRequest,
    ) -> result_model.ConnectResult:
        async_result = []
        self._connect(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
    ):
        """
        切断
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='webSocketSession',
            function='disconnect',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.connection_id is not None:
            body["connectionId"] = request.connection_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.DisconnectResult,
                callback=callback,
                body=body,
            )
        )

    def disconnect(
        self,
        request: request_model.DisconnectRequest,
    ) -> result_model.DisconnectResult:
        async_result = []
        self._disconnect(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
    ):
        """
        オーナーIDを指定して通知を送信
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='webSocketSession',
            function='sendNotificationByOwnerId',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.issuer is not None:
            body["issuer"] = request.issuer
        if request.subject is not None:
            body["subject"] = request.subject
        if request.payload is not None:
            body["payload"] = request.payload
        if request.enable_transfer_mobile_notification is not None:
            body["enableTransferMobileNotification"] = request.enable_transfer_mobile_notification
        if request.sound is not None:
            body["sound"] = request.sound

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.SendNotificationByOwnerIdResult,
                callback=callback,
                body=body,
            )
        )

    def send_notification_by_owner_id(
        self,
        request: request_model.SendNotificationByOwnerIdRequest,
    ) -> result_model.SendNotificationByOwnerIdResult:
        async_result = []
        self._send_notification_by_owner_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result
