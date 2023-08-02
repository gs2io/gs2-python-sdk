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

from .model import *


class DescribeNamespacesRequest(core.Gs2Request):

    context_stack: str = None
    page_token: str = None
    limit: int = None

    def with_page_token(self, page_token: str) -> DescribeNamespacesRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeNamespacesRequest:
        self.limit = limit
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DescribeNamespacesRequest]:
        if data is None:
            return None
        return DescribeNamespacesRequest()\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class CreateNamespaceRequest(core.Gs2Request):

    context_stack: str = None
    name: str = None
    description: str = None
    start_script: ScriptSetting = None
    pass_script: ScriptSetting = None
    error_script: ScriptSetting = None
    lowest_state_machine_version: int = None
    log_setting: LogSetting = None

    def with_name(self, name: str) -> CreateNamespaceRequest:
        self.name = name
        return self

    def with_description(self, description: str) -> CreateNamespaceRequest:
        self.description = description
        return self

    def with_start_script(self, start_script: ScriptSetting) -> CreateNamespaceRequest:
        self.start_script = start_script
        return self

    def with_pass_script(self, pass_script: ScriptSetting) -> CreateNamespaceRequest:
        self.pass_script = pass_script
        return self

    def with_error_script(self, error_script: ScriptSetting) -> CreateNamespaceRequest:
        self.error_script = error_script
        return self

    def with_lowest_state_machine_version(self, lowest_state_machine_version: int) -> CreateNamespaceRequest:
        self.lowest_state_machine_version = lowest_state_machine_version
        return self

    def with_log_setting(self, log_setting: LogSetting) -> CreateNamespaceRequest:
        self.log_setting = log_setting
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[CreateNamespaceRequest]:
        if data is None:
            return None
        return CreateNamespaceRequest()\
            .with_name(data.get('name'))\
            .with_description(data.get('description'))\
            .with_start_script(ScriptSetting.from_dict(data.get('startScript')))\
            .with_pass_script(ScriptSetting.from_dict(data.get('passScript')))\
            .with_error_script(ScriptSetting.from_dict(data.get('errorScript')))\
            .with_lowest_state_machine_version(data.get('lowestStateMachineVersion'))\
            .with_log_setting(LogSetting.from_dict(data.get('logSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "startScript": self.start_script.to_dict() if self.start_script else None,
            "passScript": self.pass_script.to_dict() if self.pass_script else None,
            "errorScript": self.error_script.to_dict() if self.error_script else None,
            "lowestStateMachineVersion": self.lowest_state_machine_version,
            "logSetting": self.log_setting.to_dict() if self.log_setting else None,
        }


class GetNamespaceStatusRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetNamespaceStatusRequest:
        self.namespace_name = namespace_name
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetNamespaceStatusRequest]:
        if data is None:
            return None
        return GetNamespaceStatusRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class GetNamespaceRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetNamespaceRequest:
        self.namespace_name = namespace_name
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetNamespaceRequest]:
        if data is None:
            return None
        return GetNamespaceRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class UpdateNamespaceRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    description: str = None
    start_script: ScriptSetting = None
    pass_script: ScriptSetting = None
    error_script: ScriptSetting = None
    lowest_state_machine_version: int = None
    log_setting: LogSetting = None

    def with_namespace_name(self, namespace_name: str) -> UpdateNamespaceRequest:
        self.namespace_name = namespace_name
        return self

    def with_description(self, description: str) -> UpdateNamespaceRequest:
        self.description = description
        return self

    def with_start_script(self, start_script: ScriptSetting) -> UpdateNamespaceRequest:
        self.start_script = start_script
        return self

    def with_pass_script(self, pass_script: ScriptSetting) -> UpdateNamespaceRequest:
        self.pass_script = pass_script
        return self

    def with_error_script(self, error_script: ScriptSetting) -> UpdateNamespaceRequest:
        self.error_script = error_script
        return self

    def with_lowest_state_machine_version(self, lowest_state_machine_version: int) -> UpdateNamespaceRequest:
        self.lowest_state_machine_version = lowest_state_machine_version
        return self

    def with_log_setting(self, log_setting: LogSetting) -> UpdateNamespaceRequest:
        self.log_setting = log_setting
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[UpdateNamespaceRequest]:
        if data is None:
            return None
        return UpdateNamespaceRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_description(data.get('description'))\
            .with_start_script(ScriptSetting.from_dict(data.get('startScript')))\
            .with_pass_script(ScriptSetting.from_dict(data.get('passScript')))\
            .with_error_script(ScriptSetting.from_dict(data.get('errorScript')))\
            .with_lowest_state_machine_version(data.get('lowestStateMachineVersion'))\
            .with_log_setting(LogSetting.from_dict(data.get('logSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "description": self.description,
            "startScript": self.start_script.to_dict() if self.start_script else None,
            "passScript": self.pass_script.to_dict() if self.pass_script else None,
            "errorScript": self.error_script.to_dict() if self.error_script else None,
            "lowestStateMachineVersion": self.lowest_state_machine_version,
            "logSetting": self.log_setting.to_dict() if self.log_setting else None,
        }


class DeleteNamespaceRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteNamespaceRequest:
        self.namespace_name = namespace_name
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DeleteNamespaceRequest]:
        if data is None:
            return None
        return DeleteNamespaceRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class DescribeStateMachineMastersRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeStateMachineMastersRequest:
        self.namespace_name = namespace_name
        return self

    def with_page_token(self, page_token: str) -> DescribeStateMachineMastersRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeStateMachineMastersRequest:
        self.limit = limit
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DescribeStateMachineMastersRequest]:
        if data is None:
            return None
        return DescribeStateMachineMastersRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class UpdateStateMachineMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    main_state_machine_name: str = None
    payload: str = None

    def with_namespace_name(self, namespace_name: str) -> UpdateStateMachineMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_main_state_machine_name(self, main_state_machine_name: str) -> UpdateStateMachineMasterRequest:
        self.main_state_machine_name = main_state_machine_name
        return self

    def with_payload(self, payload: str) -> UpdateStateMachineMasterRequest:
        self.payload = payload
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[UpdateStateMachineMasterRequest]:
        if data is None:
            return None
        return UpdateStateMachineMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_main_state_machine_name(data.get('mainStateMachineName'))\
            .with_payload(data.get('payload'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "mainStateMachineName": self.main_state_machine_name,
            "payload": self.payload,
        }


class GetStateMachineMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    version: int = None

    def with_namespace_name(self, namespace_name: str) -> GetStateMachineMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_version(self, version: int) -> GetStateMachineMasterRequest:
        self.version = version
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetStateMachineMasterRequest]:
        if data is None:
            return None
        return GetStateMachineMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_version(data.get('version'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "version": self.version,
        }


class DeleteStateMachineMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    version: int = None

    def with_namespace_name(self, namespace_name: str) -> DeleteStateMachineMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_version(self, version: int) -> DeleteStateMachineMasterRequest:
        self.version = version
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DeleteStateMachineMasterRequest]:
        if data is None:
            return None
        return DeleteStateMachineMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_version(data.get('version'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "version": self.version,
        }


class DescribeStatusesRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    status: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeStatusesRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> DescribeStatusesRequest:
        self.access_token = access_token
        return self

    def with_status(self, status: str) -> DescribeStatusesRequest:
        self.status = status
        return self

    def with_page_token(self, page_token: str) -> DescribeStatusesRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeStatusesRequest:
        self.limit = limit
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DescribeStatusesRequest]:
        if data is None:
            return None
        return DescribeStatusesRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_status(data.get('status'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "status": self.status,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class DescribeStatusesByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    status: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeStatusesByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> DescribeStatusesByUserIdRequest:
        self.user_id = user_id
        return self

    def with_status(self, status: str) -> DescribeStatusesByUserIdRequest:
        self.status = status
        return self

    def with_page_token(self, page_token: str) -> DescribeStatusesByUserIdRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeStatusesByUserIdRequest:
        self.limit = limit
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DescribeStatusesByUserIdRequest]:
        if data is None:
            return None
        return DescribeStatusesByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_status(data.get('status'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "status": self.status,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class GetStatusRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    status_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetStatusRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> GetStatusRequest:
        self.access_token = access_token
        return self

    def with_status_name(self, status_name: str) -> GetStatusRequest:
        self.status_name = status_name
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetStatusRequest]:
        if data is None:
            return None
        return GetStatusRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_status_name(data.get('statusName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "statusName": self.status_name,
        }


class GetStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    status_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> GetStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_status_name(self, status_name: str) -> GetStatusByUserIdRequest:
        self.status_name = status_name
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[GetStatusByUserIdRequest]:
        if data is None:
            return None
        return GetStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_status_name(data.get('statusName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "statusName": self.status_name,
        }


class StartStateMachineByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    args: str = None
    ttl: int = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> StartStateMachineByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> StartStateMachineByUserIdRequest:
        self.user_id = user_id
        return self

    def with_args(self, args: str) -> StartStateMachineByUserIdRequest:
        self.args = args
        return self

    def with_ttl(self, ttl: int) -> StartStateMachineByUserIdRequest:
        self.ttl = ttl
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> StartStateMachineByUserIdRequest:
        self.duplication_avoider = duplication_avoider
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[StartStateMachineByUserIdRequest]:
        if data is None:
            return None
        return StartStateMachineByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_args(data.get('args'))\
            .with_ttl(data.get('ttl'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "args": self.args,
            "ttl": self.ttl,
        }


class StartStateMachineByStampSheetRequest(core.Gs2Request):

    context_stack: str = None
    stamp_sheet: str = None
    key_id: str = None

    def with_stamp_sheet(self, stamp_sheet: str) -> StartStateMachineByStampSheetRequest:
        self.stamp_sheet = stamp_sheet
        return self

    def with_key_id(self, key_id: str) -> StartStateMachineByStampSheetRequest:
        self.key_id = key_id
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[StartStateMachineByStampSheetRequest]:
        if data is None:
            return None
        return StartStateMachineByStampSheetRequest()\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampSheet": self.stamp_sheet,
            "keyId": self.key_id,
        }


class EmitRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    status_name: str = None
    event_name: str = None
    args: str = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> EmitRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> EmitRequest:
        self.access_token = access_token
        return self

    def with_status_name(self, status_name: str) -> EmitRequest:
        self.status_name = status_name
        return self

    def with_event_name(self, event_name: str) -> EmitRequest:
        self.event_name = event_name
        return self

    def with_args(self, args: str) -> EmitRequest:
        self.args = args
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> EmitRequest:
        self.duplication_avoider = duplication_avoider
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[EmitRequest]:
        if data is None:
            return None
        return EmitRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_status_name(data.get('statusName'))\
            .with_event_name(data.get('eventName'))\
            .with_args(data.get('args'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "statusName": self.status_name,
            "eventName": self.event_name,
            "args": self.args,
        }


class EmitByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    status_name: str = None
    event_name: str = None
    args: str = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> EmitByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> EmitByUserIdRequest:
        self.user_id = user_id
        return self

    def with_status_name(self, status_name: str) -> EmitByUserIdRequest:
        self.status_name = status_name
        return self

    def with_event_name(self, event_name: str) -> EmitByUserIdRequest:
        self.event_name = event_name
        return self

    def with_args(self, args: str) -> EmitByUserIdRequest:
        self.args = args
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> EmitByUserIdRequest:
        self.duplication_avoider = duplication_avoider
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[EmitByUserIdRequest]:
        if data is None:
            return None
        return EmitByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_status_name(data.get('statusName'))\
            .with_event_name(data.get('eventName'))\
            .with_args(data.get('args'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "statusName": self.status_name,
            "eventName": self.event_name,
            "args": self.args,
        }


class DeleteStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    status_name: str = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> DeleteStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_status_name(self, status_name: str) -> DeleteStatusByUserIdRequest:
        self.status_name = status_name
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> DeleteStatusByUserIdRequest:
        self.duplication_avoider = duplication_avoider
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[DeleteStatusByUserIdRequest]:
        if data is None:
            return None
        return DeleteStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_status_name(data.get('statusName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "statusName": self.status_name,
        }


class ExitStateMachineRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    status_name: str = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> ExitStateMachineRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> ExitStateMachineRequest:
        self.access_token = access_token
        return self

    def with_status_name(self, status_name: str) -> ExitStateMachineRequest:
        self.status_name = status_name
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> ExitStateMachineRequest:
        self.duplication_avoider = duplication_avoider
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[ExitStateMachineRequest]:
        if data is None:
            return None
        return ExitStateMachineRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_status_name(data.get('statusName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "statusName": self.status_name,
        }


class ExitStateMachineByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    status_name: str = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> ExitStateMachineByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> ExitStateMachineByUserIdRequest:
        self.user_id = user_id
        return self

    def with_status_name(self, status_name: str) -> ExitStateMachineByUserIdRequest:
        self.status_name = status_name
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> ExitStateMachineByUserIdRequest:
        self.duplication_avoider = duplication_avoider
        return self

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return None

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> Optional[ExitStateMachineByUserIdRequest]:
        if data is None:
            return None
        return ExitStateMachineByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_status_name(data.get('statusName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "statusName": self.status_name,
        }