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
    transaction_setting: TransactionSetting = None
    log_setting: LogSetting = None

    def with_name(self, name: str) -> CreateNamespaceRequest:
        self.name = name
        return self

    def with_description(self, description: str) -> CreateNamespaceRequest:
        self.description = description
        return self

    def with_transaction_setting(self, transaction_setting: TransactionSetting) -> CreateNamespaceRequest:
        self.transaction_setting = transaction_setting
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
            .with_transaction_setting(TransactionSetting.from_dict(data.get('transactionSetting')))\
            .with_log_setting(LogSetting.from_dict(data.get('logSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "transactionSetting": self.transaction_setting.to_dict() if self.transaction_setting else None,
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
    transaction_setting: TransactionSetting = None
    log_setting: LogSetting = None

    def with_namespace_name(self, namespace_name: str) -> UpdateNamespaceRequest:
        self.namespace_name = namespace_name
        return self

    def with_description(self, description: str) -> UpdateNamespaceRequest:
        self.description = description
        return self

    def with_transaction_setting(self, transaction_setting: TransactionSetting) -> UpdateNamespaceRequest:
        self.transaction_setting = transaction_setting
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
            .with_transaction_setting(TransactionSetting.from_dict(data.get('transactionSetting')))\
            .with_log_setting(LogSetting.from_dict(data.get('logSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "description": self.description,
            "transactionSetting": self.transaction_setting.to_dict() if self.transaction_setting else None,
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


class DescribeBalanceParameterModelsRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DescribeBalanceParameterModelsRequest:
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
    ) -> Optional[DescribeBalanceParameterModelsRequest]:
        if data is None:
            return None
        return DescribeBalanceParameterModelsRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class GetBalanceParameterModelRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    parameter_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetBalanceParameterModelRequest:
        self.namespace_name = namespace_name
        return self

    def with_parameter_name(self, parameter_name: str) -> GetBalanceParameterModelRequest:
        self.parameter_name = parameter_name
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
    ) -> Optional[GetBalanceParameterModelRequest]:
        if data is None:
            return None
        return GetBalanceParameterModelRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_parameter_name(data.get('parameterName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "parameterName": self.parameter_name,
        }


class DescribeBalanceParameterModelMastersRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeBalanceParameterModelMastersRequest:
        self.namespace_name = namespace_name
        return self

    def with_page_token(self, page_token: str) -> DescribeBalanceParameterModelMastersRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeBalanceParameterModelMastersRequest:
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
    ) -> Optional[DescribeBalanceParameterModelMastersRequest]:
        if data is None:
            return None
        return DescribeBalanceParameterModelMastersRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class CreateBalanceParameterModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    name: str = None
    description: str = None
    metadata: str = None
    total_value: int = None
    initial_value_strategy: str = None
    parameters: List[BalanceParameterValueModel] = None

    def with_namespace_name(self, namespace_name: str) -> CreateBalanceParameterModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_name(self, name: str) -> CreateBalanceParameterModelMasterRequest:
        self.name = name
        return self

    def with_description(self, description: str) -> CreateBalanceParameterModelMasterRequest:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> CreateBalanceParameterModelMasterRequest:
        self.metadata = metadata
        return self

    def with_total_value(self, total_value: int) -> CreateBalanceParameterModelMasterRequest:
        self.total_value = total_value
        return self

    def with_initial_value_strategy(self, initial_value_strategy: str) -> CreateBalanceParameterModelMasterRequest:
        self.initial_value_strategy = initial_value_strategy
        return self

    def with_parameters(self, parameters: List[BalanceParameterValueModel]) -> CreateBalanceParameterModelMasterRequest:
        self.parameters = parameters
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
    ) -> Optional[CreateBalanceParameterModelMasterRequest]:
        if data is None:
            return None
        return CreateBalanceParameterModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_name(data.get('name'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_total_value(data.get('totalValue'))\
            .with_initial_value_strategy(data.get('initialValueStrategy'))\
            .with_parameters([
                BalanceParameterValueModel.from_dict(data.get('parameters')[i])
                for i in range(len(data.get('parameters')) if data.get('parameters') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "totalValue": self.total_value,
            "initialValueStrategy": self.initial_value_strategy,
            "parameters": [
                self.parameters[i].to_dict() if self.parameters[i] else None
                for i in range(len(self.parameters) if self.parameters else 0)
            ],
        }


class GetBalanceParameterModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    parameter_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetBalanceParameterModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_parameter_name(self, parameter_name: str) -> GetBalanceParameterModelMasterRequest:
        self.parameter_name = parameter_name
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
    ) -> Optional[GetBalanceParameterModelMasterRequest]:
        if data is None:
            return None
        return GetBalanceParameterModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_parameter_name(data.get('parameterName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "parameterName": self.parameter_name,
        }


class UpdateBalanceParameterModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    parameter_name: str = None
    description: str = None
    metadata: str = None
    total_value: int = None
    initial_value_strategy: str = None
    parameters: List[BalanceParameterValueModel] = None

    def with_namespace_name(self, namespace_name: str) -> UpdateBalanceParameterModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_parameter_name(self, parameter_name: str) -> UpdateBalanceParameterModelMasterRequest:
        self.parameter_name = parameter_name
        return self

    def with_description(self, description: str) -> UpdateBalanceParameterModelMasterRequest:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> UpdateBalanceParameterModelMasterRequest:
        self.metadata = metadata
        return self

    def with_total_value(self, total_value: int) -> UpdateBalanceParameterModelMasterRequest:
        self.total_value = total_value
        return self

    def with_initial_value_strategy(self, initial_value_strategy: str) -> UpdateBalanceParameterModelMasterRequest:
        self.initial_value_strategy = initial_value_strategy
        return self

    def with_parameters(self, parameters: List[BalanceParameterValueModel]) -> UpdateBalanceParameterModelMasterRequest:
        self.parameters = parameters
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
    ) -> Optional[UpdateBalanceParameterModelMasterRequest]:
        if data is None:
            return None
        return UpdateBalanceParameterModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_total_value(data.get('totalValue'))\
            .with_initial_value_strategy(data.get('initialValueStrategy'))\
            .with_parameters([
                BalanceParameterValueModel.from_dict(data.get('parameters')[i])
                for i in range(len(data.get('parameters')) if data.get('parameters') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "parameterName": self.parameter_name,
            "description": self.description,
            "metadata": self.metadata,
            "totalValue": self.total_value,
            "initialValueStrategy": self.initial_value_strategy,
            "parameters": [
                self.parameters[i].to_dict() if self.parameters[i] else None
                for i in range(len(self.parameters) if self.parameters else 0)
            ],
        }


class DeleteBalanceParameterModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    parameter_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteBalanceParameterModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_parameter_name(self, parameter_name: str) -> DeleteBalanceParameterModelMasterRequest:
        self.parameter_name = parameter_name
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
    ) -> Optional[DeleteBalanceParameterModelMasterRequest]:
        if data is None:
            return None
        return DeleteBalanceParameterModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_parameter_name(data.get('parameterName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "parameterName": self.parameter_name,
        }


class DescribeRarityParameterModelsRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DescribeRarityParameterModelsRequest:
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
    ) -> Optional[DescribeRarityParameterModelsRequest]:
        if data is None:
            return None
        return DescribeRarityParameterModelsRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class GetRarityParameterModelRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    parameter_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetRarityParameterModelRequest:
        self.namespace_name = namespace_name
        return self

    def with_parameter_name(self, parameter_name: str) -> GetRarityParameterModelRequest:
        self.parameter_name = parameter_name
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
    ) -> Optional[GetRarityParameterModelRequest]:
        if data is None:
            return None
        return GetRarityParameterModelRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_parameter_name(data.get('parameterName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "parameterName": self.parameter_name,
        }


class DescribeRarityParameterModelMastersRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeRarityParameterModelMastersRequest:
        self.namespace_name = namespace_name
        return self

    def with_page_token(self, page_token: str) -> DescribeRarityParameterModelMastersRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeRarityParameterModelMastersRequest:
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
    ) -> Optional[DescribeRarityParameterModelMastersRequest]:
        if data is None:
            return None
        return DescribeRarityParameterModelMastersRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class CreateRarityParameterModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    name: str = None
    description: str = None
    metadata: str = None
    maximum_parameter_count: int = None
    parameter_counts: List[RarityParameterCountModel] = None
    parameters: List[RarityParameterValueModel] = None

    def with_namespace_name(self, namespace_name: str) -> CreateRarityParameterModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_name(self, name: str) -> CreateRarityParameterModelMasterRequest:
        self.name = name
        return self

    def with_description(self, description: str) -> CreateRarityParameterModelMasterRequest:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> CreateRarityParameterModelMasterRequest:
        self.metadata = metadata
        return self

    def with_maximum_parameter_count(self, maximum_parameter_count: int) -> CreateRarityParameterModelMasterRequest:
        self.maximum_parameter_count = maximum_parameter_count
        return self

    def with_parameter_counts(self, parameter_counts: List[RarityParameterCountModel]) -> CreateRarityParameterModelMasterRequest:
        self.parameter_counts = parameter_counts
        return self

    def with_parameters(self, parameters: List[RarityParameterValueModel]) -> CreateRarityParameterModelMasterRequest:
        self.parameters = parameters
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
    ) -> Optional[CreateRarityParameterModelMasterRequest]:
        if data is None:
            return None
        return CreateRarityParameterModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_name(data.get('name'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_maximum_parameter_count(data.get('maximumParameterCount'))\
            .with_parameter_counts([
                RarityParameterCountModel.from_dict(data.get('parameterCounts')[i])
                for i in range(len(data.get('parameterCounts')) if data.get('parameterCounts') else 0)
            ])\
            .with_parameters([
                RarityParameterValueModel.from_dict(data.get('parameters')[i])
                for i in range(len(data.get('parameters')) if data.get('parameters') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "name": self.name,
            "description": self.description,
            "metadata": self.metadata,
            "maximumParameterCount": self.maximum_parameter_count,
            "parameterCounts": [
                self.parameter_counts[i].to_dict() if self.parameter_counts[i] else None
                for i in range(len(self.parameter_counts) if self.parameter_counts else 0)
            ],
            "parameters": [
                self.parameters[i].to_dict() if self.parameters[i] else None
                for i in range(len(self.parameters) if self.parameters else 0)
            ],
        }


class GetRarityParameterModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    parameter_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetRarityParameterModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_parameter_name(self, parameter_name: str) -> GetRarityParameterModelMasterRequest:
        self.parameter_name = parameter_name
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
    ) -> Optional[GetRarityParameterModelMasterRequest]:
        if data is None:
            return None
        return GetRarityParameterModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_parameter_name(data.get('parameterName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "parameterName": self.parameter_name,
        }


class UpdateRarityParameterModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    parameter_name: str = None
    description: str = None
    metadata: str = None
    maximum_parameter_count: int = None
    parameter_counts: List[RarityParameterCountModel] = None
    parameters: List[RarityParameterValueModel] = None

    def with_namespace_name(self, namespace_name: str) -> UpdateRarityParameterModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_parameter_name(self, parameter_name: str) -> UpdateRarityParameterModelMasterRequest:
        self.parameter_name = parameter_name
        return self

    def with_description(self, description: str) -> UpdateRarityParameterModelMasterRequest:
        self.description = description
        return self

    def with_metadata(self, metadata: str) -> UpdateRarityParameterModelMasterRequest:
        self.metadata = metadata
        return self

    def with_maximum_parameter_count(self, maximum_parameter_count: int) -> UpdateRarityParameterModelMasterRequest:
        self.maximum_parameter_count = maximum_parameter_count
        return self

    def with_parameter_counts(self, parameter_counts: List[RarityParameterCountModel]) -> UpdateRarityParameterModelMasterRequest:
        self.parameter_counts = parameter_counts
        return self

    def with_parameters(self, parameters: List[RarityParameterValueModel]) -> UpdateRarityParameterModelMasterRequest:
        self.parameters = parameters
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
    ) -> Optional[UpdateRarityParameterModelMasterRequest]:
        if data is None:
            return None
        return UpdateRarityParameterModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_description(data.get('description'))\
            .with_metadata(data.get('metadata'))\
            .with_maximum_parameter_count(data.get('maximumParameterCount'))\
            .with_parameter_counts([
                RarityParameterCountModel.from_dict(data.get('parameterCounts')[i])
                for i in range(len(data.get('parameterCounts')) if data.get('parameterCounts') else 0)
            ])\
            .with_parameters([
                RarityParameterValueModel.from_dict(data.get('parameters')[i])
                for i in range(len(data.get('parameters')) if data.get('parameters') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "parameterName": self.parameter_name,
            "description": self.description,
            "metadata": self.metadata,
            "maximumParameterCount": self.maximum_parameter_count,
            "parameterCounts": [
                self.parameter_counts[i].to_dict() if self.parameter_counts[i] else None
                for i in range(len(self.parameter_counts) if self.parameter_counts else 0)
            ],
            "parameters": [
                self.parameters[i].to_dict() if self.parameters[i] else None
                for i in range(len(self.parameters) if self.parameters else 0)
            ],
        }


class DeleteRarityParameterModelMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    parameter_name: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteRarityParameterModelMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_parameter_name(self, parameter_name: str) -> DeleteRarityParameterModelMasterRequest:
        self.parameter_name = parameter_name
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
    ) -> Optional[DeleteRarityParameterModelMasterRequest]:
        if data is None:
            return None
        return DeleteRarityParameterModelMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_parameter_name(data.get('parameterName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "parameterName": self.parameter_name,
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


class GetCurrentParameterMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None

    def with_namespace_name(self, namespace_name: str) -> GetCurrentParameterMasterRequest:
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
    ) -> Optional[GetCurrentParameterMasterRequest]:
        if data is None:
            return None
        return GetCurrentParameterMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
        }


class UpdateCurrentParameterMasterRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    settings: str = None

    def with_namespace_name(self, namespace_name: str) -> UpdateCurrentParameterMasterRequest:
        self.namespace_name = namespace_name
        return self

    def with_settings(self, settings: str) -> UpdateCurrentParameterMasterRequest:
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
    ) -> Optional[UpdateCurrentParameterMasterRequest]:
        if data is None:
            return None
        return UpdateCurrentParameterMasterRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_settings(data.get('settings'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "settings": self.settings,
        }


class UpdateCurrentParameterMasterFromGitHubRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    checkout_setting: GitHubCheckoutSetting = None

    def with_namespace_name(self, namespace_name: str) -> UpdateCurrentParameterMasterFromGitHubRequest:
        self.namespace_name = namespace_name
        return self

    def with_checkout_setting(self, checkout_setting: GitHubCheckoutSetting) -> UpdateCurrentParameterMasterFromGitHubRequest:
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
    ) -> Optional[UpdateCurrentParameterMasterFromGitHubRequest]:
        if data is None:
            return None
        return UpdateCurrentParameterMasterFromGitHubRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_checkout_setting(GitHubCheckoutSetting.from_dict(data.get('checkoutSetting')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "checkoutSetting": self.checkout_setting.to_dict() if self.checkout_setting else None,
        }


class DescribeBalanceParameterStatusesRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    parameter_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeBalanceParameterStatusesRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> DescribeBalanceParameterStatusesRequest:
        self.access_token = access_token
        return self

    def with_parameter_name(self, parameter_name: str) -> DescribeBalanceParameterStatusesRequest:
        self.parameter_name = parameter_name
        return self

    def with_page_token(self, page_token: str) -> DescribeBalanceParameterStatusesRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeBalanceParameterStatusesRequest:
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
    ) -> Optional[DescribeBalanceParameterStatusesRequest]:
        if data is None:
            return None
        return DescribeBalanceParameterStatusesRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "parameterName": self.parameter_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class DescribeBalanceParameterStatusesByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeBalanceParameterStatusesByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> DescribeBalanceParameterStatusesByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> DescribeBalanceParameterStatusesByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_page_token(self, page_token: str) -> DescribeBalanceParameterStatusesByUserIdRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeBalanceParameterStatusesByUserIdRequest:
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
    ) -> Optional[DescribeBalanceParameterStatusesByUserIdRequest]:
        if data is None:
            return None
        return DescribeBalanceParameterStatusesByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class GetBalanceParameterStatusRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    parameter_name: str = None
    property_id: str = None

    def with_namespace_name(self, namespace_name: str) -> GetBalanceParameterStatusRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> GetBalanceParameterStatusRequest:
        self.access_token = access_token
        return self

    def with_parameter_name(self, parameter_name: str) -> GetBalanceParameterStatusRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> GetBalanceParameterStatusRequest:
        self.property_id = property_id
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
    ) -> Optional[GetBalanceParameterStatusRequest]:
        if data is None:
            return None
        return GetBalanceParameterStatusRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
        }


class GetBalanceParameterStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    property_id: str = None

    def with_namespace_name(self, namespace_name: str) -> GetBalanceParameterStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> GetBalanceParameterStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> GetBalanceParameterStatusByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> GetBalanceParameterStatusByUserIdRequest:
        self.property_id = property_id
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
    ) -> Optional[GetBalanceParameterStatusByUserIdRequest]:
        if data is None:
            return None
        return GetBalanceParameterStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
        }


class DeleteBalanceParameterStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    property_id: str = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteBalanceParameterStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> DeleteBalanceParameterStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> DeleteBalanceParameterStatusByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> DeleteBalanceParameterStatusByUserIdRequest:
        self.property_id = property_id
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> DeleteBalanceParameterStatusByUserIdRequest:
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
    ) -> Optional[DeleteBalanceParameterStatusByUserIdRequest]:
        if data is None:
            return None
        return DeleteBalanceParameterStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
        }


class ReDrawBalanceParameterStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    property_id: str = None
    fixed_parameter_names: List[str] = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> ReDrawBalanceParameterStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> ReDrawBalanceParameterStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> ReDrawBalanceParameterStatusByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> ReDrawBalanceParameterStatusByUserIdRequest:
        self.property_id = property_id
        return self

    def with_fixed_parameter_names(self, fixed_parameter_names: List[str]) -> ReDrawBalanceParameterStatusByUserIdRequest:
        self.fixed_parameter_names = fixed_parameter_names
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> ReDrawBalanceParameterStatusByUserIdRequest:
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
    ) -> Optional[ReDrawBalanceParameterStatusByUserIdRequest]:
        if data is None:
            return None
        return ReDrawBalanceParameterStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))\
            .with_fixed_parameter_names([
                data.get('fixedParameterNames')[i]
                for i in range(len(data.get('fixedParameterNames')) if data.get('fixedParameterNames') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
            "fixedParameterNames": [
                self.fixed_parameter_names[i]
                for i in range(len(self.fixed_parameter_names) if self.fixed_parameter_names else 0)
            ],
        }


class ReDrawBalanceParameterStatusByStampSheetRequest(core.Gs2Request):

    context_stack: str = None
    stamp_sheet: str = None
    key_id: str = None

    def with_stamp_sheet(self, stamp_sheet: str) -> ReDrawBalanceParameterStatusByStampSheetRequest:
        self.stamp_sheet = stamp_sheet
        return self

    def with_key_id(self, key_id: str) -> ReDrawBalanceParameterStatusByStampSheetRequest:
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
    ) -> Optional[ReDrawBalanceParameterStatusByStampSheetRequest]:
        if data is None:
            return None
        return ReDrawBalanceParameterStatusByStampSheetRequest()\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampSheet": self.stamp_sheet,
            "keyId": self.key_id,
        }


class SetBalanceParameterStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    property_id: str = None
    parameter_values: List[BalanceParameterValue] = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> SetBalanceParameterStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> SetBalanceParameterStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> SetBalanceParameterStatusByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> SetBalanceParameterStatusByUserIdRequest:
        self.property_id = property_id
        return self

    def with_parameter_values(self, parameter_values: List[BalanceParameterValue]) -> SetBalanceParameterStatusByUserIdRequest:
        self.parameter_values = parameter_values
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> SetBalanceParameterStatusByUserIdRequest:
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
    ) -> Optional[SetBalanceParameterStatusByUserIdRequest]:
        if data is None:
            return None
        return SetBalanceParameterStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))\
            .with_parameter_values([
                BalanceParameterValue.from_dict(data.get('parameterValues')[i])
                for i in range(len(data.get('parameterValues')) if data.get('parameterValues') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
            "parameterValues": [
                self.parameter_values[i].to_dict() if self.parameter_values[i] else None
                for i in range(len(self.parameter_values) if self.parameter_values else 0)
            ],
        }


class SetBalanceParameterStatusByStampSheetRequest(core.Gs2Request):

    context_stack: str = None
    stamp_sheet: str = None
    key_id: str = None

    def with_stamp_sheet(self, stamp_sheet: str) -> SetBalanceParameterStatusByStampSheetRequest:
        self.stamp_sheet = stamp_sheet
        return self

    def with_key_id(self, key_id: str) -> SetBalanceParameterStatusByStampSheetRequest:
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
    ) -> Optional[SetBalanceParameterStatusByStampSheetRequest]:
        if data is None:
            return None
        return SetBalanceParameterStatusByStampSheetRequest()\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampSheet": self.stamp_sheet,
            "keyId": self.key_id,
        }


class DescribeRarityParameterStatusesRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    parameter_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeRarityParameterStatusesRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> DescribeRarityParameterStatusesRequest:
        self.access_token = access_token
        return self

    def with_parameter_name(self, parameter_name: str) -> DescribeRarityParameterStatusesRequest:
        self.parameter_name = parameter_name
        return self

    def with_page_token(self, page_token: str) -> DescribeRarityParameterStatusesRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeRarityParameterStatusesRequest:
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
    ) -> Optional[DescribeRarityParameterStatusesRequest]:
        if data is None:
            return None
        return DescribeRarityParameterStatusesRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "parameterName": self.parameter_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class DescribeRarityParameterStatusesByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    page_token: str = None
    limit: int = None

    def with_namespace_name(self, namespace_name: str) -> DescribeRarityParameterStatusesByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> DescribeRarityParameterStatusesByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> DescribeRarityParameterStatusesByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_page_token(self, page_token: str) -> DescribeRarityParameterStatusesByUserIdRequest:
        self.page_token = page_token
        return self

    def with_limit(self, limit: int) -> DescribeRarityParameterStatusesByUserIdRequest:
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
    ) -> Optional[DescribeRarityParameterStatusesByUserIdRequest]:
        if data is None:
            return None
        return DescribeRarityParameterStatusesByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_page_token(data.get('pageToken'))\
            .with_limit(data.get('limit'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "pageToken": self.page_token,
            "limit": self.limit,
        }


class GetRarityParameterStatusRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    access_token: str = None
    parameter_name: str = None
    property_id: str = None

    def with_namespace_name(self, namespace_name: str) -> GetRarityParameterStatusRequest:
        self.namespace_name = namespace_name
        return self

    def with_access_token(self, access_token: str) -> GetRarityParameterStatusRequest:
        self.access_token = access_token
        return self

    def with_parameter_name(self, parameter_name: str) -> GetRarityParameterStatusRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> GetRarityParameterStatusRequest:
        self.property_id = property_id
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
    ) -> Optional[GetRarityParameterStatusRequest]:
        if data is None:
            return None
        return GetRarityParameterStatusRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_access_token(data.get('accessToken'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "accessToken": self.access_token,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
        }


class GetRarityParameterStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    property_id: str = None

    def with_namespace_name(self, namespace_name: str) -> GetRarityParameterStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> GetRarityParameterStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> GetRarityParameterStatusByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> GetRarityParameterStatusByUserIdRequest:
        self.property_id = property_id
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
    ) -> Optional[GetRarityParameterStatusByUserIdRequest]:
        if data is None:
            return None
        return GetRarityParameterStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
        }


class DeleteRarityParameterStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    property_id: str = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> DeleteRarityParameterStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> DeleteRarityParameterStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> DeleteRarityParameterStatusByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> DeleteRarityParameterStatusByUserIdRequest:
        self.property_id = property_id
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> DeleteRarityParameterStatusByUserIdRequest:
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
    ) -> Optional[DeleteRarityParameterStatusByUserIdRequest]:
        if data is None:
            return None
        return DeleteRarityParameterStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
        }


class ReDrawRarityParameterStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    property_id: str = None
    fixed_parameter_names: List[str] = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> ReDrawRarityParameterStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> ReDrawRarityParameterStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> ReDrawRarityParameterStatusByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> ReDrawRarityParameterStatusByUserIdRequest:
        self.property_id = property_id
        return self

    def with_fixed_parameter_names(self, fixed_parameter_names: List[str]) -> ReDrawRarityParameterStatusByUserIdRequest:
        self.fixed_parameter_names = fixed_parameter_names
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> ReDrawRarityParameterStatusByUserIdRequest:
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
    ) -> Optional[ReDrawRarityParameterStatusByUserIdRequest]:
        if data is None:
            return None
        return ReDrawRarityParameterStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))\
            .with_fixed_parameter_names([
                data.get('fixedParameterNames')[i]
                for i in range(len(data.get('fixedParameterNames')) if data.get('fixedParameterNames') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
            "fixedParameterNames": [
                self.fixed_parameter_names[i]
                for i in range(len(self.fixed_parameter_names) if self.fixed_parameter_names else 0)
            ],
        }


class ReDrawRarityParameterStatusByStampSheetRequest(core.Gs2Request):

    context_stack: str = None
    stamp_sheet: str = None
    key_id: str = None

    def with_stamp_sheet(self, stamp_sheet: str) -> ReDrawRarityParameterStatusByStampSheetRequest:
        self.stamp_sheet = stamp_sheet
        return self

    def with_key_id(self, key_id: str) -> ReDrawRarityParameterStatusByStampSheetRequest:
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
    ) -> Optional[ReDrawRarityParameterStatusByStampSheetRequest]:
        if data is None:
            return None
        return ReDrawRarityParameterStatusByStampSheetRequest()\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampSheet": self.stamp_sheet,
            "keyId": self.key_id,
        }


class AddRarityParameterStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    property_id: str = None
    count: int = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> AddRarityParameterStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> AddRarityParameterStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> AddRarityParameterStatusByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> AddRarityParameterStatusByUserIdRequest:
        self.property_id = property_id
        return self

    def with_count(self, count: int) -> AddRarityParameterStatusByUserIdRequest:
        self.count = count
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> AddRarityParameterStatusByUserIdRequest:
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
    ) -> Optional[AddRarityParameterStatusByUserIdRequest]:
        if data is None:
            return None
        return AddRarityParameterStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))\
            .with_count(data.get('count'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
            "count": self.count,
        }


class AddRarityParameterStatusByStampSheetRequest(core.Gs2Request):

    context_stack: str = None
    stamp_sheet: str = None
    key_id: str = None

    def with_stamp_sheet(self, stamp_sheet: str) -> AddRarityParameterStatusByStampSheetRequest:
        self.stamp_sheet = stamp_sheet
        return self

    def with_key_id(self, key_id: str) -> AddRarityParameterStatusByStampSheetRequest:
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
    ) -> Optional[AddRarityParameterStatusByStampSheetRequest]:
        if data is None:
            return None
        return AddRarityParameterStatusByStampSheetRequest()\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampSheet": self.stamp_sheet,
            "keyId": self.key_id,
        }


class VerifyRarityParameterStatusRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    parameter_name: str = None
    access_token: str = None
    property_id: str = None
    verify_type: str = None
    parameter_value_name: str = None
    parameter_count: int = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> VerifyRarityParameterStatusRequest:
        self.namespace_name = namespace_name
        return self

    def with_parameter_name(self, parameter_name: str) -> VerifyRarityParameterStatusRequest:
        self.parameter_name = parameter_name
        return self

    def with_access_token(self, access_token: str) -> VerifyRarityParameterStatusRequest:
        self.access_token = access_token
        return self

    def with_property_id(self, property_id: str) -> VerifyRarityParameterStatusRequest:
        self.property_id = property_id
        return self

    def with_verify_type(self, verify_type: str) -> VerifyRarityParameterStatusRequest:
        self.verify_type = verify_type
        return self

    def with_parameter_value_name(self, parameter_value_name: str) -> VerifyRarityParameterStatusRequest:
        self.parameter_value_name = parameter_value_name
        return self

    def with_parameter_count(self, parameter_count: int) -> VerifyRarityParameterStatusRequest:
        self.parameter_count = parameter_count
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> VerifyRarityParameterStatusRequest:
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
    ) -> Optional[VerifyRarityParameterStatusRequest]:
        if data is None:
            return None
        return VerifyRarityParameterStatusRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_access_token(data.get('accessToken'))\
            .with_property_id(data.get('propertyId'))\
            .with_verify_type(data.get('verifyType'))\
            .with_parameter_value_name(data.get('parameterValueName'))\
            .with_parameter_count(data.get('parameterCount'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "parameterName": self.parameter_name,
            "accessToken": self.access_token,
            "propertyId": self.property_id,
            "verifyType": self.verify_type,
            "parameterValueName": self.parameter_value_name,
            "parameterCount": self.parameter_count,
        }


class VerifyRarityParameterStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    parameter_name: str = None
    user_id: str = None
    property_id: str = None
    verify_type: str = None
    parameter_value_name: str = None
    parameter_count: int = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> VerifyRarityParameterStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_parameter_name(self, parameter_name: str) -> VerifyRarityParameterStatusByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_user_id(self, user_id: str) -> VerifyRarityParameterStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_property_id(self, property_id: str) -> VerifyRarityParameterStatusByUserIdRequest:
        self.property_id = property_id
        return self

    def with_verify_type(self, verify_type: str) -> VerifyRarityParameterStatusByUserIdRequest:
        self.verify_type = verify_type
        return self

    def with_parameter_value_name(self, parameter_value_name: str) -> VerifyRarityParameterStatusByUserIdRequest:
        self.parameter_value_name = parameter_value_name
        return self

    def with_parameter_count(self, parameter_count: int) -> VerifyRarityParameterStatusByUserIdRequest:
        self.parameter_count = parameter_count
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> VerifyRarityParameterStatusByUserIdRequest:
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
    ) -> Optional[VerifyRarityParameterStatusByUserIdRequest]:
        if data is None:
            return None
        return VerifyRarityParameterStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_user_id(data.get('userId'))\
            .with_property_id(data.get('propertyId'))\
            .with_verify_type(data.get('verifyType'))\
            .with_parameter_value_name(data.get('parameterValueName'))\
            .with_parameter_count(data.get('parameterCount'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "parameterName": self.parameter_name,
            "userId": self.user_id,
            "propertyId": self.property_id,
            "verifyType": self.verify_type,
            "parameterValueName": self.parameter_value_name,
            "parameterCount": self.parameter_count,
        }


class VerifyRarityParameterStatusByStampTaskRequest(core.Gs2Request):

    context_stack: str = None
    stamp_task: str = None
    key_id: str = None

    def with_stamp_task(self, stamp_task: str) -> VerifyRarityParameterStatusByStampTaskRequest:
        self.stamp_task = stamp_task
        return self

    def with_key_id(self, key_id: str) -> VerifyRarityParameterStatusByStampTaskRequest:
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
    ) -> Optional[VerifyRarityParameterStatusByStampTaskRequest]:
        if data is None:
            return None
        return VerifyRarityParameterStatusByStampTaskRequest()\
            .with_stamp_task(data.get('stampTask'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampTask": self.stamp_task,
            "keyId": self.key_id,
        }


class SetRarityParameterStatusByUserIdRequest(core.Gs2Request):

    context_stack: str = None
    namespace_name: str = None
    user_id: str = None
    parameter_name: str = None
    property_id: str = None
    parameter_values: List[RarityParameterValue] = None
    duplication_avoider: str = None

    def with_namespace_name(self, namespace_name: str) -> SetRarityParameterStatusByUserIdRequest:
        self.namespace_name = namespace_name
        return self

    def with_user_id(self, user_id: str) -> SetRarityParameterStatusByUserIdRequest:
        self.user_id = user_id
        return self

    def with_parameter_name(self, parameter_name: str) -> SetRarityParameterStatusByUserIdRequest:
        self.parameter_name = parameter_name
        return self

    def with_property_id(self, property_id: str) -> SetRarityParameterStatusByUserIdRequest:
        self.property_id = property_id
        return self

    def with_parameter_values(self, parameter_values: List[RarityParameterValue]) -> SetRarityParameterStatusByUserIdRequest:
        self.parameter_values = parameter_values
        return self

    def with_duplication_avoider(self, duplication_avoider: str) -> SetRarityParameterStatusByUserIdRequest:
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
    ) -> Optional[SetRarityParameterStatusByUserIdRequest]:
        if data is None:
            return None
        return SetRarityParameterStatusByUserIdRequest()\
            .with_namespace_name(data.get('namespaceName'))\
            .with_user_id(data.get('userId'))\
            .with_parameter_name(data.get('parameterName'))\
            .with_property_id(data.get('propertyId'))\
            .with_parameter_values([
                RarityParameterValue.from_dict(data.get('parameterValues')[i])
                for i in range(len(data.get('parameterValues')) if data.get('parameterValues') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceName": self.namespace_name,
            "userId": self.user_id,
            "parameterName": self.parameter_name,
            "propertyId": self.property_id,
            "parameterValues": [
                self.parameter_values[i].to_dict() if self.parameter_values[i] else None
                for i in range(len(self.parameter_values) if self.parameter_values else 0)
            ],
        }


class SetRarityParameterStatusByStampSheetRequest(core.Gs2Request):

    context_stack: str = None
    stamp_sheet: str = None
    key_id: str = None

    def with_stamp_sheet(self, stamp_sheet: str) -> SetRarityParameterStatusByStampSheetRequest:
        self.stamp_sheet = stamp_sheet
        return self

    def with_key_id(self, key_id: str) -> SetRarityParameterStatusByStampSheetRequest:
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
    ) -> Optional[SetRarityParameterStatusByStampSheetRequest]:
        if data is None:
            return None
        return SetRarityParameterStatusByStampSheetRequest()\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_key_id(data.get('keyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stampSheet": self.stamp_sheet,
            "keyId": self.key_id,
        }