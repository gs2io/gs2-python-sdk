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
from ranking.rest import Gs2RankingRestClient
from core.model import Gs2Constant
import private.ranking.request as request_model
import private.ranking.result as result_model


class Gs2RankingPrivateRestClient(Gs2RankingRestClient):

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
            service='ranking',
            region=self.session.region,
        ) + "/system/{ownerId}".format(
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

    def _put_score_impl(
        self,
        request: request_model.PutScoreImplRequest,
        callback: Callable[[AsyncResult[result_model.PutScoreImplResult]], None],
        is_blocking: bool,
    ):
        """
        スコア登録の遅延実行処理
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='ranking',
            region=self.session.region,
        ) + "/system/{ownerId}/{namespaceName}/category/{categoryName}/score/put".format(
            ownerId=request.owner_id if request.owner_id is not None and request.owner_id != '' else 'null',
            namespaceName=request.namespace_name if request.namespace_name is not None and request.namespace_name != '' else 'null',
            categoryName=request.category_name if request.category_name is not None and request.category_name != '' else 'null',
        )
        headers = self._create_authorized_headers()
        body = {
            'contextStack': request.context_stack,
        }
        if request.score is not None:
            body["score"] = request.score.to_dict() if request.score is not None else None
        if request.page_token is not None:
            body["pageToken"] = request.page_token

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='POST',
            result_type=result_model.PutScoreImplResult,
            callback=callback,
            headers=headers,
            body=body,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def put_score_impl(
        self,
        request: request_model.PutScoreImplRequest,
    ) -> result_model.PutScoreImplResult:
        async_result = []
        with timeout(30):
            self._put_score_impl(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def put_score_impl_async(
        self,
        request: request_model.PutScoreImplRequest,
    ) -> result_model.PutScoreImplResult:
        async_result = []
        self._put_score_impl(
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

    def _calc_all_ranking(
        self,
        request: request_model.CalcAllRankingRequest,
        callback: Callable[[AsyncResult[result_model.CalcAllRankingResult]], None],
        is_blocking: bool,
    ):
        """
        ランキングの計算処理
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='ranking',
            region=self.session.region,
        ) + "/system/calc/ranking"
        headers = self._create_authorized_headers()
        body = {
            'contextStack': request.context_stack,
        }

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='POST',
            result_type=result_model.CalcAllRankingResult,
            callback=callback,
            headers=headers,
            body=body,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def calc_all_ranking(
        self,
        request: request_model.CalcAllRankingRequest,
    ) -> result_model.CalcAllRankingResult:
        async_result = []
        with timeout(30):
            self._calc_all_ranking(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def calc_all_ranking_async(
        self,
        request: request_model.CalcAllRankingRequest,
    ) -> result_model.CalcAllRankingResult:
        async_result = []
        self._calc_all_ranking(
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

    def _calc_ranking(
        self,
        request: request_model.CalcRankingRequest,
        callback: Callable[[AsyncResult[result_model.CalcRankingResult]], None],
        is_blocking: bool,
    ):
        """
        ランキングの計算処理
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='ranking',
            region=self.session.region,
        ) + "/system/{ownerId}/{namespaceName}/category/{categoryName}/calc/ranking".format(
            ownerId=request.owner_id if request.owner_id is not None and request.owner_id != '' else 'null',
            namespaceName=request.namespace_name if request.namespace_name is not None and request.namespace_name != '' else 'null',
            categoryName=request.category_name if request.category_name is not None and request.category_name != '' else 'null',
        )
        headers = self._create_authorized_headers()
        body = {
            'contextStack': request.context_stack,
        }
        if request.calculate_started_at is not None:
            body["calculateStartedAt"] = request.calculate_started_at
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.force is not None:
            body["force"] = request.force

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='POST',
            result_type=result_model.CalcRankingResult,
            callback=callback,
            headers=headers,
            body=body,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def calc_ranking(
        self,
        request: request_model.CalcRankingRequest,
    ) -> result_model.CalcRankingResult:
        async_result = []
        with timeout(30):
            self._calc_ranking(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def calc_ranking_async(
        self,
        request: request_model.CalcRankingRequest,
    ) -> result_model.CalcRankingResult:
        async_result = []
        self._calc_ranking(
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

    def _calc_index(
        self,
        request: request_model.CalcIndexRequest,
        callback: Callable[[AsyncResult[result_model.CalcIndexResult]], None],
        is_blocking: bool,
    ):
        """
        ランキングのインデックス計算処理
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='ranking',
            region=self.session.region,
        ) + "/system/{ownerId}/{namespaceName}/category/{categoryName}/calc/index".format(
            ownerId=request.owner_id if request.owner_id is not None and request.owner_id != '' else 'null',
            namespaceName=request.namespace_name if request.namespace_name is not None and request.namespace_name != '' else 'null',
            categoryName=request.category_name if request.category_name is not None and request.category_name != '' else 'null',
        )
        headers = self._create_authorized_headers()
        body = {
            'contextStack': request.context_stack,
        }
        if request.calculate_started_at is not None:
            body["calculateStartedAt"] = request.calculate_started_at

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='POST',
            result_type=result_model.CalcIndexResult,
            callback=callback,
            headers=headers,
            body=body,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def calc_index(
        self,
        request: request_model.CalcIndexRequest,
    ) -> result_model.CalcIndexResult:
        async_result = []
        with timeout(30):
            self._calc_index(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def calc_index_async(
        self,
        request: request_model.CalcIndexRequest,
    ) -> result_model.CalcIndexResult:
        async_result = []
        self._calc_index(
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

    def _compaction(
        self,
        request: request_model.CompactionRequest,
        callback: Callable[[AsyncResult[result_model.CompactionResult]], None],
        is_blocking: bool,
    ):
        """
        テーブルのコンパクション処理
        :param request: Request
        :param callback: Callback
        """
        url = Gs2Constant.ENDPOINT_HOST.format(
            service='ranking',
            region=self.session.region,
        ) + "/system/{ownerId}/{namespaceName}/category/{categoryName}/calc/compaction".format(
            ownerId=request.owner_id if request.owner_id is not None and request.owner_id != '' else 'null',
            namespaceName=request.namespace_name if request.namespace_name is not None and request.namespace_name != '' else 'null',
            categoryName=request.category_name if request.category_name is not None and request.category_name != '' else 'null',
        )
        headers = self._create_authorized_headers()
        body = {
            'contextStack': request.context_stack,
        }

        if request.request_id:
            headers["X-GS2-REQUEST-ID"] = request.request_id

        _job = NetworkJob(
            url=url,
            method='POST',
            result_type=result_model.CompactionResult,
            callback=callback,
            headers=headers,
            body=body,
        )

        self.session.send(
            job=_job,
            is_blocking=is_blocking,
        )

    def compaction(
        self,
        request: request_model.CompactionRequest,
    ) -> result_model.CompactionResult:
        async_result = []
        with timeout(30):
            self._compaction(
                request,
                lambda result: async_result.append(result),
                is_blocking=True,
            )

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result


    async def compaction_async(
        self,
        request: request_model.CompactionRequest,
    ) -> result_model.CompactionResult:
        async_result = []
        self._compaction(
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
