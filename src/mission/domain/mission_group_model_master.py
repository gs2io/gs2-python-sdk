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
from mission import Gs2MissionRestClient, request as request_, result as result_
from mission.domain.iterator.completes import DescribeCompletesIterator
from mission.domain.iterator.completes_by_user_id import DescribeCompletesByUserIdIterator
from mission.domain.iterator.counter_model_masters import DescribeCounterModelMastersIterator
from mission.domain.iterator.mission_group_model_masters import DescribeMissionGroupModelMastersIterator
from mission.domain.iterator.namespaces import DescribeNamespacesIterator
from mission.domain.iterator.counters import DescribeCountersIterator
from mission.domain.iterator.counters_by_user_id import DescribeCountersByUserIdIterator
from mission.domain.iterator.counter_models import DescribeCounterModelsIterator
from mission.domain.iterator.mission_group_models import DescribeMissionGroupModelsIterator
from mission.domain.iterator.mission_task_models import DescribeMissionTaskModelsIterator
from mission.domain.iterator.mission_task_model_masters import DescribeMissionTaskModelMastersIterator
from mission.domain.cache.complete import CompleteDomainCache
from mission.domain.cache.counter_model_master import CounterModelMasterDomainCache
from mission.domain.cache.mission_group_model_master import MissionGroupModelMasterDomainCache
from mission.domain.cache.namespace import NamespaceDomainCache
from mission.domain.cache.counter import CounterDomainCache
from mission.domain.cache.counter_model import CounterModelDomainCache
from mission.domain.cache.mission_group_model import MissionGroupModelDomainCache
from mission.domain.cache.mission_task_model import MissionTaskModelDomainCache
from mission.domain.cache.mission_task_model_master import MissionTaskModelMasterDomainCache
from mission.domain.mission_task_model_master import MissionTaskModelMasterDomain


class MissionGroupModelMasterDomain:
    _session: Gs2RestSession
    _client: Gs2MissionRestClient
    _mission_group_model_master_cache: MissionGroupModelMasterDomainCache
    _namespace_name: str
    _mission_group_name: str
    _mission_task_model_master_cache: MissionTaskModelMasterDomainCache

    def __init__(
        self,
        session: Gs2RestSession,
        mission_group_model_master_cache: MissionGroupModelMasterDomainCache,
        namespace_name: str,
        mission_group_name: str,
    ):
        self._session = session
        self._client = Gs2MissionRestClient(
            session,
        )
        self._mission_group_model_master_cache = mission_group_model_master_cache
        self._namespace_name = namespace_name
        self._mission_group_name = mission_group_name
        self._mission_task_model_master_cache = MissionTaskModelMasterDomainCache()

    def load(
        self,
        request: request_.GetMissionGroupModelMasterRequest,
    ) -> result_.GetMissionGroupModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_mission_group_name(self._mission_group_name)
        r = self._client.get_mission_group_model_master(
            request,
        )
        self._mission_group_model_master_cache.update(r.item)
        return r

    def update(
        self,
        request: request_.UpdateMissionGroupModelMasterRequest,
    ) -> result_.UpdateMissionGroupModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_mission_group_name(self._mission_group_name)
        r = self._client.update_mission_group_model_master(
            request,
        )
        self._mission_group_model_master_cache.update(r.item)
        return r

    def delete(
        self,
        request: request_.DeleteMissionGroupModelMasterRequest,
    ) -> result_.DeleteMissionGroupModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_mission_group_name(self._mission_group_name)
        r = self._client.delete_mission_group_model_master(
            request,
        )
        self._mission_group_model_master_cache.delete(r.item)
        return r

    def create_mission_task_model_master(
        self,
        request: request_.CreateMissionTaskModelMasterRequest,
    ) -> result_.CreateMissionTaskModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_mission_group_name(self._mission_group_name)
        r = self._client.create_mission_task_model_master(
            request,
        )
        return r

    def mission_task_model_masters(
        self,
    ) -> DescribeMissionTaskModelMastersIterator:
        return DescribeMissionTaskModelMastersIterator(
            self._mission_task_model_master_cache,
            self._client,
            self._namespace_name,
            self._mission_group_name,
        )

    def mission_task_model_master(
        self,
        mission_task_name: str,
    ) -> MissionTaskModelMasterDomain:
        return MissionTaskModelMasterDomain(
            self._session,
            self._mission_task_model_master_cache,
            self._namespace_name,
            self._mission_group_name,
            mission_task_name,
        )
