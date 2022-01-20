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


class DescribeNamespacesResult(core.Gs2Result):
    items: List[Namespace] = None
    next_page_token: str = None

    def with_items(self, items: List[Namespace]) -> DescribeNamespacesResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeNamespacesResult:
        self.next_page_token = next_page_token
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
    ) -> Optional[DescribeNamespacesResult]:
        if data is None:
            return None
        return DescribeNamespacesResult()\
            .with_items([
                Namespace.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class CreateNamespaceResult(core.Gs2Result):
    item: Namespace = None

    def with_item(self, item: Namespace) -> CreateNamespaceResult:
        self.item = item
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
    ) -> Optional[CreateNamespaceResult]:
        if data is None:
            return None
        return CreateNamespaceResult()\
            .with_item(Namespace.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class GetNamespaceStatusResult(core.Gs2Result):
    status: str = None

    def with_status(self, status: str) -> GetNamespaceStatusResult:
        self.status = status
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
    ) -> Optional[GetNamespaceStatusResult]:
        if data is None:
            return None
        return GetNamespaceStatusResult()\
            .with_status(data.get('status'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status,
        }


class GetNamespaceResult(core.Gs2Result):
    item: Namespace = None

    def with_item(self, item: Namespace) -> GetNamespaceResult:
        self.item = item
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
    ) -> Optional[GetNamespaceResult]:
        if data is None:
            return None
        return GetNamespaceResult()\
            .with_item(Namespace.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class UpdateNamespaceResult(core.Gs2Result):
    item: Namespace = None

    def with_item(self, item: Namespace) -> UpdateNamespaceResult:
        self.item = item
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
    ) -> Optional[UpdateNamespaceResult]:
        if data is None:
            return None
        return UpdateNamespaceResult()\
            .with_item(Namespace.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DeleteNamespaceResult(core.Gs2Result):
    item: Namespace = None

    def with_item(self, item: Namespace) -> DeleteNamespaceResult:
        self.item = item
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
    ) -> Optional[DeleteNamespaceResult]:
        if data is None:
            return None
        return DeleteNamespaceResult()\
            .with_item(Namespace.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DescribeFormModelMastersResult(core.Gs2Result):
    items: List[FormModelMaster] = None
    next_page_token: str = None

    def with_items(self, items: List[FormModelMaster]) -> DescribeFormModelMastersResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeFormModelMastersResult:
        self.next_page_token = next_page_token
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
    ) -> Optional[DescribeFormModelMastersResult]:
        if data is None:
            return None
        return DescribeFormModelMastersResult()\
            .with_items([
                FormModelMaster.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class CreateFormModelMasterResult(core.Gs2Result):
    item: FormModelMaster = None

    def with_item(self, item: FormModelMaster) -> CreateFormModelMasterResult:
        self.item = item
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
    ) -> Optional[CreateFormModelMasterResult]:
        if data is None:
            return None
        return CreateFormModelMasterResult()\
            .with_item(FormModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class GetFormModelMasterResult(core.Gs2Result):
    item: FormModelMaster = None

    def with_item(self, item: FormModelMaster) -> GetFormModelMasterResult:
        self.item = item
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
    ) -> Optional[GetFormModelMasterResult]:
        if data is None:
            return None
        return GetFormModelMasterResult()\
            .with_item(FormModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class UpdateFormModelMasterResult(core.Gs2Result):
    item: FormModelMaster = None

    def with_item(self, item: FormModelMaster) -> UpdateFormModelMasterResult:
        self.item = item
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
    ) -> Optional[UpdateFormModelMasterResult]:
        if data is None:
            return None
        return UpdateFormModelMasterResult()\
            .with_item(FormModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DeleteFormModelMasterResult(core.Gs2Result):
    item: FormModelMaster = None

    def with_item(self, item: FormModelMaster) -> DeleteFormModelMasterResult:
        self.item = item
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
    ) -> Optional[DeleteFormModelMasterResult]:
        if data is None:
            return None
        return DeleteFormModelMasterResult()\
            .with_item(FormModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DescribeMoldModelsResult(core.Gs2Result):
    items: List[MoldModel] = None

    def with_items(self, items: List[MoldModel]) -> DescribeMoldModelsResult:
        self.items = items
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
    ) -> Optional[DescribeMoldModelsResult]:
        if data is None:
            return None
        return DescribeMoldModelsResult()\
            .with_items([
                MoldModel.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
        }


class GetMoldModelResult(core.Gs2Result):
    item: MoldModel = None

    def with_item(self, item: MoldModel) -> GetMoldModelResult:
        self.item = item
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
    ) -> Optional[GetMoldModelResult]:
        if data is None:
            return None
        return GetMoldModelResult()\
            .with_item(MoldModel.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DescribeMoldModelMastersResult(core.Gs2Result):
    items: List[MoldModelMaster] = None
    next_page_token: str = None

    def with_items(self, items: List[MoldModelMaster]) -> DescribeMoldModelMastersResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeMoldModelMastersResult:
        self.next_page_token = next_page_token
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
    ) -> Optional[DescribeMoldModelMastersResult]:
        if data is None:
            return None
        return DescribeMoldModelMastersResult()\
            .with_items([
                MoldModelMaster.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class CreateMoldModelMasterResult(core.Gs2Result):
    item: MoldModelMaster = None

    def with_item(self, item: MoldModelMaster) -> CreateMoldModelMasterResult:
        self.item = item
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
    ) -> Optional[CreateMoldModelMasterResult]:
        if data is None:
            return None
        return CreateMoldModelMasterResult()\
            .with_item(MoldModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class GetMoldModelMasterResult(core.Gs2Result):
    item: MoldModelMaster = None

    def with_item(self, item: MoldModelMaster) -> GetMoldModelMasterResult:
        self.item = item
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
    ) -> Optional[GetMoldModelMasterResult]:
        if data is None:
            return None
        return GetMoldModelMasterResult()\
            .with_item(MoldModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class UpdateMoldModelMasterResult(core.Gs2Result):
    item: MoldModelMaster = None

    def with_item(self, item: MoldModelMaster) -> UpdateMoldModelMasterResult:
        self.item = item
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
    ) -> Optional[UpdateMoldModelMasterResult]:
        if data is None:
            return None
        return UpdateMoldModelMasterResult()\
            .with_item(MoldModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DeleteMoldModelMasterResult(core.Gs2Result):
    item: MoldModelMaster = None

    def with_item(self, item: MoldModelMaster) -> DeleteMoldModelMasterResult:
        self.item = item
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
    ) -> Optional[DeleteMoldModelMasterResult]:
        if data is None:
            return None
        return DeleteMoldModelMasterResult()\
            .with_item(MoldModelMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class ExportMasterResult(core.Gs2Result):
    item: CurrentFormMaster = None

    def with_item(self, item: CurrentFormMaster) -> ExportMasterResult:
        self.item = item
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
    ) -> Optional[ExportMasterResult]:
        if data is None:
            return None
        return ExportMasterResult()\
            .with_item(CurrentFormMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class GetCurrentFormMasterResult(core.Gs2Result):
    item: CurrentFormMaster = None

    def with_item(self, item: CurrentFormMaster) -> GetCurrentFormMasterResult:
        self.item = item
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
    ) -> Optional[GetCurrentFormMasterResult]:
        if data is None:
            return None
        return GetCurrentFormMasterResult()\
            .with_item(CurrentFormMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class UpdateCurrentFormMasterResult(core.Gs2Result):
    item: CurrentFormMaster = None

    def with_item(self, item: CurrentFormMaster) -> UpdateCurrentFormMasterResult:
        self.item = item
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
    ) -> Optional[UpdateCurrentFormMasterResult]:
        if data is None:
            return None
        return UpdateCurrentFormMasterResult()\
            .with_item(CurrentFormMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class UpdateCurrentFormMasterFromGitHubResult(core.Gs2Result):
    item: CurrentFormMaster = None

    def with_item(self, item: CurrentFormMaster) -> UpdateCurrentFormMasterFromGitHubResult:
        self.item = item
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
    ) -> Optional[UpdateCurrentFormMasterFromGitHubResult]:
        if data is None:
            return None
        return UpdateCurrentFormMasterFromGitHubResult()\
            .with_item(CurrentFormMaster.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DescribeMoldsResult(core.Gs2Result):
    items: List[Mold] = None
    next_page_token: str = None

    def with_items(self, items: List[Mold]) -> DescribeMoldsResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeMoldsResult:
        self.next_page_token = next_page_token
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
    ) -> Optional[DescribeMoldsResult]:
        if data is None:
            return None
        return DescribeMoldsResult()\
            .with_items([
                Mold.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class DescribeMoldsByUserIdResult(core.Gs2Result):
    items: List[Mold] = None
    next_page_token: str = None

    def with_items(self, items: List[Mold]) -> DescribeMoldsByUserIdResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeMoldsByUserIdResult:
        self.next_page_token = next_page_token
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
    ) -> Optional[DescribeMoldsByUserIdResult]:
        if data is None:
            return None
        return DescribeMoldsByUserIdResult()\
            .with_items([
                Mold.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class GetMoldResult(core.Gs2Result):
    item: Mold = None
    mold_model: MoldModel = None

    def with_item(self, item: Mold) -> GetMoldResult:
        self.item = item
        return self

    def with_mold_model(self, mold_model: MoldModel) -> GetMoldResult:
        self.mold_model = mold_model
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
    ) -> Optional[GetMoldResult]:
        if data is None:
            return None
        return GetMoldResult()\
            .with_item(Mold.from_dict(data.get('item')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
        }


class GetMoldByUserIdResult(core.Gs2Result):
    item: Mold = None
    mold_model: MoldModel = None

    def with_item(self, item: Mold) -> GetMoldByUserIdResult:
        self.item = item
        return self

    def with_mold_model(self, mold_model: MoldModel) -> GetMoldByUserIdResult:
        self.mold_model = mold_model
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
    ) -> Optional[GetMoldByUserIdResult]:
        if data is None:
            return None
        return GetMoldByUserIdResult()\
            .with_item(Mold.from_dict(data.get('item')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
        }


class SetMoldCapacityByUserIdResult(core.Gs2Result):
    item: Mold = None
    mold_model: MoldModel = None

    def with_item(self, item: Mold) -> SetMoldCapacityByUserIdResult:
        self.item = item
        return self

    def with_mold_model(self, mold_model: MoldModel) -> SetMoldCapacityByUserIdResult:
        self.mold_model = mold_model
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
    ) -> Optional[SetMoldCapacityByUserIdResult]:
        if data is None:
            return None
        return SetMoldCapacityByUserIdResult()\
            .with_item(Mold.from_dict(data.get('item')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
        }


class AddMoldCapacityByUserIdResult(core.Gs2Result):
    item: Mold = None
    mold_model: MoldModel = None

    def with_item(self, item: Mold) -> AddMoldCapacityByUserIdResult:
        self.item = item
        return self

    def with_mold_model(self, mold_model: MoldModel) -> AddMoldCapacityByUserIdResult:
        self.mold_model = mold_model
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
    ) -> Optional[AddMoldCapacityByUserIdResult]:
        if data is None:
            return None
        return AddMoldCapacityByUserIdResult()\
            .with_item(Mold.from_dict(data.get('item')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
        }


class DeleteMoldResult(core.Gs2Result):
    item: Mold = None

    def with_item(self, item: Mold) -> DeleteMoldResult:
        self.item = item
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
    ) -> Optional[DeleteMoldResult]:
        if data is None:
            return None
        return DeleteMoldResult()\
            .with_item(Mold.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class DeleteMoldByUserIdResult(core.Gs2Result):
    item: Mold = None

    def with_item(self, item: Mold) -> DeleteMoldByUserIdResult:
        self.item = item
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
    ) -> Optional[DeleteMoldByUserIdResult]:
        if data is None:
            return None
        return DeleteMoldByUserIdResult()\
            .with_item(Mold.from_dict(data.get('item')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
        }


class AddCapacityByStampSheetResult(core.Gs2Result):
    item: Mold = None
    mold_model: MoldModel = None

    def with_item(self, item: Mold) -> AddCapacityByStampSheetResult:
        self.item = item
        return self

    def with_mold_model(self, mold_model: MoldModel) -> AddCapacityByStampSheetResult:
        self.mold_model = mold_model
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
    ) -> Optional[AddCapacityByStampSheetResult]:
        if data is None:
            return None
        return AddCapacityByStampSheetResult()\
            .with_item(Mold.from_dict(data.get('item')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
        }


class SetCapacityByStampSheetResult(core.Gs2Result):
    item: Mold = None
    mold_model: MoldModel = None

    def with_item(self, item: Mold) -> SetCapacityByStampSheetResult:
        self.item = item
        return self

    def with_mold_model(self, mold_model: MoldModel) -> SetCapacityByStampSheetResult:
        self.mold_model = mold_model
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
    ) -> Optional[SetCapacityByStampSheetResult]:
        if data is None:
            return None
        return SetCapacityByStampSheetResult()\
            .with_item(Mold.from_dict(data.get('item')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
        }


class DescribeFormsResult(core.Gs2Result):
    items: List[Form] = None
    next_page_token: str = None

    def with_items(self, items: List[Form]) -> DescribeFormsResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeFormsResult:
        self.next_page_token = next_page_token
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
    ) -> Optional[DescribeFormsResult]:
        if data is None:
            return None
        return DescribeFormsResult()\
            .with_items([
                Form.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class DescribeFormsByUserIdResult(core.Gs2Result):
    items: List[Form] = None
    next_page_token: str = None

    def with_items(self, items: List[Form]) -> DescribeFormsByUserIdResult:
        self.items = items
        return self

    def with_next_page_token(self, next_page_token: str) -> DescribeFormsByUserIdResult:
        self.next_page_token = next_page_token
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
    ) -> Optional[DescribeFormsByUserIdResult]:
        if data is None:
            return None
        return DescribeFormsByUserIdResult()\
            .with_items([
                Form.from_dict(data.get('items')[i])
                for i in range(len(data.get('items')) if data.get('items') else 0)
            ])\
            .with_next_page_token(data.get('nextPageToken'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [
                self.items[i].to_dict() if self.items[i] else None
                for i in range(len(self.items) if self.items else 0)
            ],
            "nextPageToken": self.next_page_token,
        }


class GetFormResult(core.Gs2Result):
    item: Form = None
    mold: Mold = None
    mold_model: MoldModel = None
    form_model: FormModel = None

    def with_item(self, item: Form) -> GetFormResult:
        self.item = item
        return self

    def with_mold(self, mold: Mold) -> GetFormResult:
        self.mold = mold
        return self

    def with_mold_model(self, mold_model: MoldModel) -> GetFormResult:
        self.mold_model = mold_model
        return self

    def with_form_model(self, form_model: FormModel) -> GetFormResult:
        self.form_model = form_model
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
    ) -> Optional[GetFormResult]:
        if data is None:
            return None
        return GetFormResult()\
            .with_item(Form.from_dict(data.get('item')))\
            .with_mold(Mold.from_dict(data.get('mold')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))\
            .with_form_model(FormModel.from_dict(data.get('formModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "mold": self.mold.to_dict() if self.mold else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
            "formModel": self.form_model.to_dict() if self.form_model else None,
        }


class GetFormByUserIdResult(core.Gs2Result):
    item: Form = None
    mold: Mold = None
    mold_model: MoldModel = None
    form_model: FormModel = None

    def with_item(self, item: Form) -> GetFormByUserIdResult:
        self.item = item
        return self

    def with_mold(self, mold: Mold) -> GetFormByUserIdResult:
        self.mold = mold
        return self

    def with_mold_model(self, mold_model: MoldModel) -> GetFormByUserIdResult:
        self.mold_model = mold_model
        return self

    def with_form_model(self, form_model: FormModel) -> GetFormByUserIdResult:
        self.form_model = form_model
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
    ) -> Optional[GetFormByUserIdResult]:
        if data is None:
            return None
        return GetFormByUserIdResult()\
            .with_item(Form.from_dict(data.get('item')))\
            .with_mold(Mold.from_dict(data.get('mold')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))\
            .with_form_model(FormModel.from_dict(data.get('formModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "mold": self.mold.to_dict() if self.mold else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
            "formModel": self.form_model.to_dict() if self.form_model else None,
        }


class GetFormWithSignatureResult(core.Gs2Result):
    item: Form = None
    body: str = None
    signature: str = None
    mold: Mold = None
    mold_model: MoldModel = None
    form_model: FormModel = None

    def with_item(self, item: Form) -> GetFormWithSignatureResult:
        self.item = item
        return self

    def with_body(self, body: str) -> GetFormWithSignatureResult:
        self.body = body
        return self

    def with_signature(self, signature: str) -> GetFormWithSignatureResult:
        self.signature = signature
        return self

    def with_mold(self, mold: Mold) -> GetFormWithSignatureResult:
        self.mold = mold
        return self

    def with_mold_model(self, mold_model: MoldModel) -> GetFormWithSignatureResult:
        self.mold_model = mold_model
        return self

    def with_form_model(self, form_model: FormModel) -> GetFormWithSignatureResult:
        self.form_model = form_model
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
    ) -> Optional[GetFormWithSignatureResult]:
        if data is None:
            return None
        return GetFormWithSignatureResult()\
            .with_item(Form.from_dict(data.get('item')))\
            .with_body(data.get('body'))\
            .with_signature(data.get('signature'))\
            .with_mold(Mold.from_dict(data.get('mold')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))\
            .with_form_model(FormModel.from_dict(data.get('formModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "body": self.body,
            "signature": self.signature,
            "mold": self.mold.to_dict() if self.mold else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
            "formModel": self.form_model.to_dict() if self.form_model else None,
        }


class GetFormWithSignatureByUserIdResult(core.Gs2Result):
    item: Form = None
    body: str = None
    signature: str = None
    mold: Mold = None
    mold_model: MoldModel = None
    form_model: FormModel = None

    def with_item(self, item: Form) -> GetFormWithSignatureByUserIdResult:
        self.item = item
        return self

    def with_body(self, body: str) -> GetFormWithSignatureByUserIdResult:
        self.body = body
        return self

    def with_signature(self, signature: str) -> GetFormWithSignatureByUserIdResult:
        self.signature = signature
        return self

    def with_mold(self, mold: Mold) -> GetFormWithSignatureByUserIdResult:
        self.mold = mold
        return self

    def with_mold_model(self, mold_model: MoldModel) -> GetFormWithSignatureByUserIdResult:
        self.mold_model = mold_model
        return self

    def with_form_model(self, form_model: FormModel) -> GetFormWithSignatureByUserIdResult:
        self.form_model = form_model
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
    ) -> Optional[GetFormWithSignatureByUserIdResult]:
        if data is None:
            return None
        return GetFormWithSignatureByUserIdResult()\
            .with_item(Form.from_dict(data.get('item')))\
            .with_body(data.get('body'))\
            .with_signature(data.get('signature'))\
            .with_mold(Mold.from_dict(data.get('mold')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))\
            .with_form_model(FormModel.from_dict(data.get('formModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "body": self.body,
            "signature": self.signature,
            "mold": self.mold.to_dict() if self.mold else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
            "formModel": self.form_model.to_dict() if self.form_model else None,
        }


class SetFormByUserIdResult(core.Gs2Result):
    item: Form = None
    mold: Mold = None
    mold_model: MoldModel = None
    form_model: FormModel = None

    def with_item(self, item: Form) -> SetFormByUserIdResult:
        self.item = item
        return self

    def with_mold(self, mold: Mold) -> SetFormByUserIdResult:
        self.mold = mold
        return self

    def with_mold_model(self, mold_model: MoldModel) -> SetFormByUserIdResult:
        self.mold_model = mold_model
        return self

    def with_form_model(self, form_model: FormModel) -> SetFormByUserIdResult:
        self.form_model = form_model
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
    ) -> Optional[SetFormByUserIdResult]:
        if data is None:
            return None
        return SetFormByUserIdResult()\
            .with_item(Form.from_dict(data.get('item')))\
            .with_mold(Mold.from_dict(data.get('mold')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))\
            .with_form_model(FormModel.from_dict(data.get('formModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "mold": self.mold.to_dict() if self.mold else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
            "formModel": self.form_model.to_dict() if self.form_model else None,
        }


class SetFormWithSignatureResult(core.Gs2Result):
    item: Form = None
    mold: Mold = None
    mold_model: MoldModel = None
    form_model: FormModel = None

    def with_item(self, item: Form) -> SetFormWithSignatureResult:
        self.item = item
        return self

    def with_mold(self, mold: Mold) -> SetFormWithSignatureResult:
        self.mold = mold
        return self

    def with_mold_model(self, mold_model: MoldModel) -> SetFormWithSignatureResult:
        self.mold_model = mold_model
        return self

    def with_form_model(self, form_model: FormModel) -> SetFormWithSignatureResult:
        self.form_model = form_model
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
    ) -> Optional[SetFormWithSignatureResult]:
        if data is None:
            return None
        return SetFormWithSignatureResult()\
            .with_item(Form.from_dict(data.get('item')))\
            .with_mold(Mold.from_dict(data.get('mold')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))\
            .with_form_model(FormModel.from_dict(data.get('formModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "mold": self.mold.to_dict() if self.mold else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
            "formModel": self.form_model.to_dict() if self.form_model else None,
        }


class AcquireActionsToFormPropertiesResult(core.Gs2Result):
    item: Form = None
    mold: Mold = None
    stamp_sheet: str = None
    stamp_sheet_encryption_key_id: str = None

    def with_item(self, item: Form) -> AcquireActionsToFormPropertiesResult:
        self.item = item
        return self

    def with_mold(self, mold: Mold) -> AcquireActionsToFormPropertiesResult:
        self.mold = mold
        return self

    def with_stamp_sheet(self, stamp_sheet: str) -> AcquireActionsToFormPropertiesResult:
        self.stamp_sheet = stamp_sheet
        return self

    def with_stamp_sheet_encryption_key_id(self, stamp_sheet_encryption_key_id: str) -> AcquireActionsToFormPropertiesResult:
        self.stamp_sheet_encryption_key_id = stamp_sheet_encryption_key_id
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
    ) -> Optional[AcquireActionsToFormPropertiesResult]:
        if data is None:
            return None
        return AcquireActionsToFormPropertiesResult()\
            .with_item(Form.from_dict(data.get('item')))\
            .with_mold(Mold.from_dict(data.get('mold')))\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_stamp_sheet_encryption_key_id(data.get('stampSheetEncryptionKeyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "mold": self.mold.to_dict() if self.mold else None,
            "stampSheet": self.stamp_sheet,
            "stampSheetEncryptionKeyId": self.stamp_sheet_encryption_key_id,
        }


class DeleteFormResult(core.Gs2Result):
    item: Form = None
    mold: Mold = None
    mold_model: MoldModel = None
    form_model: FormModel = None

    def with_item(self, item: Form) -> DeleteFormResult:
        self.item = item
        return self

    def with_mold(self, mold: Mold) -> DeleteFormResult:
        self.mold = mold
        return self

    def with_mold_model(self, mold_model: MoldModel) -> DeleteFormResult:
        self.mold_model = mold_model
        return self

    def with_form_model(self, form_model: FormModel) -> DeleteFormResult:
        self.form_model = form_model
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
    ) -> Optional[DeleteFormResult]:
        if data is None:
            return None
        return DeleteFormResult()\
            .with_item(Form.from_dict(data.get('item')))\
            .with_mold(Mold.from_dict(data.get('mold')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))\
            .with_form_model(FormModel.from_dict(data.get('formModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "mold": self.mold.to_dict() if self.mold else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
            "formModel": self.form_model.to_dict() if self.form_model else None,
        }


class DeleteFormByUserIdResult(core.Gs2Result):
    item: Form = None
    mold: Mold = None
    mold_model: MoldModel = None
    form_model: FormModel = None

    def with_item(self, item: Form) -> DeleteFormByUserIdResult:
        self.item = item
        return self

    def with_mold(self, mold: Mold) -> DeleteFormByUserIdResult:
        self.mold = mold
        return self

    def with_mold_model(self, mold_model: MoldModel) -> DeleteFormByUserIdResult:
        self.mold_model = mold_model
        return self

    def with_form_model(self, form_model: FormModel) -> DeleteFormByUserIdResult:
        self.form_model = form_model
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
    ) -> Optional[DeleteFormByUserIdResult]:
        if data is None:
            return None
        return DeleteFormByUserIdResult()\
            .with_item(Form.from_dict(data.get('item')))\
            .with_mold(Mold.from_dict(data.get('mold')))\
            .with_mold_model(MoldModel.from_dict(data.get('moldModel')))\
            .with_form_model(FormModel.from_dict(data.get('formModel')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "mold": self.mold.to_dict() if self.mold else None,
            "moldModel": self.mold_model.to_dict() if self.mold_model else None,
            "formModel": self.form_model.to_dict() if self.form_model else None,
        }


class AcquireActionToFormPropertiesByStampSheetResult(core.Gs2Result):
    item: Form = None
    mold: Mold = None
    stamp_sheet: str = None
    stamp_sheet_encryption_key_id: str = None

    def with_item(self, item: Form) -> AcquireActionToFormPropertiesByStampSheetResult:
        self.item = item
        return self

    def with_mold(self, mold: Mold) -> AcquireActionToFormPropertiesByStampSheetResult:
        self.mold = mold
        return self

    def with_stamp_sheet(self, stamp_sheet: str) -> AcquireActionToFormPropertiesByStampSheetResult:
        self.stamp_sheet = stamp_sheet
        return self

    def with_stamp_sheet_encryption_key_id(self, stamp_sheet_encryption_key_id: str) -> AcquireActionToFormPropertiesByStampSheetResult:
        self.stamp_sheet_encryption_key_id = stamp_sheet_encryption_key_id
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
    ) -> Optional[AcquireActionToFormPropertiesByStampSheetResult]:
        if data is None:
            return None
        return AcquireActionToFormPropertiesByStampSheetResult()\
            .with_item(Form.from_dict(data.get('item')))\
            .with_mold(Mold.from_dict(data.get('mold')))\
            .with_stamp_sheet(data.get('stampSheet'))\
            .with_stamp_sheet_encryption_key_id(data.get('stampSheetEncryptionKeyId'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item": self.item.to_dict() if self.item else None,
            "mold": self.mold.to_dict() if self.mold else None,
            "stampSheet": self.stamp_sheet,
            "stampSheetEncryptionKeyId": self.stamp_sheet_encryption_key_id,
        }