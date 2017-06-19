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
from mock import patch

import menandmice
import requests
# import pprint
import json


class TestClient(BaseTest):

    def test_init(self):
        self.assertEqual(self.client.baseurl,
                         "http://{0}/mmws/api/".format(self.server))
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
