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
import job_queue.model as model

from job_queue.request import \
    DescribeNamespacesRequest, \
    CreateNamespaceRequest, \
    GetNamespaceStatusRequest, \
    GetNamespaceRequest, \
    UpdateNamespaceRequest, \
    DeleteNamespaceRequest, \
    DescribeJobsByUserIdRequest, \
    GetJobByUserIdRequest, \
    PushByUserIdRequest, \
    RunRequest, \
    RunByUserIdRequest, \
    DeleteJobByUserIdRequest, \
    PushByStampSheetRequest, \
    DescribeDeadLetterJobsByUserIdRequest, \
    GetDeadLetterJobByUserIdRequest, \
    DeleteDeadLetterJobByUserIdRequest


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


class PushByNamespaceIdAndUserIdRequest(Gs2Request):
    """
    ユーザIDを指定してジョブを登録 のリクエストモデル
    """
    _namespace_id: str = None
    _user_id: str = None
    _jobs: list[model.JobEntry] = None
    _duplication_avoider: str = None

    def __init__(self):
        super(PushByNamespaceIdAndUserIdRequest, self).__init__()

    @property
    def namespace_id(self) -> str:
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id: str):
        self._namespace_id = namespace_id

    def with_namespace_id(self, namespace_id: str) -> PushByNamespaceIdAndUserIdRequest:
        self._namespace_id = namespace_id
        return self

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    def with_user_id(self, user_id: str) -> PushByNamespaceIdAndUserIdRequest:
        self._user_id = user_id
        return self

    @property
    def jobs(self) -> list[model.JobEntry]:
        return self._jobs

    @jobs.setter
    def jobs(self, jobs: list[model.JobEntry]):
        self._jobs = jobs

    def with_jobs(self, jobs: list[model.JobEntry]) -> PushByNamespaceIdAndUserIdRequest:
        self._jobs = jobs
        return self

    @property
    def duplication_avoider(self) -> str:
        return self._duplication_avoider

    @duplication_avoider.setter
    def duplication_avoider(self, duplication_avoider: str):
        self._duplication_avoider = duplication_avoider

    def with_duplication_avoider(self, duplication_avoider: str) -> PushByNamespaceIdAndUserIdRequest:
        self._duplication_avoider = duplication_avoider
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> PushByNamespaceIdAndUserIdRequest:
        return PushByNamespaceIdAndUserIdRequest()\
            .with_namespace_id(data.get('namespaceId', data.get('namespace_id')))\
            .with_user_id(data.get('userId', data.get('user_id')))\
            .with_jobs([model.JobEntry.from_dict(
                data=data,
            ) for data in data.get('jobs', data.get('jobs', []))])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceId": self._namespace_id,
            "userId": self._user_id,
            "jobs": [item.to_dict() if item else None for item in self._jobs],
        }
