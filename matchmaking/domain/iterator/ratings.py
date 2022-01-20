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

from matchmaking import Gs2MatchmakingRestClient, Rating, request
from matchmaking.domain.cache.rating import RatingDomainCache
from core.domain.access_token import AccessToken


class DescribeRatingsIterator:
    _rating_cache: RatingDomainCache
    _client: Gs2MatchmakingRestClient
    _namespace_name: str
    _access_token: AccessToken

    _index: int
    _page_token: Optional[str]
    _last: bool
    _result: List[Rating]

    fetch_size: Optional[int]

    def __init__(
        self,
        rating_cache: RatingDomainCache,
        client: Gs2MatchmakingRestClient,
        namespace_name: str,
        access_token: AccessToken,
    ):
        self._rating_cache = rating_cache
        self._client = client
        self._namespace_name = namespace_name
        self._access_token = access_token

        self._index = 0
        self._page_token = None
        self._last = False
        self._result = []

        self.fetch_size = None

        self._load()

    def _load(
        self,
    ):
        r = self._client.describe_ratings(
            request.DescribeRatingsRequest()
                .with_namespace_name(self._namespace_name)
                .with_access_token(self._access_token.token if self._access_token else None)
                .with_page_token(self._page_token)
                .with_limit(self.fetch_size)
        )
        for item in r.items:
            self._rating_cache.update(item)
        self._result = r.items
        self._page_token = r.next_page_token
        self._last = self._page_token is None

    def __iter__(self):
        return self

    def _has_next(
        self,
    ) -> bool:
        return len(self._result) != 0 or not self._last

    def __next__(self) -> Rating:
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
