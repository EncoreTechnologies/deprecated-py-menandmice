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

from base_test import BaseTest, BaseObjectTest
from mock import patch

import menandmice
from menandmice.base import BaseObject

class TestBaseObject(BaseTest):

    def test_init(self):
        obj = BaseObject()
        self.assertIsInstance(obj, dict)

    def test_add_key(self):
        obj = BaseObject()
        self.assertEquals(obj, {})

        obj.add_key('test')
        self.assertIn('test', obj)
        self.assertIsNone(obj['test'])

    def test_add_key_default(self):
        obj = BaseObject()
        self.assertEquals(obj, {})

        expected = "123"
        obj.add_key('test', default=expected)
        self.assertIn('test', obj)
        self.assertEquals(obj['test'], expected)

    def test_add_key_duplicate(self):
        obj = BaseObject()
        self.assertEquals(obj, {})

        expected = "123"
        obj.add_key('test', default=expected)
        self.assertIn('test', obj)
        self.assertEquals(obj['test'], expected)

        obj.add_key('test', default="456")
        self.assertIn('test', obj)
        self.assertEquals(obj['test'], expected)

    @patch('menandmice.base.json')
    def test_to_json(self, mock_json):
        expected = "json_dumps_result"
        mock_json.dumps.return_value = expected

        obj = BaseObject()
        obj['str'] = "123"
        obj['int'] = 456
        obj['list'] = ["first", "second"]
        obj['dict'] = {"abc": "234", "test": "value"}

        result = obj.to_json()

        mock_json.dumps.assert_called_with(obj)
        self.assertEqual(result, expected)

    @patch('menandmice.base.json')
    def test_to_json(self, mock_json):
        expected = "json_loads_result"
        mock_json.loads.return_value = expected
        json_input = "abc123"
        obj = BaseObject()

        result = obj.from_json(json_input)

        mock_json.loads.assert_called_with(json_input)
        self.assertEqual(result, expected)


    @patch('menandmice.base.urlencode')
    def test_make_query_str(self, mock_urlencode):
        urlencode_result = "urlencode_result"
        mock_urlencode.return_value = urlencode_result
        kwargs_dict = {"test": "abc123"}
        obj = BaseObject()

        result = obj.make_query_str(**kwargs_dict)

        mock_urlencode.assert_called_with(kwargs_dict)
        self.assertEqual(result, "?{}".format(urlencode_result))


    @patch('menandmice.base.urlencode')
    def test_make_query_str_empty(self, mock_urlencode):
        obj = BaseObject()
        result = obj.make_query_str()

        mock_urlencode.assert_not_called()
        self.assertEqual(result, "")
