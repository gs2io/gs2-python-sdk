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
from watch.web_socket import Gs2WatchWebSocketClient
import private.watch.request as request_model
import private.watch.result as result_model


class Gs2WatchPrivateWebSocketClient(Gs2WatchWebSocketClient):

    SERVICE = "watch"

    def __init__(
        self,
        session: Gs2WebSocketSession,
    ):
        super().__init__(session)

    def _describe_billing_activities_by_owner_id(
        self,
        request: request_model.DescribeBillingActivitiesByOwnerIdRequest,
        callback: Callable[[AsyncResult[result_model.DescribeBillingActivitiesByOwnerIdResult]], None],
    ):
        """
        オーナーIDを指定して請求にまつわるアクティビティの一覧を取得
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='billingActivity',
            function='describeBillingActivitiesByOwnerId',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.year is not None:
            body["year"] = request.year
        if request.month is not None:
            body["month"] = request.month
        if request.service is not None:
            body["service"] = request.service
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.limit is not None:
            body["limit"] = request.limit

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.DescribeBillingActivitiesByOwnerIdResult,
                callback=callback,
                body=body,
            )
        )

    def describe_billing_activities_by_owner_id(
        self,
        request: request_model.DescribeBillingActivitiesByOwnerIdRequest,
    ) -> result_model.DescribeBillingActivitiesByOwnerIdResult:
        async_result = []
        self._describe_billing_activities_by_owner_id(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result
