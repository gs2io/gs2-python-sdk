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
from schedule.web_socket import Gs2ScheduleWebSocketClient
import private.schedule.request as request_model
import private.schedule.result as result_model


class Gs2SchedulePrivateWebSocketClient(Gs2ScheduleWebSocketClient):

    SERVICE = "schedule"

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

    def _describe_triggers_by_owner_id_and_user_id(
        self,
        request: request_model.DescribeTriggersByOwnerIdAndUserIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeTriggersByOwnerIdAndUserIdResult]], None],
    ):
        """
        オーナーIDを指定してトリガーの一覧を取得
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='trigger',
            function='describeTriggersByOwnerIdAndUserId',
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
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.DescribeTriggersByOwnerIdAndUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def describe_triggers_by_owner_id_and_user_id(
        self,
        request: request_model.DescribeTriggersByOwnerIdAndUserIdRequest,
    ) -> result_model.DescribeTriggersByOwnerIdAndUserIdResult:
        async_result = []
        self._describe_triggers_by_owner_id_and_user_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_triggers_by_owner_id_and_user_id_async(
        self,
        request: request_model.DescribeTriggersByOwnerIdAndUserIdRequest,
    ) -> result_model.DescribeTriggersByOwnerIdAndUserIdResult:
        async_result = []
        self._describe_triggers_by_owner_id_and_user_id(
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

    def _get_event_by_owner_id_and_user_id(
        self,
        request: request_model.GetEventByOwnerIdAndUserIdRequest,
        callback: Callable[[AsyncResult[result_model.GetEventByOwnerIdAndUserIdResult]], None],
    ):
        """
        オーナーIDとユーザIDを指定してイベントを取得
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='event',
            function='getEventByOwnerIdAndUserId',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.event_name is not None:
            body["eventName"] = request.event_name
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.user_id is not None:
            body["userId"] = request.user_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.GetEventByOwnerIdAndUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def get_event_by_owner_id_and_user_id(
        self,
        request: request_model.GetEventByOwnerIdAndUserIdRequest,
    ) -> result_model.GetEventByOwnerIdAndUserIdResult:
        async_result = []
        self._get_event_by_owner_id_and_user_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_event_by_owner_id_and_user_id_async(
        self,
        request: request_model.GetEventByOwnerIdAndUserIdRequest,
    ) -> result_model.GetEventByOwnerIdAndUserIdResult:
        async_result = []
        self._get_event_by_owner_id_and_user_id(
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
