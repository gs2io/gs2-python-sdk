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

from chat import Gs2ChatRestClient, Message, request
from chat.domain.cache.message import MessageDomainCache
from core.domain.access_token import AccessToken


class DescribeMessagesByUserIdIterator:
    _message_cache: MessageDomainCache
    _client: Gs2ChatRestClient
    _namespace_name: str
    _room_name: str
    _password: str
    _user_id: str

    _index: int
    _start_at: int
    _last: bool
    _result: List[Message]

    fetch_size: Optional[int]

    def __init__(
        self,
        message_cache: MessageDomainCache,
        client: Gs2ChatRestClient,
        namespace_name: str,
        room_name: str,
        password: str,
        user_id: str,
    ):
        self._message_cache = message_cache
        self._client = client
        self._namespace_name = namespace_name
        self._room_name = room_name
        self._password = password
        self._user_id = user_id

        self._index = 0
        self._start_at = None
        self._last = False
        self._result = []

        self.fetch_size = None

        self._load()

    def _load(
        self,
    ):
        r = self._client.describe_messages_by_user_id(
            request.DescribeMessagesByUserIdRequest()
                .with_namespace_name(self._namespace_name)
                .with_room_name(self._room_name)
                .with_password(self._password)
                .with_user_id(self._user_id)
                .with_start_at(self._start_at)
                .with_limit(self.fetch_size)
        )
        for item in r.items:
            self._message_cache.update(item)
        self._result = r.items
        if len(self._result) > 0:
            self._start_at = self._result[-1].created_at + 1

    def __iter__(self):
        return self

    def _has_next(
        self,
    ) -> bool:
        return len(self._result) != 0 or not self._last

    def __next__(self) -> Message:
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
