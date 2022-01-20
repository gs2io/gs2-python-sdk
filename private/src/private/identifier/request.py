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
import identifier.model as model

from identifier.request import \
    DescribeUsersRequest, \
    CreateUserRequest, \
    UpdateUserRequest, \
    GetUserRequest, \
    DeleteUserRequest, \
    DescribeSecurityPoliciesRequest, \
    DescribeCommonSecurityPoliciesRequest, \
    CreateSecurityPolicyRequest, \
    UpdateSecurityPolicyRequest, \
    GetSecurityPolicyRequest, \
    DeleteSecurityPolicyRequest, \
    DescribeIdentifiersRequest, \
    CreateIdentifierRequest, \
    GetIdentifierRequest, \
    DeleteIdentifierRequest, \
    DescribePasswordsRequest, \
    CreatePasswordRequest, \
    GetPasswordRequest, \
    DeletePasswordRequest, \
    GetHasSecurityPolicyRequest, \
    AttachSecurityPolicyRequest, \
    DetachSecurityPolicyRequest, \
    LoginRequest, \
    LoginByUserRequest


class DescribeUsersByOwnerIdRequest(Gs2Request):
    """
    オーナーIDを指定してユーザの一覧を取得します のリクエストモデル
    """
    _owner_id: str = None
    _page_token: str = None
    _limit: int = None

    def __init__(self):
        super(DescribeUsersByOwnerIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> DescribeUsersByOwnerIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def page_token(self) -> str:
        return self._page_token

    @page_token.setter
    def page_token(self, page_token: str):
        self._page_token = page_token

    def with_page_token(self, page_token: str) -> DescribeUsersByOwnerIdRequest:
        self._page_token = page_token
        return self

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        self._limit = limit

    def with_limit(self, limit: int) -> DescribeUsersByOwnerIdRequest:
        self._limit = limit
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DescribeUsersByOwnerIdRequest:
        return DescribeUsersByOwnerIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_page_token(data.get('pageToken', data.get('page_token')))\
            .with_limit(data.get('limit', data.get('limit')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "pageToken": self._page_token,
            "limit": self._limit,
        }


class DescribeSecurityPoliciesByOwnerIdRequest(Gs2Request):
    """
    オーナーIDを指定してセキュリティポリシーの一覧を取得します のリクエストモデル
    """
    _owner_id: str = None
    _page_token: str = None
    _limit: int = None

    def __init__(self):
        super(DescribeSecurityPoliciesByOwnerIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> DescribeSecurityPoliciesByOwnerIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def page_token(self) -> str:
        return self._page_token

    @page_token.setter
    def page_token(self, page_token: str):
        self._page_token = page_token

    def with_page_token(self, page_token: str) -> DescribeSecurityPoliciesByOwnerIdRequest:
        self._page_token = page_token
        return self

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        self._limit = limit

    def with_limit(self, limit: int) -> DescribeSecurityPoliciesByOwnerIdRequest:
        self._limit = limit
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DescribeSecurityPoliciesByOwnerIdRequest:
        return DescribeSecurityPoliciesByOwnerIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_page_token(data.get('pageToken', data.get('page_token')))\
            .with_limit(data.get('limit', data.get('limit')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "pageToken": self._page_token,
            "limit": self._limit,
        }


class AssumeRequest(Gs2Request):
    """
    プロジェクトトークン を取得します のリクエストモデル
    """
    _client_id: str = None
    _user_id: str = None
    _duplication_avoider: str = None

    def __init__(self):
        super(AssumeRequest, self).__init__()

    @property
    def client_id(self) -> str:
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str):
        self._client_id = client_id

    def with_client_id(self, client_id: str) -> AssumeRequest:
        self._client_id = client_id
        return self

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    def with_user_id(self, user_id: str) -> AssumeRequest:
        self._user_id = user_id
        return self

    @property
    def duplication_avoider(self) -> str:
        return self._duplication_avoider

    @duplication_avoider.setter
    def duplication_avoider(self, duplication_avoider: str):
        self._duplication_avoider = duplication_avoider

    def with_duplication_avoider(self, duplication_avoider: str) -> AssumeRequest:
        self._duplication_avoider = duplication_avoider
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> AssumeRequest:
        return AssumeRequest()\
            .with_client_id(data.get('clientId', data.get('client_id')))\
            .with_user_id(data.get('userId', data.get('user_id')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "clientId": self._client_id,
            "userId": self._user_id,
        }
