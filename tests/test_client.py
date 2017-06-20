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
import requests
import json


class TestAccessEntry(BaseObjectTest):
    __test__ = True

    def setUp(self):
        super(TestAccessEntry, self).setUp()
        self.obj_class = menandmice.client.AccessEntry
        self.add_key('name')
        self.add_key('access')


class TestIdentityAccess(BaseObjectTest):
    __test__ = True

    def setUp(self):
        super(TestIdentityAccess, self).setUp()
        self.obj_class = menandmice.client.IdentityAccess
        self.add_key('identityRef')
        self.add_key('identityName')
        self.add_key('accessEntries', [menandmice.client.AccessEntry()])


class TestObjectAccess(BaseObjectTest):
    __test__ = True

    def setUp(self):
        super(TestObjectAccess, self).setUp()
        self.obj_class = menandmice.client.ObjectAccess
        self.add_key('ref')
        self.add_key('name')
        self.add_key('identityAccess', [menandmice.client.IdentityAccess()])


class TestEvent(BaseObjectTest):
    __test__ = True

    def setUp(self):
        super(TestEvent, self).setUp()
        self.obj_class = menandmice.client.Event
        self.add_key('eventType')
        self.add_key('objType')
        self.add_key('objRef')
        self.add_key('objName')
        self.add_key('timestamp')
        self.add_key('username')
        self.add_key('saveComment')
        self.add_key('eventText')


class TestPropertyDefinition(BaseObjectTest):
    __test__ = True

    def setUp(self):
        super(TestPropertyDefinition, self).setUp()
        self.obj_class = menandmice.client.PropertyDefinition
        self.add_key('name')
        self.add_key('type')
        self.add_key('system')
        self.add_key('mandatory')
        self.add_key('readOnly')
        self.add_key('multiLine')
        self.add_key('defaultValue')
        self.add_key('listItems')
        self.add_key('parentProperty')


class TestClient(BaseTest):

    def test_init(self):
        self.assertEqual(self.client.baseurl, self.url_base)
        self.assertIsInstance(self.client.session, requests.Session)
        self.assertEqual(self.client.session.auth, (self.username, self.password))
        self.assertIsInstance(self.client.DNSZones, menandmice.dns.DNSZones)
        self.assertIsInstance(self.client.DNSRecords, menandmice.dns.DNSRecords)
        self.assertIsInstance(self.client.DNSViews, menandmice.dns.DNSViews)
        self.assertIsInstance(self.client.Folders, menandmice.ipam.Folders)
        self.assertIsInstance(self.client.Users, menandmice.users.Users)
        self.assertIsInstance(self.client.Groups, menandmice.users.Groups)
        self.assertIsInstance(self.client.Roles, menandmice.users.Roles)
        self.assertIsInstance(self.client.IPAMRecords, menandmice.ipam.IPAMRecords)
        self.assertIsInstance(self.client.Ranges, menandmice.ipam.Ranges)
        self.assertIsInstance(self.client.Interfaces, menandmice.ipam.Interfaces)
        self.assertIsInstance(self.client.Devices, menandmice.ipam.Devices)
        self.assertIsInstance(self.client.ChangeRequests, menandmice.ipam.ChangeRequests)

        self.assertEqual(self.client.DNSZones.client, self.client)
        self.assertEqual(self.client.DNSRecords.client, self.client)
        self.assertEqual(self.client.DNSViews.client, self.client)
        self.assertEqual(self.client.Folders.client, self.client)
        self.assertEqual(self.client.Users.client, self.client)
        self.assertEqual(self.client.Groups.client, self.client)
        self.assertEqual(self.client.Roles.client, self.client)
        self.assertEqual(self.client.IPAMRecords.client, self.client)
        self.assertEqual(self.client.Ranges.client, self.client)
        self.assertEqual(self.client.Interfaces.client, self.client)
        self.assertEqual(self.client.Devices.client, self.client)
        self.assertEqual(self.client.ChangeRequests.client, self.client)
        self.assertIsNotNone(self.client.logger)

    def test_new_dns_zone(self):
        dns_zone = self.client.new_dns_zone({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(dns_zone, menandmice.dns.DNSZone)
        self.assertEqual(dns_zone['ref'], 'test/123')
        self.assertEqual(dns_zone['name'], 'abc')

    def test_new_dns_record(self):
        dns_record = self.client.new_dns_record({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(dns_record, menandmice.dns.DNSRecord)
        self.assertEqual(dns_record['ref'], 'test/123')
        self.assertEqual(dns_record['name'], 'abc')

    def test_new_dns_view(self):
        dns_view = self.client.new_dns_view({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(dns_view, menandmice.dns.DNSView)
        self.assertEqual(dns_view['ref'], 'test/123')
        self.assertEqual(dns_view['name'], 'abc')

    def test_new_dns_generate_directive(self):
        dns_generate_directive = self.client.new_dns_generate_directive(
            {'ref': 'test/123'}, name='abc')
        self.assertIsInstance(dns_generate_directive, menandmice.dns.DNSGenerateDirective)
        self.assertEqual(dns_generate_directive['ref'], 'test/123')
        self.assertEqual(dns_generate_directive['name'], 'abc')

    def test_new_dns_zone_options(self):
        dns_zone_options = self.client.new_dns_zone_options({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(dns_zone_options, menandmice.dns.DNSZoneOptions)
        self.assertEqual(dns_zone_options['ref'], 'test/123')
        self.assertEqual(dns_zone_options['name'], 'abc')

    def test_new_folder(self):
        folder = self.client.new_folder({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(folder, menandmice.ipam.Folder)
        self.assertEqual(folder['ref'], 'test/123')
        self.assertEqual(folder['name'], 'abc')

    def test_new_object_access(self):
        new_object_access = self.client.new_object_access({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_object_access, menandmice.client.ObjectAccess)
        self.assertEqual(new_object_access['ref'], 'test/123')
        self.assertEqual(new_object_access['name'], 'abc')

    def test_new_identity_access(self):
        new_identity_access = self.client.new_identity_access({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_identity_access, menandmice.client.IdentityAccess)
        self.assertEqual(new_identity_access['ref'], 'test/123')
        self.assertEqual(new_identity_access['name'], 'abc')

    def test_new_access_entry(self):
        new_access_entry = self.client.new_access_entry({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_access_entry, menandmice.client.AccessEntry)
        self.assertEqual(new_access_entry['ref'], 'test/123')
        self.assertEqual(new_access_entry['name'], 'abc')

    def test_new_event(self):
        new_event = self.client.new_event({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_event, menandmice.client.Event)
        self.assertEqual(new_event['ref'], 'test/123')
        self.assertEqual(new_event['name'], 'abc')

    def test_new_property_definition(self):
        new_property_definition = self.client.new_property_definition(
            {'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_property_definition, menandmice.client.PropertyDefinition)
        self.assertEqual(new_property_definition['ref'], 'test/123')
        self.assertEqual(new_property_definition['name'], 'abc')

    def test_new_role(self):
        new_role = self.client.new_role({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_role, menandmice.users.Role)
        self.assertEqual(new_role['ref'], 'test/123')
        self.assertEqual(new_role['name'], 'abc')

    def test_new_group(self):
        new_group = self.client.new_group({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_group, menandmice.users.Group)
        self.assertEqual(new_group['ref'], 'test/123')
        self.assertEqual(new_group['name'], 'abc')

    def test_new_user(self):
        new_user = self.client.new_user({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_user, menandmice.users.User)
        self.assertEqual(new_user['ref'], 'test/123')
        self.assertEqual(new_user['name'], 'abc')

    def test_new_ipam_record(self):
        new_ipam_record = self.client.new_ipam_record({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_ipam_record, menandmice.ipam.IPAMRecord)
        self.assertEqual(new_ipam_record['ref'], 'test/123')
        self.assertEqual(new_ipam_record['name'], 'abc')

    def test_new_range(self):
        new_range = self.client.new_range({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_range, menandmice.ipam.Range)
        self.assertEqual(new_range['ref'], 'test/123')
        self.assertEqual(new_range['name'], 'abc')

    def test_new_discovery(self):
        new_discovery = self.client.new_discovery({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_discovery, menandmice.ipam.Discovery)
        self.assertEqual(new_discovery['ref'], 'test/123')
        self.assertEqual(new_discovery['name'], 'abc')

    def test_new_address_block(self):
        new_address_block = self.client.new_address_block({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_address_block, menandmice.ipam.AddressBlock)
        self.assertEqual(new_address_block['ref'], 'test/123')
        self.assertEqual(new_address_block['name'], 'abc')

    def test_new_range_statistics_response(self):
        new_range_statistics_response = self.client.new_range_statistics_response(
            {'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_range_statistics_response,
                              menandmice.ipam.GetRangeStatisticsResponse)
        self.assertEqual(new_range_statistics_response['ref'], 'test/123')
        self.assertEqual(new_range_statistics_response['name'], 'abc')

    def test_new_interface(self):
        new_interface = self.client.new_interface({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_interface, menandmice.ipam.Interface)
        self.assertEqual(new_interface['ref'], 'test/123')
        self.assertEqual(new_interface['name'], 'abc')

    def test_new_device(self):
        new_device = self.client.new_device({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_device, menandmice.ipam.Device)
        self.assertEqual(new_device['ref'], 'test/123')
        self.assertEqual(new_device['name'], 'abc')

    def test_new_change_request(self):
        new_change_request = self.client.new_change_request({'ref': 'test/123'}, name='abc')
        self.assertIsInstance(new_change_request, menandmice.ipam.ChangeRequest)
        self.assertEqual(new_change_request['ref'], 'test/123')
        self.assertEqual(new_change_request['name'], 'abc')

    def test_sanitize_list(self):
        test_list = [None, "abc", ""]
        expected = ["abc"]
        sanitized = self.client.sanitize_list(test_list)
        self.assertEqual(sanitized, expected)

    def test_sanitize_list_empty(self):
        test_list = []
        expected = []
        sanitized = self.client.sanitize_list(test_list)
        self.assertEqual(sanitized, expected)

    def test_sanitize_list_nested(self):
        test_list = [[None, "abc", ""],
                     {"test": None, "good": "ok"},
                     {},
                     "str"]
        expected = [["abc"],
                    {"good": "ok"},
                    "str"]
        sanitized = self.client.sanitize_list(test_list)
        self.assertEqual(sanitized, expected)

    def test_sanitize_dict(self):
        test_dict = {'none': None,
                     'str': 'x',
                     'empty_str': ''}
        expected = {'str': 'x'}
        sanitized = self.client.sanitize_dict(test_dict)
        self.assertEqual(sanitized, expected)

    def test_sanitize_dict_nested(self):
        test_dict = {'none': None,
                     'str': 'x',
                     'list': [None, "abc", ""],
                     'empty_list': [],
                     'dict': {'none': None,
                              'str': "a",
                              'empty_str': ''},
                     'empty_dict': {}}
        expected = {'str': 'x',
                    'list': ['abc'],
                    'dict': {'str': 'a'}}
        sanitized = self.client.sanitize_dict(test_dict)
        self.assertEqual(sanitized, expected)

    @patch('menandmice.client.requests.Session')
    def test_get_200(self, session):
        url = "http://test.server.local/mmws/api/fake"
        json_str = ('{"test_int":123, '
                    '"test_str":"str"}')
        json_obj = json.loads(json_str)

        session.get.return_value.status_code = 200
        session.get.return_value.json.return_value = json_obj
        self.client.session = session

        result = self.client.get(url)

        session.get.assert_called_with(url)
        self.assertEqual(result, json_obj)

    @patch('menandmice.client.requests.Session')
    def test_get_204(self, session):
        url = "http://test.server.local/mmws/api/fake"
        json_str = ('{"test_int":123, '
                    '"test_str":"str"}')
        json_obj = json.loads(json_str)

        session.get.return_value.status_code = 204
        session.get.return_value.json.return_value = json_obj
        self.client.session = session

        result = self.client.get(url)

        session.get.assert_called_with(url)
        self.assertEqual(result, "No data to display")

    @patch('menandmice.client.requests.Session')
    def test_get_error(self, session):
        url = "http://test.server.local/mmws/api/fake"
        json_str = ('{"error": { "code": 123, "message": "this is a test"} }')
        json_obj = json.loads(json_str)

        session.get.return_value.status_code = 400
        session.get.return_value.json.return_value = json_obj
        self.client.session = session

        with self.assertRaises(requests.exceptions.HTTPError) as context:
            self.client.get(url)

        session.get.assert_called_with(url)
        self.assertEqual(str(context.exception), '123: this is a test')

    @patch('menandmice.client.requests.Session')
    def test_get_error_raise_for_status(self, session):
        url = "http://test.server.local/mmws/api/fake"
        json_str = ('{ "junk": 123 }')
        json_obj = json.loads(json_str)

        session.get.return_value.status_code = 499
        session.get.return_value.json.return_value = json_obj
        session.get.return_value.raise_for_status.side_effect = StandardError()
        self.client.session = session

        with self.assertRaises(StandardError):
            self.client.get(url)

        session.get.assert_called_with(url)

    @patch('menandmice.client.requests.Session')
    def test_post_201(self, session):
        url = "http://test.server.local/mmws/api/fake"
        payload = {"input": "abc"}
        json_str = ('{ "junk": 123 }')
        json_obj = json.loads(json_str)

        session.post.return_value.status_code = 201
        session.post.return_value.json.return_value = json_obj
        self.client.session = session

        response = self.client.post(url, payload)

        session.post.assert_called_with(url, json=payload)
        self.assertEqual(response, json_obj)

    @patch('menandmice.client.requests.Session')
    def test_post_error(self, session):
        url = "http://test.server.local/mmws/api/fake"
        payload = {"input": "abc"}
        json_str = ('{"error": { "code": 123, "message": "this is a test"} }')
        json_obj = json.loads(json_str)

        session.post.return_value.status_code = 400
        session.post.return_value.json.return_value = json_obj
        self.client.session = session

        with self.assertRaises(requests.exceptions.HTTPError) as context:
            self.client.post(url, payload)

        session.post.assert_called_with(url, json=payload)
        self.assertEqual(str(context.exception), '123: this is a test')

    @patch('menandmice.client.requests.Session')
    def test_post_error_raise_for_status(self, session):
        url = "http://test.server.local/mmws/api/fake"
        payload = {"input": "abc"}
        json_str = ('{ "junk": 123 }')
        json_obj = json.loads(json_str)

        session.post.return_value.status_code = 499
        session.post.return_value.json.return_value = json_obj
        session.post.return_value.raise_for_status.side_effect = StandardError()
        self.client.session = session

        with self.assertRaises(StandardError):
            self.client.post(url, payload)

        session.post.assert_called_with(url, json=payload)

    @patch('menandmice.client.requests.Session')
    def test_delete_204(self, session):
        url = "http://test.server.local/mmws/api/fake"
        json_str = ('{"test_int":123, '
                    '"test_str":"str"}')
        json_obj = json.loads(json_str)

        session.delete.return_value.status_code = 204
        session.delete.return_value.json.return_value = json_obj
        self.client.session = session

        result = self.client.delete(url)

        session.delete.assert_called_with(url)
        self.assertEqual(result, "Successfully removed!")

    @patch('menandmice.client.requests.Session')
    def test_delete_error(self, session):
        url = "http://test.server.local/mmws/api/fake"
        json_str = ('{"error": { "code": 123, "message": "this is a test"} }')
        json_obj = json.loads(json_str)

        session.delete.return_value.status_code = 400
        session.delete.return_value.json.return_value = json_obj
        self.client.session = session

        with self.assertRaises(requests.exceptions.HTTPError) as context:
            self.client.delete(url)

        session.delete.assert_called_with(url)
        self.assertEqual(str(context.exception), '123: this is a test')

    @patch('menandmice.client.requests.Session')
    def test_delete_error_raise_for_status(self, session):
        url = "http://test.server.local/mmws/api/fake"
        json_str = ('{ "junk": 123 }')
        json_obj = json.loads(json_str)

        session.delete.return_value.status_code = 499
        session.delete.return_value.json.return_value = json_obj
        session.delete.return_value.raise_for_status.side_effect = StandardError()
        self.client.session = session

        with self.assertRaises(StandardError):
            self.client.delete(url)

        session.delete.assert_called_with(url)

    @patch('menandmice.client.requests.Session')
    def test_put_204(self, session):
        url = "http://test.server.local/mmws/api/fake"
        payload = {"input": "abc"}
        json_str = ('{ "junk": 123 }')
        json_obj = json.loads(json_str)

        session.put.return_value.status_code = 204
        session.put.return_value.json.return_value = json_obj
        self.client.session = session

        response = self.client.put(url, payload)

        session.put.assert_called_with(url, json=payload)
        self.assertEqual(response, "Successfully updated!")

    @patch('menandmice.client.requests.Session')
    def test_put_sanitize(self, session):
        url = "http://test.server.local/mmws/api/fake"
        payload = {"input": "abc"}
        json_str = ('{ "junk": 123, "empty_str": "", "empty_list": [], "empty_dict": {} }')
        json_obj = json.loads(json_str)

        session.put.return_value.status_code = 204
        session.put.return_value.json.return_value = json_obj
        self.client.session = session

        response = self.client.put(url, payload, sanitize_override=True)

        session.put.assert_called_with(url, json=payload)
        self.assertEqual(response, "Successfully updated!")

    @patch('menandmice.client.requests.Session')
    def test_put_sanitize_override(self, session):
        url = "http://test.server.local/mmws/api/fake"
        payload = {"input": "abc"}
        json_str = ('{ "junk": 123, "empty_str": "", "empty_list": [], "empty_dict": {} }')
        json_obj = json.loads(json_str)

        session.put.return_value.status_code = 204
        session.put.return_value.json.return_value = json_obj
        self.client.session = session

        response = self.client.put(url, payload, sanitize_override=True)

        session.put.assert_called_with(url, json=payload)
        self.assertEqual(response, "Successfully updated!")

    @patch('menandmice.client.requests.Session')
    def test_put_error(self, session):
        url = "http://test.server.local/mmws/api/fake"
        payload = {"input": "abc"}
        json_str = ('{"error": { "code": 123, "message": "this is a test"} }')
        json_obj = json.loads(json_str)

        session.put.return_value.status_code = 400
        session.put.return_value.json.return_value = json_obj
        self.client.session = session

        with self.assertRaises(requests.exceptions.HTTPError) as context:
            self.client.put(url, payload)

        session.put.assert_called_with(url, json=payload)
        self.assertEqual(str(context.exception), '123: this is a test')

    @patch('menandmice.client.requests.Session')
    def test_put_error_raise_for_status(self, session):
        url = "http://test.server.local/mmws/api/fake"
        payload = {"input": "abc"}
        json_str = ('{ "junk": 123 }')
        json_obj = json.loads(json_str)

        session.put.return_value.status_code = 499
        session.put.return_value.json.return_value = json_obj
        session.put.return_value.raise_for_status.side_effect = StandardError()
        self.client.session = session

        with self.assertRaises(StandardError):
            self.client.put(url, payload)

        session.put.assert_called_with(url, json=payload)

    @patch('menandmice.client.Client.make_query_str')
    @patch('menandmice.client.Client.delete')
    def test_delete_item(self, mock_delete, mock_make_query_str):
        base_url = self.url_base
        json_str = ('{ "junk": 123 }')
        json_obj = json.loads(json_str)
        query_str = "&mock_query_str=xxx"
        ref = "DNSZones/123"
        kwargs = {"arg_str": "test",
                  "arg_list": ["test"],
                  "arg_dict": {"sub_key": 123}}

        mock_delete.return_value = json_obj
        mock_make_query_str.return_value = query_str

        response = self.client.delete_item(ref, **kwargs)

        expected_url = "{0}{1}{2}".format(base_url, ref, query_str)
        mock_make_query_str.assert_called_with(**kwargs)
        mock_delete.assert_called_with(expected_url)
        self.assertEqual(response, json_obj)

    @patch('menandmice.client.Client.put')
    def test_update_item(self, mock_put):
        base_url = self.url_base
        json_str = ('{ "junk": 123 }')
        json_obj = json.loads(json_str)
        ref = "DNSZones/123"
        properties = "123"
        obj_type = "TestType"
        save_comment = "Encore's update"
        delete_unspecified = False
        expected_payload = {
            "ref": ref,
            "objType": obj_type,
            "saveComment": save_comment,
            "deleteUnspecified": delete_unspecified,
            "properties": [properties]  # checks to ensure list is created
        }

        mock_put.return_value = json_obj

        response = self.client.update_item(ref,
                                           properties,
                                           obj_type,
                                           save_comment,
                                           delete_unspecified)

        expected_url = "{0}{1}".format(base_url, ref)
        mock_put.assert_called_with(expected_url, expected_payload)
        self.assertEqual(response, json_obj)

    @patch('menandmice.client.Client.make_query_str')
    @patch('menandmice.client.Client.get')
    def test_get_item_access(self, mock_get, mock_make_query_str):
        base_url = self.url_base
        json_str = ('{ "result": { "objectAccess": { "ref": "xxx", "name": "test" } } }')
        json_obj = json.loads(json_str)
        query_str = "&mock_query_str=xxx"
        ref = "DNSZones/123"
        kwargs = {"arg_str": "test",
                  "arg_list": ["test"],
                  "arg_dict": {"sub_key": 123}}

        mock_get.return_value = json_obj
        mock_make_query_str.return_value = query_str

        response = self.client.get_item_access(ref, **kwargs)

        expected_url = "{0}{1}/Access{2}".format(base_url, ref, query_str)
        expected_resp = menandmice.client.ObjectAccess(json_obj['result']['objectAccess'])
        mock_make_query_str.assert_called_with(**kwargs)
        mock_get.assert_called_with(expected_url)
        self.assertEqual(response, expected_resp)

    @patch('menandmice.client.Client.put')
    def test_set_item_access(self, mock_put):
        base_url = self.url_base
        json_str = ('{ "junk": 123 }')
        json_obj = json.loads(json_str)
        ref = "DNSZones/123"
        obj_type = "TestType"
        save_comment = "Encore's update"
        identity_access = "test123"
        expected_payload = {
            "objType": obj_type,
            "saveComment": save_comment,
            "identityAccess": [identity_access]  # checks to ensure list is created
        }

        mock_put.return_value = json_obj

        response = self.client.set_item_access(ref,
                                               identity_access,
                                               obj_type,
                                               save_comment)

        expected_url = "{0}{1}/Access".format(base_url, ref)
        mock_put.assert_called_with(expected_url, expected_payload)
        self.assertEqual(response, json_obj)

    @patch('menandmice.client.Client.make_query_str')
    @patch('menandmice.client.Client.get')
    def test_get_item_history(self, mock_get, mock_make_query_str):
        base_url = self.url_base
        json_str = ('{ "result": { "events": [{ "ref": "xxx", "name": "test" },'
                    ' { "ref": "abc", "name": 123 }] } }')
        json_obj = json.loads(json_str)
        query_str = "&mock_query_str=xxx"
        ref = "DNSZones/123"
        kwargs = {"arg_str": "test"}

        mock_get.return_value = json_obj
        mock_make_query_str.return_value = query_str

        response = self.client.get_item_history(ref, **kwargs)

        expected_url = "{0}{1}/History{2}".format(base_url, ref, query_str)
        expected_resp = [menandmice.client.Event(e) for e in json_obj['result']['events']]
        mock_make_query_str.assert_called_with(**kwargs)
        mock_get.assert_called_with(expected_url)
        self.assertEqual(response, expected_resp)

    @patch('menandmice.client.Client.get')
    def test_get_property_definitions(self, mock_get):
        base_url = self.url_base
        json_str = ('{ "result": { "propertyDefinitions": [{ "ref": "xxx", "name": "test" },'
                    ' { "ref": "abc", "name": 123 }] } }')
        json_obj = json.loads(json_str)
        ref = "DNSZones/123"
        property_name = ""

        mock_get.return_value = json_obj

        response = self.client.get_property_definitions(ref, property_name)

        expected_url = "{0}{1}/PropertyDefinitions".format(base_url, ref)
        prop_defs = json_obj['result']['propertyDefinitions']
        expected_resp = [menandmice.client.PropertyDefinition(e) for e in prop_defs]
        mock_get.assert_called_with(expected_url)
        self.assertEqual(response, expected_resp)

    @patch('menandmice.client.Client.get')
    def test_get_property_definitions_named(self, mock_get):
        base_url = self.url_base
        json_str = ('{ "result": { "propertyDefinitions": [{ "ref": "xxx", "name": "test" },'
                    ' { "ref": "abc", "name": 123 }] } }')
        json_obj = json.loads(json_str)
        ref = "DNSZones/123"
        property_name = "prop_name"

        mock_get.return_value = json_obj

        response = self.client.get_property_definitions(ref, property_name)

        expected_url = "{0}{1}/PropertyDefinitions/{2}".format(base_url, ref, property_name)
        prop_defs = json_obj['result']['propertyDefinitions']
        expected_resp = [menandmice.client.PropertyDefinition(e) for e in prop_defs]
        mock_get.assert_called_with(expected_url)
        self.assertEqual(response, expected_resp)

    @patch('menandmice.client.Client.post')
    def test_add_property_definition(self, mock_post):
        base_url = self.url_base
        json_str = ('{ "result": 123 }')
        json_obj = json.loads(json_str)
        ref = "DNSZones/123"
        property_definition = "prop_def"
        save_comment = "Encore comment"
        expected_payload = {
            'saveComment': save_comment,
            'propertyDefinition': property_definition
        }

        mock_post.return_value = json_obj

        response = self.client.add_property_definition(ref,
                                                       property_definition,
                                                       save_comment)

        expected_url = "{0}{1}/PropertyDefinitions".format(base_url, ref)
        mock_post.assert_called_with(expected_url, expected_payload)
        self.assertEqual(response, json_obj)

    @patch('menandmice.client.Client.put')
    def test_update_property_definition(self, mock_put):
        base_url = self.url_base
        json_str = ('{ "result": 123 }')
        json_obj = json.loads(json_str)

        ref = "DNSZones/123"
        property_name = "prop_name"
        property_definition = "prop_def"
        update_existing = True
        save_comment = "Encore comment"
        expected_payload = {
            'updateExisting': update_existing,
            'saveComment': save_comment,
            'propertyDefinition': property_definition
        }

        mock_put.return_value = json_obj

        response = self.client.update_property_definition(ref,
                                                          property_name,
                                                          property_definition,
                                                          update_existing,
                                                          save_comment)

        expected_url = "{0}{1}/PropertyDefinitions/{2}".format(base_url,
                                                               ref,
                                                               property_name)
        mock_put.assert_called_with(expected_url, expected_payload)
        self.assertEqual(response, json_obj)

    @patch('menandmice.client.Client.delete')
    def test_delete_property_definition(self, mock_delete):
        base_url = self.url_base
        json_str = ('{ "result": 123 }')
        json_obj = json.loads(json_str)

        ref = "DNSZones/123"
        property_name = "prop_name"
        save_comment = "Encore comment"
        query_string = "?saveComment=Encore+comment"

        mock_delete.return_value = json_obj

        response = self.client.delete_property_definition(ref,
                                                          property_name,
                                                          save_comment)

        expected_url = "{0}{1}/PropertyDefinitions/{2}{3}".format(base_url,
                                                                  ref,
                                                                  property_name,
                                                                  query_string)
        mock_delete.assert_called_with(expected_url)
        self.assertEqual(response, json_obj)

    @patch('menandmice.client.Client.delete')
    def test_delete_property_definition_no_comment(self, mock_delete):
        base_url = self.url_base
        json_str = ('{ "result": 123 }')
        json_obj = json.loads(json_str)
        ref = "DNSZones/123"
        property_name = "prop_name"

        mock_delete.return_value = json_obj

        response = self.client.delete_property_definition(ref,
                                                          property_name,
                                                          "")

        expected_url = "{0}{1}/PropertyDefinitions/{2}".format(base_url,
                                                               ref,
                                                               property_name)
        mock_delete.assert_called_with(expected_url)
        self.assertEqual(response, json_obj)
