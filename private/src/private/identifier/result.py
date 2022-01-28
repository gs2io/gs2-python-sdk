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
import identifier.model as model

from identifier.result import \
    DescribeUsersResult, \
    CreateUserResult, \
    UpdateUserResult, \
    GetUserResult, \
    DeleteUserResult, \
    DescribeSecurityPoliciesResult, \
    DescribeCommonSecurityPoliciesResult, \
    CreateSecurityPolicyResult, \
    UpdateSecurityPolicyResult, \
    GetSecurityPolicyResult, \
    DeleteSecurityPolicyResult, \
    DescribeIdentifiersResult, \
    CreateIdentifierResult, \
    GetIdentifierResult, \
    DeleteIdentifierResult, \
    DescribePasswordsResult, \
    CreatePasswordResult, \
    GetPasswordResult, \
    DeletePasswordResult, \
    GetHasSecurityPolicyResult, \
    AttachSecurityPolicyResult, \
    DetachSecurityPolicyResult, \
    LoginResult, \
    LoginByUserResult


class DescribeUsersByOwnerIdResult(Gs2Result):
    """
    オーナーIDを指定してユーザの一覧を取得します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(DescribeUsersByOwnerIdResult, self).__init__()
        # ユーザのリスト
        self._items = []
        for item in response.get('items', []):
            self._items.append(model.User(item))
        # リストの続きを取得するためのページトークン
        self._next_page_token = response.get('nextPageToken') if 'nextPageToken' in response else None

    @property
    def items(self) -> List[model.User]:
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
        return super(DescribeUsersByOwnerIdResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [item.to_dict() for item in self._items],
            "nextPageToken": self._next_page_token,
        }


class DescribeSecurityPoliciesByOwnerIdResult(Gs2Result):
    """
    オーナーIDを指定してセキュリティポリシーの一覧を取得します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(DescribeSecurityPoliciesByOwnerIdResult, self).__init__()
        # セキュリティポリシーのリスト
        self._items = []
        for item in response.get('items', []):
            self._items.append(model.SecurityPolicy(item))
        # リストの続きを取得するためのページトークン
        self._next_page_token = response.get('nextPageToken') if 'nextPageToken' in response else None

    @property
    def items(self) -> List[model.SecurityPolicy]:
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
        return super(DescribeSecurityPoliciesByOwnerIdResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [item.to_dict() for item in self._items],
            "nextPageToken": self._next_page_token,
        }


class AssumeResult(Gs2Result):
    """
    プロジェクトトークン を取得します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(AssumeResult, self).__init__()
        # プロジェクトトークン
        self._item = model.ProjectToken(response.get('item')) if 'item' in response else None

    @property
    def item(self) -> model.ProjectToken:
        return self._item

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(AssumeResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self._item.to_dict(),
        }
