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
import project.model as model

from project.request import \
    CreateAccountRequest, \
    VerifyRequest, \
    SignInRequest, \
    IssueAccountTokenRequest, \
    ForgetRequest, \
    IssuePasswordRequest, \
    UpdateAccountRequest, \
    DeleteAccountRequest, \
    DescribeProjectsRequest, \
    CreateProjectRequest, \
    GetProjectRequest, \
    GetProjectTokenRequest, \
    GetProjectTokenByIdentifierRequest, \
    UpdateProjectRequest, \
    DeleteProjectRequest, \
    DescribeBillingMethodsRequest, \
    CreateBillingMethodRequest, \
    GetBillingMethodRequest, \
    UpdateBillingMethodRequest, \
    DeleteBillingMethodRequest, \
    DescribeReceiptsRequest, \
    DescribeBillingsRequest


class DescribeAccountsRequest(Gs2Request):
    """
    GS2アカウントの一覧を取得します のリクエストモデル
    """
    _page_token: str = None
    _limit: int = None

    def __init__(self):
        super(DescribeAccountsRequest, self).__init__()

    @property
    def page_token(self) -> str:
        return self._page_token

    @page_token.setter
    def page_token(self, page_token: str):
        self._page_token = page_token

    def with_page_token(self, page_token: str) -> DescribeAccountsRequest:
        self._page_token = page_token
        return self

    @property
    def limit(self) -> int:
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        self._limit = limit

    def with_limit(self, limit: int) -> DescribeAccountsRequest:
        self._limit = limit
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DescribeAccountsRequest:
        return DescribeAccountsRequest()\
            .with_page_token(data.get('pageToken', data.get('page_token')))\
            .with_limit(data.get('limit', data.get('limit')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "pageToken": self._page_token,
            "limit": self._limit,
        }


class GetAccountByAccountNameRequest(Gs2Request):
    """
    GS2アカウントを取得します のリクエストモデル
    """
    _account_name: str = None

    def __init__(self):
        super(GetAccountByAccountNameRequest, self).__init__()

    @property
    def account_name(self) -> str:
        return self._account_name

    @account_name.setter
    def account_name(self, account_name: str):
        self._account_name = account_name

    def with_account_name(self, account_name: str) -> GetAccountByAccountNameRequest:
        self._account_name = account_name
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> GetAccountByAccountNameRequest:
        return GetAccountByAccountNameRequest()\
            .with_account_name(data.get('accountName', data.get('account_name')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "accountName": self._account_name,
        }


class UpdateAccountByAccountNameRequest(Gs2Request):
    """
    GS2アカウントを更新します のリクエストモデル
    """
    _account_name: str = None
    _email: str = None
    _full_name: str = None
    _company_name: str = None
    _password: str = None

    def __init__(self):
        super(UpdateAccountByAccountNameRequest, self).__init__()

    @property
    def account_name(self) -> str:
        return self._account_name

    @account_name.setter
    def account_name(self, account_name: str):
        self._account_name = account_name

    def with_account_name(self, account_name: str) -> UpdateAccountByAccountNameRequest:
        self._account_name = account_name
        return self

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    def with_email(self, email: str) -> UpdateAccountByAccountNameRequest:
        self._email = email
        return self

    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, full_name: str):
        self._full_name = full_name

    def with_full_name(self, full_name: str) -> UpdateAccountByAccountNameRequest:
        self._full_name = full_name
        return self

    @property
    def company_name(self) -> str:
        return self._company_name

    @company_name.setter
    def company_name(self, company_name: str):
        self._company_name = company_name

    def with_company_name(self, company_name: str) -> UpdateAccountByAccountNameRequest:
        self._company_name = company_name
        return self

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password

    def with_password(self, password: str) -> UpdateAccountByAccountNameRequest:
        self._password = password
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> UpdateAccountByAccountNameRequest:
        return UpdateAccountByAccountNameRequest()\
            .with_account_name(data.get('accountName', data.get('account_name')))\
            .with_email(data.get('email', data.get('email')))\
            .with_full_name(data.get('fullName', data.get('full_name')))\
            .with_company_name(data.get('companyName', data.get('company_name')))\
            .with_password(data.get('password', data.get('password')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "accountName": self._account_name,
            "email": self._email,
            "fullName": self._full_name,
            "companyName": self._company_name,
            "password": self._password,
        }


class DeleteAccountByAccountNameRequest(Gs2Request):
    """
    GS2アカウントを削除します のリクエストモデル
    """
    _account_name: str = None

    def __init__(self):
        super(DeleteAccountByAccountNameRequest, self).__init__()

    @property
    def account_name(self) -> str:
        return self._account_name

    @account_name.setter
    def account_name(self, account_name: str):
        self._account_name = account_name

    def with_account_name(self, account_name: str) -> DeleteAccountByAccountNameRequest:
        self._account_name = account_name
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DeleteAccountByAccountNameRequest:
        return DeleteAccountByAccountNameRequest()\
            .with_account_name(data.get('accountName', data.get('account_name')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "accountName": self._account_name,
        }


class DeleteAccountByEmailRequest(Gs2Request):
    """
    GS2アカウントを削除します のリクエストモデル
    """
    _email: str = None

    def __init__(self):
        super(DeleteAccountByEmailRequest, self).__init__()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    def with_email(self, email: str) -> DeleteAccountByEmailRequest:
        self._email = email
        return self

    @staticmethod
    def from_dict(
        data: Dict[str, Any],
    ) -> DeleteAccountByEmailRequest:
        return DeleteAccountByEmailRequest()\
            .with_email(data.get('email', data.get('email')))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "email": self._email,
        }
