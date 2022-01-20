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
from identifier import Gs2IdentifierRestClient, request as request_, result as result_
from identifier.domain.iterator.users import DescribeUsersIterator
from identifier.domain.iterator.security_policies import DescribeSecurityPoliciesIterator
from identifier.domain.iterator.common_security_policies import DescribeCommonSecurityPoliciesIterator
from identifier.domain.iterator.identifiers import DescribeIdentifiersIterator
from identifier.domain.iterator.passwords import DescribePasswordsIterator
from identifier.domain.cache.user import UserDomainCache
from identifier.domain.cache.security_policy import SecurityPolicyDomainCache
from identifier.domain.cache.identifier import IdentifierDomainCache
from identifier.domain.cache.password import PasswordDomainCache


class SecurityPolicyDomain:
    _session: Gs2RestSession
    _client: Gs2IdentifierRestClient
    _security_policy_cache: SecurityPolicyDomainCache
    _security_policy_name: str

    def __init__(
        self,
        session: Gs2RestSession,
        security_policy_cache: SecurityPolicyDomainCache,
        security_policy_name: str,
    ):
        self._session = session
        self._client = Gs2IdentifierRestClient(
            session,
        )
        self._security_policy_cache = security_policy_cache
        self._security_policy_name = security_policy_name

    def load(
        self,
        request: request_.GetSecurityPolicyRequest,
    ) -> result_.GetSecurityPolicyResult:
        request.with_security_policy_name(self._security_policy_name)
        r = self._client.get_security_policy(
            request,
        )
        self._security_policy_cache.update(r.item)
        return r
