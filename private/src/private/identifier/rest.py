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
from identifier.rest import Gs2IdentifierRestClient
from core.model import Gs2Constant
import private.identifier.request as request_model
import private.identifier.result as result_model


class Gs2IdentifierPrivateRestClient(Gs2IdentifierRestClient):

    def __init__(self, session: Gs2RestSession):
        super().__init__(session)

    def _describe_users_by_owner_id(
        self,
        request: request_model.DescribeUsersByOwnerIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeUsersByOwnerIdResult]], None],
        is_blocking: bool,
    ):
        """
        オーナーIDを指定してユーザの一覧を取得します
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='identifier',
            region=self.session.region,
        ) + "/system/user/{ownerId}".format(
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
            result_type=result_model.DescribeUsersByOwnerIdResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def describe_users_by_owner_id(
        self,
        request: request_model.DescribeUsersByOwnerIdRequest,
    ) -> result_model.DescribeUsersByOwnerIdResult:
        async_result = []
        with timeout(30):
            self._describe_users_by_owner_id(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

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
            is_blocking=False,
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
        is_blocking: bool,
    ):
        """
        オーナーIDを指定してセキュリティポリシーの一覧を取得します
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='identifier',
            region=self.session.region,
        ) + "/system/securityPolicy/{ownerId}".format(
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
            result_type=result_model.DescribeSecurityPoliciesByOwnerIdResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def describe_security_policies_by_owner_id(
        self,
        request: request_model.DescribeSecurityPoliciesByOwnerIdRequest,
    ) -> result_model.DescribeSecurityPoliciesByOwnerIdResult:
        async_result = []
        with timeout(30):
            self._describe_security_policies_by_owner_id(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

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
            is_blocking=False,
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
        is_blocking: bool,
    ):
        """
        プロジェクトトークン を取得します
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='identifier',
            region=self.session.region,
        ) + "/projectToken/assume"
        headers = self._create_authorized_headers()
        body = {
            "clientId": request.client_id,
            "userId": request.user_id,
            'contextStack': request.context_stack,
        }

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id
        headers["X-GS2-DUPLICATION-AVOIDER"] = request.duplication_avoider

        _job = NetworkJob(
            url=url,
            method='POST',
            result_type=result_model.AssumeResult,
            callback=callback,
            headers=headers,
            body=body,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def assume(
        self,
        request: request_model.AssumeRequest,
    ) -> result_model.AssumeResult:
        async_result = []
        with timeout(30):
            self._assume(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

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
            is_blocking=False,
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result
