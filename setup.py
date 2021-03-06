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
#
# deny overwrite

import os

from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='gs2-python-sdk',
    version='1.0.70',
    package_dir={
        'gs2': '.'
    },
    packages=[
        "",
    ],
    install_requires=[
        'websocket_client >= 0.59.0',
        'pycrypto >= 2.6.1',
        'simplejson >= 3.17.2',
        'requests >= 2.25.1',
    ],
    tests_require=[],
    license='Apache License 2.0',
    description='GS2 SDK for Python.',
    url='https://gs2.io/',
    author='Game Server Services, Inc.',
    author_email='contact@gs2.io',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)