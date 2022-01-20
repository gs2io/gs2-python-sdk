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

from core import Gs2RestSession
from core.domain.access_token import AccessToken
from exchange import Gs2ExchangeRestClient, request as request_, result as result_
from exchange.domain.iterator.namespaces import DescribeNamespacesIterator
from exchange.domain.iterator.rate_models import DescribeRateModelsIterator
from exchange.domain.iterator.rate_model_masters import DescribeRateModelMastersIterator
from exchange.domain.iterator.awaits import DescribeAwaitsIterator
from exchange.domain.iterator.awaits_by_user_id import DescribeAwaitsByUserIdIterator
from exchange.domain.cache.namespace import NamespaceDomainCache
from exchange.domain.cache.rate_model import RateModelDomainCache
from exchange.domain.cache.rate_model_master import RateModelMasterDomainCache
from exchange.domain.cache.await_ import AwaitDomainCache
from exchange.domain.await_ import AwaitDomain
from exchange.domain.await__access_token import AwaitAccessTokenDomain
from exchange.domain.await__access_token import AwaitAccessTokenDomain


class UserDomain:
    _session: Gs2RestSession
    _client: Gs2ExchangeRestClient
    _namespace_name: str
    _user_id: str
    _await_cache: AwaitDomainCache

    def __init__(
        self,
        session: Gs2RestSession,
        namespace_name: str,
        user_id: str,
    ):
        self._session = session
        self._client = Gs2ExchangeRestClient(
            session,
        )
        self._namespace_name = namespace_name
        self._user_id = user_id
        self._await_cache = AwaitDomainCache()

    def exchange(
        self,
        request: request_.ExchangeByUserIdRequest,
    ) -> result_.ExchangeByUserIdResult:
        request.with_namespace_name(self._namespace_name)
        request.with_user_id(self._user_id)
        r = self._client.exchange_by_user_id(
            request,
        )
        return r

    def create_await(
        self,
        request: request_.CreateAwaitByUserIdRequest,
    ) -> result_.CreateAwaitByUserIdResult:
        request.with_namespace_name(self._namespace_name)
        request.with_user_id(self._user_id)
        r = self._client.create_await_by_user_id(
            request,
        )
        return r

    def awaits(
        self,
        rate_name: str,
    ) -> DescribeAwaitsByUserIdIterator:
        return DescribeAwaitsByUserIdIterator(
            self._await_cache,
            self._client,
            self._namespace_name,
            self._user_id,
            rate_name,
        )

    def await_(
        self,
        await_name: str,
    ) -> AwaitDomain:
        return AwaitDomain(
            self._session,
            self._await_cache,
            self._namespace_name,
            self._user_id,
            await_name,
        )
