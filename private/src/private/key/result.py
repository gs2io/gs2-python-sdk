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
import key.model as model

from key.result import \
    DescribeNamespacesResult, \
    CreateNamespaceResult, \
    GetNamespaceStatusResult, \
    GetNamespaceResult, \
    UpdateNamespaceResult, \
    DeleteNamespaceResult, \
    DescribeKeysResult, \
    CreateKeyResult, \
    UpdateKeyResult, \
    GetKeyResult, \
    DeleteKeyResult, \
    EncryptResult, \
    DecryptResult, \
    DescribeGitHubApiKeysResult, \
    CreateGitHubApiKeyResult, \
    UpdateGitHubApiKeyResult, \
    GetGitHubApiKeyResult, \
    DeleteGitHubApiKeyResult


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


class EncryptByKeyIdResult(Gs2Result):
    """
    オーナーIDを指定してデータを暗号化します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(EncryptByKeyIdResult, self).__init__()
        # 暗号化済みデータ
        self._data = response.get('data') if 'data' in response else None

    @property
    def data(self) -> str:
        return self._data

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(EncryptByKeyIdResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "data": self._data,
        }


class DecryptByKeyIdResult(Gs2Result):
    """
    オーナーIDを指定してデータを復号します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(DecryptByKeyIdResult, self).__init__()
        # 復号済みデータ
        self._data = response.get('data') if 'data' in response else None

    @property
    def data(self) -> str:
        return self._data

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(DecryptByKeyIdResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "data": self._data,
        }


class GetGitHubApiKeyWithApiKeyResult(Gs2Result):
    """
    GitHub のAPIキーを取得します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(GetGitHubApiKeyWithApiKeyResult, self).__init__()
        # GitHub のAPIキー
        self._item = model.GitHubApiKey(response.get('item')) if 'item' in response else None
        # APIキー
        self._api_key = response.get('apiKey') if 'apiKey' in response else None

    @property
    def item(self) -> model.GitHubApiKey:
        return self._item

    @property
    def api_key(self) -> str:
        return self._api_key

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(GetGitHubApiKeyWithApiKeyResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self._item.to_dict(),
            "apiKey": self._api_key,
        }
