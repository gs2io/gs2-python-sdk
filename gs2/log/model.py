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
from gs2 import core


class InGameLogTag(core.Gs2Model):
    key: str = None
    value: str = None

    def with_key(self, key: str) -> InGameLogTag:
        self.key = key
        return self

    def with_value(self, value: str) -> InGameLogTag:
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
    ) -> Optional[InGameLogTag]:
        if data is None:
            return None
        return InGameLogTag()\
            .with_key(data.get('key'))\
            .with_value(data.get('value'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "key": self.key,
            "value": self.value,
        }


class MetricModel(core.Gs2Model):
    name: str = None
    type: str = None
    labels: List[str] = None

    def with_name(self, name: str) -> MetricModel:
        self.name = name
        return self

    def with_type(self, type: str) -> MetricModel:
        self.type = type
        return self

    def with_labels(self, labels: List[str]) -> MetricModel:
        self.labels = labels
        return self

    @classmethod
    def create_grn(
        cls,
    ):
        return ''.format(
        )

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
    ) -> Optional[MetricModel]:
        if data is None:
            return None
        return MetricModel()\
            .with_name(data.get('name'))\
            .with_type(data.get('type'))\
            .with_labels(None if data.get('labels') is None else [
                data.get('labels')[i]
                for i in range(len(data.get('labels')))
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "type": self.type,
            "labels": None if self.labels is None else [
                self.labels[i]
                for i in range(len(self.labels))
            ],
        }


class Trace(core.Gs2Model):
    trace_id: str = None
    spans: List[LogEntry] = None
    truncated: bool = None

    def with_trace_id(self, trace_id: str) -> Trace:
        self.trace_id = trace_id
        return self

    def with_spans(self, spans: List[LogEntry]) -> Trace:
        self.spans = spans
        return self

    def with_truncated(self, truncated: bool) -> Trace:
        self.truncated = truncated
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
    ) -> Optional[Trace]:
        if data is None:
            return None
        return Trace()\
            .with_trace_id(data.get('traceId'))\
            .with_spans(None if data.get('spans') is None else [
                LogEntry.from_dict(data.get('spans')[i])
                for i in range(len(data.get('spans')))
            ])\
            .with_truncated(data.get('truncated'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "traceId": self.trace_id,
            "spans": None if self.spans is None else [
                self.spans[i].to_dict() if self.spans[i] else None
                for i in range(len(self.spans))
            ],
            "truncated": self.truncated,
        }


class TimeseriesValue(core.Gs2Model):
    key: str = None
    value: float = None

    def with_key(self, key: str) -> TimeseriesValue:
        self.key = key
        return self

    def with_value(self, value: float) -> TimeseriesValue:
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
    ) -> Optional[TimeseriesValue]:
        if data is None:
            return None
        return TimeseriesValue()\
            .with_key(data.get('key'))\
            .with_value(data.get('value'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "key": self.key,
            "value": self.value,
        }


class TimeseriesPoint(core.Gs2Model):
    timestamp: int = None
    values: List[TimeseriesValue] = None

    def with_timestamp(self, timestamp: int) -> TimeseriesPoint:
        self.timestamp = timestamp
        return self

    def with_values(self, values: List[TimeseriesValue]) -> TimeseriesPoint:
        self.values = values
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
    ) -> Optional[TimeseriesPoint]:
        if data is None:
            return None
        return TimeseriesPoint()\
            .with_timestamp(data.get('timestamp'))\
            .with_values(None if data.get('values') is None else [
                TimeseriesValue.from_dict(data.get('values')[i])
                for i in range(len(data.get('values')))
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "values": None if self.values is None else [
                self.values[i].to_dict() if self.values[i] else None
                for i in range(len(self.values))
            ],
        }


class TimeseriesMetadata(core.Gs2Model):
    keys: List[str] = None
    group_by: List[str] = None

    def with_keys(self, keys: List[str]) -> TimeseriesMetadata:
        self.keys = keys
        return self

    def with_group_by(self, group_by: List[str]) -> TimeseriesMetadata:
        self.group_by = group_by
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
    ) -> Optional[TimeseriesMetadata]:
        if data is None:
            return None
        return TimeseriesMetadata()\
            .with_keys(None if data.get('keys') is None else [
                data.get('keys')[i]
                for i in range(len(data.get('keys')))
            ])\
            .with_group_by(None if data.get('groupBy') is None else [
                data.get('groupBy')[i]
                for i in range(len(data.get('groupBy')))
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "keys": None if self.keys is None else [
                self.keys[i]
                for i in range(len(self.keys))
            ],
            "groupBy": None if self.group_by is None else [
                self.group_by[i]
                for i in range(len(self.group_by))
            ],
        }


class NumericRange(core.Gs2Model):
    min: float = None
    max: float = None

    def with_min(self, min: float) -> NumericRange:
        self.min = min
        return self

    def with_max(self, max: float) -> NumericRange:
        self.max = max
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
    ) -> Optional[NumericRange]:
        if data is None:
            return None
        return NumericRange()\
            .with_min(data.get('min'))\
            .with_max(data.get('max'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "min": self.min,
            "max": self.max,
        }


class LogEntry(core.Gs2Model):
    timestamp: int = None
    status: str = None
    duration: int = None
    line: str = None
    labels: List[Label] = None

    def with_timestamp(self, timestamp: int) -> LogEntry:
        self.timestamp = timestamp
        return self

    def with_status(self, status: str) -> LogEntry:
        self.status = status
        return self

    def with_duration(self, duration: int) -> LogEntry:
        self.duration = duration
        return self

    def with_line(self, line: str) -> LogEntry:
        self.line = line
        return self

    def with_labels(self, labels: List[Label]) -> LogEntry:
        self.labels = labels
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
    ) -> Optional[LogEntry]:
        if data is None:
            return None
        return LogEntry()\
            .with_timestamp(data.get('timestamp'))\
            .with_status(data.get('status'))\
            .with_duration(data.get('duration'))\
            .with_line(data.get('line'))\
            .with_labels(None if data.get('labels') is None else [
                Label.from_dict(data.get('labels')[i])
                for i in range(len(data.get('labels')))
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "status": self.status,
            "duration": self.duration,
            "line": self.line,
            "labels": None if self.labels is None else [
                self.labels[i].to_dict() if self.labels[i] else None
                for i in range(len(self.labels))
            ],
        }


class Label(core.Gs2Model):
    key: str = None
    value: str = None

    def with_key(self, key: str) -> Label:
        self.key = key
        return self

    def with_value(self, value: str) -> Label:
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
    ) -> Optional[Label]:
        if data is None:
            return None
        return Label()\
            .with_key(data.get('key'))\
            .with_value(data.get('value'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "key": self.key,
            "value": self.value,
        }


class FacetValueCount(core.Gs2Model):
    value: str = None
    count: int = None

    def with_value(self, value: str) -> FacetValueCount:
        self.value = value
        return self

    def with_count(self, count: int) -> FacetValueCount:
        self.count = count
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
    ) -> Optional[FacetValueCount]:
        if data is None:
            return None
        return FacetValueCount()\
            .with_value(data.get('value'))\
            .with_count(data.get('count'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "value": self.value,
            "count": self.count,
        }


class Facet(core.Gs2Model):
    field: str = None
    values: List[FacetValueCount] = None
    range: NumericRange = None
    global_range: NumericRange = None

    def with_field(self, field: str) -> Facet:
        self.field = field
        return self

    def with_values(self, values: List[FacetValueCount]) -> Facet:
        self.values = values
        return self

    def with_range(self, range: NumericRange) -> Facet:
        self.range = range
        return self

    def with_global_range(self, global_range: NumericRange) -> Facet:
        self.global_range = global_range
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
    ) -> Optional[Facet]:
        if data is None:
            return None
        return Facet()\
            .with_field(data.get('field'))\
            .with_values(None if data.get('values') is None else [
                FacetValueCount.from_dict(data.get('values')[i])
                for i in range(len(data.get('values')))
            ])\
            .with_range(NumericRange.from_dict(data.get('range')))\
            .with_global_range(NumericRange.from_dict(data.get('globalRange')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "field": self.field,
            "values": None if self.values is None else [
                self.values[i].to_dict() if self.values[i] else None
                for i in range(len(self.values))
            ],
            "range": self.range.to_dict() if self.range else None,
            "globalRange": self.global_range.to_dict() if self.global_range else None,
        }


class AggregationConfig(core.Gs2Model):
    type: str = None
    field: str = None

    def with_type(self, type: str) -> AggregationConfig:
        self.type = type
        return self

    def with_field(self, field: str) -> AggregationConfig:
        self.field = field
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
    ) -> Optional[AggregationConfig]:
        if data is None:
            return None
        return AggregationConfig()\
            .with_type(data.get('type'))\
            .with_field(data.get('field'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": self.type,
            "field": self.field,
        }


class Dashboard(core.Gs2Model):
    dashboard_id: str = None
    name: str = None
    display_name: str = None
    description: str = None
    payload: str = None
    created_at: int = None
    updated_at: int = None

    def with_dashboard_id(self, dashboard_id: str) -> Dashboard:
        self.dashboard_id = dashboard_id
        return self

    def with_name(self, name: str) -> Dashboard:
        self.name = name
        return self

    def with_display_name(self, display_name: str) -> Dashboard:
        self.display_name = display_name
        return self

    def with_description(self, description: str) -> Dashboard:
        self.description = description
        return self

    def with_payload(self, payload: str) -> Dashboard:
        self.payload = payload
        return self

    def with_created_at(self, created_at: int) -> Dashboard:
        self.created_at = created_at
        return self

    def with_updated_at(self, updated_at: int) -> Dashboard:
        self.updated_at = updated_at
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
        dashboard_name,
    ):
        return 'grn:gs2:{region}:{ownerId}:log:{namespaceName}:dashboard:{dashboardName}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
            dashboardName=dashboard_name,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):dashboard:(?P<dashboardName>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):dashboard:(?P<dashboardName>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):dashboard:(?P<dashboardName>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

    @classmethod
    def get_dashboard_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):dashboard:(?P<dashboardName>.+)', grn)
        if match is None:
            return None
        return match.group('dashboard_name')

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
    ) -> Optional[Dashboard]:
        if data is None:
            return None
        return Dashboard()\
            .with_dashboard_id(data.get('dashboardId'))\
            .with_name(data.get('name'))\
            .with_display_name(data.get('displayName'))\
            .with_description(data.get('description'))\
            .with_payload(data.get('payload'))\
            .with_created_at(data.get('createdAt'))\
            .with_updated_at(data.get('updatedAt'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "dashboardId": self.dashboard_id,
            "name": self.name,
            "displayName": self.display_name,
            "description": self.description,
            "payload": self.payload,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }


class FacetModel(core.Gs2Model):
    facet_model_id: str = None
    field: str = None
    type: str = None
    display_name: str = None
    order: int = None

    def with_facet_model_id(self, facet_model_id: str) -> FacetModel:
        self.facet_model_id = facet_model_id
        return self

    def with_field(self, field: str) -> FacetModel:
        self.field = field
        return self

    def with_type(self, type: str) -> FacetModel:
        self.type = type
        return self

    def with_display_name(self, display_name: str) -> FacetModel:
        self.display_name = display_name
        return self

    def with_order(self, order: int) -> FacetModel:
        self.order = order
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
        field,
    ):
        return 'grn:gs2:{region}:{ownerId}:log:{namespaceName}:model:facet:{field}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
            field=field,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):model:facet:(?P<field>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):model:facet:(?P<field>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):model:facet:(?P<field>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

    @classmethod
    def get_field_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):model:facet:(?P<field>.+)', grn)
        if match is None:
            return None
        return match.group('field')

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
    ) -> Optional[FacetModel]:
        if data is None:
            return None
        return FacetModel()\
            .with_facet_model_id(data.get('facetModelId'))\
            .with_field(data.get('field'))\
            .with_type(data.get('type'))\
            .with_display_name(data.get('displayName'))\
            .with_order(data.get('order'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "facetModelId": self.facet_model_id,
            "field": self.field,
            "type": self.type,
            "displayName": self.display_name,
            "order": self.order,
        }


class Insight(core.Gs2Model):
    insight_id: str = None
    name: str = None
    task_id: str = None
    host: str = None
    password: str = None
    status: str = None
    created_at: int = None
    revision: int = None

    def with_insight_id(self, insight_id: str) -> Insight:
        self.insight_id = insight_id
        return self

    def with_name(self, name: str) -> Insight:
        self.name = name
        return self

    def with_task_id(self, task_id: str) -> Insight:
        self.task_id = task_id
        return self

    def with_host(self, host: str) -> Insight:
        self.host = host
        return self

    def with_password(self, password: str) -> Insight:
        self.password = password
        return self

    def with_status(self, status: str) -> Insight:
        self.status = status
        return self

    def with_created_at(self, created_at: int) -> Insight:
        self.created_at = created_at
        return self

    def with_revision(self, revision: int) -> Insight:
        self.revision = revision
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
        insight_name,
    ):
        return 'grn:gs2:{region}:{ownerId}:log:{namespaceName}:insight:{insightName}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
            insightName=insight_name,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):insight:(?P<insightName>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):insight:(?P<insightName>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):insight:(?P<insightName>.+)', grn)
        if match is None:
            return None
        return match.group('namespace_name')

    @classmethod
    def get_insight_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+):insight:(?P<insightName>.+)', grn)
        if match is None:
            return None
        return match.group('insight_name')

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
    ) -> Optional[Insight]:
        if data is None:
            return None
        return Insight()\
            .with_insight_id(data.get('insightId'))\
            .with_name(data.get('name'))\
            .with_task_id(data.get('taskId'))\
            .with_host(data.get('host'))\
            .with_password(data.get('password'))\
            .with_status(data.get('status'))\
            .with_created_at(data.get('createdAt'))\
            .with_revision(data.get('revision'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "insightId": self.insight_id,
            "name": self.name,
            "taskId": self.task_id,
            "host": self.host,
            "password": self.password,
            "status": self.status,
            "createdAt": self.created_at,
            "revision": self.revision,
        }


class AccessLogWithTelemetry(core.Gs2Model):
    timestamp: int = None
    source_request_id: str = None
    request_id: str = None
    duration: int = None
    service: str = None
    method: str = None
    user_id: str = None
    request: str = None
    result: str = None
    status: str = None

    def with_timestamp(self, timestamp: int) -> AccessLogWithTelemetry:
        self.timestamp = timestamp
        return self

    def with_source_request_id(self, source_request_id: str) -> AccessLogWithTelemetry:
        self.source_request_id = source_request_id
        return self

    def with_request_id(self, request_id: str) -> AccessLogWithTelemetry:
        self.request_id = request_id
        return self

    def with_duration(self, duration: int) -> AccessLogWithTelemetry:
        self.duration = duration
        return self

    def with_service(self, service: str) -> AccessLogWithTelemetry:
        self.service = service
        return self

    def with_method(self, method: str) -> AccessLogWithTelemetry:
        self.method = method
        return self

    def with_user_id(self, user_id: str) -> AccessLogWithTelemetry:
        self.user_id = user_id
        return self

    def with_request(self, request: str) -> AccessLogWithTelemetry:
        self.request = request
        return self

    def with_result(self, result: str) -> AccessLogWithTelemetry:
        self.result = result
        return self

    def with_status(self, status: str) -> AccessLogWithTelemetry:
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
    ) -> Optional[AccessLogWithTelemetry]:
        if data is None:
            return None
        return AccessLogWithTelemetry()\
            .with_timestamp(data.get('timestamp'))\
            .with_source_request_id(data.get('sourceRequestId'))\
            .with_request_id(data.get('requestId'))\
            .with_duration(data.get('duration'))\
            .with_service(data.get('service'))\
            .with_method(data.get('method'))\
            .with_user_id(data.get('userId'))\
            .with_request(data.get('request'))\
            .with_result(data.get('result'))\
            .with_status(data.get('status'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "sourceRequestId": self.source_request_id,
            "requestId": self.request_id,
            "duration": self.duration,
            "service": self.service,
            "method": self.method,
            "userId": self.user_id,
            "request": self.request,
            "result": self.result,
            "status": self.status,
        }


class InGameLog(core.Gs2Model):
    timestamp: int = None
    request_id: str = None
    user_id: str = None
    tags: List[InGameLogTag] = None
    payload: str = None

    def with_timestamp(self, timestamp: int) -> InGameLog:
        self.timestamp = timestamp
        return self

    def with_request_id(self, request_id: str) -> InGameLog:
        self.request_id = request_id
        return self

    def with_user_id(self, user_id: str) -> InGameLog:
        self.user_id = user_id
        return self

    def with_tags(self, tags: List[InGameLogTag]) -> InGameLog:
        self.tags = tags
        return self

    def with_payload(self, payload: str) -> InGameLog:
        self.payload = payload
        return self

    @classmethod
    def create_grn(
        cls,
    ):
        return ''.format(
        )

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
    ) -> Optional[InGameLog]:
        if data is None:
            return None
        return InGameLog()\
            .with_timestamp(data.get('timestamp'))\
            .with_request_id(data.get('requestId'))\
            .with_user_id(data.get('userId'))\
            .with_tags(None if data.get('tags') is None else [
                InGameLogTag.from_dict(data.get('tags')[i])
                for i in range(len(data.get('tags')))
            ])\
            .with_payload(data.get('payload'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "requestId": self.request_id,
            "userId": self.user_id,
            "tags": None if self.tags is None else [
                self.tags[i].to_dict() if self.tags[i] else None
                for i in range(len(self.tags))
            ],
            "payload": self.payload,
        }


class ExecuteStampTaskLogCount(core.Gs2Model):
    service: str = None
    method: str = None
    user_id: str = None
    action: str = None
    count: int = None

    def with_service(self, service: str) -> ExecuteStampTaskLogCount:
        self.service = service
        return self

    def with_method(self, method: str) -> ExecuteStampTaskLogCount:
        self.method = method
        return self

    def with_user_id(self, user_id: str) -> ExecuteStampTaskLogCount:
        self.user_id = user_id
        return self

    def with_action(self, action: str) -> ExecuteStampTaskLogCount:
        self.action = action
        return self

    def with_count(self, count: int) -> ExecuteStampTaskLogCount:
        self.count = count
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
    ) -> Optional[ExecuteStampTaskLogCount]:
        if data is None:
            return None
        return ExecuteStampTaskLogCount()\
            .with_service(data.get('service'))\
            .with_method(data.get('method'))\
            .with_user_id(data.get('userId'))\
            .with_action(data.get('action'))\
            .with_count(data.get('count'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "service": self.service,
            "method": self.method,
            "userId": self.user_id,
            "action": self.action,
            "count": self.count,
        }


class ExecuteStampTaskLog(core.Gs2Model):
    timestamp: int = None
    task_id: str = None
    service: str = None
    method: str = None
    user_id: str = None
    action: str = None
    args: str = None

    def with_timestamp(self, timestamp: int) -> ExecuteStampTaskLog:
        self.timestamp = timestamp
        return self

    def with_task_id(self, task_id: str) -> ExecuteStampTaskLog:
        self.task_id = task_id
        return self

    def with_service(self, service: str) -> ExecuteStampTaskLog:
        self.service = service
        return self

    def with_method(self, method: str) -> ExecuteStampTaskLog:
        self.method = method
        return self

    def with_user_id(self, user_id: str) -> ExecuteStampTaskLog:
        self.user_id = user_id
        return self

    def with_action(self, action: str) -> ExecuteStampTaskLog:
        self.action = action
        return self

    def with_args(self, args: str) -> ExecuteStampTaskLog:
        self.args = args
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
    ) -> Optional[ExecuteStampTaskLog]:
        if data is None:
            return None
        return ExecuteStampTaskLog()\
            .with_timestamp(data.get('timestamp'))\
            .with_task_id(data.get('taskId'))\
            .with_service(data.get('service'))\
            .with_method(data.get('method'))\
            .with_user_id(data.get('userId'))\
            .with_action(data.get('action'))\
            .with_args(data.get('args'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "taskId": self.task_id,
            "service": self.service,
            "method": self.method,
            "userId": self.user_id,
            "action": self.action,
            "args": self.args,
        }


class ExecuteStampSheetLogCount(core.Gs2Model):
    service: str = None
    method: str = None
    user_id: str = None
    action: str = None
    count: int = None

    def with_service(self, service: str) -> ExecuteStampSheetLogCount:
        self.service = service
        return self

    def with_method(self, method: str) -> ExecuteStampSheetLogCount:
        self.method = method
        return self

    def with_user_id(self, user_id: str) -> ExecuteStampSheetLogCount:
        self.user_id = user_id
        return self

    def with_action(self, action: str) -> ExecuteStampSheetLogCount:
        self.action = action
        return self

    def with_count(self, count: int) -> ExecuteStampSheetLogCount:
        self.count = count
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
    ) -> Optional[ExecuteStampSheetLogCount]:
        if data is None:
            return None
        return ExecuteStampSheetLogCount()\
            .with_service(data.get('service'))\
            .with_method(data.get('method'))\
            .with_user_id(data.get('userId'))\
            .with_action(data.get('action'))\
            .with_count(data.get('count'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "service": self.service,
            "method": self.method,
            "userId": self.user_id,
            "action": self.action,
            "count": self.count,
        }


class ExecuteStampSheetLog(core.Gs2Model):
    timestamp: int = None
    transaction_id: str = None
    service: str = None
    method: str = None
    user_id: str = None
    action: str = None
    args: str = None

    def with_timestamp(self, timestamp: int) -> ExecuteStampSheetLog:
        self.timestamp = timestamp
        return self

    def with_transaction_id(self, transaction_id: str) -> ExecuteStampSheetLog:
        self.transaction_id = transaction_id
        return self

    def with_service(self, service: str) -> ExecuteStampSheetLog:
        self.service = service
        return self

    def with_method(self, method: str) -> ExecuteStampSheetLog:
        self.method = method
        return self

    def with_user_id(self, user_id: str) -> ExecuteStampSheetLog:
        self.user_id = user_id
        return self

    def with_action(self, action: str) -> ExecuteStampSheetLog:
        self.action = action
        return self

    def with_args(self, args: str) -> ExecuteStampSheetLog:
        self.args = args
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
    ) -> Optional[ExecuteStampSheetLog]:
        if data is None:
            return None
        return ExecuteStampSheetLog()\
            .with_timestamp(data.get('timestamp'))\
            .with_transaction_id(data.get('transactionId'))\
            .with_service(data.get('service'))\
            .with_method(data.get('method'))\
            .with_user_id(data.get('userId'))\
            .with_action(data.get('action'))\
            .with_args(data.get('args'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "transactionId": self.transaction_id,
            "service": self.service,
            "method": self.method,
            "userId": self.user_id,
            "action": self.action,
            "args": self.args,
        }


class IssueStampSheetLogCount(core.Gs2Model):
    service: str = None
    method: str = None
    user_id: str = None
    action: str = None
    count: int = None

    def with_service(self, service: str) -> IssueStampSheetLogCount:
        self.service = service
        return self

    def with_method(self, method: str) -> IssueStampSheetLogCount:
        self.method = method
        return self

    def with_user_id(self, user_id: str) -> IssueStampSheetLogCount:
        self.user_id = user_id
        return self

    def with_action(self, action: str) -> IssueStampSheetLogCount:
        self.action = action
        return self

    def with_count(self, count: int) -> IssueStampSheetLogCount:
        self.count = count
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
    ) -> Optional[IssueStampSheetLogCount]:
        if data is None:
            return None
        return IssueStampSheetLogCount()\
            .with_service(data.get('service'))\
            .with_method(data.get('method'))\
            .with_user_id(data.get('userId'))\
            .with_action(data.get('action'))\
            .with_count(data.get('count'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "service": self.service,
            "method": self.method,
            "userId": self.user_id,
            "action": self.action,
            "count": self.count,
        }


class IssueStampSheetLog(core.Gs2Model):
    timestamp: int = None
    transaction_id: str = None
    service: str = None
    method: str = None
    user_id: str = None
    action: str = None
    args: str = None
    tasks: List[str] = None

    def with_timestamp(self, timestamp: int) -> IssueStampSheetLog:
        self.timestamp = timestamp
        return self

    def with_transaction_id(self, transaction_id: str) -> IssueStampSheetLog:
        self.transaction_id = transaction_id
        return self

    def with_service(self, service: str) -> IssueStampSheetLog:
        self.service = service
        return self

    def with_method(self, method: str) -> IssueStampSheetLog:
        self.method = method
        return self

    def with_user_id(self, user_id: str) -> IssueStampSheetLog:
        self.user_id = user_id
        return self

    def with_action(self, action: str) -> IssueStampSheetLog:
        self.action = action
        return self

    def with_args(self, args: str) -> IssueStampSheetLog:
        self.args = args
        return self

    def with_tasks(self, tasks: List[str]) -> IssueStampSheetLog:
        self.tasks = tasks
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
    ) -> Optional[IssueStampSheetLog]:
        if data is None:
            return None
        return IssueStampSheetLog()\
            .with_timestamp(data.get('timestamp'))\
            .with_transaction_id(data.get('transactionId'))\
            .with_service(data.get('service'))\
            .with_method(data.get('method'))\
            .with_user_id(data.get('userId'))\
            .with_action(data.get('action'))\
            .with_args(data.get('args'))\
            .with_tasks(None if data.get('tasks') is None else [
                data.get('tasks')[i]
                for i in range(len(data.get('tasks')))
            ])

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "transactionId": self.transaction_id,
            "service": self.service,
            "method": self.method,
            "userId": self.user_id,
            "action": self.action,
            "args": self.args,
            "tasks": None if self.tasks is None else [
                self.tasks[i]
                for i in range(len(self.tasks))
            ],
        }


class AccessLogCount(core.Gs2Model):
    service: str = None
    method: str = None
    user_id: str = None
    count: int = None

    def with_service(self, service: str) -> AccessLogCount:
        self.service = service
        return self

    def with_method(self, method: str) -> AccessLogCount:
        self.method = method
        return self

    def with_user_id(self, user_id: str) -> AccessLogCount:
        self.user_id = user_id
        return self

    def with_count(self, count: int) -> AccessLogCount:
        self.count = count
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
    ) -> Optional[AccessLogCount]:
        if data is None:
            return None
        return AccessLogCount()\
            .with_service(data.get('service'))\
            .with_method(data.get('method'))\
            .with_user_id(data.get('userId'))\
            .with_count(data.get('count'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "service": self.service,
            "method": self.method,
            "userId": self.user_id,
            "count": self.count,
        }


class AccessLog(core.Gs2Model):
    timestamp: int = None
    request_id: str = None
    service: str = None
    method: str = None
    user_id: str = None
    request: str = None
    result: str = None

    def with_timestamp(self, timestamp: int) -> AccessLog:
        self.timestamp = timestamp
        return self

    def with_request_id(self, request_id: str) -> AccessLog:
        self.request_id = request_id
        return self

    def with_service(self, service: str) -> AccessLog:
        self.service = service
        return self

    def with_method(self, method: str) -> AccessLog:
        self.method = method
        return self

    def with_user_id(self, user_id: str) -> AccessLog:
        self.user_id = user_id
        return self

    def with_request(self, request: str) -> AccessLog:
        self.request = request
        return self

    def with_result(self, result: str) -> AccessLog:
        self.result = result
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
    ) -> Optional[AccessLog]:
        if data is None:
            return None
        return AccessLog()\
            .with_timestamp(data.get('timestamp'))\
            .with_request_id(data.get('requestId'))\
            .with_service(data.get('service'))\
            .with_method(data.get('method'))\
            .with_user_id(data.get('userId'))\
            .with_request(data.get('request'))\
            .with_result(data.get('result'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "requestId": self.request_id,
            "service": self.service,
            "method": self.method,
            "userId": self.user_id,
            "request": self.request,
            "result": self.result,
        }


class Namespace(core.Gs2Model):
    namespace_id: str = None
    name: str = None
    description: str = None
    type: str = None
    gcp_credential_json: str = None
    big_query_dataset_name: str = None
    log_expire_days: int = None
    aws_region: str = None
    aws_access_key_id: str = None
    aws_secret_access_key: str = None
    firehose_stream_name: str = None
    firehose_compress_data: str = None
    status: str = None
    created_at: int = None
    updated_at: int = None
    revision: int = None

    def with_namespace_id(self, namespace_id: str) -> Namespace:
        self.namespace_id = namespace_id
        return self

    def with_name(self, name: str) -> Namespace:
        self.name = name
        return self

    def with_description(self, description: str) -> Namespace:
        self.description = description
        return self

    def with_type(self, type: str) -> Namespace:
        self.type = type
        return self

    def with_gcp_credential_json(self, gcp_credential_json: str) -> Namespace:
        self.gcp_credential_json = gcp_credential_json
        return self

    def with_big_query_dataset_name(self, big_query_dataset_name: str) -> Namespace:
        self.big_query_dataset_name = big_query_dataset_name
        return self

    def with_log_expire_days(self, log_expire_days: int) -> Namespace:
        self.log_expire_days = log_expire_days
        return self

    def with_aws_region(self, aws_region: str) -> Namespace:
        self.aws_region = aws_region
        return self

    def with_aws_access_key_id(self, aws_access_key_id: str) -> Namespace:
        self.aws_access_key_id = aws_access_key_id
        return self

    def with_aws_secret_access_key(self, aws_secret_access_key: str) -> Namespace:
        self.aws_secret_access_key = aws_secret_access_key
        return self

    def with_firehose_stream_name(self, firehose_stream_name: str) -> Namespace:
        self.firehose_stream_name = firehose_stream_name
        return self

    def with_firehose_compress_data(self, firehose_compress_data: str) -> Namespace:
        self.firehose_compress_data = firehose_compress_data
        return self

    def with_status(self, status: str) -> Namespace:
        self.status = status
        return self

    def with_created_at(self, created_at: int) -> Namespace:
        self.created_at = created_at
        return self

    def with_updated_at(self, updated_at: int) -> Namespace:
        self.updated_at = updated_at
        return self

    def with_revision(self, revision: int) -> Namespace:
        self.revision = revision
        return self

    @classmethod
    def create_grn(
        cls,
        region,
        owner_id,
        namespace_name,
    ):
        return 'grn:gs2:{region}:{ownerId}:log:{namespaceName}'.format(
            region=region,
            ownerId=owner_id,
            namespaceName=namespace_name,
        )

    @classmethod
    def get_region_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+)', grn)
        if match is None:
            return None
        return match.group('region')

    @classmethod
    def get_owner_id_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+)', grn)
        if match is None:
            return None
        return match.group('owner_id')

    @classmethod
    def get_namespace_name_from_grn(
        cls,
        grn: str,
    ) -> Optional[str]:
        match = re.search('grn:gs2:(?P<region>.+):(?P<ownerId>.+):log:(?P<namespaceName>.+)', grn)
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
            .with_type(data.get('type'))\
            .with_gcp_credential_json(data.get('gcpCredentialJson'))\
            .with_big_query_dataset_name(data.get('bigQueryDatasetName'))\
            .with_log_expire_days(data.get('logExpireDays'))\
            .with_aws_region(data.get('awsRegion'))\
            .with_aws_access_key_id(data.get('awsAccessKeyId'))\
            .with_aws_secret_access_key(data.get('awsSecretAccessKey'))\
            .with_firehose_stream_name(data.get('firehoseStreamName'))\
            .with_firehose_compress_data(data.get('firehoseCompressData'))\
            .with_status(data.get('status'))\
            .with_created_at(data.get('createdAt'))\
            .with_updated_at(data.get('updatedAt'))\
            .with_revision(data.get('revision'))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "namespaceId": self.namespace_id,
            "name": self.name,
            "description": self.description,
            "type": self.type,
            "gcpCredentialJson": self.gcp_credential_json,
            "bigQueryDatasetName": self.big_query_dataset_name,
            "logExpireDays": self.log_expire_days,
            "awsRegion": self.aws_region,
            "awsAccessKeyId": self.aws_access_key_id,
            "awsSecretAccessKey": self.aws_secret_access_key,
            "firehoseStreamName": self.firehose_stream_name,
            "firehoseCompressData": self.firehose_compress_data,
            "status": self.status,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "revision": self.revision,
        }