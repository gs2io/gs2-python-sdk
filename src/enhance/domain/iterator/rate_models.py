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

from typing import List, Optional

from enhance import Gs2EnhanceRestClient, RateModel, request
from enhance.domain.cache.rate_model import RateModelDomainCache
from core.domain.access_token import AccessToken


class DescribeRateModelsIterator:
    _rate_model_cache: RateModelDomainCache
    _client: Gs2EnhanceRestClient
    _namespace_name: str

    _index: int
    _last: bool
    _result: List[RateModel]

    fetch_size: Optional[int]

    def __init__(
        self,
        rate_model_cache: RateModelDomainCache,
        client: Gs2EnhanceRestClient,
        namespace_name: str,
    ):
        self._rate_model_cache = rate_model_cache
        self._client = client
        self._namespace_name = namespace_name

        self._index = 0
        self._last = False
        self._result = []

        self.fetch_size = None

        self._load()

    def _load(
        self,
    ):
        r = self._client.describe_rate_models(
            request.DescribeRateModelsRequest()
                .with_namespace_name(self._namespace_name)
        )
        for item in r.items:
            self._rate_model_cache.update(item)
        self._result = r.items
        self._last = True

    def __iter__(self):
        return self

    def _has_next(
        self,
    ) -> bool:
        return len(self._result) != 0 or not self._last

    def __next__(self) -> RateModel:
        if not self._has_next():
            raise StopIteration()
        if len(self._result) == 0 and not self._last:
            self._load()
        if len(self._result) == 0:
            raise StopIteration()
        ret = self._result[0]
        self._result = self._result[1:]
        if len(self._result) == 0 and not self._last:
            self._load()
        return ret
