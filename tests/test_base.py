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

from base_test import BaseTest
from mock import patch, Mock, call

import json

from menandmice.base import BaseObject
from menandmice.base import BaseService


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
    def test_from_json(self, mock_json):
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


class TestBaseService(BaseTest):

    def test_init(self):
        obj = BaseService()
        self.assertIsInstance(obj, dict)
        self.assertIsInstance(obj, BaseObject)
        self.assertEqual(obj.client, None)
        self.assertEqual(obj.url_base, "")
        self.assertEqual(obj.entity_class, None)
        self.assertEqual(obj.get_response_entity_key, "")
        self.assertEqual(obj.get_response_all_key, "")
        self.assertEqual(obj.get_is_singular, False)
        self.assertEqual(obj.ref_key, 'ref')

    def test_init_kwargs(self):
        expected_client = self.client
        expected_url_base = self.url_base
        expected_entity_class = TestBaseService
        expected_get_response_entity_key = 'entity'
        expected_get_response_all_key = 'all'
        expected_get_is_singular = True
        expected_ref_key = 'specialRef'

        obj = BaseService(client=expected_client,
                          url_base=expected_url_base,
                          entity_class=expected_entity_class,
                          get_response_entity_key=expected_get_response_entity_key,
                          get_response_all_key=expected_get_response_all_key,
                          get_is_singular=expected_get_is_singular,
                          ref_key=expected_ref_key)
        self.assertIsInstance(obj, dict)
        self.assertIsInstance(obj, BaseObject)
        self.assertEqual(obj.client, expected_client)
        self.assertEqual(obj.url_base, expected_url_base)
        self.assertEqual(obj.entity_class, expected_entity_class)
        self.assertEqual(obj.get_response_entity_key, expected_get_response_entity_key)
        self.assertEqual(obj.get_response_all_key, expected_get_response_all_key)
        self.assertEqual(obj.get_is_singular, expected_get_is_singular)
        self.assertEqual(obj.ref_key, expected_ref_key)

    def test_build(self):
        expected_dict = {"int": 123, "str": "def", "list": [1, 2, 3]}
        mock_entity_class = Mock()
        mock_entity_class.return_value = "abc"

        obj = BaseService(entity_class=mock_entity_class)
        result = obj.build(expected_dict)

        mock_entity_class.assert_called_with(**expected_dict)
        self.assertTrue(result, mock_entity_class.return_value)

    @patch("menandmice.base.json")
    def test_build_json(self, mock_json):
        expected_dict = {"int": 123, "str": "def", "list": [1, 2, 3]}
        expected_json_str = json.dumps(expected_dict)
        mock_json.loads.return_value = expected_dict

        mock_entity_class = Mock()
        mock_entity_class.return_value = "abc"

        obj = BaseService(entity_class=mock_entity_class)
        result = obj.build(expected_json_str)

        mock_json.loads.assert_called_with(expected_json_str)
        mock_entity_class.assert_called_with(**expected_dict)
        self.assertTrue(result, mock_entity_class.return_value)

    @patch("menandmice.base.BaseService.build")
    @patch("menandmice.base.BaseService.make_query_str")
    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_get_all(self, mock_ref_or_raise, mock_make_query_str, mock_build):
        expected_base_url = self.url_base
        expected_url_base = "DNSZones"
        expected_ref = ""
        expected_ref_key = "ref_key"
        expected_get_is_singular = False  # we want to get all
        expected_get_response_entity_key = 'ref_entity'
        expected_get_response_all_key = 'ref_all'
        expected_query_str = "?filter=encoretest"

        expected_entities = [1, 2, 3, 4]
        expected_calls = [call(c) for c in expected_entities]
        key = expected_get_response_all_key

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.get.return_value = {'result': {key: expected_entities}}
        mock_ref_or_raise.return_value = expected_ref
        mock_make_query_str.return_value = expected_query_str
        mock_build.side_effect = expected_entities

        mock_kwargs = {"testarg1": 123, "testarg2": "value2"}

        obj = BaseService(client=mock_client,
                          url_base=expected_url_base,
                          get_response_entity_key=expected_get_response_entity_key,
                          get_response_all_key=expected_get_response_all_key,
                          get_is_singular=expected_get_is_singular,
                          ref_key=expected_ref_key)
        result = obj.get(**mock_kwargs)

        mock_ref_or_raise.assert_called_with("", expected_ref_key)
        mock_make_query_str.assert_called_with(**mock_kwargs)
        mock_client.get.assert_called_with("{0}{1}{2}".format(expected_base_url,
                                                              expected_url_base,
                                                              expected_query_str))
        mock_build.assert_has_calls(expected_calls)
        self.assertEquals(result, expected_entities)

    @patch("menandmice.base.BaseService.build")
    @patch("menandmice.base.BaseService.make_query_str")
    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_get_singular(self, mock_ref_or_raise, mock_make_query_str, mock_build):
        expected_base_url = self.url_base
        expected_url_base = "DNSZones"
        expected_ref = "DNSZones/123"
        expected_ref_key = "ref_key"
        expected_get_is_singular = True  # we want to get singular
        expected_get_response_entity_key = 'ref_entity'
        expected_get_response_all_key = 'ref_all'
        expected_query_str = "?filter=encoretest"

        expected_entity = 1
        expected_calls = [call(expected_entity)]
        key = expected_get_response_entity_key

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.get.return_value = {'result': {key: expected_entity}}
        mock_ref_or_raise.return_value = expected_ref
        mock_make_query_str.return_value = expected_query_str
        mock_build.side_effect = [expected_entity]

        mock_kwargs = {"testarg1": 123, "testarg2": "value2"}

        obj = BaseService(client=mock_client,
                          url_base=expected_url_base,
                          get_response_entity_key=expected_get_response_entity_key,
                          get_response_all_key=expected_get_response_all_key,
                          get_is_singular=expected_get_is_singular,
                          ref_key=expected_ref_key)
        result = obj.get(**mock_kwargs)

        mock_ref_or_raise.assert_called_with("", expected_ref_key)
        mock_make_query_str.assert_called_with(**mock_kwargs)
        mock_client.get.assert_called_with("{0}{1}{2}".format(expected_base_url,
                                                              expected_ref,
                                                              expected_query_str))
        mock_build.assert_has_calls(expected_calls)
        self.assertEquals(result, [expected_entity])

    @patch("menandmice.base.BaseService.build")
    @patch("menandmice.base.BaseService.make_query_str")
    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_get_ref(self, mock_ref_or_raise, mock_make_query_str, mock_build):
        expected_base_url = self.url_base
        expected_url_base = "DNSZones"
        expected_ref = "DNSZones/123"
        expected_ref_key = "ref_key"
        expected_get_is_singular = False  # we want to get singular
        expected_get_response_entity_key = 'ref_entity'
        expected_get_response_all_key = 'ref_all'
        expected_query_str = "?filter=encoretest"

        expected_entity = 1
        expected_calls = [call(expected_entity)]
        key = expected_get_response_entity_key

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.get.return_value = {'result': {key: expected_entity}}
        mock_ref_or_raise.return_value = expected_ref
        mock_make_query_str.return_value = expected_query_str
        mock_build.side_effect = [expected_entity]

        mock_kwargs = {"testarg1": 123, "testarg2": "value2"}

        obj = BaseService(client=mock_client,
                          url_base=expected_url_base,
                          get_response_entity_key=expected_get_response_entity_key,
                          get_response_all_key=expected_get_response_all_key,
                          get_is_singular=expected_get_is_singular,
                          ref_key=expected_ref_key)
        result = obj.get(expected_ref, **mock_kwargs)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_make_query_str.assert_called_with(**mock_kwargs)
        mock_client.get.assert_called_with("{0}{1}{2}".format(expected_base_url,
                                                              expected_ref,
                                                              expected_query_str))
        mock_build.assert_has_calls(expected_calls)
        self.assertEquals(result, [expected_entity])
