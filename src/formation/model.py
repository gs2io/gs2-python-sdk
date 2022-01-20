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

import re
from typing import *
import core


class AcquireAction(core.Gs2Model):
    action: str = None
    request: str = None

    def with_action(self, action: str) -> AcquireAction:
        self.action = action
        return self

    def with_request(self, request: str) -> AcquireAction:
        self.request = request
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
    ) -> Optional[AcquireAction]:
        if data is None:
            return None
        return AcquireAction()\
            .with_action(data.get('action'))\
            .with_request(data.get('request'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "action": self.action,
            "request": self.request,
        }


class LogSetting(core.Gs2Model):
    logging_namespace_id: str = None

    def with_logging_namespace_id(self, logging_namespace_id: str) -> LogSetting:
        self.logging_namespace_id = logging_namespace_id
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
    ) -> Optional[LogSetting]:
        if data is None:
            return None
        return LogSetting()\
            .with_logging_namespace_id(data.get('loggingNamespaceId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "loggingNamespaceId": self.logging_namespace_id,
        }


class ScriptSetting(core.Gs2Model):
    trigger_script_id: str = None
    done_trigger_target_type: str = None
    done_trigger_script_id: str = None
    done_trigger_queue_namespace_id: str = None

    def with_trigger_script_id(self, trigger_script_id: str) -> ScriptSetting:
        self.trigger_script_id = trigger_script_id
        return self

    def with_done_trigger_target_type(self, done_trigger_target_type: str) -> ScriptSetting:
        self.done_trigger_target_type = done_trigger_target_type
        return self

    def with_done_trigger_script_id(self, done_trigger_script_id: str) -> ScriptSetting:
        self.done_trigger_script_id = done_trigger_script_id
        return self

    def with_done_trigger_queue_namespace_id(self, done_trigger_queue_namespace_id: str) -> ScriptSetting:
        self.done_trigger_queue_namespace_id = done_trigger_queue_namespace_id
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
    ) -> Optional[ScriptSetting]:
        if data is None:
            return None
        return ScriptSetting()\
            .with_trigger_script_id(data.get('triggerScriptId'))\
            .with_done_trigger_target_type(data.get('doneTriggerTargetType'))\
            .with_done_trigger_script_id(data.get('doneTriggerScriptId'))\
            .with_done_trigger_queue_namespace_id(data.get('doneTriggerQueueNamespaceId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "triggerScriptId": self.trigger_script_id,
            "doneTriggerTargetType": self.done_trigger_target_type,
            "doneTriggerScriptId": self.done_trigger_script_id,
            "doneTriggerQueueNamespaceId": self.done_trigger_queue_namespace_id,
        }


class GitHubCheckoutSetting(core.Gs2Model):
    api_key_id: str = None
    repository_name: str = None
    source_path: str = None
    reference_type: str = None
    commit_hash: str = None
    branch_name: str = None
    tag_name: str = None

    def with_api_key_id(self, api_key_id: str) -> GitHubCheckoutSetting:
        self.api_key_id = api_key_id
        return self

    def with_repository_name(self, repository_name: str) -> GitHubCheckoutSetting:
        self.repository_name = repository_name
        return self

    def with_source_path(self, source_path: str) -> GitHubCheckoutSetting:
        self.source_path = source_path
        return self

    def with_reference_type(self, reference_type: str) -> GitHubCheckoutSetting:
        self.reference_type = reference_type
        return self

    def with_commit_hash(self, commit_hash: str) -> GitHubCheckoutSetting:
        self.commit_hash = commit_hash
        return self

    def with_branch_name(self, branch_name: str) -> GitHubCheckoutSetting:
        self.branch_name = branch_name
        return self

    def with_tag_name(self, tag_name: str) -> GitHubCheckoutSetting:
        self.tag_name = tag_name
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
    ) -> Optional[GitHubCheckoutSetting]:
        if data is None:
            return None
        return GitHubCheckoutSetting()\
            .with_api_key_id(data.get('apiKeyId'))\
            .with_repository_name(data.get('repositoryName'))\
            .with_source_path(data.get('sourcePath'))\
            .with_reference_type(data.get('referenceType'))\
            .with_commit_hash(data.get('commitHash'))\
            .with_branch_name(data.get('branchName'))\
            .with_tag_name(data.get('tagName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "apiKeyId": self.api_key_id,
            "repositoryName": self.repository_name,
            "sourcePath": self.source_path,
            "referenceType": self.reference_type,
            "commitHash": self.commit_hash,
            "branchName": self.branch_name,
            "tagName": self.tag_name,
        }


class Config(core.Gs2Model):
    key: str = None
    value: str = None

    def with_key(self, key: str) -> Config:
        self.key = key
        return self

    def with_value(self, value: str) -> Config:
        self.value = value
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
    ) -> Optional[Config]:
        if data is None:
            return None
        return Config()\
            .with_key(data.get('key'))\
            .with_value(data.get('value'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "key": self.key,
            "value": self.value,
        }


class AcquireActionConfig(core.Gs2Model):
    name: str = None
    config: List[Config] = None

    def with_name(self, name: str) -> AcquireActionConfig:
        self.name = name
        return self

    def with_config(self, config: List[Config]) -> AcquireActionConfig:
        self.config = config
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
    ) -> Optional[AcquireActionConfig]:
        if data is None:
            return None
        return AcquireActionConfig()\
            .with_name(data.get('name'))\
            .with_config([
                Config.from_dict(data.get('config')[i])
                for i in range(len(data.get('config')) if data.get('config') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "config": [
                self.config[i].to_dict() if self.config[i] else None
                for i in range(len(self.config) if self.config else 0)
            ],
        }


class SlotWithSignature(core.Gs2Model):
    name: str = None
    property_type: str = None
    body: str = None
    signature: str = None
    metadata: str = None

    def with_name(self, name: str) -> SlotWithSignature:
        self.name = name
        return self

    def with_property_type(self, property_type: str) -> SlotWithSignature:
        self.property_type = property_type
        return self

    def with_body(self, body: str) -> SlotWithSignature:
        self.body = body
        return self

    def with_signature(self, signature: str) -> SlotWithSignature:
        self.signature = signature
        return self

    def with_metadata(self, metadata: str) -> SlotWithSignature:
        self.metadata = metadata
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
    ) -> Optional[SlotWithSignature]:
        if data is None:
            return None
        return SlotWithSignature()\
            .with_name(data.get('name'))\
            .with_property_type(data.get('propertyType'))\
            .with_body(data.get('body'))\
            .with_signature(data.get('signature'))\
            .with_metadata(data.get('metadata'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "propertyType": self.property_type,
            "body": self.body,
            "signature": self.signature,
            "metadata": self.metadata,
        }


class SlotModel(core.Gs2Model):
    name: str = None
    property_regex: str = None
    metadata: str = None

    def with_name(self, name: str) -> SlotModel:
        self.name = name
        return self

    def with_property_regex(self, property_regex: str) -> SlotModel:
        self.property_regex = property_regex
        return self

    def with_metadata(self, metadata: str) -> SlotModel:
        self.metadata = metadata
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
    ) -> Optional[SlotModel]:
        if data is None:
            return None
        return SlotModel()\
            .with_name(data.get('name'))\
            .with_property_regex(data.get('propertyRegex'))\
            .with_metadata(data.get('metadata'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "propertyRegex": self.property_regex,
            "metadata": self.metadata,
        }


class Slot(core.Gs2Model):
    name: str = None
    property_id: str = None
    metadata: str = None

    def with_name(self, name: str) -> Slot:
        self.name = name
        return self

    def with_property_id(self, property_id: str) -> Slot:
        self.property_id = property_id
        return self

    def with_metadata(self, metadata: str) -> Slot:
        self.metadata = metadata
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
    ) -> Optional[Slot]:
        if data is None:
            return None
        return Slot()\
            .with_name(data.get('name'))\
            .with_property_id(data.get('propertyId'))\
            .with_metadata(data.get('metadata'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "propertyId": self.property_id,
            "metadata": self.metadata,
        }


class Form(core.Gs2Model):
    form_id: str = None
    name: str = None
    index: int = None
    slots: List[Slot] = None
    created_at: int = None
    updated_at: int = None

    def with_form_id(self, form_id: str) -> Form:
        self.form_id = form_id
        return self

    def with_name(self, name: str) -> Form:
        self.name = name
        return self

    def with_index(self, index: int) -> Form:
        self.index = index
        return self

    def with_slots(self, slots: List[Slot]) -> Form:
        self.slots = slots
        return self

    def with_created_at(self, created_at: int) -> Form:
        self.created_at = created_at
        return self

    def with_updated_at(self, updated_at: int) -> Form:
        self.updated_at = updated_at
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
        user_id,
        mold_name,
        index,
    ):
        return 'grn:gs2:{region}:{ownerId}:formation:{namespaceName}:user:{userId}:mold:{moldName}:form:{index}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
            userId=user_id,
            moldName=mold_name,
            index=index,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+):form:(?P<index>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+):form:(?P<index>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+):form:(?P<index>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

    @classmethod
    def get_user_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+):form:(?P<index>.+)', grn)
        if match is None:
            return None
        return match.group('user_id')

    @classmethod
    def get_mold_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+):form:(?P<index>.+)', grn)
        if match is None:
            return None
        return match.group('mold_name')

    @classmethod
    def get_index_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+):form:(?P<index>.+)', grn)
        if match is None:
            return None
        return match.group('index')

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
    ) -> Optional[Form]:
        if data is None:
            return None
        return Form()\
            .with_form_id(data.get('formId'))\
            .with_name(data.get('name'))\
            .with_index(data.get('index'))\
            .with_slots([
                Slot.from_dict(data.get('slots')[i])
                for i in range(len(data.get('slots')) if data.get('slots') else 0)
            ])\
            .with_created_at(data.get('createdAt'))\
            .with_updated_at(data.get('updatedAt'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "formId": self.form_id,
            "name": self.name,
            "index": self.index,
            "slots": [
                self.slots[i].to_dict() if self.slots[i] else None
                for i in range(len(self.slots) if self.slots else 0)
            ],
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }


class Mold(core.Gs2Model):
    mold_id: str = None
    name: str = None
    user_id: str = None
    capacity: int = None
    created_at: int = None
    updated_at: int = None

    def with_mold_id(self, mold_id: str) -> Mold:
        self.mold_id = mold_id
        return self

    def with_name(self, name: str) -> Mold:
        self.name = name
        return self

    def with_user_id(self, user_id: str) -> Mold:
        self.user_id = user_id
        return self

    def with_capacity(self, capacity: int) -> Mold:
        self.capacity = capacity
        return self

    def with_created_at(self, created_at: int) -> Mold:
        self.created_at = created_at
        return self

    def with_updated_at(self, updated_at: int) -> Mold:
        self.updated_at = updated_at
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
        user_id,
        mold_name,
    ):
        return 'grn:gs2:{region}:{ownerId}:formation:{namespaceName}:user:{userId}:mold:{moldName}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
            userId=user_id,
            moldName=mold_name,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

    @classmethod
    def get_user_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('user_id')

    @classmethod
    def get_mold_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):user:(?P<userId>.+):mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('mold_name')

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
    ) -> Optional[Mold]:
        if data is None:
            return None
        return Mold()\
            .with_mold_id(data.get('moldId'))\
            .with_name(data.get('name'))\
            .with_user_id(data.get('userId'))\
            .with_capacity(data.get('capacity'))\
            .with_created_at(data.get('createdAt'))\
            .with_updated_at(data.get('updatedAt'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "moldId": self.mold_id,
            "name": self.name,
            "userId": self.user_id,
            "capacity": self.capacity,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }


class CurrentFormMaster(core.Gs2Model):
    namespace_id: str = None
    settings: str = None

    def with_namespace_id(self, namespace_id: str) -> CurrentFormMaster:
        self.namespace_id = namespace_id
        return self

    def with_settings(self, settings: str) -> CurrentFormMaster:
        self.settings = settings
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
    ):
        return 'grn:gs2:{region}:{ownerId}:formation:{namespaceName}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

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
    ) -> Optional[CurrentFormMaster]:
        if data is None:
            return None
        return CurrentFormMaster()\
            .with_namespace_id(data.get('namespaceId'))\
            .with_settings(data.get('settings'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceId": self.namespace_id,
            "settings": self.settings,
        }


class MoldModelMaster(core.Gs2Model):
    mold_model_id: str = None
    name: str = None
    description: str = None
    metadata: str = None
    initial_max_capacity: int = None
    max_capacity: int = None
    form_model_name: str = None
    created_at: int = None
    updated_at: int = None

    def with_mold_model_id(self, mold_model_id: str) -> MoldModelMaster:
        self.mold_model_id = mold_model_id
        return self

    def with_name(self, name: str) -> MoldModelMaster:
        self.name = name
        return self

    def with_description(self, description: str) -> MoldModelMaster:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> MoldModelMaster:
        self.metadata = metadata
        return self

    def with_initial_max_capacity(self, initial_max_capacity: int) -> MoldModelMaster:
        self.initial_max_capacity = initial_max_capacity
        return self

    def with_max_capacity(self, max_capacity: int) -> MoldModelMaster:
        self.max_capacity = max_capacity
        return self

    def with_form_model_name(self, form_model_name: str) -> MoldModelMaster:
        self.form_model_name = form_model_name
        return self

    def with_created_at(self, created_at: int) -> MoldModelMaster:
        self.created_at = created_at
        return self

    def with_updated_at(self, updated_at: int) -> MoldModelMaster:
        self.updated_at = updated_at
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
        mold_name,
    ):
        return 'grn:gs2:{region}:{ownerId}:formation:{namespaceName}:model:mold:{moldName}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
            moldName=mold_name,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

    @classmethod
    def get_mold_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('mold_name')

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
    ) -> Optional[MoldModelMaster]:
        if data is None:
            return None
        return MoldModelMaster()\
            .with_mold_model_id(data.get('moldModelId'))\
            .with_name(data.get('name'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_initial_max_capacity(data.get('initialMaxCapacity'))\
            .with_max_capacity(data.get('maxCapacity'))\
            .with_form_model_name(data.get('formModelName'))\
            .with_created_at(data.get('createdAt'))\
            .with_updated_at(data.get('updatedAt'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "moldModelId": self.mold_model_id,
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "initialMaxCapacity": self.initial_max_capacity,
            "maxCapacity": self.max_capacity,
            "formModelName": self.form_model_name,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }


class MoldModel(core.Gs2Model):
    mold_model_id: str = None
    name: str = None
    metadata: str = None
    initial_max_capacity: int = None
    max_capacity: int = None
    form_model: FormModel = None

    def with_mold_model_id(self, mold_model_id: str) -> MoldModel:
        self.mold_model_id = mold_model_id
        return self

    def with_name(self, name: str) -> MoldModel:
        self.name = name
        return self

    def with_metadata(self, metadata: str) -> MoldModel:
        self.metadata = metadata
        return self

    def with_initial_max_capacity(self, initial_max_capacity: int) -> MoldModel:
        self.initial_max_capacity = initial_max_capacity
        return self

    def with_max_capacity(self, max_capacity: int) -> MoldModel:
        self.max_capacity = max_capacity
        return self

    def with_form_model(self, form_model: FormModel) -> MoldModel:
        self.form_model = form_model
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
        mold_name,
    ):
        return 'grn:gs2:{region}:{ownerId}:formation:{namespaceName}:model:mold:{moldName}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
            moldName=mold_name,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

    @classmethod
    def get_mold_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:mold:(?P<moldName>.+)', grn)
        if match is None:
            return None
        return match.group('mold_name')

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
    ) -> Optional[MoldModel]:
        if data is None:
            return None
        return MoldModel()\
            .with_mold_model_id(data.get('moldModelId'))\
            .with_name(data.get('name'))\
            .with_metadata(data.get('metadata'))\
            .with_initial_max_capacity(data.get('initialMaxCapacity'))\
            .with_max_capacity(data.get('maxCapacity'))\
            .with_form_model(FormModel.from_dict(data.get('formModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "moldModelId": self.mold_model_id,
            "name": self.name,
            "metadata": self.metadata,
            "initialMaxCapacity": self.initial_max_capacity,
            "maxCapacity": self.max_capacity,
            "formModel": self.form_model.to_dict() if self.form_model else None,
        }


class FormModelMaster(core.Gs2Model):
    form_model_id: str = None
    name: str = None
    description: str = None
    metadata: str = None
    slots: List[SlotModel] = None
    created_at: int = None
    updated_at: int = None

    def with_form_model_id(self, form_model_id: str) -> FormModelMaster:
        self.form_model_id = form_model_id
        return self

    def with_name(self, name: str) -> FormModelMaster:
        self.name = name
        return self

    def with_description(self, description: str) -> FormModelMaster:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> FormModelMaster:
        self.metadata = metadata
        return self

    def with_slots(self, slots: List[SlotModel]) -> FormModelMaster:
        self.slots = slots
        return self

    def with_created_at(self, created_at: int) -> FormModelMaster:
        self.created_at = created_at
        return self

    def with_updated_at(self, updated_at: int) -> FormModelMaster:
        self.updated_at = updated_at
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
        form_model_name,
    ):
        return 'grn:gs2:{region}:{ownerId}:formation:{namespaceName}:model:form:{formModelName}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
            formModelName=form_model_name,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:form:(?P<formModelName>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:form:(?P<formModelName>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:form:(?P<formModelName>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

    @classmethod
    def get_form_model_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:form:(?P<formModelName>.+)', grn)
        if match is None:
            return None
        return match.group('form_model_name')

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
    ) -> Optional[FormModelMaster]:
        if data is None:
            return None
        return FormModelMaster()\
            .with_form_model_id(data.get('formModelId'))\
            .with_name(data.get('name'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_slots([
                SlotModel.from_dict(data.get('slots')[i])
                for i in range(len(data.get('slots')) if data.get('slots') else 0)
            ])\
            .with_created_at(data.get('createdAt'))\
            .with_updated_at(data.get('updatedAt'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "formModelId": self.form_model_id,
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "slots": [
                self.slots[i].to_dict() if self.slots[i] else None
                for i in range(len(self.slots) if self.slots else 0)
            ],
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }


class FormModel(core.Gs2Model):
    form_model_id: str = None
    name: str = None
    metadata: str = None
    slots: List[SlotModel] = None

    def with_form_model_id(self, form_model_id: str) -> FormModel:
        self.form_model_id = form_model_id
        return self

    def with_name(self, name: str) -> FormModel:
        self.name = name
        return self

    def with_metadata(self, metadata: str) -> FormModel:
        self.metadata = metadata
        return self

    def with_slots(self, slots: List[SlotModel]) -> FormModel:
        self.slots = slots
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
        form_model_name,
    ):
        return 'grn:gs2:{region}:{ownerId}:formation:{namespaceName}:model:form:{formModelName}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
            formModelName=form_model_name,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:form:(?P<formModelName>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:form:(?P<formModelName>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:form:(?P<formModelName>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

    @classmethod
    def get_form_model_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+):model:form:(?P<formModelName>.+)', grn)
        if match is None:
            return None
        return match.group('form_model_name')

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
    ) -> Optional[FormModel]:
        if data is None:
            return None
        return FormModel()\
            .with_form_model_id(data.get('formModelId'))\
            .with_name(data.get('name'))\
            .with_metadata(data.get('metadata'))\
            .with_slots([
                SlotModel.from_dict(data.get('slots')[i])
                for i in range(len(data.get('slots')) if data.get('slots') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "formModelId": self.form_model_id,
            "name": self.name,
            "metadata": self.metadata,
            "slots": [
                self.slots[i].to_dict() if self.slots[i] else None
                for i in range(len(self.slots) if self.slots else 0)
            ],
        }


class Namespace(core.Gs2Model):
    namespace_id: str = None
    name: str = None
    description: str = None
    update_mold_script: ScriptSetting = None
    update_form_script: ScriptSetting = None
    log_setting: LogSetting = None
    created_at: int = None
    updated_at: int = None

    def with_namespace_id(self, namespace_id: str) -> Namespace:
        self.namespace_id = namespace_id
        return self

    def with_name(self, name: str) -> Namespace:
        self.name = name
        return self

    def with_description(self, description: str) -> Namespace:
        self.description = description
        return self

    def with_update_mold_script(self, update_mold_script: ScriptSetting) -> Namespace:
        self.update_mold_script = update_mold_script
        return self

    def with_update_form_script(self, update_form_script: ScriptSetting) -> Namespace:
        self.update_form_script = update_form_script
        return self

    def with_log_setting(self, log_setting: LogSetting) -> Namespace:
        self.log_setting = log_setting
        return self

    def with_created_at(self, created_at: int) -> Namespace:
        self.created_at = created_at
        return self

    def with_updated_at(self, updated_at: int) -> Namespace:
        self.updated_at = updated_at
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
    ):
        return 'grn:gs2:{region}:{ownerId}:formation:{namespaceName}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):formation:(?P<namespaceName>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

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
    ) -> Optional[Namespace]:
        if data is None:
            return None
        return Namespace()\
            .with_namespace_id(data.get('namespaceId'))\
            .with_name(data.get('name'))\
            .with_description(data.get('description'))\
            .with_update_mold_script(ScriptSetting.from_dict(data.get('updateMoldScript')))\
            .with_update_form_script(ScriptSetting.from_dict(data.get('updateFormScript')))\
            .with_log_setting(LogSetting.from_dict(data.get('logSetting')))\
            .with_created_at(data.get('createdAt'))\
            .with_updated_at(data.get('updatedAt'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceId": self.namespace_id,
            "name": self.name,
            "description": self.description,
            "updateMoldScript": self.update_mold_script.to_dict() if self.update_mold_script else None,
            "updateFormScript": self.update_form_script.to_dict() if self.update_form_script else None,
            "logSetting": self.log_setting.to_dict() if self.log_setting else None,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }