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
from experience.rest import Gs2ExperienceRestClient
from core.model import Gs2Constant
import private.experience.request as request_model
import private.experience.result as result_model


class Gs2ExperiencePrivateRestClient(Gs2ExperienceRestClient):

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
            service='experience',
            region=self.session.region,
        ) + "/system/{ownerId}/experience".format(
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

    def _describe_statuses_by_owner_id_and_user_id(
        self,
        request: request_model.DescribeStatusesByOwnerIdAndUserIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeStatusesByOwnerIdAndUserIdResult]], None],
        is_blocking: bool,
    ):
        """
        オーナーIDを指定してステータスの一覧を取得
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='experience',
            region=self.session.region,
        ) + "/system/{ownerId}/{namespaceName}/user/{userId}/status".format(
            ownerId=request.owner_id if request.owner_id is not None and request.owner_id != '' else 'null',
            namespaceName=request.namespace_name if request.namespace_name is not None and request.namespace_name != '' else 'null',
            userId=request.user_id if request.user_id is not None and request.user_id != '' else 'null',
        )
        headers = self._create_authorized_headers()
        query_strings = {
            'contextStack': request.context_stack,
        }
        if request.experience_name is not None:
            query_strings["experienceName"] = request.experience_name
        if request.page_token is not None:
            query_strings["pageToken"] = request.page_token
        if request.limit is not None:
            query_strings["limit"] = request.limit

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='GET',
            result_type=result_model.DescribeStatusesByOwnerIdAndUserIdResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def describe_statuses_by_owner_id_and_user_id(
        self,
        request: request_model.DescribeStatusesByOwnerIdAndUserIdRequest,
    ) -> result_model.DescribeStatusesByOwnerIdAndUserIdResult:
        async_result = []
        with timeout(30):
            self._describe_statuses_by_owner_id_and_user_id(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_statuses_by_owner_id_and_user_id_async(
        self,
        request: request_model.DescribeStatusesByOwnerIdAndUserIdRequest,
    ) -> result_model.DescribeStatusesByOwnerIdAndUserIdResult:
        async_result = []
        self._describe_statuses_by_owner_id_and_user_id(
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
