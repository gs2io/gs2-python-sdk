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
import lock.model as model

from lock.request import \
    DescribeNamespacesRequest, \
    CreateNamespaceRequest, \
    GetNamespaceStatusRequest, \
    GetNamespaceRequest, \
    UpdateNamespaceRequest, \
    DeleteNamespaceRequest, \
    DescribeMutexesRequest, \
    DescribeMutexesByUserIdRequest, \
    LockRequest, \
    LockByUserIdRequest, \
    UnlockRequest, \
    UnlockByUserIdRequest, \
    GetMutexRequest, \
    GetMutexByUserIdRequest, \
    DeleteMutexByUserIdRequest


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


class LockByOwnerIdAndUserIdRequest(Gs2Request):
    """
    オーナーIDとユーザIDを指定してミューテックスを取得 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _user_id: str = None
    _property_id: str = None
    _transaction_id: str = None
    _ttl: int = None
    _duplication_avoider: str = None

    def __init__(self):
        super(LockByOwnerIdAndUserIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> LockByOwnerIdAndUserIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> LockByOwnerIdAndUserIdRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    def with_user_id(self, user_id: str) -> LockByOwnerIdAndUserIdRequest:
        self._user_id = user_id
        return self

    @property
    def property_id(self) -> str:
        return self._property_id

    @property_id.setter
    def property_id(self, property_id: str):
        self._property_id = property_id

    def with_property_id(self, property_id: str) -> LockByOwnerIdAndUserIdRequest:
        self._property_id = property_id
        return self

    @property
    def transaction_id(self) -> str:
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id: str):
        self._transaction_id = transaction_id

    def with_transaction_id(self, transaction_id: str) -> LockByOwnerIdAndUserIdRequest:
        self._transaction_id = transaction_id
        return self

    @property
    def ttl(self) -> int:
        return self._ttl

    @ttl.setter
    def ttl(self, ttl: int):
        self._ttl = ttl

    def with_ttl(self, ttl: int) -> LockByOwnerIdAndUserIdRequest:
        self._ttl = ttl
        return self

    @property
    def duplication_avoider(self) -> str:
        return self._duplication_avoider

    @duplication_avoider.setter
    def duplication_avoider(self, duplication_avoider: str):
        self._duplication_avoider = duplication_avoider

    def with_duplication_avoider(self, duplication_avoider: str) -> LockByOwnerIdAndUserIdRequest:
        self._duplication_avoider = duplication_avoider
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> LockByOwnerIdAndUserIdRequest:
        return LockByOwnerIdAndUserIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_user_id(data.get('userId', data.get('user_id')))\
            .with_property_id(data.get('propertyId', data.get('property_id')))\
            .with_transaction_id(data.get('transactionId', data.get('transaction_id')))\
            .with_ttl(data.get('ttl', data.get('ttl')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "userId": self._user_id,
            "propertyId": self._property_id,
            "transactionId": self._transaction_id,
            "ttl": self._ttl,
        }


class UnlockByOwnerIdAndUserIdRequest(Gs2Request):
    """
    オーナーIDとユーザIDを指定してミューテックスを解放 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _user_id: str = None
    _property_id: str = None
    _transaction_id: str = None
    _duplication_avoider: str = None

    def __init__(self):
        super(UnlockByOwnerIdAndUserIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> UnlockByOwnerIdAndUserIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> UnlockByOwnerIdAndUserIdRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    def with_user_id(self, user_id: str) -> UnlockByOwnerIdAndUserIdRequest:
        self._user_id = user_id
        return self

    @property
    def property_id(self) -> str:
        return self._property_id

    @property_id.setter
    def property_id(self, property_id: str):
        self._property_id = property_id

    def with_property_id(self, property_id: str) -> UnlockByOwnerIdAndUserIdRequest:
        self._property_id = property_id
        return self

    @property
    def transaction_id(self) -> str:
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id: str):
        self._transaction_id = transaction_id

    def with_transaction_id(self, transaction_id: str) -> UnlockByOwnerIdAndUserIdRequest:
        self._transaction_id = transaction_id
        return self

    @property
    def duplication_avoider(self) -> str:
        return self._duplication_avoider

    @duplication_avoider.setter
    def duplication_avoider(self, duplication_avoider: str):
        self._duplication_avoider = duplication_avoider

    def with_duplication_avoider(self, duplication_avoider: str) -> UnlockByOwnerIdAndUserIdRequest:
        self._duplication_avoider = duplication_avoider
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> UnlockByOwnerIdAndUserIdRequest:
        return UnlockByOwnerIdAndUserIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_user_id(data.get('userId', data.get('user_id')))\
            .with_property_id(data.get('propertyId', data.get('property_id')))\
            .with_transaction_id(data.get('transactionId', data.get('transaction_id')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "userId": self._user_id,
            "propertyId": self._property_id,
            "transactionId": self._transaction_id,
        }


class GetMutexByOwnerIdAndUserIdRequest(Gs2Request):
    """
    オーナーIDとユーザIDを指定してミューテックスを取得 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _user_id: str = None
    _property_id: str = None
    _duplication_avoider: str = None

    def __init__(self):
        super(GetMutexByOwnerIdAndUserIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> GetMutexByOwnerIdAndUserIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> GetMutexByOwnerIdAndUserIdRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    def with_user_id(self, user_id: str) -> GetMutexByOwnerIdAndUserIdRequest:
        self._user_id = user_id
        return self

    @property
    def property_id(self) -> str:
        return self._property_id

    @property_id.setter
    def property_id(self, property_id: str):
        self._property_id = property_id

    def with_property_id(self, property_id: str) -> GetMutexByOwnerIdAndUserIdRequest:
        self._property_id = property_id
        return self

    @property
    def duplication_avoider(self) -> str:
        return self._duplication_avoider

    @duplication_avoider.setter
    def duplication_avoider(self, duplication_avoider: str):
        self._duplication_avoider = duplication_avoider

    def with_duplication_avoider(self, duplication_avoider: str) -> GetMutexByOwnerIdAndUserIdRequest:
        self._duplication_avoider = duplication_avoider
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> GetMutexByOwnerIdAndUserIdRequest:
        return GetMutexByOwnerIdAndUserIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_user_id(data.get('userId', data.get('user_id')))\
            .with_property_id(data.get('propertyId', data.get('property_id')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "userId": self._user_id,
            "propertyId": self._property_id,
        }


class DeleteMutexByOwnerIdAndUserIdRequest(Gs2Request):
    """
    ミューテックスを削除 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _user_id: str = None
    _property_id: str = None
    _duplication_avoider: str = None

    def __init__(self):
        super(DeleteMutexByOwnerIdAndUserIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> DeleteMutexByOwnerIdAndUserIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> DeleteMutexByOwnerIdAndUserIdRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    def with_user_id(self, user_id: str) -> DeleteMutexByOwnerIdAndUserIdRequest:
        self._user_id = user_id
        return self

    @property
    def property_id(self) -> str:
        return self._property_id

    @property_id.setter
    def property_id(self, property_id: str):
        self._property_id = property_id

    def with_property_id(self, property_id: str) -> DeleteMutexByOwnerIdAndUserIdRequest:
        self._property_id = property_id
        return self

    @property
    def duplication_avoider(self) -> str:
        return self._duplication_avoider

    @duplication_avoider.setter
    def duplication_avoider(self, duplication_avoider: str):
        self._duplication_avoider = duplication_avoider

    def with_duplication_avoider(self, duplication_avoider: str) -> DeleteMutexByOwnerIdAndUserIdRequest:
        self._duplication_avoider = duplication_avoider
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DeleteMutexByOwnerIdAndUserIdRequest:
        return DeleteMutexByOwnerIdAndUserIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_user_id(data.get('userId', data.get('user_id')))\
            .with_property_id(data.get('propertyId', data.get('property_id')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "userId": self._user_id,
            "propertyId": self._property_id,
        }
