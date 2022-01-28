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
from core.model import Gs2Result
import exchange.model as model

from exchange.result import \
    DescribeNamespacesResult, \
    CreateNamespaceResult, \
    GetNamespaceStatusResult, \
    GetNamespaceResult, \
    UpdateNamespaceResult, \
    DeleteNamespaceResult, \
    DescribeRateModelsResult, \
    GetRateModelResult, \
    DescribeRateModelMastersResult, \
    CreateRateModelMasterResult, \
    GetRateModelMasterResult, \
    UpdateRateModelMasterResult, \
    DeleteRateModelMasterResult, \
    ExchangeResult, \
    ExchangeByUserIdResult, \
    ExchangeByStampSheetResult, \
    ExportMasterResult, \
    GetCurrentRateMasterResult, \
    UpdateCurrentRateMasterResult, \
    UpdateCurrentRateMasterFromGitHubResult, \
    CreateAwaitByUserIdResult, \
    DescribeAwaitsResult, \
    DescribeAwaitsByUserIdResult, \
    GetAwaitResult, \
    GetAwaitByUserIdResult, \
    AcquireResult, \
    AcquireByUserIdResult, \
    AcquireForceByUserIdResult, \
    SkipResult, \
    SkipByUserIdResult, \
    DeleteAwaitResult, \
    DeleteAwaitByUserIdResult, \
    CreateAwaitByStampSheetResult, \
    DeleteAwaitByStampTaskResult


class DescribeNamespacesByOwnerIdResult(Gs2Result):
    """
    オーナーIDを指定してネームスペースの一覧を取得 のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(DescribeNamespacesByOwnerIdResult, self).__init__()
        # ネームスペースのリスト
        self._items = []
        for item in response.get('items', []):
            self._items.append(model.Namespace(item))
        # リストの続きを取得するためのページトークン
        self._next_page_token = response.get('nextPageToken') if 'nextPageToken' in response else None

    @property
    def items(self) -> List[model.Namespace]:
        return self._items

    @property
    def next_page_token(self) -> str:
        return self._next_page_token

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(DescribeNamespacesByOwnerIdResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [item.to_dict() for item in self._items],
            "nextPageToken": self._next_page_token,
        }
