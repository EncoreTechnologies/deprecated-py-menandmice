# Licensed to the Encore Technologies ("Encore") under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# module
import menandmice

# testing
import unittest

# utilities
import os

# variables to allow integration testing with a real server
MM_SERVER = os.getenv('MM_SERVER', 'testserver')
MM_USERNAME = os.getenv('MM_USERNAME', 'testusername')
MM_PASSWORD = os.getenv('MM_USERNAME', 'testpassword')


class BaseTest(unittest.TestCase):

    @property
    def server(self):
        return MM_SERVER

    @property
    def username(self):
        return MM_USERNAME

    @property
    def password(self):
        return MM_PASSWORD

    def setUp(self):
        super(BaseTest, self).setUp()
        self.client = menandmice.client.Client(self.server,
                                               self.username,
                                               self.password)

    def tearDown(self):
        super(BaseTest, self).tearDown()
        del self.client


class BaseObjectTest(BaseTest):
    __test__ = False

    def setUp(self):
        super(BaseObjectTest, self).setUp()
        self.obj_class = None
        self.obj_dict = {}

    def tearDown(self):
        super(BaseObjectTest, self).tearDown()
        del self.obj_class
        del self.obj_dict

    def add_key(self, key, default=None):
        self.obj_dict[key] = default

    def test_init(self):
        obj = self.obj_class()
        self.assertIsInstance(obj, menandmice.base.BaseObject)
        self.assertIsInstance(obj, dict)
        self.assertEquals(sorted(obj.keys()), sorted(self.obj_dict.keys()))
        for k, v in obj.items():
            self.assertEquals(v, self.obj_dict[k], msg="key = {}".format(k))

    def test_init_dict(self):
        expected_dict = self.obj_dict
        obj = self.obj_class(expected_dict)
        self.assertEquals(obj, expected_dict)

    def test_init_kwargs(self):
        expected_dict = self.obj_dict
        obj = self.obj_class(**expected_dict)
        self.assertEquals(obj, expected_dict)
