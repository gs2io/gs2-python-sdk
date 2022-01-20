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
from watch.rest import Gs2WatchRestClient
from core.model import Gs2Constant
import private.watch.request as request_model
import private.watch.result as result_model


class Gs2WatchPrivateRestClient(Gs2WatchRestClient):

    def __init__(self, session: Gs2RestSession):
        super().__init__(session)

    def _describe_billing_activities_by_owner_id(
        self,
        request: request_model.DescribeBillingActivitiesByOwnerIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeBillingActivitiesByOwnerIdResult]], None],
        is_blocking: bool,
    ):
        """
        オーナーIDを指定して請求にまつわるアクティビティの一覧を取得
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='watch',
            region=self.session.region,
        ) + "/system/{ownerId}/{year}/{month}".format(
            ownerId=request.owner_id if request.owner_id is not None and request.owner_id != '' else 'null',
            year=request.year if request.year is not None and request.year != '' else 'null',
            month=request.month if request.month is not None and request.month != '' else 'null',
        )
        headers = self._create_authorized_headers()
        query_strings = {
            'contextStack': request.context_stack,
        }
        if request.service is not None:
            query_strings["service"] = request.service
        if request.page_token is not None:
            query_strings["pageToken"] = request.page_token
        if request.limit is not None:
            query_strings["limit"] = request.limit

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='GET',
            result_type=result_model.DescribeBillingActivitiesByOwnerIdResult,
            callback=callback,
            headers=headers,
            query_strings=query_strings,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def describe_billing_activities_by_owner_id(
        self,
        request: request_model.DescribeBillingActivitiesByOwnerIdRequest,
    ) -> result_model.DescribeBillingActivitiesByOwnerIdResult:
        async_result = []
        with timeout(30):
            self._describe_billing_activities_by_owner_id(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def describe_billing_activities_by_owner_id_async(
        self,
        request: request_model.DescribeBillingActivitiesByOwnerIdRequest,
    ) -> result_model.DescribeBillingActivitiesByOwnerIdResult:
        async_result = []
        self._describe_billing_activities_by_owner_id(
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
