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

from __future__ import annotations

from typing import *
from core.model import Gs2Request
import ranking.model as model

from ranking.request import \
    DescribeNamespacesRequest, \
    CreateNamespaceRequest, \
    GetNamespaceStatusRequest, \
    GetNamespaceRequest, \
    UpdateNamespaceRequest, \
    DeleteNamespaceRequest, \
    DescribeCategoryModelsRequest, \
    GetCategoryModelRequest, \
    DescribeCategoryModelMastersRequest, \
    CreateCategoryModelMasterRequest, \
    GetCategoryModelMasterRequest, \
    UpdateCategoryModelMasterRequest, \
    DeleteCategoryModelMasterRequest, \
    DescribeSubscribesByCategoryNameRequest, \
    DescribeSubscribesByCategoryNameAndUserIdRequest, \
    SubscribeRequest, \
    SubscribeByUserIdRequest, \
    GetSubscribeRequest, \
    GetSubscribeByUserIdRequest, \
    UnsubscribeRequest, \
    UnsubscribeByUserIdRequest, \
    DescribeScoresRequest, \
    DescribeScoresByUserIdRequest, \
    GetScoreRequest, \
    GetScoreByUserIdRequest, \
    DescribeRankingsRequest, \
    DescribeRankingssByUserIdRequest, \
    DescribeNearRankingsRequest, \
    GetRankingRequest, \
    GetRankingByUserIdRequest, \
    PutScoreRequest, \
    PutScoreByUserIdRequest, \
    ExportMasterRequest, \
    GetCurrentRankingMasterRequest, \
    UpdateCurrentRankingMasterRequest, \
    UpdateCurrentRankingMasterFromGitHubRequest


class DescribeNamespacesByOwnerIdRequest(Gs2Request):
    """
    オーナーIDを指定してネームスペースの一覧を取得 のリクエストモデル
    """
    _owner_id: str = None
    _page_token: str = None
    _limit: int = None

    def __init__(self):
        super(DescribeNamespacesByOwnerIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> DescribeNamespacesByOwnerIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def page_token(self) -> str:
        return self._page_token

    @page_token.setter
    def page_token(self, page_token: str):
        self._page_token = page_token

    def with_page_token(self, page_token: str) -> DescribeNamespacesByOwnerIdRequest:
        self._page_token = page_token
        return self

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        self._limit = limit

    def with_limit(self, limit: int) -> DescribeNamespacesByOwnerIdRequest:
        self._limit = limit
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DescribeNamespacesByOwnerIdRequest:
        return DescribeNamespacesByOwnerIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_page_token(data.get('pageToken', data.get('page_token')))\
            .with_limit(data.get('limit', data.get('limit')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "pageToken": self._page_token,
            "limit": self._limit,
        }


class PutScoreImplRequest(Gs2Request):
    """
    スコア登録の遅延実行処理 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _category_name: str = None
    _score: model.Score = None
    _page_token: str = None

    def __init__(self):
        super(PutScoreImplRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> PutScoreImplRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> PutScoreImplRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def category_name(self) -> str:
        return self._category_name

    @category_name.setter
    def category_name(self, category_name: str):
        self._category_name = category_name

    def with_category_name(self, category_name: str) -> PutScoreImplRequest:
        self._category_name = category_name
        return self

    @property
    def score(self) -> model.Score:
        return self._score

    @score.setter
    def score(self, score: model.Score):
        self._score = score

    def with_score(self, score: model.Score) -> PutScoreImplRequest:
        self._score = score
        return self

    @property
    def page_token(self) -> str:
        return self._page_token

    @page_token.setter
    def page_token(self, page_token: str):
        self._page_token = page_token

    def with_page_token(self, page_token: str) -> PutScoreImplRequest:
        self._page_token = page_token
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> PutScoreImplRequest:
        return PutScoreImplRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_category_name(data.get('categoryName', data.get('category_name')))\
            .with_score(model.Score.from_dict(
                namespace,
                data.get('score', data.get('score')),
            ) if data.get('score', data.get('score')) not in [None, ''] else None)\
            .with_page_token(data.get('pageToken', data.get('page_token')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "categoryName": self._category_name,
            "score": self._score.to_dict() if self._score else None,
            "pageToken": self._page_token,
        }


class CalcAllRankingRequest(Gs2Request):
    """
    ランキングの計算処理 のリクエストモデル
    """

    def __init__(self):
        super(CalcAllRankingRequest, self).__init__()

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> CalcAllRankingRequest:
        return CalcAllRankingRequest()\

    def to_dict(self) -> Dict[str, Any]:
        return {
        }


class CalcRankingRequest(Gs2Request):
    """
    ランキングの計算処理 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _category_name: str = None
    _calculate_started_at: str = None
    _page_token: str = None
    _force: bool = None

    def __init__(self):
        super(CalcRankingRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> CalcRankingRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> CalcRankingRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def category_name(self) -> str:
        return self._category_name

    @category_name.setter
    def category_name(self, category_name: str):
        self._category_name = category_name

    def with_category_name(self, category_name: str) -> CalcRankingRequest:
        self._category_name = category_name
        return self

    @property
    def calculate_started_at(self) -> str:
        return self._calculate_started_at

    @calculate_started_at.setter
    def calculate_started_at(self, calculate_started_at: str):
        self._calculate_started_at = calculate_started_at

    def with_calculate_started_at(self, calculate_started_at: str) -> CalcRankingRequest:
        self._calculate_started_at = calculate_started_at
        return self

    @property
    def page_token(self) -> str:
        return self._page_token

    @page_token.setter
    def page_token(self, page_token: str):
        self._page_token = page_token

    def with_page_token(self, page_token: str) -> CalcRankingRequest:
        self._page_token = page_token
        return self

    @property
    def force(self) -> bool:
        return self._force

    @force.setter
    def force(self, force: bool):
        self._force = force

    def with_force(self, force: bool) -> CalcRankingRequest:
        self._force = force
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> CalcRankingRequest:
        return CalcRankingRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_category_name(data.get('categoryName', data.get('category_name')))\
            .with_calculate_started_at(data.get('calculateStartedAt', data.get('calculate_started_at')))\
            .with_page_token(data.get('pageToken', data.get('page_token')))\
            .with_force(data.get('force', data.get('force')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "categoryName": self._category_name,
            "calculateStartedAt": self._calculate_started_at,
            "pageToken": self._page_token,
            "force": self._force,
        }


class CalcIndexRequest(Gs2Request):
    """
    ランキングのインデックス計算処理 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _category_name: str = None
    _calculate_started_at: str = None

    def __init__(self):
        super(CalcIndexRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> CalcIndexRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> CalcIndexRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def category_name(self) -> str:
        return self._category_name

    @category_name.setter
    def category_name(self, category_name: str):
        self._category_name = category_name

    def with_category_name(self, category_name: str) -> CalcIndexRequest:
        self._category_name = category_name
        return self

    @property
    def calculate_started_at(self) -> str:
        return self._calculate_started_at

    @calculate_started_at.setter
    def calculate_started_at(self, calculate_started_at: str):
        self._calculate_started_at = calculate_started_at

    def with_calculate_started_at(self, calculate_started_at: str) -> CalcIndexRequest:
        self._calculate_started_at = calculate_started_at
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> CalcIndexRequest:
        return CalcIndexRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_category_name(data.get('categoryName', data.get('category_name')))\
            .with_calculate_started_at(data.get('calculateStartedAt', data.get('calculate_started_at')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "categoryName": self._category_name,
            "calculateStartedAt": self._calculate_started_at,
        }


class CompactionRequest(Gs2Request):
    """
    テーブルのコンパクション処理 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _category_name: str = None

    def __init__(self):
        super(CompactionRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> CompactionRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> CompactionRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def category_name(self) -> str:
        return self._category_name

    @category_name.setter
    def category_name(self, category_name: str):
        self._category_name = category_name

    def with_category_name(self, category_name: str) -> CompactionRequest:
        self._category_name = category_name
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> CompactionRequest:
        return CompactionRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_category_name(data.get('categoryName', data.get('category_name')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "categoryName": self._category_name,
        }
