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
import realtime.model as model

from realtime.request import \
    DescribeNamespacesRequest, \
    CreateNamespaceRequest, \
    GetNamespaceStatusRequest, \
    GetNamespaceRequest, \
    UpdateNamespaceRequest, \
    DeleteNamespaceRequest, \
    DescribeRoomsRequest, \
    WantRoomRequest, \
    GetRoomRequest, \
    DeleteRoomRequest


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


class CreateRoomRequest(Gs2Request):
    """
    ルームを作成。 のリクエストモデル
    """
    _owner_id: str = None
    _namespace_name: str = None
    _name: str = None
    _ip_address: str = None
    _port: int = None
    _encryption_key: str = None

    def __init__(self):
        super(CreateRoomRequest, self).__init__()

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id: str):
        self._owner_id = owner_id

    def with_owner_id(self, owner_id: str) -> CreateRoomRequest:
        self._owner_id = owner_id
        return self

    @property
    def namespace_name(self) -> str:
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name: str):
        self._namespace_name = namespace_name

    def with_namespace_name(self, namespace_name: str) -> CreateRoomRequest:
        self._namespace_name = namespace_name
        return self

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def with_name(self, name: str) -> CreateRoomRequest:
        self._name = name
        return self

    @property
    def ip_address(self) -> str:
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address: str):
        self._ip_address = ip_address

    def with_ip_address(self, ip_address: str) -> CreateRoomRequest:
        self._ip_address = ip_address
        return self

    @property
    def port(self) -> int:
        return self._port

    @port.setter
    def port(self, port: int):
        self._port = port

    def with_port(self, port: int) -> CreateRoomRequest:
        self._port = port
        return self

    @property
    def encryption_key(self) -> str:
        return self._encryption_key

    @encryption_key.setter
    def encryption_key(self, encryption_key: str):
        self._encryption_key = encryption_key

    def with_encryption_key(self, encryption_key: str) -> CreateRoomRequest:
        self._encryption_key = encryption_key
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> CreateRoomRequest:
        return CreateRoomRequest()\
            .with_owner_id(data.get('ownerId', data.get('owner_id')))\
            .with_namespace_name(data.get('namespaceName', data.get('namespace_name')))\
            .with_name(data.get('name', data.get('name')))\
            .with_ip_address(data.get('ipAddress', data.get('ip_address')))\
            .with_port(data.get('port', data.get('port')))\
            .with_encryption_key(data.get('encryptionKey', data.get('encryption_key')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ownerId": self._owner_id,
            "namespaceName": self._namespace_name,
            "name": self._name,
            "ipAddress": self._ip_address,
            "port": self._port,
            "encryptionKey": self._encryption_key,
        }


class ShutdownRoomRequest(Gs2Request):
    """
    ルームを停止 のリクエストモデル
    """
    _ip_address: str = None
    _port: int = None
    _server_spec: str = None
    _running_time: int = None
    _outbound_bytes: int = None

    def __init__(self):
        super(ShutdownRoomRequest, self).__init__()

    @property
    def ip_address(self) -> str:
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address: str):
        self._ip_address = ip_address

    def with_ip_address(self, ip_address: str) -> ShutdownRoomRequest:
        self._ip_address = ip_address
        return self

    @property
    def port(self) -> int:
        return self._port

    @port.setter
    def port(self, port: int):
        self._port = port

    def with_port(self, port: int) -> ShutdownRoomRequest:
        self._port = port
        return self

    @property
    def server_spec(self) -> str:
        return self._server_spec

    @server_spec.setter
    def server_spec(self, server_spec: str):
        self._server_spec = server_spec

    def with_server_spec(self, server_spec: str) -> ShutdownRoomRequest:
        self._server_spec = server_spec
        return self

    @property
    def running_time(self) -> int:
        return self._running_time

    @running_time.setter
    def running_time(self, running_time: int):
        self._running_time = running_time

    def with_running_time(self, running_time: int) -> ShutdownRoomRequest:
        self._running_time = running_time
        return self

    @property
    def outbound_bytes(self) -> int:
        return self._outbound_bytes

    @outbound_bytes.setter
    def outbound_bytes(self, outbound_bytes: int):
        self._outbound_bytes = outbound_bytes

    def with_outbound_bytes(self, outbound_bytes: int) -> ShutdownRoomRequest:
        self._outbound_bytes = outbound_bytes
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> ShutdownRoomRequest:
        return ShutdownRoomRequest()\
            .with_ip_address(data.get('ipAddress', data.get('ip_address')))\
            .with_port(data.get('port', data.get('port')))\
            .with_server_spec(data.get('serverSpec', data.get('server_spec')))\
            .with_running_time(data.get('runningTime', data.get('running_time')))\
            .with_outbound_bytes(data.get('outboundBytes', data.get('outbound_bytes')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ipAddress": self._ip_address,
            "port": self._port,
            "serverSpec": self._server_spec,
            "runningTime": self._running_time,
            "outboundBytes": self._outbound_bytes,
        }
