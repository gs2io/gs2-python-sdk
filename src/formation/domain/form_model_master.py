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
from formation import Gs2FormationRestClient, request as request_, result as result_
from formation.domain.iterator.namespaces import DescribeNamespacesIterator
from formation.domain.iterator.form_model_masters import DescribeFormModelMastersIterator
from formation.domain.iterator.mold_models import DescribeMoldModelsIterator
from formation.domain.iterator.mold_model_masters import DescribeMoldModelMastersIterator
from formation.domain.iterator.molds import DescribeMoldsIterator
from formation.domain.iterator.molds_by_user_id import DescribeMoldsByUserIdIterator
from formation.domain.iterator.forms import DescribeFormsIterator
from formation.domain.iterator.forms_by_user_id import DescribeFormsByUserIdIterator
from formation.domain.cache.namespace import NamespaceDomainCache
from formation.domain.cache.form_model_master import FormModelMasterDomainCache
from formation.domain.cache.mold_model import MoldModelDomainCache
from formation.domain.cache.mold_model_master import MoldModelMasterDomainCache
from formation.domain.cache.mold import MoldDomainCache
from formation.domain.cache.form import FormDomainCache


class FormModelMasterDomain:
    _session: Gs2RestSession
    _client: Gs2FormationRestClient
    _form_model_master_cache: FormModelMasterDomainCache
    _namespace_name: str
    _form_model_name: str

    def __init__(
        self,
        session: Gs2RestSession,
        form_model_master_cache: FormModelMasterDomainCache,
        namespace_name: str,
        form_model_name: str,
    ):
        self._session = session
        self._client = Gs2FormationRestClient(
            session,
        )
        self._form_model_master_cache = form_model_master_cache
        self._namespace_name = namespace_name
        self._form_model_name = form_model_name

    def load(
        self,
        request: request_.GetFormModelMasterRequest,
    ) -> result_.GetFormModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_form_model_name(self._form_model_name)
        r = self._client.get_form_model_master(
            request,
        )
        self._form_model_master_cache.update(r.item)
        return r

    def update(
        self,
        request: request_.UpdateFormModelMasterRequest,
    ) -> result_.UpdateFormModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_form_model_name(self._form_model_name)
        r = self._client.update_form_model_master(
            request,
        )
        self._form_model_master_cache.update(r.item)
        return r

    def delete(
        self,
        request: request_.DeleteFormModelMasterRequest,
    ) -> result_.DeleteFormModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_form_model_name(self._form_model_name)
        r = self._client.delete_form_model_master(
            request,
        )
        self._form_model_master_cache.delete(r.item)
        return r
