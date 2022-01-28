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
import project.model as model

from project.result import \
    CreateAccountResult, \
    VerifyResult, \
    SignInResult, \
    IssueAccountTokenResult, \
    ForgetResult, \
    IssuePasswordResult, \
    UpdateAccountResult, \
    DeleteAccountResult, \
    DescribeProjectsResult, \
    CreateProjectResult, \
    GetProjectResult, \
    GetProjectTokenResult, \
    GetProjectTokenByIdentifierResult, \
    UpdateProjectResult, \
    DeleteProjectResult, \
    DescribeBillingMethodsResult, \
    CreateBillingMethodResult, \
    GetBillingMethodResult, \
    UpdateBillingMethodResult, \
    DeleteBillingMethodResult, \
    DescribeReceiptsResult, \
    DescribeBillingsResult


class DescribeAccountsResult(Gs2Result):
    """
    GS2アカウントの一覧を取得します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(DescribeAccountsResult, self).__init__()
        # GS2アカウントのリスト
        self._items = []
        for item in response.get('items', []):
            self._items.append(model.Account(item))
        # リストの続きを取得するためのページトークン
        self._next_page_token = response.get('nextPageToken') if 'nextPageToken' in response else None

    @property
    def items(self) -> List[model.Account]:
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
        return super(DescribeAccountsResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [item.to_dict() for item in self._items],
            "nextPageToken": self._next_page_token,
        }


class GetAccountByAccountNameResult(Gs2Result):
    """
    GS2アカウントを取得します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(GetAccountByAccountNameResult, self).__init__()
        # GS2アカウント
        self._item = model.Account(response.get('item')) if 'item' in response else None

    @property
    def item(self) -> model.Account:
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
        return super(GetAccountByAccountNameResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self._item.to_dict(),
        }


class UpdateAccountByAccountNameResult(Gs2Result):
    """
    GS2アカウントを更新します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(UpdateAccountByAccountNameResult, self).__init__()
        # 更新したGS2アカウント
        self._item = model.Account(response.get('item')) if 'item' in response else None

    @property
    def item(self) -> model.Account:
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
        return super(UpdateAccountByAccountNameResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self._item.to_dict(),
        }


class DeleteAccountByAccountNameResult(Gs2Result):
    """
    GS2アカウントを削除します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(DeleteAccountByAccountNameResult, self).__init__()

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(DeleteAccountByAccountNameResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
        }


class DeleteAccountByEmailResult(Gs2Result):
    """
    GS2アカウントを削除します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(DeleteAccountByEmailResult, self).__init__()

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(DeleteAccountByEmailResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
        }
