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
from key.web_socket import Gs2KeyWebSocketClient
import private.key.request as request_model
import private.key.result as result_model


class Gs2KeyPrivateWebSocketClient(Gs2KeyWebSocketClient):

    SERVICE = "key"

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

    def _encrypt_by_key_id(
        self,
        request: request_model.EncryptByKeyIdRequest,
        callback: Callable[[AsyncResult[result_model.EncryptByKeyIdResult]], None],
    ):
        """
        オーナーIDを指定してデータを暗号化します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='key',
            function='encryptByKeyId',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.key_id is not None:
            body["keyId"] = request.key_id
        if request.data is not None:
            body["data"] = request.data

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.EncryptByKeyIdResult,
                callback=callback,
                body=body,
            )
        )

    def encrypt_by_key_id(
        self,
        request: request_model.EncryptByKeyIdRequest,
    ) -> result_model.EncryptByKeyIdResult:
        async_result = []
        self._encrypt_by_key_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def encrypt_by_key_id_async(
        self,
        request: request_model.EncryptByKeyIdRequest,
    ) -> result_model.EncryptByKeyIdResult:
        async_result = []
        self._encrypt_by_key_id(
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

    def _decrypt_by_key_id(
        self,
        request: request_model.DecryptByKeyIdRequest,
        callback: Callable[[AsyncResult[result_model.DecryptByKeyIdResult]], None],
    ):
        """
        オーナーIDを指定してデータを復号します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='key',
            function='decryptByKeyId',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.key_id is not None:
            body["keyId"] = request.key_id
        if request.data is not None:
            body["data"] = request.data

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.DecryptByKeyIdResult,
                callback=callback,
                body=body,
            )
        )

    def decrypt_by_key_id(
        self,
        request: request_model.DecryptByKeyIdRequest,
    ) -> result_model.DecryptByKeyIdResult:
        async_result = []
        self._decrypt_by_key_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def decrypt_by_key_id_async(
        self,
        request: request_model.DecryptByKeyIdRequest,
    ) -> result_model.DecryptByKeyIdResult:
        async_result = []
        self._decrypt_by_key_id(
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

    def _get_git_hub_api_key_with_api_key(
        self,
        request: request_model.GetGitHubApiKeyWithApiKeyRequest,
        callback: Callable[[AsyncResult[result_model.GetGitHubApiKeyWithApiKeyResult]], None],
    ):
        """
        GitHub のAPIキーを取得します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='gitHubApiKey',
            function='getGitHubApiKeyWithApiKey',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.git_hub_api_key_id is not None:
            body["gitHubApiKeyId"] = request.git_hub_api_key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.GetGitHubApiKeyWithApiKeyResult,
                callback=callback,
                body=body,
            )
        )

    def get_git_hub_api_key_with_api_key(
        self,
        request: request_model.GetGitHubApiKeyWithApiKeyRequest,
    ) -> result_model.GetGitHubApiKeyWithApiKeyResult:
        async_result = []
        self._get_git_hub_api_key_with_api_key(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_git_hub_api_key_with_api_key_async(
        self,
        request: request_model.GetGitHubApiKeyWithApiKeyRequest,
    ) -> result_model.GetGitHubApiKeyWithApiKeyResult:
        async_result = []
        self._get_git_hub_api_key_with_api_key(
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
