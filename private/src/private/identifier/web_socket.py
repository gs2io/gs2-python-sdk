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
from identifier.web_socket import Gs2IdentifierWebSocketClient
import private.identifier.request as request_model
import private.identifier.result as result_model


class Gs2IdentifierPrivateWebSocketClient(Gs2IdentifierWebSocketClient):

    SERVICE = "identifier"

    def __init__(
        self,
        session: Gs2WebSocketSession,
    ):
        super().__init__(session)

    def _describe_users_by_owner_id(
        self,
        request: request_model.DescribeUsersByOwnerIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeUsersByOwnerIdResult]], None],
    ):
        """
        オーナーIDを指定してユーザの一覧を取得します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='user',
            function='describeUsersByOwnerId',
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
                result_type=result_model.DescribeUsersByOwnerIdResult,
                callback=callback,
                body=body,
            )
        )

    def describe_users_by_owner_id(
        self,
        request: request_model.DescribeUsersByOwnerIdRequest,
    ) -> result_model.DescribeUsersByOwnerIdResult:
        async_result = []
        self._describe_users_by_owner_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_users_by_owner_id_async(
        self,
        request: request_model.DescribeUsersByOwnerIdRequest,
    ) -> result_model.DescribeUsersByOwnerIdResult:
        async_result = []
        self._describe_users_by_owner_id(
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

    def _describe_security_policies_by_owner_id(
        self,
        request: request_model.DescribeSecurityPoliciesByOwnerIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeSecurityPoliciesByOwnerIdResult]], None],
    ):
        """
        オーナーIDを指定してセキュリティポリシーの一覧を取得します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='securityPolicy',
            function='describeSecurityPoliciesByOwnerId',
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
                result_type=result_model.DescribeSecurityPoliciesByOwnerIdResult,
                callback=callback,
                body=body,
            )
        )

    def describe_security_policies_by_owner_id(
        self,
        request: request_model.DescribeSecurityPoliciesByOwnerIdRequest,
    ) -> result_model.DescribeSecurityPoliciesByOwnerIdResult:
        async_result = []
        self._describe_security_policies_by_owner_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_security_policies_by_owner_id_async(
        self,
        request: request_model.DescribeSecurityPoliciesByOwnerIdRequest,
    ) -> result_model.DescribeSecurityPoliciesByOwnerIdResult:
        async_result = []
        self._describe_security_policies_by_owner_id(
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

    def _assume(
        self,
        request: request_model.AssumeRequest,
        callback: Callable[[AsyncResult[result_model.AssumeResult]], None],
    ):
        """
        プロジェクトトークン を取得します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='projectToken',
            function='assume',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.client_id is not None:
            body["clientId"] = request.client_id
        if request.user_id is not None:
            body["userId"] = request.user_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.AssumeResult,
                callback=callback,
                body=body,
            )
        )

    def assume(
        self,
        request: request_model.AssumeRequest,
    ) -> result_model.AssumeResult:
        async_result = []
        self._assume(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def assume_async(
        self,
        request: request_model.AssumeRequest,
    ) -> result_model.AssumeResult:
        async_result = []
        self._assume(
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
