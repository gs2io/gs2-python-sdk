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
from chat import Gs2ChatRestClient, request as request_, result as result_
from chat.domain.iterator.namespaces import DescribeNamespacesIterator
from chat.domain.iterator.rooms import DescribeRoomsIterator
from chat.domain.iterator.messages import DescribeMessagesIterator
from chat.domain.iterator.messages_by_user_id import DescribeMessagesByUserIdIterator
from chat.domain.iterator.subscribes import DescribeSubscribesIterator
from chat.domain.iterator.subscribes_by_user_id import DescribeSubscribesByUserIdIterator
from chat.domain.iterator.subscribes_by_room_name import DescribeSubscribesByRoomNameIterator
from chat.domain.cache.namespace import NamespaceDomainCache
from chat.domain.cache.room import RoomDomainCache
from chat.domain.cache.message import MessageDomainCache
from chat.domain.cache.subscribe import SubscribeDomainCache


class SubscribeAccessTokenDomain:
    _session: Gs2RestSession
    _client: Gs2ChatRestClient
    _subscribe_cache: SubscribeDomainCache
    _namespace_name: str
    _access_token: AccessToken
    _room_name: str

    def __init__(
        self,
        session: Gs2RestSession,
        subscribe_cache: SubscribeDomainCache,
        namespace_name: str,
        access_token: AccessToken,
        room_name: str,
    ):
        self._session = session
        self._client = Gs2ChatRestClient(
            session,
        )
        self._subscribe_cache = subscribe_cache
        self._namespace_name = namespace_name
        self._access_token = access_token
        self._room_name = room_name

    def subscribe(
        self,
        request: request_.SubscribeRequest,
    ) -> result_.SubscribeResult:
        request.with_namespace_name(self._namespace_name)
        request.with_access_token(self._access_token.token if self._access_token else None)
        request.with_room_name(self._room_name)
        r = self._client.subscribe(
            request,
        )
        self._subscribe_cache.update(r.item)
        return r

    def load(
        self,
        request: request_.GetSubscribeRequest,
    ) -> result_.GetSubscribeResult:
        request.with_namespace_name(self._namespace_name)
        request.with_access_token(self._access_token.token if self._access_token else None)
        request.with_room_name(self._room_name)
        r = self._client.get_subscribe(
            request,
        )
        self._subscribe_cache.update(r.item)
        return r

    def update_notification_type(
        self,
        request: request_.UpdateNotificationTypeRequest,
    ) -> result_.UpdateNotificationTypeResult:
        request.with_namespace_name(self._namespace_name)
        request.with_access_token(self._access_token.token if self._access_token else None)
        request.with_room_name(self._room_name)
        r = self._client.update_notification_type(
            request,
        )
        self._subscribe_cache.update(r.item)
        return r

    def unsubscribe(
        self,
        request: request_.UnsubscribeRequest,
    ) -> result_.UnsubscribeResult:
        request.with_namespace_name(self._namespace_name)
        request.with_access_token(self._access_token.token if self._access_token else None)
        request.with_room_name(self._room_name)
        r = self._client.unsubscribe(
            request,
        )
        self._subscribe_cache.update(r.item)
        return r
