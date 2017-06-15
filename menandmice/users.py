import json

from menandmice.base import BaseObject
from menandmice.base import BaseService


class Role(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.name = self.get_value('name', kwargs)
        self.description = self.get_value('description', kwargs)
        self.users = self.build_obj_list(Group, self.get_value('users', kwargs))
        self.groups = self.build_obj_list(User, self.get_value('groups', kwargs))


class User(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.name = self.get_value('name', kwargs)
        self.password = self.get_value('password', kwargs)
        self.fullName = self.get_value('fullName', kwargs)
        self.description = self.get_value('description', kwargs)
        self.email = self.get_value('email', kwargs)
        self.authenticationType = self.get_value('authenticationType', kwargs)
        self.roles = self.build_obj_list(Role, self.get_value('roles', kwargs))
        self.groups = self.build_obj_list(Group, self.get_value('groups', kwargs))


class Group(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.name = self.get_value('name', kwargs)
        self.description = self.get_value('description', kwargs)
        self.adIntegrated = self.get_value('adIntegrated', kwargs)
        self.groupMembers = self.build_obj_list(User, self.get_value('groupMembers', kwargs))
        self.roles = self.build_obj_list(Role, self.get_value('roles', kwargs))


class Groups(BaseService):
    def __init__(self, client):
        super(Groups, self).__init__(client=client,
                                     url_base="Groups",
                                     entity_class=Group,
                                     get_response_entity_key="group",
                                     get_response_all_key="groups")

    def add(self, group_input, saveComment=""):
        if isinstance(group_input, Group):
            group_input = json.loads(group_input.to_json())
        payload = {
            "saveComment": saveComment,
            "group": group_input
        }
        group_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                      self.url_base),
                                      payload)
        group_return = []
        for ref in group_json['result']['objRefs']:
            group_return.append(self.get(ref)[0])
        return group_return

    def getGroupRoles(self, group_ref, **kwargs):
        all_roles = []
        query_string = ""
        if kwargs:
            for key, value in kwargs.items():
                if not query_string:
                    query_string += "?{0}={1}".format(key, value)
                else:
                    query_string += "&{0}={1}".format(key, value)
        role_response = self.client.get(
            "{0}{1}/Roles{2}".format(self.client.baseurl, group_ref, query_string))
        for role in role_response['result']['roles']:
            all_roles.append(Roles(self.client).build(role))
        return all_roles

    def deleteGroupRole(self, group_ref, role_ref, saveComment=""):
        if saveComment:
            saveComment = "?{0}".format(saveComment)
        return self.client.delete("{0}{1}/{2}{3}".format(self.client.baseurl,
                                                         group_ref,
                                                         role_ref,
                                                         saveComment))

    def addGroupRole(self, group_ref, role_ref, saveComment=""):
        payload = {
            "saveComment": saveComment
        }
        return self.client.put("{0}{1}/{2}".format(self.client.baseurl,
                                                   group_ref,
                                                   role_ref),
                               payload,
                               True)

    def getUserRoles(self, group_ref, **kwargs):
        all_users = []
        query_string = ""
        if kwargs:
            for key, value in kwargs.items():
                if not query_string:
                    query_string += "?{0}={1}".format(key, value)
                else:
                    query_string += "&{0}={1}".format(key, value)
        role_response = self.client.get(
            "{0}{1}/Users{2}".format(self.client.baseurl, group_ref, query_string))
        for user in role_response['result']['users']:
            all_users.append(User(self.client).build(user))
        return all_users

    def deleteUserRole(self, group_ref, user_ref, saveComment=""):
        if saveComment:
            saveComment = "?{0}".format(saveComment)
        return self.client.delete("{0}{1}/{2}{3}".format(self.client.baseurl,
                                                         group_ref,
                                                         user_ref,
                                                         saveComment))

    def addUserRole(self, group_ref, user_ref, saveComment=""):
        payload = {
            "saveComment": saveComment
        }
        return self.client.put("{0}{1}/{2}".format(self.client.baseurl,
                                                   group_ref,
                                                   user_ref),
                               payload,
                               True)


class Roles(BaseService):
    def __init__(self, client):
        super(Roles, self).__init__(client=client,
                                    url_base="Roles",
                                    entity_class=Role,
                                    get_response_entity_key="role",
                                    get_response_all_key="roles")

    def add(self, role_input, saveComment=""):
        if isinstance(role_input, Role):
            role_input = json.loads(role_input.to_json())
        payload = {
            "saveComment": saveComment,
            "role": role_input
        }
        role_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
        role_return = []
        for ref in role_json['result']['objRefs']:
            role_return.append(self.get(ref)[0])
        return role_return

    def getRoleGroups(self, role_ref, **kwargs):
        all_groups = []
        query_string = self.make_query_str(**kwargs)
        group_response = self.client.get(
            "{0}{1}/Groups{2}".format(self.client.baseurl, role_ref, query_string))
        for group in group_response['result']['groups']:
            all_groups.append(Group(self.client).build(group))
        return all_groups

    def getRoleUsers(self, role_ref, **kwargs):
        all_users = []
        query_string = self.make_query_str(**kwargs)
        user_response = self.client.get(
            "{0}{1}/Users{2}".format(self.client.baseurl, role_ref, query_string))
        for user in user_response['result']['users']:
            all_users.append(User(self.client).build(user))
        return all_users


class Users(BaseService):
    def __init__(self, client):
        super(Users, self).__init__(client=client,
                                    url_base="Users",
                                    entity_class=User,
                                    get_response_entity_key="user",
                                    get_response_all_key="users")

    def add(self, user_input, saveComment=""):
        if isinstance(user_input, User):
            user_input = json.loads(user_input.to_json())
        payload = {
            "saveComment": saveComment,
            "user": user_input
        }
        user_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
        user_return = []
        for ref in user_json['result']['objRefs']:
            user_return.append(self.get(ref)[0])
        return user_return

    def getUsersGroups(self, user_ref, **kwargs):
        all_groups = []
        query_string = self.make_query_str(**kwargs)
        group_response = self.client.get("{0}{1}{2}".format(
            self.client.baseurl, user_ref, query_string))
        for group in group_response['result']['groups']:
            all_groups.append(Groups(self.client).build(group))
        return all_groups

    def getUserRoles(self, user_ref, **kwargs):
        all_roles = []
        query_string = self.make_query_str(**kwargs)
        role_response = self.client.get(
            "{0}{1}/Roles{2}".format(self.client.baseurl, user_ref, query_string))
        for role in role_response['result']['roles']:
            all_roles.append(Roles(self.client).build(role))
        return all_roles

    def deleteUserRole(self, user_ref, role_ref, saveComment=""):
        if saveComment:
            saveComment = "?{0}".format(saveComment)
        return self.client.delete("{0}{1}/{2}{3}".format(self.client.baseurl,
                                                         user_ref,
                                                         role_ref,
                                                         saveComment))

    def addUserRole(self, user_ref, role_ref, saveComment=""):
        payload = {
            "saveComment": saveComment
        }
        return self.client.put("{0}{1}/{2}".format(self.client.baseurl,
                                                   user_ref,
                                                   role_ref),
                               payload,
                               True)
