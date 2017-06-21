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

from base_test import BaseObjectTest
from base_test import BaseTest
from mock import call
from mock import Mock
from mock import patch

import menandmice

from menandmice.users import Group
from menandmice.users import Groups
from menandmice.users import Role
from menandmice.users import Roles
from menandmice.users import User
from menandmice.users import Users


class TestRole(BaseObjectTest):
    __test__ = True

    def setUp(self):
        super(TestRole, self).setUp()
        self.obj_class = menandmice.client.Role
        self.add_key('ref')
        self.add_key('name')
        self.add_key('description')
        self.add_key('users', [])  # list of User()
        self.add_key('groups', [])  # list of Group()


class TestUser(BaseObjectTest):
    __test__ = True

    def setUp(self):
        super(TestUser, self).setUp()
        self.obj_class = menandmice.client.User
        self.add_key('ref')
        self.add_key('name')
        self.add_key('password')
        self.add_key('fullName')
        self.add_key('description')
        self.add_key('email')
        self.add_key('authenticationType')
        self.add_key('roles', [])  # list of Role()
        self.add_key('groups', [])  # list of Group()


class TestGroup(BaseObjectTest):
    __test__ = True

    def setUp(self):
        super(TestGroup, self).setUp()
        self.obj_class = menandmice.client.Group
        self.add_key('ref')
        self.add_key('name')
        self.add_key('description')
        self.add_key('adIntegrated')
        self.add_key('groupMembers', [])   # list of User()
        self.add_key('roles', [])   # list of Role()


class TestGroups(BaseTest):

    def test_init(self):
        expected_client = "Test Client"
        expected_url_base = "Groups"
        expected_entity_class = menandmice.client.Group
        expected_get_response_entity_key = "group"
        expected_get_response_all_key = "groups"
        expected_get_is_singular = False
        expected_ref_key = "ref"
        obj = Groups(client=expected_client)

        self.assertIsInstance(obj, dict)
        self.assertIsInstance(obj, menandmice.base.BaseObject)
        self.assertIsInstance(obj, menandmice.base.BaseService)
        self.assertEqual(obj.client, expected_client)
        self.assertEqual(obj.url_base, expected_url_base)
        self.assertEqual(obj.entity_class, expected_entity_class)
        self.assertEqual(obj.get_response_entity_key, expected_get_response_entity_key)
        self.assertEqual(obj.get_response_all_key, expected_get_response_all_key)
        self.assertEqual(obj.get_is_singular, expected_get_is_singular)
        self.assertEqual(obj.ref_key, expected_ref_key)

    @patch("menandmice.users.Groups.get")
    def test_add(self, mock_get):
        expected_group = "test group"
        expected_save_comment = ""
        expected_payload = {
            "saveComment": expected_save_comment,
            "group": expected_group
        }

        expected_get_refs = ["ref1", "ref2", "ref3"]
        expected_get_calls = [call(c) for c in expected_get_refs]
        expected_results = ["get_" + ref for ref in expected_get_refs]
        expected_base_url = self.url_base
        expected_url_base = "Groups"

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.post.return_value = {'result': {'objRefs': expected_get_refs}}
        mock_get.side_effect = [[result] for result in expected_results]

        obj = Groups(client=mock_client)
        results = obj.add(expected_group)

        mock_client.post.assert_called_with("{0}{1}".format(expected_base_url,
                                                            expected_url_base),
                                            expected_payload)
        mock_get.assert_has_calls(expected_get_calls)
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Groups.make_query_str")
    @patch("menandmice.users.Groups.ref_or_raise")
    def test_get_group_roles(self, mock_ref_or_raise, mock_make_query_str):
        expected_group = "test group"
        expected_roles = [{"ref": "ref1", "name": "name1"},
                          {"ref": "ref2", "name": "name2"},
                          {"ref": "ref3", "name": "name3"}, ]
        expected_results = [Role(role) for role in expected_roles]
        expected_base_url = self.url_base
        expected_kwargs = {"test": "value", "int": 123}
        expected_group_ref = "Groups/123"
        expected_query_str = "?query=xyz"

        mock_ref_or_raise.return_value = expected_group_ref
        mock_make_query_str.return_value = expected_query_str

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.get.return_value = {'result': {'roles': expected_roles}}

        obj = Groups(client=mock_client)
        results = obj.get_group_roles(expected_group, **expected_kwargs)

        mock_client.get.assert_called_with("{0}{1}/Roles{2}".format(expected_base_url,
                                                                    expected_group_ref,
                                                                    expected_query_str))
        mock_make_query_str.assert_called_with(**expected_kwargs)
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Groups.make_query_str")
    @patch("menandmice.users.Groups.ref_or_raise")
    def test_delete_group_role(self, mock_ref_or_raise, mock_make_query_str):
        expected_group = "test group"
        expected_role = "test role"

        expected_group_ref = "Groups/123"
        expected_role_ref = "Roles/123"

        expected_results = "test"
        expected_base_url = self.url_base
        expected_save_comment = "save_comment"
        expected_query_str = "?saveComment=test"

        mock_ref_or_raise.side_effect = [expected_group_ref, expected_role_ref]
        mock_make_query_str.return_value = expected_query_str

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.delete.return_value = expected_results

        obj = Groups(client=mock_client)
        results = obj.delete_group_role(expected_group,
                                        expected_role,
                                        expected_save_comment)

        mock_client.delete.assert_called_with("{0}{1}/{2}{3}".format(expected_base_url,
                                                                     expected_group_ref,
                                                                     expected_role_ref,
                                                                     expected_query_str))
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Groups.ref_or_raise")
    def test_add_group_role(self, mock_ref_or_raise):
        expected_group = "test group"
        expected_role = "test role"

        expected_group_ref = "Groups/123"
        expected_role_ref = "Roles/123"

        expected_results = "test"
        expected_base_url = self.url_base
        expected_save_comment = "save_comment"
        expected_payload = {"saveComment": expected_save_comment}

        mock_ref_or_raise.side_effect = [expected_group_ref, expected_role_ref]

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.put.return_value = expected_results

        obj = Groups(client=mock_client)
        results = obj.add_group_role(expected_group,
                                     expected_role,
                                     expected_save_comment)

        mock_client.put.assert_called_with("{0}{1}/{2}".format(expected_base_url,
                                                               expected_group_ref,
                                                               expected_role_ref),
                                           expected_payload,
                                           True)
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Groups.make_query_str")
    @patch("menandmice.users.Groups.ref_or_raise")
    def test_get_group_users(self, mock_ref_or_raise, mock_make_query_str):
        expected_group = "test group"
        expected_users = [{"ref": "ref1", "name": "name1"},
                          {"ref": "ref2", "name": "name2"},
                          {"ref": "ref3", "name": "name3"}, ]
        expected_results = [User(user) for user in expected_users]
        expected_base_url = self.url_base
        expected_kwargs = {"test": "value", "int": 123}
        expected_group_ref = "Groups/123"
        expected_query_str = "?query=xyz"

        mock_ref_or_raise.return_value = expected_group_ref
        mock_make_query_str.return_value = expected_query_str

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.get.return_value = {'result': {'users': expected_users}}

        obj = Groups(client=mock_client)
        results = obj.get_group_users(expected_group, **expected_kwargs)

        mock_client.get.assert_called_with("{0}{1}/Users{2}".format(expected_base_url,
                                                                    expected_group_ref,
                                                                    expected_query_str))
        mock_make_query_str.assert_called_with(**expected_kwargs)
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Groups.make_query_str")
    @patch("menandmice.users.Groups.ref_or_raise")
    def test_delete_group_user(self, mock_ref_or_raise, mock_make_query_str):
        expected_group = "test group"
        expected_user = "test user"

        expected_group_ref = "Groups/123"
        expected_user_ref = "Users/123"

        expected_results = "test"
        expected_base_url = self.url_base
        expected_save_comment = "save_comment"
        expected_query_str = "?saveComment=test"

        mock_ref_or_raise.side_effect = [expected_group_ref, expected_user_ref]
        mock_make_query_str.return_value = expected_query_str

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.delete.return_value = expected_results

        obj = Groups(client=mock_client)
        results = obj.delete_group_user(expected_group,
                                        expected_user,
                                        expected_save_comment)

        mock_client.delete.assert_called_with("{0}{1}/{2}{3}".format(expected_base_url,
                                                                     expected_group_ref,
                                                                     expected_user_ref,
                                                                     expected_query_str))
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Groups.ref_or_raise")
    def test_add_group_user(self, mock_ref_or_raise):
        expected_group = "test group"
        expected_user = "test user"

        expected_group_ref = "Groups/123"
        expected_user_ref = "Users/123"

        expected_results = "test"
        expected_base_url = self.url_base
        expected_save_comment = "save_comment"
        expected_payload = {"saveComment": expected_save_comment}

        mock_ref_or_raise.side_effect = [expected_group_ref, expected_user_ref]

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.put.return_value = expected_results

        obj = Groups(client=mock_client)
        results = obj.add_group_user(expected_group,
                                     expected_user,
                                     expected_save_comment)

        mock_client.put.assert_called_with("{0}{1}/{2}".format(expected_base_url,
                                                               expected_group_ref,
                                                               expected_user_ref),
                                           expected_payload,
                                           True)
        self.assertEquals(results, expected_results)


class TestRoles(BaseTest):

    def test_init(self):
        expected_client = "Test Client"
        expected_url_base = "Roles"
        expected_entity_class = menandmice.client.Role
        expected_get_response_entity_key = "role"
        expected_get_response_all_key = "roles"
        expected_get_is_singular = False
        expected_ref_key = "ref"
        obj = Roles(client=expected_client)

        self.assertIsInstance(obj, dict)
        self.assertIsInstance(obj, menandmice.base.BaseObject)
        self.assertIsInstance(obj, menandmice.base.BaseService)
        self.assertEqual(obj.client, expected_client)
        self.assertEqual(obj.url_base, expected_url_base)
        self.assertEqual(obj.entity_class, expected_entity_class)
        self.assertEqual(obj.get_response_entity_key, expected_get_response_entity_key)
        self.assertEqual(obj.get_response_all_key, expected_get_response_all_key)
        self.assertEqual(obj.get_is_singular, expected_get_is_singular)
        self.assertEqual(obj.ref_key, expected_ref_key)

    @patch("menandmice.users.Roles.get")
    def test_add(self, mock_get):
        expected_role = "test role"
        expected_save_comment = ""
        expected_payload = {
            "saveComment": expected_save_comment,
            "role": expected_role
        }

        expected_get_refs = ["ref1", "ref2", "ref3"]
        expected_get_calls = [call(c) for c in expected_get_refs]
        expected_results = ["get_" + ref for ref in expected_get_refs]
        expected_base_url = self.url_base
        expected_url_base = "Roles"

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.post.return_value = {'result': {'objRefs': expected_get_refs}}
        mock_get.side_effect = [[result] for result in expected_results]

        obj = Roles(client=mock_client)
        results = obj.add(expected_role)

        mock_client.post.assert_called_with("{0}{1}".format(expected_base_url,
                                                            expected_url_base),
                                            expected_payload)
        mock_get.assert_has_calls(expected_get_calls)
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Roles.make_query_str")
    @patch("menandmice.users.Roles.ref_or_raise")
    def test_get_role_users(self, mock_ref_or_raise, mock_make_query_str):
        expected_role = "test role"
        expected_users = [{"ref": "ref1", "name": "name1"},
                          {"ref": "ref2", "name": "name2"},
                          {"ref": "ref3", "name": "name3"}]
        expected_results = [User(user) for user in expected_users]
        expected_base_url = self.url_base
        expected_kwargs = {"test": "value", "int": 123}
        expected_role_ref = "Roles/123"
        expected_query_str = "?query=xyz"

        mock_ref_or_raise.return_value = expected_role_ref
        mock_make_query_str.return_value = expected_query_str

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.get.return_value = {'result': {'users': expected_users}}

        obj = Roles(client=mock_client)
        results = obj.get_role_users(expected_role, **expected_kwargs)

        mock_client.get.assert_called_with("{0}{1}/Users{2}".format(expected_base_url,
                                                                    expected_role_ref,
                                                                    expected_query_str))
        mock_make_query_str.assert_called_with(**expected_kwargs)
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Roles.make_query_str")
    @patch("menandmice.users.Roles.ref_or_raise")
    def test_get_role_groups(self, mock_ref_or_raise, mock_make_query_str):
        expected_role = "test role"
        expected_groups = [{"ref": "ref1", "name": "name1"},
                           {"ref": "ref2", "name": "name2"},
                           {"ref": "ref3", "name": "name3"}]
        expected_results = [Group(group) for group in expected_groups]
        expected_base_url = self.url_base
        expected_kwargs = {"test": "value", "int": 123}
        expected_role_ref = "Roles/123"
        expected_query_str = "?query=xyz"

        mock_ref_or_raise.return_value = expected_role_ref
        mock_make_query_str.return_value = expected_query_str

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.get.return_value = {'result': {'groups': expected_groups}}

        obj = Roles(client=mock_client)
        results = obj.get_role_groups(expected_role, **expected_kwargs)

        mock_client.get.assert_called_with("{0}{1}/Groups{2}".format(expected_base_url,
                                                                     expected_role_ref,
                                                                     expected_query_str))
        mock_make_query_str.assert_called_with(**expected_kwargs)
        self.assertEquals(results, expected_results)


class TestUsers(BaseTest):

    def test_init(self):
        expected_client = "Test Client"
        expected_url_base = "Users"
        expected_entity_class = menandmice.client.User
        expected_get_response_entity_key = "user"
        expected_get_response_all_key = "users"
        expected_get_is_singular = False
        expected_ref_key = "ref"
        obj = Users(client=expected_client)

        self.assertIsInstance(obj, dict)
        self.assertIsInstance(obj, menandmice.base.BaseObject)
        self.assertIsInstance(obj, menandmice.base.BaseService)
        self.assertEqual(obj.client, expected_client)
        self.assertEqual(obj.url_base, expected_url_base)
        self.assertEqual(obj.entity_class, expected_entity_class)
        self.assertEqual(obj.get_response_entity_key, expected_get_response_entity_key)
        self.assertEqual(obj.get_response_all_key, expected_get_response_all_key)
        self.assertEqual(obj.get_is_singular, expected_get_is_singular)
        self.assertEqual(obj.ref_key, expected_ref_key)

    @patch("menandmice.users.Users.get")
    def test_add(self, mock_get):
        expected_user = "test user"
        expected_save_comment = ""
        expected_payload = {
            "saveComment": expected_save_comment,
            "user": expected_user
        }

        expected_get_refs = ["ref1", "ref2", "ref3"]
        expected_get_calls = [call(c) for c in expected_get_refs]
        expected_results = ["get_" + ref for ref in expected_get_refs]
        expected_base_url = self.url_base
        expected_url_base = "Users"

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.post.return_value = {'result': {'objRefs': expected_get_refs}}
        mock_get.side_effect = [[result] for result in expected_results]

        obj = Users(client=mock_client)
        results = obj.add(expected_user)

        mock_client.post.assert_called_with("{0}{1}".format(expected_base_url,
                                                            expected_url_base),
                                            expected_payload)
        mock_get.assert_has_calls(expected_get_calls)
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Users.make_query_str")
    @patch("menandmice.users.Users.ref_or_raise")
    def test_get_user_groups(self, mock_ref_or_raise, mock_make_query_str):
        expected_user = "test user"
        expected_groups = [{"ref": "ref1", "name": "name1"},
                           {"ref": "ref2", "name": "name2"},
                           {"ref": "ref3", "name": "name3"}]
        expected_results = [Group(group) for group in expected_groups]
        expected_base_url = self.url_base
        expected_kwargs = {"test": "value", "int": 123}
        expected_user_ref = "Users/123"
        expected_query_str = "?query=xyz"

        mock_ref_or_raise.return_value = expected_user_ref
        mock_make_query_str.return_value = expected_query_str

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.get.return_value = {'result': {'groups': expected_groups}}

        obj = Users(client=mock_client)
        results = obj.get_user_groups(expected_user, **expected_kwargs)

        mock_client.get.assert_called_with("{0}{1}/Groups{2}".format(expected_base_url,
                                                                     expected_user_ref,
                                                                     expected_query_str))
        mock_make_query_str.assert_called_with(**expected_kwargs)
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Users.make_query_str")
    @patch("menandmice.users.Users.ref_or_raise")
    def test_get_user_roles(self, mock_ref_or_raise, mock_make_query_str):
        expected_user = "test user"
        expected_roles = [{"ref": "ref1", "name": "name1"},
                          {"ref": "ref2", "name": "name2"},
                          {"ref": "ref3", "name": "name3"}]
        expected_results = [Role(role) for role in expected_roles]
        expected_base_url = self.url_base
        expected_kwargs = {"test": "value", "int": 123}
        expected_user_ref = "Users/123"
        expected_query_str = "?query=xyz"

        mock_ref_or_raise.return_value = expected_user_ref
        mock_make_query_str.return_value = expected_query_str

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.get.return_value = {'result': {'roles': expected_roles}}

        obj = Users(client=mock_client)
        results = obj.get_user_roles(expected_user, **expected_kwargs)

        mock_client.get.assert_called_with("{0}{1}/Roles{2}".format(expected_base_url,
                                                                    expected_user_ref,
                                                                    expected_query_str))
        mock_make_query_str.assert_called_with(**expected_kwargs)
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Users.make_query_str")
    @patch("menandmice.users.Users.ref_or_raise")
    def test_delete_user_role(self, mock_ref_or_raise, mock_make_query_str):
        expected_user = "test user"
        expected_role = "test role"

        expected_user_ref = "Users/123"
        expected_role_ref = "Roles/123"

        expected_results = "test"
        expected_base_url = self.url_base
        expected_save_comment = "save_comment"
        expected_query_str = "?saveComment=test"

        mock_ref_or_raise.side_effect = [expected_user_ref, expected_role_ref]
        mock_make_query_str.return_value = expected_query_str

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.delete.return_value = expected_results

        obj = Users(client=mock_client)
        results = obj.delete_user_role(expected_user,
                                       expected_role,
                                       expected_save_comment)

        mock_client.delete.assert_called_with("{0}{1}/{2}{3}".format(expected_base_url,
                                                                     expected_user_ref,
                                                                     expected_role_ref,
                                                                     expected_query_str))
        self.assertEquals(results, expected_results)

    @patch("menandmice.users.Users.ref_or_raise")
    def test_add_user_role(self, mock_ref_or_raise):
        expected_user = "test user"
        expected_role = "test role"

        expected_user_ref = "Users/123"
        expected_role_ref = "Roles/123"

        expected_results = "test"
        expected_base_url = self.url_base
        expected_save_comment = "save_comment"
        expected_payload = {"saveComment": expected_save_comment}

        mock_ref_or_raise.side_effect = [expected_user_ref, expected_role_ref]

        mock_client = Mock()
        mock_client.baseurl = expected_base_url
        mock_client.put.return_value = expected_results

        obj = Users(client=mock_client)
        results = obj.add_user_role(expected_user,
                                    expected_role,
                                    expected_save_comment)

        mock_client.put.assert_called_with("{0}{1}/{2}".format(expected_base_url,
                                                               expected_user_ref,
                                                               expected_role_ref),
                                           expected_payload,
                                           True)
        self.assertEquals(results, expected_results)
