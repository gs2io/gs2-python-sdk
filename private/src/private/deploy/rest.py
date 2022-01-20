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
from deploy.rest import Gs2DeployRestClient
from core.model import Gs2Constant
import private.deploy.request as request_model
import private.deploy.result as result_model


class Gs2DeployPrivateRestClient(Gs2DeployRestClient):

    def __init__(self, session: Gs2RestSession):
        super().__init__(session)

    def _describe_stacks_by_owner_id(
        self,
        request: request_model.DescribeStacksByOwnerIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeStacksByOwnerIdResult]], None],
        is_blocking: bool,
    ):
        """
        オーナーIDを指定してスタックの一覧を取得
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='deploy',
            region=self.session.region,
        ) + "/system/{ownerId}/stack".format(
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
            result_type=result_model.DescribeStacksByOwnerIdResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def describe_stacks_by_owner_id(
        self,
        request: request_model.DescribeStacksByOwnerIdRequest,
    ) -> result_model.DescribeStacksByOwnerIdResult:
        async_result = []
        with timeout(30):
            self._describe_stacks_by_owner_id(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_stacks_by_owner_id_async(
        self,
        request: request_model.DescribeStacksByOwnerIdRequest,
    ) -> result_model.DescribeStacksByOwnerIdResult:
        async_result = []
        self._describe_stacks_by_owner_id(
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

    def _run_stack_task(
        self,
        request: request_model.RunStackTaskRequest,
        callback: Callable[[AsyncResult[result_model.RunStackTaskResult]], None],
        is_blocking: bool,
    ):
        """
        実行中のスタックの処理を実行
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='deploy',
            region=self.session.region,
        ) + "/run/working/{ownerId}/stack/{stackName}".format(
            ownerId=request.owner_id if request.owner_id is not None and request.owner_id != '' else 'null',
            stackName=request.stack_name if request.stack_name is not None and request.stack_name != '' else 'null',
        )
        headers = self._create_authorized_headers()
        query_strings = {
            'contextStack': request.context_stack,
        }

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='GET',
            result_type=result_model.RunStackTaskResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def run_stack_task(
        self,
        request: request_model.RunStackTaskRequest,
    ) -> result_model.RunStackTaskResult:
        async_result = []
        with timeout(30):
            self._run_stack_task(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def run_stack_task_async(
        self,
        request: request_model.RunStackTaskRequest,
    ) -> result_model.RunStackTaskResult:
        async_result = []
        self._run_stack_task(
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

    def _run_resource_task(
        self,
        request: request_model.RunResourceTaskRequest,
        callback: Callable[[AsyncResult[result_model.RunResourceTaskResult]], None],
        is_blocking: bool,
    ):
        """
        作成中のリソースの処理を実行
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='deploy',
            region=self.session.region,
        ) + "/run/working/{ownerId}/stack/{stackName}/resource/{resourceName}".format(
            ownerId=request.owner_id if request.owner_id is not None and request.owner_id != '' else 'null',
            stackName=request.stack_name if request.stack_name is not None and request.stack_name != '' else 'null',
            resourceName=request.resource_name if request.resource_name is not None and request.resource_name != '' else 'null',
        )
        headers = self._create_authorized_headers()
        query_strings = {
            'contextStack': request.context_stack,
        }

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='GET',
            result_type=result_model.RunResourceTaskResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def run_resource_task(
        self,
        request: request_model.RunResourceTaskRequest,
    ) -> result_model.RunResourceTaskResult:
        async_result = []
        with timeout(30):
            self._run_resource_task(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def run_resource_task_async(
        self,
        request: request_model.RunResourceTaskRequest,
    ) -> result_model.RunResourceTaskResult:
        async_result = []
        self._run_resource_task(
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
