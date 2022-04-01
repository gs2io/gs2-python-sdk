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

from ranking import Gs2RankingRestClient, Score, request
from ranking.domain.cache.score import ScoreDomainCache
from core.domain.access_token import AccessToken


class DescribeScoresIterator:
    _score_cache: ScoreDomainCache
    _client: Gs2RankingRestClient
    _namespace_name: str
    _category_name: str
    _access_token: AccessToken
    _scorer_user_id: str

    _index: int
    _page_token: Optional[str]
    _last: bool
    _result: List[Score]

    fetch_size: Optional[int]

    def __init__(
        self,
        score_cache: ScoreDomainCache,
        client: Gs2RankingRestClient,
        namespace_name: str,
        category_name: str,
        access_token: AccessToken,
        scorer_user_id: str,
    ):
        self._score_cache = score_cache
        self._client = client
        self._namespace_name = namespace_name
        self._category_name = category_name
        self._access_token = access_token
        self._scorer_user_id = scorer_user_id

        self._index = 0
        self._page_token = None
        self._last = False
        self._result = []

        self.fetch_size = None

        self._load()

    def _load(
        self,
    ):
        r = self._client.describe_scores(
            request.DescribeScoresRequest()
                .with_namespace_name(self._namespace_name)
                .with_category_name(self._category_name)
                .with_access_token(self._access_token.token if self._access_token else None)
                .with_scorer_user_id(self._scorer_user_id)
                .with_page_token(self._page_token)
                .with_limit(self.fetch_size)
        )
        for item in r.items:
            self._score_cache.update(item)
        self._result = r.items
        self._page_token = r.next_page_token
        self._last = self._page_token is None

    def __iter__(self):
        return self

    def _has_next(
        self,
    ) -> bool:
        return len(self._result) != 0 or not self._last

    def __next__(self) -> Score:
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
