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
from project.web_socket import Gs2ProjectWebSocketClient
import private.project.request as request_model
import private.project.result as result_model


class Gs2ProjectPrivateWebSocketClient(Gs2ProjectWebSocketClient):

    SERVICE = "project"

    def __init__(
        self,
        session: Gs2WebSocketSession,
    ):
        super().__init__(session)

    def _describe_accounts(
        self,
        request: request_model.DescribeAccountsRequest,
        callback: Callable[[AsyncResult[result_model.DescribeAccountsResult]], None],
    ):
        """
        GS2アカウントの一覧を取得します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='account',
            function='describeAccounts',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.DescribeAccountsResult,
                callback=callback,
                body=body,
            )
        )

    def describe_accounts(
        self,
        request: request_model.DescribeAccountsRequest,
    ) -> result_model.DescribeAccountsResult:
        async_result = []
        self._describe_accounts(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_accounts_async(
        self,
        request: request_model.DescribeAccountsRequest,
    ) -> result_model.DescribeAccountsResult:
        async_result = []
        self._describe_accounts(
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

    def _get_account_by_account_name(
        self,
        request: request_model.GetAccountByAccountNameRequest,
        callback: Callable[[AsyncResult[result_model.GetAccountByAccountNameResult]], None],
    ):
        """
        GS2アカウントを取得します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='account',
            function='getAccountByAccountName',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.account_name is not None:
            body["accountName"] = request.account_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.GetAccountByAccountNameResult,
                callback=callback,
                body=body,
            )
        )

    def get_account_by_account_name(
        self,
        request: request_model.GetAccountByAccountNameRequest,
    ) -> result_model.GetAccountByAccountNameResult:
        async_result = []
        self._get_account_by_account_name(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def get_account_by_account_name_async(
        self,
        request: request_model.GetAccountByAccountNameRequest,
    ) -> result_model.GetAccountByAccountNameResult:
        async_result = []
        self._get_account_by_account_name(
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

    def _update_account_by_account_name(
        self,
        request: request_model.UpdateAccountByAccountNameRequest,
        callback: Callable[[AsyncResult[result_model.UpdateAccountByAccountNameResult]], None],
    ):
        """
        GS2アカウントを更新します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='account',
            function='updateAccountByAccountName',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.account_name is not None:
            body["accountName"] = request.account_name
        if request.email is not None:
            body["email"] = request.email
        if request.full_name is not None:
            body["fullName"] = request.full_name
        if request.company_name is not None:
            body["companyName"] = request.company_name
        if request.password is not None:
            body["password"] = request.password

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.UpdateAccountByAccountNameResult,
                callback=callback,
                body=body,
            )
        )

    def update_account_by_account_name(
        self,
        request: request_model.UpdateAccountByAccountNameRequest,
    ) -> result_model.UpdateAccountByAccountNameResult:
        async_result = []
        self._update_account_by_account_name(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def update_account_by_account_name_async(
        self,
        request: request_model.UpdateAccountByAccountNameRequest,
    ) -> result_model.UpdateAccountByAccountNameResult:
        async_result = []
        self._update_account_by_account_name(
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

    def _delete_account_by_account_name(
        self,
        request: request_model.DeleteAccountByAccountNameRequest,
        callback: Callable[[AsyncResult[result_model.DeleteAccountByAccountNameResult]], None],
    ):
        """
        GS2アカウントを削除します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='account',
            function='deleteAccountByAccountName',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.account_name is not None:
            body["accountName"] = request.account_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.DeleteAccountByAccountNameResult,
                callback=callback,
                body=body,
            )
        )

    def delete_account_by_account_name(
        self,
        request: request_model.DeleteAccountByAccountNameRequest,
    ) -> result_model.DeleteAccountByAccountNameResult:
        async_result = []
        self._delete_account_by_account_name(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_account_by_account_name_async(
        self,
        request: request_model.DeleteAccountByAccountNameRequest,
    ) -> result_model.DeleteAccountByAccountNameResult:
        async_result = []
        self._delete_account_by_account_name(
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

    def _delete_account_by_email(
        self,
        request: request_model.DeleteAccountByEmailRequest,
        callback: Callable[[AsyncResult[result_model.DeleteAccountByEmailResult]], None],
    ):
        """
        GS2アカウントを削除します
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='account',
            function='deleteAccountByEmail',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.email is not None:
            body["email"] = request.email

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.DeleteAccountByEmailResult,
                callback=callback,
                body=body,
            )
        )

    def delete_account_by_email(
        self,
        request: request_model.DeleteAccountByEmailRequest,
    ) -> result_model.DeleteAccountByEmailResult:
        async_result = []
        self._delete_account_by_email(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def delete_account_by_email_async(
        self,
        request: request_model.DeleteAccountByEmailRequest,
    ) -> result_model.DeleteAccountByEmailResult:
        async_result = []
        self._delete_account_by_email(
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
