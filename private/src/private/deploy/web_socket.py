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
from deploy.web_socket import Gs2DeployWebSocketClient
import private.deploy.request as request_model
import private.deploy.result as result_model


class Gs2DeployPrivateWebSocketClient(Gs2DeployWebSocketClient):

    SERVICE = "deploy"

    def __init__(
        self,
        session: Gs2WebSocketSession,
    ):
        super().__init__(session)

    def _describe_stacks_by_owner_id(
        self,
        request: request_model.DescribeStacksByOwnerIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeStacksByOwnerIdResult]], None],
    ):
        """
        オーナーIDを指定してスタックの一覧を取得
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='stack',
            function='describeStacksByOwnerId',
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
                result_type=result_model.DescribeStacksByOwnerIdResult,
                callback=callback,
                body=body,
            )
        )

    def describe_stacks_by_owner_id(
        self,
        request: request_model.DescribeStacksByOwnerIdRequest,
    ) -> result_model.DescribeStacksByOwnerIdResult:
        async_result = []
        self._describe_stacks_by_owner_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
    ):
        """
        実行中のスタックの処理を実行
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='workingStack',
            function='runStackTask',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.stack_name is not None:
            body["stackName"] = request.stack_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.RunStackTaskResult,
                callback=callback,
                body=body,
            )
        )

    def run_stack_task(
        self,
        request: request_model.RunStackTaskRequest,
    ) -> result_model.RunStackTaskResult:
        async_result = []
        self._run_stack_task(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
    ):
        """
        作成中のリソースの処理を実行
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='workingResource',
            function='runResourceTask',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.stack_name is not None:
            body["stackName"] = request.stack_name
        if request.resource_name is not None:
            body["resourceName"] = request.resource_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.RunResourceTaskResult,
                callback=callback,
                body=body,
            )
        )

    def run_resource_task(
        self,
        request: request_model.RunResourceTaskRequest,
    ) -> result_model.RunResourceTaskResult:
        async_result = []
        self._run_resource_task(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result
