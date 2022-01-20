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
from urllib.parse import quote

from core.rest import *
from auth.rest import Gs2AuthRestClient
from core.model import Gs2Constant
import private.auth.request as request_model
import private.auth.result as result_model


class Gs2AuthPrivateRestClient(Gs2AuthRestClient):

    def __init__(self, session: Gs2RestSession):
        super().__init__(session)
