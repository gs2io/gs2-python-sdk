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
import limit.model as model

from limit.request import \
    DescribeNamespacesRequest, \
    CreateNamespaceRequest, \
    GetNamespaceStatusRequest, \
    GetNamespaceRequest, \
    UpdateNamespaceRequest, \
    DeleteNamespaceRequest, \
    DescribeCountersRequest, \
    DescribeCountersByUserIdRequest, \
    GetCounterRequest, \
    GetCounterByUserIdRequest, \
    CountUpRequest, \
    CountUpByUserIdRequest, \
    DeleteCounterByUserIdRequest, \
    CountUpByStampTaskRequest, \
    DeleteByStampSheetRequest, \
    DescribeLimitModelMastersRequest, \
    CreateLimitModelMasterRequest, \
    GetLimitModelMasterRequest, \
    UpdateLimitModelMasterRequest, \
    DeleteLimitModelMasterRequest, \
    ExportMasterRequest, \
    GetCurrentLimitMasterRequest, \
    UpdateCurrentLimitMasterRequest, \
    UpdateCurrentLimitMasterFromGitHubRequest, \
    DescribeLimitModelsRequest, \
    GetLimitModelRequest


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


class GetCounterByOwnerIdAndUserIdRequest(Gs2Request):
    """
    カウンターを取得 のリクエストモデル
    """
    _namespace_name: str = None
    _owner_id: str = None
    _limit_name: str = None
    _user_id: str = None
    _counter_name: str = None
    _duplication_avoider: str = None

    def __init__(self):
        super(GetCounterByOwnerIdAndUserIdRequest, self).__init__()

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> GetCounterByOwnerIdAndUserIdRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> GetCounterByOwnerIdAndUserIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def limit_name(self) -> str:
        return self._limit_name

    @limit_name.setter
    def limit_name(self, limit_name: str):
        self._limit_name = limit_name

    def with_limit_name(self, limit_name: str) -> GetCounterByOwnerIdAndUserIdRequest:
        self._limit_name = limit_name
        return self

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    def with_user_id(self, user_id: str) -> GetCounterByOwnerIdAndUserIdRequest:
        self._user_id = user_id
        return self

    @property
    def counter_name(self) -> str:
        return self._counter_name

    @counter_name.setter
    def counter_name(self, counter_name: str):
        self._counter_name = counter_name

    def with_counter_name(self, counter_name: str) -> GetCounterByOwnerIdAndUserIdRequest:
        self._counter_name = counter_name
        return self

    @property
    def duplication_avoider(self) -> str:
        return self._duplication_avoider

    @duplication_avoider.setter
    def duplication_avoider(self, duplication_avoider: str):
        self._duplication_avoider = duplication_avoider

    def with_duplication_avoider(self, duplication_avoider: str) -> GetCounterByOwnerIdAndUserIdRequest:
        self._duplication_avoider = duplication_avoider
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> GetCounterByOwnerIdAndUserIdRequest:
        return GetCounterByOwnerIdAndUserIdRequest()\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_limit_name(data.get('limitName', data.get('limit_name')))\
            .with_user_id(data.get('userId', data.get('user_id')))\
            .with_counter_name(data.get('counterName', data.get('counter_name')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self._namespace_name,
            "ownerId": self._owner_id,
            "limitName": self._limit_name,
            "userId": self._user_id,
            "counterName": self._counter_name,
        }
