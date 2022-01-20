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
from ranking.web_socket import Gs2RankingWebSocketClient
import private.ranking.request as request_model
import private.ranking.result as result_model


class Gs2RankingPrivateWebSocketClient(Gs2RankingWebSocketClient):

    SERVICE = "ranking"

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

    def _put_score_impl(
        self,
        request: request_model.PutScoreImplRequest,
        callback: Callable[[AsyncResult[result_model.PutScoreImplResult]], None],
    ):
        """
        スコア登録の遅延実行処理
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='ranking',
            function='putScoreImpl',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.category_name is not None:
            body["categoryName"] = request.category_name
        if request.score is not None:
            body["score"] = request.score.to_dict() if request.score is not None else None
        if request.page_token is not None:
            body["pageToken"] = request.page_token

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.PutScoreImplResult,
                callback=callback,
                body=body,
            )
        )

    def put_score_impl(
        self,
        request: request_model.PutScoreImplRequest,
    ) -> result_model.PutScoreImplResult:
        async_result = []
        self._put_score_impl(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
    ):
        """
        ランキングの計算処理
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='ranking',
            function='calcAllRanking',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.CalcAllRankingResult,
                callback=callback,
                body=body,
            )
        )

    def calc_all_ranking(
        self,
        request: request_model.CalcAllRankingRequest,
    ) -> result_model.CalcAllRankingResult:
        async_result = []
        self._calc_all_ranking(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
    ):
        """
        ランキングの計算処理
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='ranking',
            function='calcRanking',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.category_name is not None:
            body["categoryName"] = request.category_name
        if request.calculate_started_at is not None:
            body["calculateStartedAt"] = request.calculate_started_at
        if request.page_token is not None:
            body["pageToken"] = request.page_token
        if request.force is not None:
            body["force"] = request.force

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.CalcRankingResult,
                callback=callback,
                body=body,
            )
        )

    def calc_ranking(
        self,
        request: request_model.CalcRankingRequest,
    ) -> result_model.CalcRankingResult:
        async_result = []
        self._calc_ranking(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
    ):
        """
        ランキングのインデックス計算処理
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='ranking',
            function='calcIndex',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.category_name is not None:
            body["categoryName"] = request.category_name
        if request.calculate_started_at is not None:
            body["calculateStartedAt"] = request.calculate_started_at

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.CalcIndexResult,
                callback=callback,
                body=body,
            )
        )

    def calc_index(
        self,
        request: request_model.CalcIndexRequest,
    ) -> result_model.CalcIndexResult:
        async_result = []
        self._calc_index(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
    ):
        """
        テーブルのコンパクション処理
        :param request: Request
        :param callback: Callback
        """
        import uuid

        request_id = str(uuid.uuid4())
        body = self._create_metadata(
            service=self.SERVICE,
            component='ranking',
            function='compaction',
            request_id=request_id,
            private=True,
        )

        body['contextStack'] = str(request.context_stack)
        if request.owner_id is not None:
            body["ownerId"] = request.owner_id
        if request.namespace_name is not None:
            body["namespaceName"] = request.namespace_name
        if request.category_name is not None:
            body["categoryName"] = request.category_name

        if request.request_id:
            body["xGs2RequestId"] = request.request_id

        self.session.send(
            NetworkJob(
                request_id=request_id,
                result_type=result_model.CompactionResult,
                callback=callback,
                body=body,
            )
        )

    def compaction(
        self,
        request: request_model.CompactionRequest,
    ) -> result_model.CompactionResult:
        async_result = []
        self._compaction(
            request,
            lambda result: async_result.append(result),
        )

        with timeout(30):
            while not async_result:
                time.sleep(0.01)

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
        )

        import asyncio
        with timeout(30):
            while not async_result:
                await asyncio.sleep(0.01)

        if async_result[0].error:
            raise async_result[0].error
        return async_result[0].result
