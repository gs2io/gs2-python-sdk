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
import key.model as model

from key.request import \
    DescribeNamespacesRequest, \
    CreateNamespaceRequest, \
    GetNamespaceStatusRequest, \
    GetNamespaceRequest, \
    UpdateNamespaceRequest, \
    DeleteNamespaceRequest, \
    DescribeKeysRequest, \
    CreateKeyRequest, \
    UpdateKeyRequest, \
    GetKeyRequest, \
    DeleteKeyRequest, \
    EncryptRequest, \
    DecryptRequest, \
    DescribeGitHubApiKeysRequest, \
    CreateGitHubApiKeyRequest, \
    UpdateGitHubApiKeyRequest, \
    GetGitHubApiKeyRequest, \
    DeleteGitHubApiKeyRequest


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


class EncryptByKeyIdRequest(Gs2Request):
    """
    オーナーIDを指定してデータを暗号化します のリクエストモデル
    """
    _key_id: str = None
    _data: str = None

    def __init__(self):
        super(EncryptByKeyIdRequest, self).__init__()

    @property
    def key_id(self) -> str:
        return self._key_id

    @key_id.setter
    def key_id(self, key_id: str):
        self._key_id = key_id

    def with_key_id(self, key_id: str) -> EncryptByKeyIdRequest:
        self._key_id = key_id
        return self

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, data: str):
        self._data = data

    def with_data(self, data: str) -> EncryptByKeyIdRequest:
        self._data = data
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> EncryptByKeyIdRequest:
        return EncryptByKeyIdRequest()\
            .with_key_id(data.get('keyId', data.get('key_id')))\
            .with_data(data.get('data', data.get('data')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "keyId": self._key_id,
            "data": self._data,
        }


class DecryptByKeyIdRequest(Gs2Request):
    """
    オーナーIDを指定してデータを復号します のリクエストモデル
    """
    _key_id: str = None
    _data: str = None

    def __init__(self):
        super(DecryptByKeyIdRequest, self).__init__()

    @property
    def key_id(self) -> str:
        return self._key_id

    @key_id.setter
    def key_id(self, key_id: str):
        self._key_id = key_id

    def with_key_id(self, key_id: str) -> DecryptByKeyIdRequest:
        self._key_id = key_id
        return self

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, data: str):
        self._data = data

    def with_data(self, data: str) -> DecryptByKeyIdRequest:
        self._data = data
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DecryptByKeyIdRequest:
        return DecryptByKeyIdRequest()\
            .with_key_id(data.get('keyId', data.get('key_id')))\
            .with_data(data.get('data', data.get('data')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "keyId": self._key_id,
            "data": self._data,
        }


class GetGitHubApiKeyWithApiKeyRequest(Gs2Request):
    """
    GitHub のAPIキーを取得します のリクエストモデル
    """
    _git_hub_api_key_id: str = None

    def __init__(self):
        super(GetGitHubApiKeyWithApiKeyRequest, self).__init__()

    @property
    def git_hub_api_key_id(self) -> str:
        return self._git_hub_api_key_id

    @git_hub_api_key_id.setter
    def git_hub_api_key_id(self, git_hub_api_key_id: str):
        self._git_hub_api_key_id = git_hub_api_key_id

    def with_git_hub_api_key_id(self, git_hub_api_key_id: str) -> GetGitHubApiKeyWithApiKeyRequest:
        self._git_hub_api_key_id = git_hub_api_key_id
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> GetGitHubApiKeyWithApiKeyRequest:
        return GetGitHubApiKeyWithApiKeyRequest()\
            .with_git_hub_api_key_id(data.get('gitHubApiKeyId', data.get('git_hub_api_key_id')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "gitHubApiKeyId": self._git_hub_api_key_id,
        }
