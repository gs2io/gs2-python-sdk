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
import deploy.model as model

from deploy.request import \
    DescribeStacksRequest, \
    CreateStackRequest, \
    CreateStackFromGitHubRequest, \
    ValidateRequest, \
    GetStackStatusRequest, \
    GetStackRequest, \
    UpdateStackRequest, \
    UpdateStackFromGitHubRequest, \
    DeleteStackRequest, \
    ForceDeleteStackRequest, \
    DeleteStackResourcesRequest, \
    DeleteStackEntityRequest, \
    DescribeResourcesRequest, \
    GetResourceRequest, \
    DescribeEventsRequest, \
    GetEventRequest, \
    DescribeOutputsRequest, \
    GetOutputRequest


class DescribeStacksByOwnerIdRequest(Gs2Request):
    """
    オーナーIDを指定してスタックの一覧を取得 のリクエストモデル
    """
    _owner_id: str = None
    _page_token: str = None
    _limit: int = None

    def __init__(self):
        super(DescribeStacksByOwnerIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> DescribeStacksByOwnerIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def page_token(self) -> str:
        return self._page_token

    @page_token.setter
    def page_token(self, page_token: str):
        self._page_token = page_token

    def with_page_token(self, page_token: str) -> DescribeStacksByOwnerIdRequest:
        self._page_token = page_token
        return self

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        self._limit = limit

    def with_limit(self, limit: int) -> DescribeStacksByOwnerIdRequest:
        self._limit = limit
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DescribeStacksByOwnerIdRequest:
        return DescribeStacksByOwnerIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_page_token(data.get('pageToken', data.get('page_token')))\
            .with_limit(data.get('limit', data.get('limit')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "pageToken": self._page_token,
            "limit": self._limit,
        }


class RunStackTaskRequest(Gs2Request):
    """
    実行中のスタックの処理を実行 のリクエストモデル
    """
    _owner_id: str = None
    _stack_name: str = None

    def __init__(self):
        super(RunStackTaskRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> RunStackTaskRequest:
        self._owner_id = owner_id
        return self

    @property
    def stack_name(self) -> str:
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name: str):
        self._stack_name = stack_name

    def with_stack_name(self, stack_name: str) -> RunStackTaskRequest:
        self._stack_name = stack_name
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> RunStackTaskRequest:
        return RunStackTaskRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_stack_name(data.get('stackName', data.get('stack_name')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "stackName": self._stack_name,
        }


class RunResourceTaskRequest(Gs2Request):
    """
    作成中のリソースの処理を実行 のリクエストモデル
    """
    _owner_id: str = None
    _stack_name: str = None
    _resource_name: str = None

    def __init__(self):
        super(RunResourceTaskRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> RunResourceTaskRequest:
        self._owner_id = owner_id
        return self

    @property
    def stack_name(self) -> str:
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name: str):
        self._stack_name = stack_name

    def with_stack_name(self, stack_name: str) -> RunResourceTaskRequest:
        self._stack_name = stack_name
        return self

    @property
    def resource_name(self) -> str:
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name: str):
        self._resource_name = resource_name

    def with_resource_name(self, resource_name: str) -> RunResourceTaskRequest:
        self._resource_name = resource_name
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> RunResourceTaskRequest:
        return RunResourceTaskRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_stack_name(data.get('stackName', data.get('stack_name')))\
            .with_resource_name(data.get('resourceName', data.get('resource_name')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "stackName": self._stack_name,
            "resourceName": self._resource_name,
        }
