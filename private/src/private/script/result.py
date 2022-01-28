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
from core.model import Gs2Result
import script.model as model

from script.result import \
    DescribeNamespacesResult, \
    CreateNamespaceResult, \
    GetNamespaceStatusResult, \
    GetNamespaceResult, \
    UpdateNamespaceResult, \
    DeleteNamespaceResult, \
    DescribeScriptsResult, \
    CreateScriptResult, \
    CreateScriptFromGitHubResult, \
    GetScriptResult, \
    UpdateScriptResult, \
    UpdateScriptFromGitHubResult, \
    DeleteScriptResult, \
    InvokeScriptResult, \
    DebugInvokeResult


class DescribeNamespacesByOwnerIdResult(Gs2Result):
    """
    オーナーIDを指定してネームスペースの一覧を取得 のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(DescribeNamespacesByOwnerIdResult, self).__init__()
        # ネームスペースのリスト
        self._items = []
        for item in response.get('items', []):
            self._items.append(model.Namespace(item))
        # リストの続きを取得するためのページトークン
        self._next_page_token = response.get('nextPageToken') if 'nextPageToken' in response else None

    @property
    def items(self) -> List[model.Namespace]:
        return self._items

    @property
    def next_page_token(self) -> str:
        return self._next_page_token

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(DescribeNamespacesByOwnerIdResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": [item.to_dict() for item in self._items],
            "nextPageToken": self._next_page_token,
        }


class InvokeResult(Gs2Result):
    """
    スクリプトを実行します のレスポンスモデル
    """
    
    def __init__(
        self,
        response: Dict[str, Any],
    ):
        super(InvokeResult, self).__init__()
        # ステータスコード
        self._code = response.get('code') if 'code' in response else None
        # 戻り値
        self._result = response.get('result') if 'result' in response else None
        # スクリプトの実行時間(ミリ秒)
        self._execute_time = response.get('executeTime') if 'executeTime' in response else None
        # 費用の計算対象となった時間(秒)
        self._charged = response.get('charged') if 'charged' in response else None
        # 標準出力の内容のリスト
        self._output = []
        for item in response.get('output', []):
            self._output.append(str(item))

    @property
    def code(self) -> int:
        return self._code

    @property
    def result(self) -> str:
        return self._result

    @property
    def execute_time(self) -> int:
        return self._execute_time

    @property
    def charged(self) -> int:
        return self._charged

    @property
    def output(self) -> List[str]:
        return self._output

    def get(self, key, default=None):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return default

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(InvokeResult, self).__getitem__(key)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "code": self._code,
            "result": self._result,
            "executeTime": self._execute_time,
            "charged": self._charged,
            "output": self._output,
        }
