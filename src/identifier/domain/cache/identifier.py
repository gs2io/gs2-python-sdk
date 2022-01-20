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

from typing import Dict, List

from core import Gs2RestSession
from core.domain.access_token import AccessToken
from identifier import Gs2IdentifierRestClient, request as request_, result as result_
from identifier.model import Identifier


class IdentifierDomainCache:

    _items: Dict[str, Identifier]

    def __init__(self):
        self._items = {}

    def update(
        self,
        item: Identifier,
    ):
        keys = ":".join([
            str(item.user_name),
        ])
        self._items[keys] = item

    def get(
        self,
        user_name: str,
    ) -> Identifier:
        keys = ":".join([
            str(user_name),
        ])
        return self._items[keys]

    def delete(
        self,
        item: Identifier,
    ):
        keys = ":".join([
            str(item.user_name),
        ])
        if keys in self._items:
            del self._items[keys]
