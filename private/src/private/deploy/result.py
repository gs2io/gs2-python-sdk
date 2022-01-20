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
import deploy.model as model

from deploy.result import \
    DescribeStacksResult, \
    CreateStackResult, \
    CreateStackFromGitHubResult, \
    ValidateResult, \
    GetStackStatusResult, \
    GetStackResult, \
    UpdateStackResult, \
    UpdateStackFromGitHubResult, \
    DeleteStackResult, \
    ForceDeleteStackResult, \
    DeleteStackResourcesResult, \
    DeleteStackEntityResult, \
    DescribeResourcesResult, \
    GetResourceResult, \
    DescribeEventsResult, \
    GetEventResult, \
    DescribeOutputsResult, \
    GetOutputResult


class DescribeStacksByOwnerIdResult(Gs2Result):
    """
    オーナーIDを指定してスタックの一覧を取得 のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(DescribeStacksByOwnerIdResult, self).__init__()
        # スタックのリスト
        self._items = []
        for item in response.get('items', []):
            self._items.append(model.Stack(item))
        # リストの続きを取得するためのページトークン
        self._next_page_token = response.get('nextPageToken') if 'nextPageToken' in response else None

    @property
    def items(self) -> List[model.Stack]:
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
        return super(DescribeStacksByOwnerIdResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [item.to_dict() for item in self._items],
            "nextPageToken": self._next_page_token,
        }


class RunStackTaskResult(Gs2Result):
    """
    実行中のスタックの処理を実行 のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(RunStackTaskResult, self).__init__()
        # None
        self._status = response.get('status') if 'status' in response else None

    @property
    def status(self) -> str:
        return self._status

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(RunStackTaskResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self._status,
        }


class RunResourceTaskResult(Gs2Result):
    """
    作成中のリソースの処理を実行 のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(RunResourceTaskResult, self).__init__()
        # None
        self._status = response.get('status') if 'status' in response else None

    @property
    def status(self) -> str:
        return self._status

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(RunResourceTaskResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self._status,
        }
