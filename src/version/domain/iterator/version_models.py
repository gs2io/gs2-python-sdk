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

from version import Gs2VersionRestClient, VersionModel, request
from version.domain.cache.version_model import VersionModelDomainCache
from core.domain.access_token import AccessToken


class DescribeVersionModelsIterator:
    _version_model_cache: VersionModelDomainCache
    _client: Gs2VersionRestClient
    _namespace_name: str

    _index: int
    _last: bool
    _result: List[VersionModel]

    fetch_size: Optional[int]

    def __init__(
        self,
        version_model_cache: VersionModelDomainCache,
        client: Gs2VersionRestClient,
        namespace_name: str,
    ):
        self._version_model_cache = version_model_cache
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
        r = self._client.describe_version_models(
            request.DescribeVersionModelsRequest()
                .with_namespace_name(self._namespace_name)
        )
        for item in r.items:
            self._version_model_cache.update(item)
        self._result = r.items
        self._last = True

    def __iter__(self):
        return self

    def _has_next(
        self,
    ) -> bool:
        return len(self._result) != 0 or not self._last

    def __next__(self) -> VersionModel:
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
