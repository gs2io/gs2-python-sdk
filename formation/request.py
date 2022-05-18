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

from formation.model import *


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
    update_mold_script: ScriptSetting = None
    update_form_script: ScriptSetting = None
    log_setting: LogSetting = None

    def with_name(self, name: str) -> CreateNamespaceRequest:
        self.name = name
        return self

    def with_description(self, description: str) -> CreateNamespaceRequest:
        self.description = description
        return self

    def with_update_mold_script(self, update_mold_script: ScriptSetting) -> CreateNamespaceRequest:
        self.update_mold_script = update_mold_script
        return self

    def with_update_form_script(self, update_form_script: ScriptSetting) -> CreateNamespaceRequest:
        self.update_form_script = update_form_script
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
            .with_update_mold_script(ScriptSetting.from_dict(data.get('updateMoldScript')))\
            .with_update_form_script(ScriptSetting.from_dict(data.get('updateFormScript')))\
            .with_log_setting(LogSetting.from_dict(data.get('logSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "updateMoldScript": self.update_mold_script.to_dict() if self.update_mold_script else None,
            "updateFormScript": self.update_form_script.to_dict() if self.update_form_script else None,
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
    update_mold_script: ScriptSetting = None
    update_form_script: ScriptSetting = None
    log_setting: LogSetting = None

    def with_namespace_name(self, namespace_name: str) -> UpdateNamespaceRequest:
        self.namespace_name = namespace_name
        return self

    def with_description(self, description: str) -> UpdateNamespaceRequest:
        self.description = description
        return self

    def with_update_mold_script(self, update_mold_script: ScriptSetting) -> UpdateNamespaceRequest:
        self.update_mold_script = update_mold_script
        return self

    def with_update_form_script(self, update_form_script: ScriptSetting) -> UpdateNamespaceRequest:
        self.update_form_script = update_form_script
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
            .with_update_mold_script(ScriptSetting.from_dict(data.get('updateMoldScript')))\
            .with_update_form_script(ScriptSetting.from_dict(data.get('updateFormScript')))\
            .with_log_setting(LogSetting.from_dict(data.get('logSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "description": self.description,
            "updateMoldScript": self.update_mold_script.to_dict() if self.update_mold_script else None,
            "updateFormScript": self.update_form_script.to_dict() if self.update_form_script else None,
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


class DescribeFormModelMastersRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeFormModelMastersRequest:
        self.namespace_name = namespace_name
        return self

    def with_page_token(self, page_token: str) -> DescribeFormModelMastersRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeFormModelMastersRequest:
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
    ) -> Optional[DescribeFormModelMastersRequest]:
        if data is None:
            return None
        return DescribeFormModelMastersRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class CreateFormModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    name: str = None
    description: str = None
    metadata: str = None
    slots: List[SlotModel] = None

    def with_namespace_name(self, namespace_name: str) -> CreateFormModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_name(self, name: str) -> CreateFormModelMasterRequest:
        self.name = name
        return self

    def with_description(self, description: str) -> CreateFormModelMasterRequest:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> CreateFormModelMasterRequest:
        self.metadata = metadata
        return self

    def with_slots(self, slots: List[SlotModel]) -> CreateFormModelMasterRequest:
        self.slots = slots
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
    ) -> Optional[CreateFormModelMasterRequest]:
        if data is None:
            return None
        return CreateFormModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_name(data.get('name'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_slots([
                SlotModel.from_dict(data.get('slots')[i])
                for i in range(len(data.get('slots')) if data.get('slots') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "slots": [
                self.slots[i].to_dict() if self.slots[i] else None
                for i in range(len(self.slots) if self.slots else 0)
            ],
        }


class GetFormModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    form_model_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetFormModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_form_model_name(self, form_model_name: str) -> GetFormModelMasterRequest:
        self.form_model_name = form_model_name
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
    ) -> Optional[GetFormModelMasterRequest]:
        if data is None:
            return None
        return GetFormModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_form_model_name(data.get('formModelName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "formModelName": self.form_model_name,
        }


class UpdateFormModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    form_model_name: str = None
    description: str = None
    metadata: str = None
    slots: List[SlotModel] = None

    def with_namespace_name(self, namespace_name: str) -> UpdateFormModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_form_model_name(self, form_model_name: str) -> UpdateFormModelMasterRequest:
        self.form_model_name = form_model_name
        return self

    def with_description(self, description: str) -> UpdateFormModelMasterRequest:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> UpdateFormModelMasterRequest:
        self.metadata = metadata
        return self

    def with_slots(self, slots: List[SlotModel]) -> UpdateFormModelMasterRequest:
        self.slots = slots
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
    ) -> Optional[UpdateFormModelMasterRequest]:
        if data is None:
            return None
        return UpdateFormModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_form_model_name(data.get('formModelName'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_slots([
                SlotModel.from_dict(data.get('slots')[i])
                for i in range(len(data.get('slots')) if data.get('slots') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "formModelName": self.form_model_name,
            "description": self.description,
            "metadata": self.metadata,
            "slots": [
                self.slots[i].to_dict() if self.slots[i] else None
                for i in range(len(self.slots) if self.slots else 0)
            ],
        }


class DeleteFormModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    form_model_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteFormModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_form_model_name(self, form_model_name: str) -> DeleteFormModelMasterRequest:
        self.form_model_name = form_model_name
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
    ) -> Optional[DeleteFormModelMasterRequest]:
        if data is None:
            return None
        return DeleteFormModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_form_model_name(data.get('formModelName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "formModelName": self.form_model_name,
        }


class DescribeMoldModelsRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DescribeMoldModelsRequest:
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
    ) -> Optional[DescribeMoldModelsRequest]:
        if data is None:
            return None
        return DescribeMoldModelsRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class GetMoldModelRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    mold_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetMoldModelRequest:
        self.namespace_name = namespace_name
        return self

    def with_mold_name(self, mold_name: str) -> GetMoldModelRequest:
        self.mold_name = mold_name
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
    ) -> Optional[GetMoldModelRequest]:
        if data is None:
            return None
        return GetMoldModelRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_mold_name(data.get('moldName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "moldName": self.mold_name,
        }


class DescribeMoldModelMastersRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeMoldModelMastersRequest:
        self.namespace_name = namespace_name
        return self

    def with_page_token(self, page_token: str) -> DescribeMoldModelMastersRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeMoldModelMastersRequest:
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
    ) -> Optional[DescribeMoldModelMastersRequest]:
        if data is None:
            return None
        return DescribeMoldModelMastersRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class CreateMoldModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    name: str = None
    description: str = None
    metadata: str = None
    form_model_name: str = None
    initial_max_capacity: int = None
    max_capacity: int = None

    def with_namespace_name(self, namespace_name: str) -> CreateMoldModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_name(self, name: str) -> CreateMoldModelMasterRequest:
        self.name = name
        return self

    def with_description(self, description: str) -> CreateMoldModelMasterRequest:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> CreateMoldModelMasterRequest:
        self.metadata = metadata
        return self

    def with_form_model_name(self, form_model_name: str) -> CreateMoldModelMasterRequest:
        self.form_model_name = form_model_name
        return self

    def with_initial_max_capacity(self, initial_max_capacity: int) -> CreateMoldModelMasterRequest:
        self.initial_max_capacity = initial_max_capacity
        return self

    def with_max_capacity(self, max_capacity: int) -> CreateMoldModelMasterRequest:
        self.max_capacity = max_capacity
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
    ) -> Optional[CreateMoldModelMasterRequest]:
        if data is None:
            return None
        return CreateMoldModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_name(data.get('name'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_form_model_name(data.get('formModelName'))\
            .with_initial_max_capacity(data.get('initialMaxCapacity'))\
            .with_max_capacity(data.get('maxCapacity'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "formModelName": self.form_model_name,
            "initialMaxCapacity": self.initial_max_capacity,
            "maxCapacity": self.max_capacity,
        }


class GetMoldModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    mold_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetMoldModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_mold_name(self, mold_name: str) -> GetMoldModelMasterRequest:
        self.mold_name = mold_name
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
    ) -> Optional[GetMoldModelMasterRequest]:
        if data is None:
            return None
        return GetMoldModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_mold_name(data.get('moldName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "moldName": self.mold_name,
        }


class UpdateMoldModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    mold_name: str = None
    description: str = None
    metadata: str = None
    form_model_name: str = None
    initial_max_capacity: int = None
    max_capacity: int = None

    def with_namespace_name(self, namespace_name: str) -> UpdateMoldModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_mold_name(self, mold_name: str) -> UpdateMoldModelMasterRequest:
        self.mold_name = mold_name
        return self

    def with_description(self, description: str) -> UpdateMoldModelMasterRequest:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> UpdateMoldModelMasterRequest:
        self.metadata = metadata
        return self

    def with_form_model_name(self, form_model_name: str) -> UpdateMoldModelMasterRequest:
        self.form_model_name = form_model_name
        return self

    def with_initial_max_capacity(self, initial_max_capacity: int) -> UpdateMoldModelMasterRequest:
        self.initial_max_capacity = initial_max_capacity
        return self

    def with_max_capacity(self, max_capacity: int) -> UpdateMoldModelMasterRequest:
        self.max_capacity = max_capacity
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
    ) -> Optional[UpdateMoldModelMasterRequest]:
        if data is None:
            return None
        return UpdateMoldModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_mold_name(data.get('moldName'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_form_model_name(data.get('formModelName'))\
            .with_initial_max_capacity(data.get('initialMaxCapacity'))\
            .with_max_capacity(data.get('maxCapacity'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "moldName": self.mold_name,
            "description": self.description,
            "metadata": self.metadata,
            "formModelName": self.form_model_name,
            "initialMaxCapacity": self.initial_max_capacity,
            "maxCapacity": self.max_capacity,
        }


class DeleteMoldModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    mold_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteMoldModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_mold_name(self, mold_name: str) -> DeleteMoldModelMasterRequest:
        self.mold_name = mold_name
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
    ) -> Optional[DeleteMoldModelMasterRequest]:
        if data is None:
            return None
        return DeleteMoldModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_mold_name(data.get('moldName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "moldName": self.mold_name,
        }


class ExportMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> ExportMasterRequest:
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
    ) -> Optional[ExportMasterRequest]:
        if data is None:
            return None
        return ExportMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class GetCurrentFormMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetCurrentFormMasterRequest:
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
    ) -> Optional[GetCurrentFormMasterRequest]:
        if data is None:
            return None
        return GetCurrentFormMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class UpdateCurrentFormMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    settings: str = None

    def with_namespace_name(self, namespace_name: str) -> UpdateCurrentFormMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_settings(self, settings: str) -> UpdateCurrentFormMasterRequest:
        self.settings = settings
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
    ) -> Optional[UpdateCurrentFormMasterRequest]:
        if data is None:
            return None
        return UpdateCurrentFormMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_settings(data.get('settings'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "settings": self.settings,
        }


class UpdateCurrentFormMasterFromGitHubRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    checkout_setting: GitHubCheckoutSetting = None

    def with_namespace_name(self, namespace_name: str) -> UpdateCurrentFormMasterFromGitHubRequest:
        self.namespace_name = namespace_name
        return self

    def with_checkout_setting(self, checkout_setting: GitHubCheckoutSetting) -> UpdateCurrentFormMasterFromGitHubRequest:
        self.checkout_setting = checkout_setting
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
    ) -> Optional[UpdateCurrentFormMasterFromGitHubRequest]:
        if data is None:
            return None
        return UpdateCurrentFormMasterFromGitHubRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_checkout_setting(GitHubCheckoutSetting.from_dict(data.get('checkoutSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "checkoutSetting": self.checkout_setting.to_dict() if self.checkout_setting else None,
        }


class DescribeMoldsRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    page_token: str = None
    limit: int = None
    access_token: str = None

    def with_namespace_name(self, namespace_name: str) -> DescribeMoldsRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> DescribeMoldsRequest:
        self.access_token = access_token
        return self

    def with_page_token(self, page_token: str) -> DescribeMoldsRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeMoldsRequest:
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
    ) -> Optional[DescribeMoldsRequest]:
        if data is None:
            return None
        return DescribeMoldsRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class DescribeMoldsByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeMoldsByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> DescribeMoldsByUserIdRequest:
        self.user_id = user_id
        return self

    def with_page_token(self, page_token: str) -> DescribeMoldsByUserIdRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeMoldsByUserIdRequest:
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
    ) -> Optional[DescribeMoldsByUserIdRequest]:
        if data is None:
            return None
        return DescribeMoldsByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class GetMoldRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    mold_name: str = None
    access_token: str = None

    def with_namespace_name(self, namespace_name: str) -> GetMoldRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> GetMoldRequest:
        self.access_token = access_token
        return self

    def with_mold_name(self, mold_name: str) -> GetMoldRequest:
        self.mold_name = mold_name
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
    ) -> Optional[GetMoldRequest]:
        if data is None:
            return None
        return GetMoldRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_mold_name(data.get('moldName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "moldName": self.mold_name,
        }


class GetMoldByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    mold_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetMoldByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> GetMoldByUserIdRequest:
        self.user_id = user_id
        return self

    def with_mold_name(self, mold_name: str) -> GetMoldByUserIdRequest:
        self.mold_name = mold_name
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
    ) -> Optional[GetMoldByUserIdRequest]:
        if data is None:
            return None
        return GetMoldByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_mold_name(data.get('moldName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "moldName": self.mold_name,
        }


class SetMoldCapacityByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    mold_name: str = None
    capacity: int = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> SetMoldCapacityByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> SetMoldCapacityByUserIdRequest:
        self.user_id = user_id
        return self

    def with_mold_name(self, mold_name: str) -> SetMoldCapacityByUserIdRequest:
        self.mold_name = mold_name
        return self

    def with_capacity(self, capacity: int) -> SetMoldCapacityByUserIdRequest:
        self.capacity = capacity
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> SetMoldCapacityByUserIdRequest:
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
    ) -> Optional[SetMoldCapacityByUserIdRequest]:
        if data is None:
            return None
        return SetMoldCapacityByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_mold_name(data.get('moldName'))\
            .with_capacity(data.get('capacity'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "moldName": self.mold_name,
            "capacity": self.capacity,
        }


class AddMoldCapacityByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    mold_name: str = None
    capacity: int = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> AddMoldCapacityByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> AddMoldCapacityByUserIdRequest:
        self.user_id = user_id
        return self

    def with_mold_name(self, mold_name: str) -> AddMoldCapacityByUserIdRequest:
        self.mold_name = mold_name
        return self

    def with_capacity(self, capacity: int) -> AddMoldCapacityByUserIdRequest:
        self.capacity = capacity
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> AddMoldCapacityByUserIdRequest:
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
    ) -> Optional[AddMoldCapacityByUserIdRequest]:
        if data is None:
            return None
        return AddMoldCapacityByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_mold_name(data.get('moldName'))\
            .with_capacity(data.get('capacity'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "moldName": self.mold_name,
            "capacity": self.capacity,
        }


class DeleteMoldRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    mold_name: str = None
    access_token: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteMoldRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> DeleteMoldRequest:
        self.access_token = access_token
        return self

    def with_mold_name(self, mold_name: str) -> DeleteMoldRequest:
        self.mold_name = mold_name
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
    ) -> Optional[DeleteMoldRequest]:
        if data is None:
            return None
        return DeleteMoldRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_mold_name(data.get('moldName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "moldName": self.mold_name,
        }


class DeleteMoldByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    mold_name: str = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteMoldByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> DeleteMoldByUserIdRequest:
        self.user_id = user_id
        return self

    def with_mold_name(self, mold_name: str) -> DeleteMoldByUserIdRequest:
        self.mold_name = mold_name
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> DeleteMoldByUserIdRequest:
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
    ) -> Optional[DeleteMoldByUserIdRequest]:
        if data is None:
            return None
        return DeleteMoldByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_mold_name(data.get('moldName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "moldName": self.mold_name,
        }


class AddCapacityByStampSheetRequest(core.Gs2Request):

    context_stack: str = None
    stamp_sheet: str = None
    key_id: str = None

    def with_stamp_sheet(self, stamp_sheet: str) -> AddCapacityByStampSheetRequest:
        self.stamp_sheet = stamp_sheet
        return self

    def with_key_id(self, key_id: str) -> AddCapacityByStampSheetRequest:
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
    ) -> Optional[AddCapacityByStampSheetRequest]:
        if data is None:
            return None
        return AddCapacityByStampSheetRequest()\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampSheet": self.stamp_sheet,
            "keyId": self.key_id,
        }


class SetCapacityByStampSheetRequest(core.Gs2Request):

    context_stack: str = None
    stamp_sheet: str = None
    key_id: str = None

    def with_stamp_sheet(self, stamp_sheet: str) -> SetCapacityByStampSheetRequest:
        self.stamp_sheet = stamp_sheet
        return self

    def with_key_id(self, key_id: str) -> SetCapacityByStampSheetRequest:
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
    ) -> Optional[SetCapacityByStampSheetRequest]:
        if data is None:
            return None
        return SetCapacityByStampSheetRequest()\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampSheet": self.stamp_sheet,
            "keyId": self.key_id,
        }


class DescribeFormsRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    mold_name: str = None
    access_token: str = None
    page_token: str = None
    limit: int = None
    access_token: str = None

    def with_namespace_name(self, namespace_name: str) -> DescribeFormsRequest:
        self.namespace_name = namespace_name
        return self

    def with_mold_name(self, mold_name: str) -> DescribeFormsRequest:
        self.mold_name = mold_name
        return self

    def with_access_token(self, access_token: str) -> DescribeFormsRequest:
        self.access_token = access_token
        return self

    def with_page_token(self, page_token: str) -> DescribeFormsRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeFormsRequest:
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
    ) -> Optional[DescribeFormsRequest]:
        if data is None:
            return None
        return DescribeFormsRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_mold_name(data.get('moldName'))\
            .with_access_token(data.get('accessToken'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "moldName": self.mold_name,
            "accessToken": self.access_token,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class DescribeFormsByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    mold_name: str = None
    user_id: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeFormsByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_mold_name(self, mold_name: str) -> DescribeFormsByUserIdRequest:
        self.mold_name = mold_name
        return self

    def with_user_id(self, user_id: str) -> DescribeFormsByUserIdRequest:
        self.user_id = user_id
        return self

    def with_page_token(self, page_token: str) -> DescribeFormsByUserIdRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeFormsByUserIdRequest:
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
    ) -> Optional[DescribeFormsByUserIdRequest]:
        if data is None:
            return None
        return DescribeFormsByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_mold_name(data.get('moldName'))\
            .with_user_id(data.get('userId'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "moldName": self.mold_name,
            "userId": self.user_id,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class GetFormRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    mold_name: str = None
    index: int = None
    access_token: str = None

    def with_namespace_name(self, namespace_name: str) -> GetFormRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> GetFormRequest:
        self.access_token = access_token
        return self

    def with_mold_name(self, mold_name: str) -> GetFormRequest:
        self.mold_name = mold_name
        return self

    def with_index(self, index: int) -> GetFormRequest:
        self.index = index
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
    ) -> Optional[GetFormRequest]:
        if data is None:
            return None
        return GetFormRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_mold_name(data.get('moldName'))\
            .with_index(data.get('index'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "moldName": self.mold_name,
            "index": self.index,
        }


class GetFormByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    mold_name: str = None
    index: int = None

    def with_namespace_name(self, namespace_name: str) -> GetFormByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> GetFormByUserIdRequest:
        self.user_id = user_id
        return self

    def with_mold_name(self, mold_name: str) -> GetFormByUserIdRequest:
        self.mold_name = mold_name
        return self

    def with_index(self, index: int) -> GetFormByUserIdRequest:
        self.index = index
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
    ) -> Optional[GetFormByUserIdRequest]:
        if data is None:
            return None
        return GetFormByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_mold_name(data.get('moldName'))\
            .with_index(data.get('index'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "moldName": self.mold_name,
            "index": self.index,
        }


class GetFormWithSignatureRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    mold_name: str = None
    index: int = None
    key_id: str = None
    access_token: str = None

    def with_namespace_name(self, namespace_name: str) -> GetFormWithSignatureRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> GetFormWithSignatureRequest:
        self.access_token = access_token
        return self

    def with_mold_name(self, mold_name: str) -> GetFormWithSignatureRequest:
        self.mold_name = mold_name
        return self

    def with_index(self, index: int) -> GetFormWithSignatureRequest:
        self.index = index
        return self

    def with_key_id(self, key_id: str) -> GetFormWithSignatureRequest:
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
    ) -> Optional[GetFormWithSignatureRequest]:
        if data is None:
            return None
        return GetFormWithSignatureRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_mold_name(data.get('moldName'))\
            .with_index(data.get('index'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "moldName": self.mold_name,
            "index": self.index,
            "keyId": self.key_id,
        }


class GetFormWithSignatureByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    mold_name: str = None
    index: int = None
    key_id: str = None

    def with_namespace_name(self, namespace_name: str) -> GetFormWithSignatureByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> GetFormWithSignatureByUserIdRequest:
        self.user_id = user_id
        return self

    def with_mold_name(self, mold_name: str) -> GetFormWithSignatureByUserIdRequest:
        self.mold_name = mold_name
        return self

    def with_index(self, index: int) -> GetFormWithSignatureByUserIdRequest:
        self.index = index
        return self

    def with_key_id(self, key_id: str) -> GetFormWithSignatureByUserIdRequest:
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
    ) -> Optional[GetFormWithSignatureByUserIdRequest]:
        if data is None:
            return None
        return GetFormWithSignatureByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_mold_name(data.get('moldName'))\
            .with_index(data.get('index'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "moldName": self.mold_name,
            "index": self.index,
            "keyId": self.key_id,
        }


class SetFormByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    mold_name: str = None
    index: int = None
    slots: List[Slot] = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> SetFormByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> SetFormByUserIdRequest:
        self.user_id = user_id
        return self

    def with_mold_name(self, mold_name: str) -> SetFormByUserIdRequest:
        self.mold_name = mold_name
        return self

    def with_index(self, index: int) -> SetFormByUserIdRequest:
        self.index = index
        return self

    def with_slots(self, slots: List[Slot]) -> SetFormByUserIdRequest:
        self.slots = slots
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> SetFormByUserIdRequest:
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
    ) -> Optional[SetFormByUserIdRequest]:
        if data is None:
            return None
        return SetFormByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_mold_name(data.get('moldName'))\
            .with_index(data.get('index'))\
            .with_slots([
                Slot.from_dict(data.get('slots')[i])
                for i in range(len(data.get('slots')) if data.get('slots') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "moldName": self.mold_name,
            "index": self.index,
            "slots": [
                self.slots[i].to_dict() if self.slots[i] else None
                for i in range(len(self.slots) if self.slots else 0)
            ],
        }


class SetFormWithSignatureRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    mold_name: str = None
    index: int = None
    slots: List[SlotWithSignature] = None
    key_id: str = None
    access_token: str = None

    def with_namespace_name(self, namespace_name: str) -> SetFormWithSignatureRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> SetFormWithSignatureRequest:
        self.access_token = access_token
        return self

    def with_mold_name(self, mold_name: str) -> SetFormWithSignatureRequest:
        self.mold_name = mold_name
        return self

    def with_index(self, index: int) -> SetFormWithSignatureRequest:
        self.index = index
        return self

    def with_slots(self, slots: List[SlotWithSignature]) -> SetFormWithSignatureRequest:
        self.slots = slots
        return self

    def with_key_id(self, key_id: str) -> SetFormWithSignatureRequest:
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
    ) -> Optional[SetFormWithSignatureRequest]:
        if data is None:
            return None
        return SetFormWithSignatureRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_mold_name(data.get('moldName'))\
            .with_index(data.get('index'))\
            .with_slots([
                SlotWithSignature.from_dict(data.get('slots')[i])
                for i in range(len(data.get('slots')) if data.get('slots') else 0)
            ])\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "moldName": self.mold_name,
            "index": self.index,
            "slots": [
                self.slots[i].to_dict() if self.slots[i] else None
                for i in range(len(self.slots) if self.slots else 0)
            ],
            "keyId": self.key_id,
        }


class AcquireActionsToFormPropertiesRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    mold_name: str = None
    index: int = None
    acquire_action: AcquireAction = None
    queue_namespace_id: str = None
    key_id: str = None
    config: List[AcquireActionConfig] = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> AcquireActionsToFormPropertiesRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> AcquireActionsToFormPropertiesRequest:
        self.user_id = user_id
        return self

    def with_mold_name(self, mold_name: str) -> AcquireActionsToFormPropertiesRequest:
        self.mold_name = mold_name
        return self

    def with_index(self, index: int) -> AcquireActionsToFormPropertiesRequest:
        self.index = index
        return self

    def with_acquire_action(self, acquire_action: AcquireAction) -> AcquireActionsToFormPropertiesRequest:
        self.acquire_action = acquire_action
        return self

    def with_queue_namespace_id(self, queue_namespace_id: str) -> AcquireActionsToFormPropertiesRequest:
        self.queue_namespace_id = queue_namespace_id
        return self

    def with_key_id(self, key_id: str) -> AcquireActionsToFormPropertiesRequest:
        self.key_id = key_id
        return self

    def with_config(self, config: List[AcquireActionConfig]) -> AcquireActionsToFormPropertiesRequest:
        self.config = config
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> AcquireActionsToFormPropertiesRequest:
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
    ) -> Optional[AcquireActionsToFormPropertiesRequest]:
        if data is None:
            return None
        return AcquireActionsToFormPropertiesRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_mold_name(data.get('moldName'))\
            .with_index(data.get('index'))\
            .with_acquire_action(AcquireAction.from_dict(data.get('acquireAction')))\
            .with_queue_namespace_id(data.get('queueNamespaceId'))\
            .with_key_id(data.get('keyId'))\
            .with_config([
                AcquireActionConfig.from_dict(data.get('config')[i])
                for i in range(len(data.get('config')) if data.get('config') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "moldName": self.mold_name,
            "index": self.index,
            "acquireAction": self.acquire_action.to_dict() if self.acquire_action else None,
            "queueNamespaceId": self.queue_namespace_id,
            "keyId": self.key_id,
            "config": [
                self.config[i].to_dict() if self.config[i] else None
                for i in range(len(self.config) if self.config else 0)
            ],
        }


class DeleteFormRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    mold_name: str = None
    index: int = None
    access_token: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteFormRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> DeleteFormRequest:
        self.access_token = access_token
        return self

    def with_mold_name(self, mold_name: str) -> DeleteFormRequest:
        self.mold_name = mold_name
        return self

    def with_index(self, index: int) -> DeleteFormRequest:
        self.index = index
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
    ) -> Optional[DeleteFormRequest]:
        if data is None:
            return None
        return DeleteFormRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_mold_name(data.get('moldName'))\
            .with_index(data.get('index'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "moldName": self.mold_name,
            "index": self.index,
        }


class DeleteFormByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    mold_name: str = None
    index: int = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteFormByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> DeleteFormByUserIdRequest:
        self.user_id = user_id
        return self

    def with_mold_name(self, mold_name: str) -> DeleteFormByUserIdRequest:
        self.mold_name = mold_name
        return self

    def with_index(self, index: int) -> DeleteFormByUserIdRequest:
        self.index = index
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> DeleteFormByUserIdRequest:
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
    ) -> Optional[DeleteFormByUserIdRequest]:
        if data is None:
            return None
        return DeleteFormByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_mold_name(data.get('moldName'))\
            .with_index(data.get('index'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "moldName": self.mold_name,
            "index": self.index,
        }


class AcquireActionToFormPropertiesByStampSheetRequest(core.Gs2Request):

    context_stack: str = None
    stamp_sheet: str = None
    key_id: str = None

    def with_stamp_sheet(self, stamp_sheet: str) -> AcquireActionToFormPropertiesByStampSheetRequest:
        self.stamp_sheet = stamp_sheet
        return self

    def with_key_id(self, key_id: str) -> AcquireActionToFormPropertiesByStampSheetRequest:
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
    ) -> Optional[AcquireActionToFormPropertiesByStampSheetRequest]:
        if data is None:
            return None
        return AcquireActionToFormPropertiesByStampSheetRequest()\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampSheet": self.stamp_sheet,
            "keyId": self.key_id,
        }