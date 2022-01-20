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
from lock.web_socket import Gs2LockWebSocketClient
import private.lock.request as request_model
import private.lock.result as result_model


class Gs2LockPrivateWebSocketClient(Gs2LockWebSocketClient):

    SERVICE = "lock"

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

    def _lock_by_owner_id_and_user_id(
        self,
        request: request_model.LockByOwnerIdAndUserIdRequest,
        callback: Callable[[AsyncResult[result_model.LockByOwnerIdAndUserIdResult]], None],
    ):
        """
        オーナーIDとユーザIDを指定してミューテックスを取得
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='mutex',
            function='lockByOwnerIdAndUserId',
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
        if request.property_id is not None:
            body["propertyId"] = request.property_id
        if request.transaction_id is not None:
            body["transactionId"] = request.transaction_id
        if request.ttl is not None:
            body["ttl"] = request.ttl

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.LockByOwnerIdAndUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def lock_by_owner_id_and_user_id(
        self,
        request: request_model.LockByOwnerIdAndUserIdRequest,
    ) -> result_model.LockByOwnerIdAndUserIdResult:
        async_result = []
        self._lock_by_owner_id_and_user_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def lock_by_owner_id_and_user_id_async(
        self,
        request: request_model.LockByOwnerIdAndUserIdRequest,
    ) -> result_model.LockByOwnerIdAndUserIdResult:
        async_result = []
        self._lock_by_owner_id_and_user_id(
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

    def _unlock_by_owner_id_and_user_id(
        self,
        request: request_model.UnlockByOwnerIdAndUserIdRequest,
        callback: Callable[[AsyncResult[result_model.UnlockByOwnerIdAndUserIdResult]], None],
    ):
        """
        オーナーIDとユーザIDを指定してミューテックスを解放
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='mutex',
            function='unlockByOwnerIdAndUserId',
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
        if request.property_id is not None:
            body["propertyId"] = request.property_id
        if request.transaction_id is not None:
            body["transactionId"] = request.transaction_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.UnlockByOwnerIdAndUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def unlock_by_owner_id_and_user_id(
        self,
        request: request_model.UnlockByOwnerIdAndUserIdRequest,
    ) -> result_model.UnlockByOwnerIdAndUserIdResult:
        async_result = []
        self._unlock_by_owner_id_and_user_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def unlock_by_owner_id_and_user_id_async(
        self,
        request: request_model.UnlockByOwnerIdAndUserIdRequest,
    ) -> result_model.UnlockByOwnerIdAndUserIdResult:
        async_result = []
        self._unlock_by_owner_id_and_user_id(
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

    def _get_mutex_by_owner_id_and_user_id(
        self,
        request: request_model.GetMutexByOwnerIdAndUserIdRequest,
        callback: Callable[[AsyncResult[result_model.GetMutexByOwnerIdAndUserIdResult]], None],
    ):
        """
        オーナーIDとユーザIDを指定してミューテックスを取得
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='mutex',
            function='getMutexByOwnerIdAndUserId',
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
        if request.property_id is not None:
            body["propertyId"] = request.property_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.GetMutexByOwnerIdAndUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def get_mutex_by_owner_id_and_user_id(
        self,
        request: request_model.GetMutexByOwnerIdAndUserIdRequest,
    ) -> result_model.GetMutexByOwnerIdAndUserIdResult:
        async_result = []
        self._get_mutex_by_owner_id_and_user_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_mutex_by_owner_id_and_user_id_async(
        self,
        request: request_model.GetMutexByOwnerIdAndUserIdRequest,
    ) -> result_model.GetMutexByOwnerIdAndUserIdResult:
        async_result = []
        self._get_mutex_by_owner_id_and_user_id(
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

    def _delete_mutex_by_owner_id_and_user_id(
        self,
        request: request_model.DeleteMutexByOwnerIdAndUserIdRequest,
        callback: Callable[[AsyncResult[result_model.DeleteMutexByOwnerIdAndUserIdResult]], None],
    ):
        """
        ミューテックスを削除
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='mutex',
            function='deleteMutexByOwnerIdAndUserId',
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
        if request.property_id is not None:
            body["propertyId"] = request.property_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.DeleteMutexByOwnerIdAndUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def delete_mutex_by_owner_id_and_user_id(
        self,
        request: request_model.DeleteMutexByOwnerIdAndUserIdRequest,
    ) -> result_model.DeleteMutexByOwnerIdAndUserIdResult:
        async_result = []
        self._delete_mutex_by_owner_id_and_user_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_mutex_by_owner_id_and_user_id_async(
        self,
        request: request_model.DeleteMutexByOwnerIdAndUserIdRequest,
    ) -> result_model.DeleteMutexByOwnerIdAndUserIdResult:
        async_result = []
        self._delete_mutex_by_owner_id_and_user_id(
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
