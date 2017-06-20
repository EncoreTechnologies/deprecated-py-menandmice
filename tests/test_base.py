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

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_delete(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.delete_item.return_value = expected_result

        kwargs_dict = {"test": "value", "test2": "value2"}

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.delete(expected_ref, **kwargs_dict)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.delete_item.assert_called_with(expected_ref, **kwargs_dict)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_update(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_properties = "test_properties"
        expected_obj_type = ""
        expected_save_comment = ""
        expected_delete_unspecified = False
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.update_item.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.update(expected_ref, expected_properties)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.update_item.assert_called_with(expected_ref,
                                                   expected_properties,
                                                   expected_obj_type,
                                                   expected_save_comment,
                                                   expected_delete_unspecified)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_update_params(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_properties = "test_properties"
        expected_obj_type = "test_obj_type"
        expected_save_comment = "test_save_comment"
        expected_delete_unspecified = True
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.update_item.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.update(expected_ref,
                            expected_properties,
                            expected_obj_type,
                            expected_save_comment,
                            expected_delete_unspecified)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.update_item.assert_called_with(expected_ref,
                                                   expected_properties,
                                                   expected_obj_type,
                                                   expected_save_comment,
                                                   expected_delete_unspecified)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_get_access(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.get_item_access.return_value = expected_result

        kwargs_dict = {"test": "value", "test2": "value2"}

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.get_access(expected_ref, **kwargs_dict)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.get_item_access.assert_called_with(expected_ref, **kwargs_dict)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_set_access(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_identity_access = "test identity access"
        expected_obj_type = ""
        expected_save_comment = ""
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.set_item_access.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.set_access(expected_ref, expected_identity_access)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.set_item_access.assert_called_with(expected_ref,
                                                       expected_identity_access,
                                                       expected_obj_type,
                                                       expected_save_comment)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_set_access_dict_and_params(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_identity_access = "test identity access"
        expected_identity_access_dict = {"identityAccess": expected_identity_access}
        expected_obj_type = "test obj type"
        expected_save_comment = "test save comment"
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.set_item_access.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.set_access(expected_ref,
                                expected_identity_access_dict,
                                expected_obj_type,
                                expected_save_comment)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.set_item_access.assert_called_with(expected_ref,
                                                       expected_identity_access,
                                                       expected_obj_type,
                                                       expected_save_comment)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_get_history(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.get_item_history.return_value = expected_result

        kwargs_dict = {"test": "value", "test2": "value2"}

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.get_history(expected_ref, **kwargs_dict)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.get_item_history.assert_called_with(expected_ref, **kwargs_dict)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_get_property_definition(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_property_name = ""
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.get_property_definitions.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.get_property_definition(expected_ref)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.get_property_definitions.assert_called_with(expected_ref,
                                                                expected_property_name)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_get_property_definition_params(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_property_name = "test_name"
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.get_property_definitions.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.get_property_definition(expected_ref,
                                             expected_property_name)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.get_property_definitions.assert_called_with(expected_ref,
                                                                expected_property_name)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_add_property_definition(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_property_definition = "property def"
        expected_save_comment = ""
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.add_property_definition.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.add_property_definition(expected_ref,
                                             expected_property_definition)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.add_property_definition.assert_called_with(expected_ref,
                                                               expected_property_definition,
                                                               expected_save_comment)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_add_property_definition_params(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_property_definition = "property def"
        expected_save_comment = "test save comment"
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.add_property_definition.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.add_property_definition(expected_ref,
                                             expected_property_definition,
                                             expected_save_comment)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.add_property_definition.assert_called_with(expected_ref,
                                                               expected_property_definition,
                                                               expected_save_comment)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_update_property_definition(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_property_name = "property name"
        expected_property_definition = "property def"
        expected_update_existing = None
        expected_save_comment = ""
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.update_property_definition.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.update_property_definition(expected_ref,
                                                expected_property_name,
                                                expected_property_definition)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.update_property_definition.assert_called_with(expected_ref,
                                                                  expected_property_name,
                                                                  expected_property_definition,
                                                                  expected_update_existing,
                                                                  expected_save_comment)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_update_property_definition_params(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_property_name = "property name"
        expected_property_definition = "property def"
        expected_update_existing = True
        expected_save_comment = "test comment"
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.update_property_definition.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.update_property_definition(expected_ref,
                                                expected_property_name,
                                                expected_property_definition,
                                                expected_update_existing,
                                                expected_save_comment)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.update_property_definition.assert_called_with(expected_ref,
                                                                  expected_property_name,
                                                                  expected_property_definition,
                                                                  expected_update_existing,
                                                                  expected_save_comment)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_delete_property_definition(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_property_name = "property name"
        expected_save_comment = ""
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.delete_property_definition.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.delete_property_definition(expected_ref,
                                                expected_property_name)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.delete_property_definition.assert_called_with(expected_ref,
                                                                  expected_property_name,
                                                                  expected_save_comment)
        self.assertEquals(result, expected_result)

    @patch("menandmice.base.BaseService.ref_or_raise")
    def test_delete_property_definition_params(self, mock_ref_or_raise):
        expected_ref_key = "ref_key"
        expected_ref = "DNSZone/123"
        expected_result = "expected return"
        expected_property_name = "property name"
        expected_save_comment = "test comment"
        mock_ref_or_raise.return_value = expected_ref
        mock_client = Mock()
        mock_client.delete_property_definition.return_value = expected_result

        obj = BaseService(client=mock_client,
                          ref_key=expected_ref_key)
        result = obj.delete_property_definition(expected_ref,
                                                expected_property_name,
                                                expected_save_comment)

        mock_ref_or_raise.assert_called_with(expected_ref, expected_ref_key)
        mock_client.delete_property_definition.assert_called_with(expected_ref,
                                                                  expected_property_name,
                                                                  expected_save_comment)
        self.assertEquals(result, expected_result)

    def test_ref_or_raise_str(self):
        expected_ref_str = "DNSZone/123"
        obj = BaseService()
        result = obj.ref_or_raise(expected_ref_str)
        self.assertEquals(result, expected_ref_str)

    def test_ref_or_raise_dict(self):
        expected_ref_str = "DNSZone/123"
        expected_ref_dict = {"ref": expected_ref_str}
        obj = BaseService()
        result = obj.ref_or_raise(expected_ref_dict)
        self.assertEquals(result, expected_ref_str)

    def test_ref_or_raise_dict_alternate_key(self):
        expected_ref_str = "DNSZone/123"
        expected_ref_key = "differentRefKey"
        expected_ref_dict = {expected_ref_key: expected_ref_str}
        obj = BaseService()
        result = obj.ref_or_raise(expected_ref_dict, key=expected_ref_key)
        self.assertEquals(result, expected_ref_str)

    def test_ref_or_raise_raise(self):
        expected_ref_int = 123
        obj = BaseService()
        with self.assertRaises(TypeError) as context:
            obj.ref_or_raise(expected_ref_int)

        self.assertEqual(str(context.exception), "Input must be of type basestring or dict")
