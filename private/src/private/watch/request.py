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
import watch.model as model

from watch.request import \
    GetChartRequest, \
    GetCumulativeRequest, \
    DescribeBillingActivitiesRequest, \
    GetBillingActivityRequest


class DescribeBillingActivitiesByOwnerIdRequest(Gs2Request):
    """
    オーナーIDを指定して請求にまつわるアクティビティの一覧を取得 のリクエストモデル
    """
    _owner_id: str = None
    _year: int = None
    _month: int = None
    _service: str = None
    _page_token: str = None
    _limit: int = None

    def __init__(self):
        super(DescribeBillingActivitiesByOwnerIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> DescribeBillingActivitiesByOwnerIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, year: int):
        self._year = year

    def with_year(self, year: int) -> DescribeBillingActivitiesByOwnerIdRequest:
        self._year = year
        return self

    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, month: int):
        self._month = month

    def with_month(self, month: int) -> DescribeBillingActivitiesByOwnerIdRequest:
        self._month = month
        return self

    @property
    def service(self) -> str:
        return self._service

    @service.setter
    def service(self, service: str):
        self._service = service

    def with_service(self, service: str) -> DescribeBillingActivitiesByOwnerIdRequest:
        self._service = service
        return self

    @property
    def page_token(self) -> str:
        return self._page_token

    @page_token.setter
    def page_token(self, page_token: str):
        self._page_token = page_token

    def with_page_token(self, page_token: str) -> DescribeBillingActivitiesByOwnerIdRequest:
        self._page_token = page_token
        return self

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        self._limit = limit

    def with_limit(self, limit: int) -> DescribeBillingActivitiesByOwnerIdRequest:
        self._limit = limit
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DescribeBillingActivitiesByOwnerIdRequest:
        return DescribeBillingActivitiesByOwnerIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_year(data.get('year', data.get('year')))\
            .with_month(data.get('month', data.get('month')))\
            .with_service(data.get('service', data.get('service')))\
            .with_page_token(data.get('pageToken', data.get('page_token')))\
            .with_limit(data.get('limit', data.get('limit')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "year": self._year,
            "month": self._month,
            "service": self._service,
            "pageToken": self._page_token,
            "limit": self._limit,
        }
