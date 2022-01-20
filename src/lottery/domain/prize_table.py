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
from lottery import Gs2LotteryRestClient, request as request_, result as result_
from lottery.domain.iterator.namespaces import DescribeNamespacesIterator
from lottery.domain.iterator.lottery_model_masters import DescribeLotteryModelMastersIterator
from lottery.domain.iterator.prize_table_masters import DescribePrizeTableMastersIterator
from lottery.domain.iterator.boxes import DescribeBoxesIterator
from lottery.domain.iterator.boxes_by_user_id import DescribeBoxesByUserIdIterator
from lottery.domain.iterator.lottery_models import DescribeLotteryModelsIterator
from lottery.domain.iterator.prize_tables import DescribePrizeTablesIterator
from lottery.domain.iterator.probabilities import DescribeProbabilitiesIterator
from lottery.domain.iterator.probabilities_by_user_id import DescribeProbabilitiesByUserIdIterator
from lottery.domain.cache.namespace import NamespaceDomainCache
from lottery.domain.cache.lottery_model_master import LotteryModelMasterDomainCache
from lottery.domain.cache.prize_table_master import PrizeTableMasterDomainCache
from lottery.domain.cache.box import BoxDomainCache
from lottery.domain.cache.lottery_model import LotteryModelDomainCache
from lottery.domain.cache.prize_table import PrizeTableDomainCache
from lottery.domain.cache.probability import ProbabilityDomainCache


class PrizeTableDomain:
    _session: Gs2RestSession
    _client: Gs2LotteryRestClient
    _prize_table_cache: PrizeTableDomainCache
    _namespace_name: str
    _prize_table_name: str

    def __init__(
        self,
        session: Gs2RestSession,
        prize_table_cache: PrizeTableDomainCache,
        namespace_name: str,
        prize_table_name: str,
    ):
        self._session = session
        self._client = Gs2LotteryRestClient(
            session,
        )
        self._prize_table_cache = prize_table_cache
        self._namespace_name = namespace_name
        self._prize_table_name = prize_table_name

    def load(
        self,
        request: request_.GetPrizeTableRequest,
    ) -> result_.GetPrizeTableResult:
        request.with_namespace_name(self._namespace_name)
        request.with_prize_table_name(self._prize_table_name)
        r = self._client.get_prize_table(
            request,
        )
        self._prize_table_cache.update(r.item)
        return r
