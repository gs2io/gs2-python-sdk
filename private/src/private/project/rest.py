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
from project.rest import Gs2ProjectRestClient
from core.model import Gs2Constant
import private.project.request as request_model
import private.project.result as result_model


class Gs2ProjectPrivateRestClient(Gs2ProjectRestClient):

    def __init__(self, session: Gs2RestSession):
        super().__init__(session)

    def _describe_accounts(
        self,
        request: request_model.DescribeAccountsRequest,
        callback: Callable[[AsyncResult[result_model.DescribeAccountsResult]], None],
        is_blocking: bool,
    ):
        """
        GS2アカウントの一覧を取得します
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='project',
            region=self.session.region,
        ) + "/system/account"
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
            result_type=result_model.DescribeAccountsResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def describe_accounts(
        self,
        request: request_model.DescribeAccountsRequest,
    ) -> result_model.DescribeAccountsResult:
        async_result = []
        with timeout(30):
            self._describe_accounts(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

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
            is_blocking=False,
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
        is_blocking: bool,
    ):
        """
        GS2アカウントを取得します
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='project',
            region=self.session.region,
        ) + "/account/{accountName}".format(
            accountName=request.account_name if request.account_name is not None and request.account_name != '' else 'null',
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
            result_type=result_model.GetAccountByAccountNameResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def get_account_by_account_name(
        self,
        request: request_model.GetAccountByAccountNameRequest,
    ) -> result_model.GetAccountByAccountNameResult:
        async_result = []
        with timeout(30):
            self._get_account_by_account_name(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

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
            is_blocking=False,
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
        is_blocking: bool,
    ):
        """
        GS2アカウントを更新します
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='project',
            region=self.session.region,
        ) + "/system/account/{accountName}".format(
            accountName=request.account_name if request.account_name is not None and request.account_name != '' else 'null',
        )
        headers = self._create_authorized_headers()
        body = {
            "email": request.email,
            "fullName": request.full_name,
            "password": request.password,
            'contextStack': request.context_stack,
        }
        if request.company_name is not None:
            body["companyName"] = request.company_name

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='PUT',
            result_type=result_model.UpdateAccountByAccountNameResult,
            callback=callback,
            headers=headers,
            body=body,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def update_account_by_account_name(
        self,
        request: request_model.UpdateAccountByAccountNameRequest,
    ) -> result_model.UpdateAccountByAccountNameResult:
        async_result = []
        with timeout(30):
            self._update_account_by_account_name(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

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
            is_blocking=False,
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
        is_blocking: bool,
    ):
        """
        GS2アカウントを削除します
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='project',
            region=self.session.region,
        ) + "/system/account/{accountName}".format(
            accountName=request.account_name if request.account_name is not None and request.account_name != '' else 'null',
        )
        headers = self._create_authorized_headers()
        query_strings = {
            'contextStack': request.context_stack,
        }

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='DELETE',
            result_type=result_model.DeleteAccountByAccountNameResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def delete_account_by_account_name(
        self,
        request: request_model.DeleteAccountByAccountNameRequest,
    ) -> result_model.DeleteAccountByAccountNameResult:
        async_result = []
        with timeout(30):
            self._delete_account_by_account_name(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

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
            is_blocking=False,
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
        is_blocking: bool,
    ):
        """
        GS2アカウントを削除します
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='project',
            region=self.session.region,
        ) + "/system/account/email/{email}".format(
            email=request.email if request.email is not None and request.email != '' else 'null',
        )
        headers = self._create_authorized_headers()
        query_strings = {
            'contextStack': request.context_stack,
        }

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='DELETE',
            result_type=result_model.DeleteAccountByEmailResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def delete_account_by_email(
        self,
        request: request_model.DeleteAccountByEmailRequest,
    ) -> result_model.DeleteAccountByEmailResult:
        async_result = []
        with timeout(30):
            self._delete_account_by_email(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

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
            is_blocking=False,
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result
