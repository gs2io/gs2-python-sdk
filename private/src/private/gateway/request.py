# encoding: utf-8
#
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

from typing import *
from core.model import Gs2Request
import gateway.model as model

from gateway.request import \
    DescribeNamespacesRequest, \
    CreateNamespaceRequest, \
    GetNamespaceStatusRequest, \
    GetNamespaceRequest, \
    UpdateNamespaceRequest, \
    DeleteNamespaceRequest, \
    DescribeWebSocketSessionsRequest, \
    DescribeWebSocketSessionsByUserIdRequest, \
    SetUserIdRequest, \
    SetUserIdByUserIdRequest, \
    SendNotificationRequest, \
    SetFirebaseTokenRequest, \
    SetFirebaseTokenByUserIdRequest, \
    GetFirebaseTokenRequest, \
    GetFirebaseTokenByUserIdRequest, \
    DeleteFirebaseTokenRequest, \
    DeleteFirebaseTokenByUserIdRequest, \
    SendMobileNotificationByUserIdRequest


class DescribeNamespacesByOwnerIdRequest(Gs2Request):
    """
    オーナーIDを指定してネームスペースの一覧を取得 のリクエストモデル
    """
    _owner_id: str = None
    _page_token: str = None
    _limit: int = None

    def __init__(self):
        super(DescribeNamespacesByOwnerIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> DescribeNamespacesByOwnerIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def page_token(self) -> str:
        return self._page_token

    @page_token.setter
    def page_token(self, page_token: str):
        self._page_token = page_token

    def with_page_token(self, page_token: str) -> DescribeNamespacesByOwnerIdRequest:
        self._page_token = page_token
        return self

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        self._limit = limit

    def with_limit(self, limit: int) -> DescribeNamespacesByOwnerIdRequest:
        self._limit = limit
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DescribeNamespacesByOwnerIdRequest:
        return DescribeNamespacesByOwnerIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_page_token(data.get('pageToken', data.get('page_token')))\
            .with_limit(data.get('limit', data.get('limit')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "pageToken": self._page_token,
            "limit": self._limit,
        }


class ConnectRequest(Gs2Request):
    """
    接続 のリクエストモデル
    """
    _owner_id: str = None
    _connection_id: str = None
    _api_id: str = None

    def __init__(self):
        super(ConnectRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> ConnectRequest:
        self._owner_id = owner_id
        return self

    @property
    def connection_id(self) -> str:
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id: str):
        self._connection_id = connection_id

    def with_connection_id(self, connection_id: str) -> ConnectRequest:
        self._connection_id = connection_id
        return self

    @property
    def api_id(self) -> str:
        return self._api_id

    @api_id.setter
    def api_id(self, api_id: str):
        self._api_id = api_id

    def with_api_id(self, api_id: str) -> ConnectRequest:
        self._api_id = api_id
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> ConnectRequest:
        return ConnectRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_connection_id(data.get('connectionId', data.get('connection_id')))\
            .with_api_id(data.get('apiId', data.get('api_id')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "connectionId": self._connection_id,
            "apiId": self._api_id,
        }


class DisconnectRequest(Gs2Request):
    """
    切断 のリクエストモデル
    """
    _owner_id: str = None
    _connection_id: str = None

    def __init__(self):
        super(DisconnectRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> DisconnectRequest:
        self._owner_id = owner_id
        return self

    @property
    def connection_id(self) -> str:
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id: str):
        self._connection_id = connection_id

    def with_connection_id(self, connection_id: str) -> DisconnectRequest:
        self._connection_id = connection_id
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DisconnectRequest:
        return DisconnectRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_connection_id(data.get('connectionId', data.get('connection_id')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "connectionId": self._connection_id,
        }


class SendNotificationByOwnerIdRequest(Gs2Request):
    """
    オーナーIDを指定して通知を送信 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _user_id: str = None
    _issuer: str = None
    _subject: str = None
    _payload: str = None
    _enable_transfer_mobile_notification: bool = None
    _sound: str = None
    _duplication_avoider: str = None

    def __init__(self):
        super(SendNotificationByOwnerIdRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> SendNotificationByOwnerIdRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> SendNotificationByOwnerIdRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    def with_user_id(self, user_id: str) -> SendNotificationByOwnerIdRequest:
        self._user_id = user_id
        return self

    @property
    def issuer(self) -> str:
        return self._issuer

    @issuer.setter
    def issuer(self, issuer: str):
        self._issuer = issuer

    def with_issuer(self, issuer: str) -> SendNotificationByOwnerIdRequest:
        self._issuer = issuer
        return self

    @property
    def subject(self) -> str:
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        self._subject = subject

    def with_subject(self, subject: str) -> SendNotificationByOwnerIdRequest:
        self._subject = subject
        return self

    @property
    def payload(self) -> str:
        return self._payload

    @payload.setter
    def payload(self, payload: str):
        self._payload = payload

    def with_payload(self, payload: str) -> SendNotificationByOwnerIdRequest:
        self._payload = payload
        return self

    @property
    def enable_transfer_mobile_notification(self) -> bool:
        return self._enable_transfer_mobile_notification

    @enable_transfer_mobile_notification.setter
    def enable_transfer_mobile_notification(self, enable_transfer_mobile_notification: bool):
        self._enable_transfer_mobile_notification = enable_transfer_mobile_notification

    def with_enable_transfer_mobile_notification(self, enable_transfer_mobile_notification: bool) -> SendNotificationByOwnerIdRequest:
        self._enable_transfer_mobile_notification = enable_transfer_mobile_notification
        return self

    @property
    def sound(self) -> str:
        return self._sound

    @sound.setter
    def sound(self, sound: str):
        self._sound = sound

    def with_sound(self, sound: str) -> SendNotificationByOwnerIdRequest:
        self._sound = sound
        return self

    @property
    def duplication_avoider(self) -> str:
        return self._duplication_avoider

    @duplication_avoider.setter
    def duplication_avoider(self, duplication_avoider: str):
        self._duplication_avoider = duplication_avoider

    def with_duplication_avoider(self, duplication_avoider: str) -> SendNotificationByOwnerIdRequest:
        self._duplication_avoider = duplication_avoider
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> SendNotificationByOwnerIdRequest:
        return SendNotificationByOwnerIdRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_user_id(data.get('userId', data.get('user_id')))\
            .with_issuer(data.get('issuer', data.get('issuer')))\
            .with_subject(data.get('subject', data.get('subject')))\
            .with_payload(data.get('payload', data.get('payload')))\
            .with_enable_transfer_mobile_notification(data.get('enableTransferMobileNotification', data.get('enable_transfer_mobile_notification')))\
            .with_sound(data.get('sound', data.get('sound')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "userId": self._user_id,
            "issuer": self._issuer,
            "subject": self._subject,
            "payload": self._payload,
            "enableTransferMobileNotification": self._enable_transfer_mobile_notification,
            "sound": self._sound,
        }
