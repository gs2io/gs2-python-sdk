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

from gs2.core import *
from .request import *
from .result import *
import time


class Gs2EnhanceWebSocketClient(web_socket.AbstractGs2WebSocketClient):

    def _describe_namespaces(
        self,
        request: DescribeNamespacesRequest,
        callback: Callable[[AsyncResult[DescribeNamespacesResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='describeNamespaces',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DescribeNamespacesResult,
                callback=callback,
                body=body,
            )
        )

    def describe_namespaces(
        self,
        request: DescribeNamespacesRequest,
    ) -> DescribeNamespacesResult:
        async_result = []
        with timeout(30):
            self._describe_namespaces(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_namespaces_async(
        self,
        request: DescribeNamespacesRequest,
    ) -> DescribeNamespacesResult:
        async_result = []
        self._describe_namespaces(
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

    def _create_namespace(
        self,
        request: CreateNamespaceRequest,
        callback: Callable[[AsyncResult[CreateNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='createNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.name is not None:
            body["name"] = request.name
        if request.description is not None:
            body["description"] = request.description
        if request.transaction_setting is not None:
            body["transactionSetting"] = request.transaction_setting.to_dict()
        if request.enhance_script is not None:
            body["enhanceScript"] = request.enhance_script.to_dict()
        if request.log_setting is not None:
            body["logSetting"] = request.log_setting.to_dict()
        if request.enable_direct_enhance is not None:
            body["enableDirectEnhance"] = request.enable_direct_enhance
        if request.queue_namespace_id is not None:
            body["queueNamespaceId"] = request.queue_namespace_id
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CreateNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def create_namespace(
        self,
        request: CreateNamespaceRequest,
    ) -> CreateNamespaceResult:
        async_result = []
        with timeout(30):
            self._create_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_namespace_async(
        self,
        request: CreateNamespaceRequest,
    ) -> CreateNamespaceResult:
        async_result = []
        self._create_namespace(
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

    def _get_namespace_status(
        self,
        request: GetNamespaceStatusRequest,
        callback: Callable[[AsyncResult[GetNamespaceStatusResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='getNamespaceStatus',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetNamespaceStatusResult,
                callback=callback,
                body=body,
            )
        )

    def get_namespace_status(
        self,
        request: GetNamespaceStatusRequest,
    ) -> GetNamespaceStatusResult:
        async_result = []
        with timeout(30):
            self._get_namespace_status(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_namespace_status_async(
        self,
        request: GetNamespaceStatusRequest,
    ) -> GetNamespaceStatusResult:
        async_result = []
        self._get_namespace_status(
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

    def _get_namespace(
        self,
        request: GetNamespaceRequest,
        callback: Callable[[AsyncResult[GetNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='getNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def get_namespace(
        self,
        request: GetNamespaceRequest,
    ) -> GetNamespaceResult:
        async_result = []
        with timeout(30):
            self._get_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_namespace_async(
        self,
        request: GetNamespaceRequest,
    ) -> GetNamespaceResult:
        async_result = []
        self._get_namespace(
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

    def _update_namespace(
        self,
        request: UpdateNamespaceRequest,
        callback: Callable[[AsyncResult[UpdateNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='updateNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.description is not None:
            body["description"] = request.description
        if request.transaction_setting is not None:
            body["transactionSetting"] = request.transaction_setting.to_dict()
        if request.enhance_script is not None:
            body["enhanceScript"] = request.enhance_script.to_dict()
        if request.log_setting is not None:
            body["logSetting"] = request.log_setting.to_dict()
        if request.enable_direct_enhance is not None:
            body["enableDirectEnhance"] = request.enable_direct_enhance
        if request.queue_namespace_id is not None:
            body["queueNamespaceId"] = request.queue_namespace_id
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UpdateNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def update_namespace(
        self,
        request: UpdateNamespaceRequest,
    ) -> UpdateNamespaceResult:
        async_result = []
        with timeout(30):
            self._update_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_namespace_async(
        self,
        request: UpdateNamespaceRequest,
    ) -> UpdateNamespaceResult:
        async_result = []
        self._update_namespace(
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

    def _delete_namespace(
        self,
        request: DeleteNamespaceRequest,
        callback: Callable[[AsyncResult[DeleteNamespaceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='deleteNamespace',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DeleteNamespaceResult,
                callback=callback,
                body=body,
            )
        )

    def delete_namespace(
        self,
        request: DeleteNamespaceRequest,
    ) -> DeleteNamespaceResult:
        async_result = []
        with timeout(30):
            self._delete_namespace(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_namespace_async(
        self,
        request: DeleteNamespaceRequest,
    ) -> DeleteNamespaceResult:
        async_result = []
        self._delete_namespace(
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

    def _get_service_version(
        self,
        request: GetServiceVersionRequest,
        callback: Callable[[AsyncResult[GetServiceVersionResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='getServiceVersion',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetServiceVersionResult,
                callback=callback,
                body=body,
            )
        )

    def get_service_version(
        self,
        request: GetServiceVersionRequest,
    ) -> GetServiceVersionResult:
        async_result = []
        with timeout(30):
            self._get_service_version(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_service_version_async(
        self,
        request: GetServiceVersionRequest,
    ) -> GetServiceVersionResult:
        async_result = []
        self._get_service_version(
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

    def _dump_user_data_by_user_id(
        self,
        request: DumpUserDataByUserIdRequest,
        callback: Callable[[AsyncResult[DumpUserDataByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='dumpUserDataByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DumpUserDataByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def dump_user_data_by_user_id(
        self,
        request: DumpUserDataByUserIdRequest,
    ) -> DumpUserDataByUserIdResult:
        async_result = []
        with timeout(30):
            self._dump_user_data_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def dump_user_data_by_user_id_async(
        self,
        request: DumpUserDataByUserIdRequest,
    ) -> DumpUserDataByUserIdResult:
        async_result = []
        self._dump_user_data_by_user_id(
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

    def _check_dump_user_data_by_user_id(
        self,
        request: CheckDumpUserDataByUserIdRequest,
        callback: Callable[[AsyncResult[CheckDumpUserDataByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='checkDumpUserDataByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CheckDumpUserDataByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def check_dump_user_data_by_user_id(
        self,
        request: CheckDumpUserDataByUserIdRequest,
    ) -> CheckDumpUserDataByUserIdResult:
        async_result = []
        with timeout(30):
            self._check_dump_user_data_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def check_dump_user_data_by_user_id_async(
        self,
        request: CheckDumpUserDataByUserIdRequest,
    ) -> CheckDumpUserDataByUserIdResult:
        async_result = []
        self._check_dump_user_data_by_user_id(
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

    def _clean_user_data_by_user_id(
        self,
        request: CleanUserDataByUserIdRequest,
        callback: Callable[[AsyncResult[CleanUserDataByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='cleanUserDataByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CleanUserDataByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def clean_user_data_by_user_id(
        self,
        request: CleanUserDataByUserIdRequest,
    ) -> CleanUserDataByUserIdResult:
        async_result = []
        with timeout(30):
            self._clean_user_data_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def clean_user_data_by_user_id_async(
        self,
        request: CleanUserDataByUserIdRequest,
    ) -> CleanUserDataByUserIdResult:
        async_result = []
        self._clean_user_data_by_user_id(
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

    def _check_clean_user_data_by_user_id(
        self,
        request: CheckCleanUserDataByUserIdRequest,
        callback: Callable[[AsyncResult[CheckCleanUserDataByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='checkCleanUserDataByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CheckCleanUserDataByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def check_clean_user_data_by_user_id(
        self,
        request: CheckCleanUserDataByUserIdRequest,
    ) -> CheckCleanUserDataByUserIdResult:
        async_result = []
        with timeout(30):
            self._check_clean_user_data_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def check_clean_user_data_by_user_id_async(
        self,
        request: CheckCleanUserDataByUserIdRequest,
    ) -> CheckCleanUserDataByUserIdResult:
        async_result = []
        self._check_clean_user_data_by_user_id(
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

    def _prepare_import_user_data_by_user_id(
        self,
        request: PrepareImportUserDataByUserIdRequest,
        callback: Callable[[AsyncResult[PrepareImportUserDataByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='prepareImportUserDataByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=PrepareImportUserDataByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def prepare_import_user_data_by_user_id(
        self,
        request: PrepareImportUserDataByUserIdRequest,
    ) -> PrepareImportUserDataByUserIdResult:
        async_result = []
        with timeout(30):
            self._prepare_import_user_data_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def prepare_import_user_data_by_user_id_async(
        self,
        request: PrepareImportUserDataByUserIdRequest,
    ) -> PrepareImportUserDataByUserIdResult:
        async_result = []
        self._prepare_import_user_data_by_user_id(
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

    def _import_user_data_by_user_id(
        self,
        request: ImportUserDataByUserIdRequest,
        callback: Callable[[AsyncResult[ImportUserDataByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='importUserDataByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.upload_token is not None:
            body["uploadToken"] = request.upload_token
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=ImportUserDataByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def import_user_data_by_user_id(
        self,
        request: ImportUserDataByUserIdRequest,
    ) -> ImportUserDataByUserIdResult:
        async_result = []
        with timeout(30):
            self._import_user_data_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def import_user_data_by_user_id_async(
        self,
        request: ImportUserDataByUserIdRequest,
    ) -> ImportUserDataByUserIdResult:
        async_result = []
        self._import_user_data_by_user_id(
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

    def _check_import_user_data_by_user_id(
        self,
        request: CheckImportUserDataByUserIdRequest,
        callback: Callable[[AsyncResult[CheckImportUserDataByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='namespace',
            function='checkImportUserDataByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.upload_token is not None:
            body["uploadToken"] = request.upload_token
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CheckImportUserDataByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def check_import_user_data_by_user_id(
        self,
        request: CheckImportUserDataByUserIdRequest,
    ) -> CheckImportUserDataByUserIdResult:
        async_result = []
        with timeout(30):
            self._check_import_user_data_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def check_import_user_data_by_user_id_async(
        self,
        request: CheckImportUserDataByUserIdRequest,
    ) -> CheckImportUserDataByUserIdResult:
        async_result = []
        self._check_import_user_data_by_user_id(
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

    def _describe_rate_models(
        self,
        request: DescribeRateModelsRequest,
        callback: Callable[[AsyncResult[DescribeRateModelsResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='rateModel',
            function='describeRateModels',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DescribeRateModelsResult,
                callback=callback,
                body=body,
            )
        )

    def describe_rate_models(
        self,
        request: DescribeRateModelsRequest,
    ) -> DescribeRateModelsResult:
        async_result = []
        with timeout(30):
            self._describe_rate_models(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_rate_models_async(
        self,
        request: DescribeRateModelsRequest,
    ) -> DescribeRateModelsResult:
        async_result = []
        self._describe_rate_models(
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

    def _get_rate_model(
        self,
        request: GetRateModelRequest,
        callback: Callable[[AsyncResult[GetRateModelResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='rateModel',
            function='getRateModel',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetRateModelResult,
                callback=callback,
                body=body,
            )
        )

    def get_rate_model(
        self,
        request: GetRateModelRequest,
    ) -> GetRateModelResult:
        async_result = []
        with timeout(30):
            self._get_rate_model(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_rate_model_async(
        self,
        request: GetRateModelRequest,
    ) -> GetRateModelResult:
        async_result = []
        self._get_rate_model(
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

    def _describe_rate_model_masters(
        self,
        request: DescribeRateModelMastersRequest,
        callback: Callable[[AsyncResult[DescribeRateModelMastersResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='rateModelMaster',
            function='describeRateModelMasters',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DescribeRateModelMastersResult,
                callback=callback,
                body=body,
            )
        )

    def describe_rate_model_masters(
        self,
        request: DescribeRateModelMastersRequest,
    ) -> DescribeRateModelMastersResult:
        async_result = []
        with timeout(30):
            self._describe_rate_model_masters(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_rate_model_masters_async(
        self,
        request: DescribeRateModelMastersRequest,
    ) -> DescribeRateModelMastersResult:
        async_result = []
        self._describe_rate_model_masters(
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

    def _create_rate_model_master(
        self,
        request: CreateRateModelMasterRequest,
        callback: Callable[[AsyncResult[CreateRateModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='rateModelMaster',
            function='createRateModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.name is not None:
            body["name"] = request.name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.target_inventory_model_id is not None:
            body["targetInventoryModelId"] = request.target_inventory_model_id
        if request.acquire_experience_suffix is not None:
            body["acquireExperienceSuffix"] = request.acquire_experience_suffix
        if request.material_inventory_model_id is not None:
            body["materialInventoryModelId"] = request.material_inventory_model_id
        if request.acquire_experience_hierarchy is not None:
            body["acquireExperienceHierarchy"] = [
                item
                for item in request.acquire_experience_hierarchy
            ]
        if request.experience_model_id is not None:
            body["experienceModelId"] = request.experience_model_id
        if request.bonus_rates is not None:
            body["bonusRates"] = [
                item.to_dict()
                for item in request.bonus_rates
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CreateRateModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def create_rate_model_master(
        self,
        request: CreateRateModelMasterRequest,
    ) -> CreateRateModelMasterResult:
        async_result = []
        with timeout(30):
            self._create_rate_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_rate_model_master_async(
        self,
        request: CreateRateModelMasterRequest,
    ) -> CreateRateModelMasterResult:
        async_result = []
        self._create_rate_model_master(
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

    def _get_rate_model_master(
        self,
        request: GetRateModelMasterRequest,
        callback: Callable[[AsyncResult[GetRateModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='rateModelMaster',
            function='getRateModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetRateModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def get_rate_model_master(
        self,
        request: GetRateModelMasterRequest,
    ) -> GetRateModelMasterResult:
        async_result = []
        with timeout(30):
            self._get_rate_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_rate_model_master_async(
        self,
        request: GetRateModelMasterRequest,
    ) -> GetRateModelMasterResult:
        async_result = []
        self._get_rate_model_master(
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

    def _update_rate_model_master(
        self,
        request: UpdateRateModelMasterRequest,
        callback: Callable[[AsyncResult[UpdateRateModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='rateModelMaster',
            function='updateRateModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.target_inventory_model_id is not None:
            body["targetInventoryModelId"] = request.target_inventory_model_id
        if request.acquire_experience_suffix is not None:
            body["acquireExperienceSuffix"] = request.acquire_experience_suffix
        if request.material_inventory_model_id is not None:
            body["materialInventoryModelId"] = request.material_inventory_model_id
        if request.acquire_experience_hierarchy is not None:
            body["acquireExperienceHierarchy"] = [
                item
                for item in request.acquire_experience_hierarchy
            ]
        if request.experience_model_id is not None:
            body["experienceModelId"] = request.experience_model_id
        if request.bonus_rates is not None:
            body["bonusRates"] = [
                item.to_dict()
                for item in request.bonus_rates
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UpdateRateModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def update_rate_model_master(
        self,
        request: UpdateRateModelMasterRequest,
    ) -> UpdateRateModelMasterResult:
        async_result = []
        with timeout(30):
            self._update_rate_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_rate_model_master_async(
        self,
        request: UpdateRateModelMasterRequest,
    ) -> UpdateRateModelMasterResult:
        async_result = []
        self._update_rate_model_master(
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

    def _delete_rate_model_master(
        self,
        request: DeleteRateModelMasterRequest,
        callback: Callable[[AsyncResult[DeleteRateModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='rateModelMaster',
            function='deleteRateModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DeleteRateModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def delete_rate_model_master(
        self,
        request: DeleteRateModelMasterRequest,
    ) -> DeleteRateModelMasterResult:
        async_result = []
        with timeout(30):
            self._delete_rate_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_rate_model_master_async(
        self,
        request: DeleteRateModelMasterRequest,
    ) -> DeleteRateModelMasterResult:
        async_result = []
        self._delete_rate_model_master(
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

    def _describe_unleash_rate_models(
        self,
        request: DescribeUnleashRateModelsRequest,
        callback: Callable[[AsyncResult[DescribeUnleashRateModelsResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='unleashRateModel',
            function='describeUnleashRateModels',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DescribeUnleashRateModelsResult,
                callback=callback,
                body=body,
            )
        )

    def describe_unleash_rate_models(
        self,
        request: DescribeUnleashRateModelsRequest,
    ) -> DescribeUnleashRateModelsResult:
        async_result = []
        with timeout(30):
            self._describe_unleash_rate_models(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_unleash_rate_models_async(
        self,
        request: DescribeUnleashRateModelsRequest,
    ) -> DescribeUnleashRateModelsResult:
        async_result = []
        self._describe_unleash_rate_models(
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

    def _get_unleash_rate_model(
        self,
        request: GetUnleashRateModelRequest,
        callback: Callable[[AsyncResult[GetUnleashRateModelResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='unleashRateModel',
            function='getUnleashRateModel',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetUnleashRateModelResult,
                callback=callback,
                body=body,
            )
        )

    def get_unleash_rate_model(
        self,
        request: GetUnleashRateModelRequest,
    ) -> GetUnleashRateModelResult:
        async_result = []
        with timeout(30):
            self._get_unleash_rate_model(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_unleash_rate_model_async(
        self,
        request: GetUnleashRateModelRequest,
    ) -> GetUnleashRateModelResult:
        async_result = []
        self._get_unleash_rate_model(
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

    def _describe_unleash_rate_model_masters(
        self,
        request: DescribeUnleashRateModelMastersRequest,
        callback: Callable[[AsyncResult[DescribeUnleashRateModelMastersResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='unleashRateModelMaster',
            function='describeUnleashRateModelMasters',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DescribeUnleashRateModelMastersResult,
                callback=callback,
                body=body,
            )
        )

    def describe_unleash_rate_model_masters(
        self,
        request: DescribeUnleashRateModelMastersRequest,
    ) -> DescribeUnleashRateModelMastersResult:
        async_result = []
        with timeout(30):
            self._describe_unleash_rate_model_masters(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_unleash_rate_model_masters_async(
        self,
        request: DescribeUnleashRateModelMastersRequest,
    ) -> DescribeUnleashRateModelMastersResult:
        async_result = []
        self._describe_unleash_rate_model_masters(
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

    def _create_unleash_rate_model_master(
        self,
        request: CreateUnleashRateModelMasterRequest,
        callback: Callable[[AsyncResult[CreateUnleashRateModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='unleashRateModelMaster',
            function='createUnleashRateModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.name is not None:
            body["name"] = request.name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.target_inventory_model_id is not None:
            body["targetInventoryModelId"] = request.target_inventory_model_id
        if request.grade_model_id is not None:
            body["gradeModelId"] = request.grade_model_id
        if request.grade_entries is not None:
            body["gradeEntries"] = [
                item.to_dict()
                for item in request.grade_entries
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CreateUnleashRateModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def create_unleash_rate_model_master(
        self,
        request: CreateUnleashRateModelMasterRequest,
    ) -> CreateUnleashRateModelMasterResult:
        async_result = []
        with timeout(30):
            self._create_unleash_rate_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_unleash_rate_model_master_async(
        self,
        request: CreateUnleashRateModelMasterRequest,
    ) -> CreateUnleashRateModelMasterResult:
        async_result = []
        self._create_unleash_rate_model_master(
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

    def _get_unleash_rate_model_master(
        self,
        request: GetUnleashRateModelMasterRequest,
        callback: Callable[[AsyncResult[GetUnleashRateModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='unleashRateModelMaster',
            function='getUnleashRateModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetUnleashRateModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def get_unleash_rate_model_master(
        self,
        request: GetUnleashRateModelMasterRequest,
    ) -> GetUnleashRateModelMasterResult:
        async_result = []
        with timeout(30):
            self._get_unleash_rate_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_unleash_rate_model_master_async(
        self,
        request: GetUnleashRateModelMasterRequest,
    ) -> GetUnleashRateModelMasterResult:
        async_result = []
        self._get_unleash_rate_model_master(
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

    def _update_unleash_rate_model_master(
        self,
        request: UpdateUnleashRateModelMasterRequest,
        callback: Callable[[AsyncResult[UpdateUnleashRateModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='unleashRateModelMaster',
            function='updateUnleashRateModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name
        if request.description is not None:
            body["description"] = request.description
        if request.metadata is not None:
            body["metadata"] = request.metadata
        if request.target_inventory_model_id is not None:
            body["targetInventoryModelId"] = request.target_inventory_model_id
        if request.grade_model_id is not None:
            body["gradeModelId"] = request.grade_model_id
        if request.grade_entries is not None:
            body["gradeEntries"] = [
                item.to_dict()
                for item in request.grade_entries
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UpdateUnleashRateModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def update_unleash_rate_model_master(
        self,
        request: UpdateUnleashRateModelMasterRequest,
    ) -> UpdateUnleashRateModelMasterResult:
        async_result = []
        with timeout(30):
            self._update_unleash_rate_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_unleash_rate_model_master_async(
        self,
        request: UpdateUnleashRateModelMasterRequest,
    ) -> UpdateUnleashRateModelMasterResult:
        async_result = []
        self._update_unleash_rate_model_master(
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

    def _delete_unleash_rate_model_master(
        self,
        request: DeleteUnleashRateModelMasterRequest,
        callback: Callable[[AsyncResult[DeleteUnleashRateModelMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='unleashRateModelMaster',
            function='deleteUnleashRateModelMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DeleteUnleashRateModelMasterResult,
                callback=callback,
                body=body,
            )
        )

    def delete_unleash_rate_model_master(
        self,
        request: DeleteUnleashRateModelMasterRequest,
    ) -> DeleteUnleashRateModelMasterResult:
        async_result = []
        with timeout(30):
            self._delete_unleash_rate_model_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_unleash_rate_model_master_async(
        self,
        request: DeleteUnleashRateModelMasterRequest,
    ) -> DeleteUnleashRateModelMasterResult:
        async_result = []
        self._delete_unleash_rate_model_master(
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

    def _direct_enhance(
        self,
        request: DirectEnhanceRequest,
        callback: Callable[[AsyncResult[DirectEnhanceResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='enhance',
            function='directEnhance',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token
        if request.target_item_set_id is not None:
            body["targetItemSetId"] = request.target_item_set_id
        if request.materials is not None:
            body["materials"] = [
                item.to_dict()
                for item in request.materials
            ]
        if request.config is not None:
            body["config"] = [
                item.to_dict()
                for item in request.config
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DirectEnhanceResult,
                callback=callback,
                body=body,
            )
        )

    def direct_enhance(
        self,
        request: DirectEnhanceRequest,
    ) -> DirectEnhanceResult:
        async_result = []
        with timeout(30):
            self._direct_enhance(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def direct_enhance_async(
        self,
        request: DirectEnhanceRequest,
    ) -> DirectEnhanceResult:
        async_result = []
        self._direct_enhance(
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

    def _direct_enhance_by_user_id(
        self,
        request: DirectEnhanceByUserIdRequest,
        callback: Callable[[AsyncResult[DirectEnhanceByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='enhance',
            function='directEnhanceByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.target_item_set_id is not None:
            body["targetItemSetId"] = request.target_item_set_id
        if request.materials is not None:
            body["materials"] = [
                item.to_dict()
                for item in request.materials
            ]
        if request.config is not None:
            body["config"] = [
                item.to_dict()
                for item in request.config
            ]
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DirectEnhanceByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def direct_enhance_by_user_id(
        self,
        request: DirectEnhanceByUserIdRequest,
    ) -> DirectEnhanceByUserIdResult:
        async_result = []
        with timeout(30):
            self._direct_enhance_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def direct_enhance_by_user_id_async(
        self,
        request: DirectEnhanceByUserIdRequest,
    ) -> DirectEnhanceByUserIdResult:
        async_result = []
        self._direct_enhance_by_user_id(
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

    def _direct_enhance_by_stamp_sheet(
        self,
        request: DirectEnhanceByStampSheetRequest,
        callback: Callable[[AsyncResult[DirectEnhanceByStampSheetResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='enhance',
            function='directEnhanceByStampSheet',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_sheet is not None:
            body["stampSheet"] = request.stamp_sheet
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DirectEnhanceByStampSheetResult,
                callback=callback,
                body=body,
            )
        )

    def direct_enhance_by_stamp_sheet(
        self,
        request: DirectEnhanceByStampSheetRequest,
    ) -> DirectEnhanceByStampSheetResult:
        async_result = []
        with timeout(30):
            self._direct_enhance_by_stamp_sheet(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def direct_enhance_by_stamp_sheet_async(
        self,
        request: DirectEnhanceByStampSheetRequest,
    ) -> DirectEnhanceByStampSheetResult:
        async_result = []
        self._direct_enhance_by_stamp_sheet(
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

    def _unleash(
        self,
        request: UnleashRequest,
        callback: Callable[[AsyncResult[UnleashResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='enhance',
            function='unleash',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token
        if request.target_item_set_id is not None:
            body["targetItemSetId"] = request.target_item_set_id
        if request.materials is not None:
            body["materials"] = [
                item
                for item in request.materials
            ]
        if request.config is not None:
            body["config"] = [
                item.to_dict()
                for item in request.config
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UnleashResult,
                callback=callback,
                body=body,
            )
        )

    def unleash(
        self,
        request: UnleashRequest,
    ) -> UnleashResult:
        async_result = []
        with timeout(30):
            self._unleash(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def unleash_async(
        self,
        request: UnleashRequest,
    ) -> UnleashResult:
        async_result = []
        self._unleash(
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

    def _unleash_by_user_id(
        self,
        request: UnleashByUserIdRequest,
        callback: Callable[[AsyncResult[UnleashByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='enhance',
            function='unleashByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.target_item_set_id is not None:
            body["targetItemSetId"] = request.target_item_set_id
        if request.materials is not None:
            body["materials"] = [
                item
                for item in request.materials
            ]
        if request.config is not None:
            body["config"] = [
                item.to_dict()
                for item in request.config
            ]
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UnleashByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def unleash_by_user_id(
        self,
        request: UnleashByUserIdRequest,
    ) -> UnleashByUserIdResult:
        async_result = []
        with timeout(30):
            self._unleash_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def unleash_by_user_id_async(
        self,
        request: UnleashByUserIdRequest,
    ) -> UnleashByUserIdResult:
        async_result = []
        self._unleash_by_user_id(
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

    def _unleash_by_stamp_sheet(
        self,
        request: UnleashByStampSheetRequest,
        callback: Callable[[AsyncResult[UnleashByStampSheetResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='enhance',
            function='unleashByStampSheet',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_sheet is not None:
            body["stampSheet"] = request.stamp_sheet
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UnleashByStampSheetResult,
                callback=callback,
                body=body,
            )
        )

    def unleash_by_stamp_sheet(
        self,
        request: UnleashByStampSheetRequest,
    ) -> UnleashByStampSheetResult:
        async_result = []
        with timeout(30):
            self._unleash_by_stamp_sheet(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def unleash_by_stamp_sheet_async(
        self,
        request: UnleashByStampSheetRequest,
    ) -> UnleashByStampSheetResult:
        async_result = []
        self._unleash_by_stamp_sheet(
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

    def _create_progress_by_user_id(
        self,
        request: CreateProgressByUserIdRequest,
        callback: Callable[[AsyncResult[CreateProgressByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='createProgressByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.rate_name is not None:
            body["rateName"] = request.rate_name
        if request.target_item_set_id is not None:
            body["targetItemSetId"] = request.target_item_set_id
        if request.materials is not None:
            body["materials"] = [
                item.to_dict()
                for item in request.materials
            ]
        if request.force is not None:
            body["force"] = request.force
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CreateProgressByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def create_progress_by_user_id(
        self,
        request: CreateProgressByUserIdRequest,
    ) -> CreateProgressByUserIdResult:
        async_result = []
        with timeout(30):
            self._create_progress_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_progress_by_user_id_async(
        self,
        request: CreateProgressByUserIdRequest,
    ) -> CreateProgressByUserIdResult:
        async_result = []
        self._create_progress_by_user_id(
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

    def _get_progress(
        self,
        request: GetProgressRequest,
        callback: Callable[[AsyncResult[GetProgressResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='getProgress',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetProgressResult,
                callback=callback,
                body=body,
            )
        )

    def get_progress(
        self,
        request: GetProgressRequest,
    ) -> GetProgressResult:
        async_result = []
        with timeout(30):
            self._get_progress(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_progress_async(
        self,
        request: GetProgressRequest,
    ) -> GetProgressResult:
        async_result = []
        self._get_progress(
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

    def _get_progress_by_user_id(
        self,
        request: GetProgressByUserIdRequest,
        callback: Callable[[AsyncResult[GetProgressByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='getProgressByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetProgressByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def get_progress_by_user_id(
        self,
        request: GetProgressByUserIdRequest,
    ) -> GetProgressByUserIdResult:
        async_result = []
        with timeout(30):
            self._get_progress_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_progress_by_user_id_async(
        self,
        request: GetProgressByUserIdRequest,
    ) -> GetProgressByUserIdResult:
        async_result = []
        self._get_progress_by_user_id(
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

    def _start(
        self,
        request: StartRequest,
        callback: Callable[[AsyncResult[StartResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='start',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name
        if request.target_item_set_id is not None:
            body["targetItemSetId"] = request.target_item_set_id
        if request.materials is not None:
            body["materials"] = [
                item.to_dict()
                for item in request.materials
            ]
        if request.access_token is not None:
            body["accessToken"] = request.access_token
        if request.force is not None:
            body["force"] = request.force
        if request.config is not None:
            body["config"] = [
                item.to_dict()
                for item in request.config
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=StartResult,
                callback=callback,
                body=body,
            )
        )

    def start(
        self,
        request: StartRequest,
    ) -> StartResult:
        async_result = []
        with timeout(30):
            self._start(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def start_async(
        self,
        request: StartRequest,
    ) -> StartResult:
        async_result = []
        self._start(
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

    def _start_by_user_id(
        self,
        request: StartByUserIdRequest,
        callback: Callable[[AsyncResult[StartByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='startByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.rate_name is not None:
            body["rateName"] = request.rate_name
        if request.target_item_set_id is not None:
            body["targetItemSetId"] = request.target_item_set_id
        if request.materials is not None:
            body["materials"] = [
                item.to_dict()
                for item in request.materials
            ]
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.force is not None:
            body["force"] = request.force
        if request.config is not None:
            body["config"] = [
                item.to_dict()
                for item in request.config
            ]
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=StartByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def start_by_user_id(
        self,
        request: StartByUserIdRequest,
    ) -> StartByUserIdResult:
        async_result = []
        with timeout(30):
            self._start_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def start_by_user_id_async(
        self,
        request: StartByUserIdRequest,
    ) -> StartByUserIdResult:
        async_result = []
        self._start_by_user_id(
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

    def _end(
        self,
        request: EndRequest,
        callback: Callable[[AsyncResult[EndResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='end',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token
        if request.config is not None:
            body["config"] = [
                item.to_dict()
                for item in request.config
            ]

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=EndResult,
                callback=callback,
                body=body,
            )
        )

    def end(
        self,
        request: EndRequest,
    ) -> EndResult:
        async_result = []
        with timeout(30):
            self._end(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def end_async(
        self,
        request: EndRequest,
    ) -> EndResult:
        async_result = []
        self._end(
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

    def _end_by_user_id(
        self,
        request: EndByUserIdRequest,
        callback: Callable[[AsyncResult[EndByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='endByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.config is not None:
            body["config"] = [
                item.to_dict()
                for item in request.config
            ]
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=EndByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def end_by_user_id(
        self,
        request: EndByUserIdRequest,
    ) -> EndByUserIdResult:
        async_result = []
        with timeout(30):
            self._end_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def end_by_user_id_async(
        self,
        request: EndByUserIdRequest,
    ) -> EndByUserIdResult:
        async_result = []
        self._end_by_user_id(
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

    def _delete_progress(
        self,
        request: DeleteProgressRequest,
        callback: Callable[[AsyncResult[DeleteProgressResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='deleteProgress',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.access_token is not None:
            body["accessToken"] = request.access_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.access_token:
            body["xGs2AccessToken"] = request.access_token
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DeleteProgressResult,
                callback=callback,
                body=body,
            )
        )

    def delete_progress(
        self,
        request: DeleteProgressRequest,
    ) -> DeleteProgressResult:
        async_result = []
        with timeout(30):
            self._delete_progress(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_progress_async(
        self,
        request: DeleteProgressRequest,
    ) -> DeleteProgressResult:
        async_result = []
        self._delete_progress(
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

    def _delete_progress_by_user_id(
        self,
        request: DeleteProgressByUserIdRequest,
        callback: Callable[[AsyncResult[DeleteProgressByUserIdResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='deleteProgressByUserId',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.user_id is not None:
            body["userId"] = request.user_id
        if request.time_offset_token is not None:
            body["timeOffsetToken"] = request.time_offset_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id
        if request.duplication_avoider:
            body["xGs2DuplicationAvoider"] = request.duplication_avoider

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DeleteProgressByUserIdResult,
                callback=callback,
                body=body,
            )
        )

    def delete_progress_by_user_id(
        self,
        request: DeleteProgressByUserIdRequest,
    ) -> DeleteProgressByUserIdResult:
        async_result = []
        with timeout(30):
            self._delete_progress_by_user_id(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_progress_by_user_id_async(
        self,
        request: DeleteProgressByUserIdRequest,
    ) -> DeleteProgressByUserIdResult:
        async_result = []
        self._delete_progress_by_user_id(
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

    def _create_progress_by_stamp_sheet(
        self,
        request: CreateProgressByStampSheetRequest,
        callback: Callable[[AsyncResult[CreateProgressByStampSheetResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='createProgressByStampSheet',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_sheet is not None:
            body["stampSheet"] = request.stamp_sheet
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=CreateProgressByStampSheetResult,
                callback=callback,
                body=body,
            )
        )

    def create_progress_by_stamp_sheet(
        self,
        request: CreateProgressByStampSheetRequest,
    ) -> CreateProgressByStampSheetResult:
        async_result = []
        with timeout(30):
            self._create_progress_by_stamp_sheet(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def create_progress_by_stamp_sheet_async(
        self,
        request: CreateProgressByStampSheetRequest,
    ) -> CreateProgressByStampSheetResult:
        async_result = []
        self._create_progress_by_stamp_sheet(
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

    def _delete_progress_by_stamp_task(
        self,
        request: DeleteProgressByStampTaskRequest,
        callback: Callable[[AsyncResult[DeleteProgressByStampTaskResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='progress',
            function='deleteProgressByStampTask',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.stamp_task is not None:
            body["stampTask"] = request.stamp_task
        if request.key_id is not None:
            body["keyId"] = request.key_id

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=DeleteProgressByStampTaskResult,
                callback=callback,
                body=body,
            )
        )

    def delete_progress_by_stamp_task(
        self,
        request: DeleteProgressByStampTaskRequest,
    ) -> DeleteProgressByStampTaskResult:
        async_result = []
        with timeout(30):
            self._delete_progress_by_stamp_task(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_progress_by_stamp_task_async(
        self,
        request: DeleteProgressByStampTaskRequest,
    ) -> DeleteProgressByStampTaskResult:
        async_result = []
        self._delete_progress_by_stamp_task(
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

    def _export_master(
        self,
        request: ExportMasterRequest,
        callback: Callable[[AsyncResult[ExportMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='currentRateMaster',
            function='exportMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=ExportMasterResult,
                callback=callback,
                body=body,
            )
        )

    def export_master(
        self,
        request: ExportMasterRequest,
    ) -> ExportMasterResult:
        async_result = []
        with timeout(30):
            self._export_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def export_master_async(
        self,
        request: ExportMasterRequest,
    ) -> ExportMasterResult:
        async_result = []
        self._export_master(
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

    def _get_current_rate_master(
        self,
        request: GetCurrentRateMasterRequest,
        callback: Callable[[AsyncResult[GetCurrentRateMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='currentRateMaster',
            function='getCurrentRateMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=GetCurrentRateMasterResult,
                callback=callback,
                body=body,
            )
        )

    def get_current_rate_master(
        self,
        request: GetCurrentRateMasterRequest,
    ) -> GetCurrentRateMasterResult:
        async_result = []
        with timeout(30):
            self._get_current_rate_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_current_rate_master_async(
        self,
        request: GetCurrentRateMasterRequest,
    ) -> GetCurrentRateMasterResult:
        async_result = []
        self._get_current_rate_master(
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

    def _pre_update_current_rate_master(
        self,
        request: PreUpdateCurrentRateMasterRequest,
        callback: Callable[[AsyncResult[PreUpdateCurrentRateMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='currentRateMaster',
            function='preUpdateCurrentRateMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=PreUpdateCurrentRateMasterResult,
                callback=callback,
                body=body,
            )
        )

    def pre_update_current_rate_master(
        self,
        request: PreUpdateCurrentRateMasterRequest,
    ) -> PreUpdateCurrentRateMasterResult:
        async_result = []
        with timeout(30):
            self._pre_update_current_rate_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def pre_update_current_rate_master_async(
        self,
        request: PreUpdateCurrentRateMasterRequest,
    ) -> PreUpdateCurrentRateMasterResult:
        async_result = []
        self._pre_update_current_rate_master(
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

    def _update_current_rate_master(
        self,
        request: UpdateCurrentRateMasterRequest,
        callback: Callable[[AsyncResult[UpdateCurrentRateMasterResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='currentRateMaster',
            function='updateCurrentRateMaster',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.mode is not None:
            body["mode"] = request.mode
        if request.settings is not None:
            body["settings"] = request.settings
        if request.upload_token is not None:
            body["uploadToken"] = request.upload_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UpdateCurrentRateMasterResult,
                callback=callback,
                body=body,
            )
        )

    def update_current_rate_master(
        self,
        request: UpdateCurrentRateMasterRequest,
    ) -> UpdateCurrentRateMasterResult:
        async_result = []
        with timeout(30):
            self._update_current_rate_master(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_current_rate_master_async(
        self,
        request: UpdateCurrentRateMasterRequest,
    ) -> UpdateCurrentRateMasterResult:
        async_result = []
        self._update_current_rate_master(
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

    def _update_current_rate_master_from_git_hub(
        self,
        request: UpdateCurrentRateMasterFromGitHubRequest,
        callback: Callable[[AsyncResult[UpdateCurrentRateMasterFromGitHubResult]], None],
    ):
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service="enhance",
            component='currentRateMaster',
            function='updateCurrentRateMasterFromGitHub',
            request_id=request_id,
        )

        if request.context_stack:
            body['contextStack'] = str(request.context_stack)
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.checkout_setting is not None:
            body["checkoutSetting"] = request.checkout_setting.to_dict()

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            web_socket.NetworkJob(
                request_id=request_id,
                result_type=UpdateCurrentRateMasterFromGitHubResult,
                callback=callback,
                body=body,
            )
        )

    def update_current_rate_master_from_git_hub(
        self,
        request: UpdateCurrentRateMasterFromGitHubRequest,
    ) -> UpdateCurrentRateMasterFromGitHubResult:
        async_result = []
        with timeout(30):
            self._update_current_rate_master_from_git_hub(
                request,
                lambda result: async_result.append(result),
            )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_current_rate_master_from_git_hub_async(
        self,
        request: UpdateCurrentRateMasterFromGitHubRequest,
    ) -> UpdateCurrentRateMasterFromGitHubResult:
        async_result = []
        self._update_current_rate_master_from_git_hub(
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