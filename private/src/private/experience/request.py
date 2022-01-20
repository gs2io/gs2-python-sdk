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
import experience.model as model

from experience.request import \
    DescribeNamespacesRequest, \
    CreateNamespaceRequest, \
    GetNamespaceStatusRequest, \
    GetNamespaceRequest, \
    UpdateNamespaceRequest, \
    DeleteNamespaceRequest, \
    DescribeExperienceModelMastersRequest, \
    CreateExperienceModelMasterRequest, \
    GetExperienceModelMasterRequest, \
    UpdateExperienceModelMasterRequest, \
    DeleteExperienceModelMasterRequest, \
    DescribeExperienceModelsRequest, \
    GetExperienceModelRequest, \
    DescribeThresholdMastersRequest, \
    CreateThresholdMasterRequest, \
    GetThresholdMasterRequest, \
    UpdateThresholdMasterRequest, \
    DeleteThresholdMasterRequest, \
    ExportMasterRequest, \
    GetCurrentExperienceMasterRequest, \
    UpdateCurrentExperienceMasterRequest, \
    UpdateCurrentExperienceMasterFromGitHubRequest, \
    DescribeStatusesRequest, \
    DescribeStatusesByUserIdRequest, \
    GetStatusRequest, \
    GetStatusByUserIdRequest, \
    GetStatusWithSignatureRequest, \
    AddExperienceByUserIdRequest, \
    SetExperienceByUserIdRequest, \
    AddRankCapByUserIdRequest, \
    SetRankCapByUserIdRequest, \
    DeleteStatusByUserIdRequest, \
    AddExperienceByStampSheetRequest, \
    AddRankCapByStampSheetRequest, \
    SetRankCapByStampSheetRequest


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


class DescribeStatusesByOwnerIdAndUserIdRequest(Gs2Request):
    """
    オーナーIDを指定してステータスの一覧を取得 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _experience_name: str = None
    _user_id: str = None
    _page_token: str = None
    _limit: int = None
    _duplication_avoider: str = None

    def __init__(self):
        super(DescribeStatusesByOwnerIdAndUserIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> DescribeStatusesByOwnerIdAndUserIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> DescribeStatusesByOwnerIdAndUserIdRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def experience_name(self) -> str:
        return self._experience_name

    @experience_name.setter
    def experience_name(self, experience_name: str):
        self._experience_name = experience_name

    def with_experience_name(self, experience_name: str) -> DescribeStatusesByOwnerIdAndUserIdRequest:
        self._experience_name = experience_name
        return self

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    def with_user_id(self, user_id: str) -> DescribeStatusesByOwnerIdAndUserIdRequest:
        self._user_id = user_id
        return self

    @property
    def page_token(self) -> str:
        return self._page_token

    @page_token.setter
    def page_token(self, page_token: str):
        self._page_token = page_token

    def with_page_token(self, page_token: str) -> DescribeStatusesByOwnerIdAndUserIdRequest:
        self._page_token = page_token
        return self

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        self._limit = limit

    def with_limit(self, limit: int) -> DescribeStatusesByOwnerIdAndUserIdRequest:
        self._limit = limit
        return self

    @property
    def duplication_avoider(self) -> str:
        return self._duplication_avoider

    @duplication_avoider.setter
    def duplication_avoider(self, duplication_avoider: str):
        self._duplication_avoider = duplication_avoider

    def with_duplication_avoider(self, duplication_avoider: str) -> DescribeStatusesByOwnerIdAndUserIdRequest:
        self._duplication_avoider = duplication_avoider
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DescribeStatusesByOwnerIdAndUserIdRequest:
        return DescribeStatusesByOwnerIdAndUserIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_experience_name(data.get('experienceName', data.get('experience_name')))\
            .with_user_id(data.get('userId', data.get('user_id')))\
            .with_page_token(data.get('pageToken', data.get('page_token')))\
            .with_limit(data.get('limit', data.get('limit')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "experienceName": self._experience_name,
            "userId": self._user_id,
            "pageToken": self._page_token,
            "limit": self._limit,
        }
