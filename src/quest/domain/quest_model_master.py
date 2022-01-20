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
from quest import Gs2QuestRestClient, request as request_, result as result_
from quest.domain.iterator.namespaces import DescribeNamespacesIterator
from quest.domain.iterator.quest_group_model_masters import DescribeQuestGroupModelMastersIterator
from quest.domain.iterator.quest_model_masters import DescribeQuestModelMastersIterator
from quest.domain.iterator.progresses_by_user_id import DescribeProgressesByUserIdIterator
from quest.domain.iterator.completed_quest_lists import DescribeCompletedQuestListsIterator
from quest.domain.iterator.completed_quest_lists_by_user_id import DescribeCompletedQuestListsByUserIdIterator
from quest.domain.iterator.quest_group_models import DescribeQuestGroupModelsIterator
from quest.domain.iterator.quest_models import DescribeQuestModelsIterator
from quest.domain.cache.namespace import NamespaceDomainCache
from quest.domain.cache.quest_group_model_master import QuestGroupModelMasterDomainCache
from quest.domain.cache.quest_model_master import QuestModelMasterDomainCache
from quest.domain.cache.progress import ProgressDomainCache
from quest.domain.cache.completed_quest_list import CompletedQuestListDomainCache
from quest.domain.cache.quest_group_model import QuestGroupModelDomainCache
from quest.domain.cache.quest_model import QuestModelDomainCache


class QuestModelMasterDomain:
    _session: Gs2RestSession
    _client: Gs2QuestRestClient
    _quest_model_master_cache: QuestModelMasterDomainCache
    _namespace_name: str
    _quest_group_name: str
    _quest_name: str

    def __init__(
        self,
        session: Gs2RestSession,
        quest_model_master_cache: QuestModelMasterDomainCache,
        namespace_name: str,
        quest_group_name: str,
        quest_name: str,
    ):
        self._session = session
        self._client = Gs2QuestRestClient(
            session,
        )
        self._quest_model_master_cache = quest_model_master_cache
        self._namespace_name = namespace_name
        self._quest_group_name = quest_group_name
        self._quest_name = quest_name

    def load(
        self,
        request: request_.GetQuestModelMasterRequest,
    ) -> result_.GetQuestModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_quest_group_name(self._quest_group_name)
        request.with_quest_name(self._quest_name)
        r = self._client.get_quest_model_master(
            request,
        )
        self._quest_model_master_cache.update(r.item)
        return r

    def update(
        self,
        request: request_.UpdateQuestModelMasterRequest,
    ) -> result_.UpdateQuestModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_quest_group_name(self._quest_group_name)
        request.with_quest_name(self._quest_name)
        r = self._client.update_quest_model_master(
            request,
        )
        self._quest_model_master_cache.update(r.item)
        return r

    def delete(
        self,
        request: request_.DeleteQuestModelMasterRequest,
    ) -> result_.DeleteQuestModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_quest_group_name(self._quest_group_name)
        request.with_quest_name(self._quest_name)
        r = self._client.delete_quest_model_master(
            request,
        )
        self._quest_model_master_cache.delete(r.item)
        return r
