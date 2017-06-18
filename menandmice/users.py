from menandmice.base import BaseObject
from menandmice.base import BaseService


class Role(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Role, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('description')
        self.add_key('users', [User()])
        self.add_key('groups', [Group()])


class User(BaseObject):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('password')
        self.add_key('fullName')
        self.add_key('description')
        self.add_key('email')
        self.add_key('authenticationType')
        self.add_key('roles', [Role()])
        self.add_key('groups', [Group()])


class Group(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Group, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('description')
        self.add_key('adIntegrated')
        self.add_key('groupMembers', [User()])
        self.add_key('roles', [Role()])


class Groups(BaseService):
    def __init__(self, client):
        super(Groups, self).__init__(client=client,
                                     url_base="Groups",
                                     entity_class=Group,
                                     get_response_entity_key="group",
                                     get_response_all_key="groups")

    def add(self, group_input, saveComment=""):
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

    def getGroupRoles(self, group, **kwargs):
        group_ref = self.ref_or_raise(group)
        all_roles = []
        query_string = self.make_query_str(**kwargs)
        role_response = self.client.get("{0}{1}/Roles{2}".format(self.client.baseurl,
                                                                 group_ref,
                                                                 query_string))
        for role in role_response['result']['roles']:
            all_roles.append(Roles(self.client).build(role))
        return all_roles

    def deleteGroupRole(self, group, role, saveComment=""):
        group_ref = self.ref_or_raise(group)
        role_ref = self.ref_or_raise(role)
        if saveComment:
            saveComment = "?{0}".format(saveComment)
        return self.client.delete("{0}{1}/{2}{3}".format(self.client.baseurl,
                                                         group_ref,
                                                         role_ref,
                                                         saveComment))

    def addGroupRole(self, group, role, saveComment=""):
        group_ref = self.ref_or_raise(group)
        role_ref = self.ref_or_raise(role)
        payload = {
            "saveComment": saveComment
        }
        return self.client.put("{0}{1}/{2}".format(self.client.baseurl,
                                                   group_ref,
                                                   role_ref),
                               payload,
                               True)

    def getUserRoles(self, group, **kwargs):
        group_ref = self.ref_or_raise(group)
        all_users = []
        query_string = self.make_query_str(**kwargs)
        role_response = self.client.get("{0}{1}/Users{2}".format(self.client.baseurl,
                                                                 group_ref,
                                                                 query_string))
        for user in role_response['result']['users']:
            all_users.append(User(self.client).build(user))
        return all_users

    def deleteUserRole(self, group, user, saveComment=""):
        group_ref = self.ref_or_raise(group)
        user_ref = self.ref_or_raise(user)
        if saveComment:
            saveComment = "?{0}".format(saveComment)
        return self.client.delete("{0}{1}/{2}{3}".format(self.client.baseurl,
                                                         group_ref,
                                                         user_ref,
                                                         saveComment))

    def addUserRole(self, group, user, saveComment=""):
        group_ref = self.ref_or_raise(group)
        user_ref = self.ref_or_raise(user)
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

    def add(self, role, saveComment=""):
        payload = {
            "saveComment": saveComment,
            "role": role
        }
        role_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                     self.url_base),
                                     payload)
        role_return = []
        for ref in role_json['result']['objRefs']:
            role_return.append(self.get(ref)[0])
        return role_return

    def getRoleGroups(self, role, **kwargs):
        role_ref = self.ref_or_raise(role)
        all_groups = []
        query_string = self.make_query_str(**kwargs)
        group_response = self.client.get("{0}{1}/Groups{2}".format(self.client.baseurl,
                                                                   role_ref,
                                                                   query_string))
        for group in group_response['result']['groups']:
            all_groups.append(Group(self.client).build(group))
        return all_groups

    def getRoleUsers(self, role, **kwargs):
        role_ref = self.ref_or_raise(role)
        all_users = []
        query_string = self.make_query_str(**kwargs)
        user_response = self.client.get("{0}{1}/Users{2}".format(self.client.baseurl,
                                                                 role_ref,
                                                                 query_string))
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

    def add(self, user, saveComment=""):
        payload = {
            "saveComment": saveComment,
            "user": user
        }
        user_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                     self.url_base),
                                     payload)
        user_return = []
        for ref in user_json['result']['objRefs']:
            user_return.append(self.get(ref)[0])
        return user_return

    def getUsersGroups(self, user, **kwargs):
        user_ref = self.ref_or_raise(user)
        all_groups = []
        query_string = self.make_query_str(**kwargs)
        group_response = self.client.get("{0}{1}{2}".format(self.client.baseurl,
                                                            user_ref,
                                                            query_string))
        for group in group_response['result']['groups']:
            all_groups.append(Groups(self.client).build(group))
        return all_groups

    def getUserRoles(self, user, **kwargs):
        user_ref = self.ref_or_raise(user)
        all_roles = []
        query_string = self.make_query_str(**kwargs)
        role_response = self.client.get("{0}{1}/Roles{2}".format(self.client.baseurl,
                                                                 user_ref,
                                                                 query_string))
        for role in role_response['result']['roles']:
            all_roles.append(Roles(self.client).build(role))
        return all_roles

    def deleteUserRole(self, user, role, saveComment=""):
        user_ref = self.ref_or_raise(user)
        role_ref = self.ref_or_raise(role)
        if saveComment:
            saveComment = "?{0}".format(saveComment)
        return self.client.delete("{0}{1}/{2}{3}".format(self.client.baseurl,
                                                         user_ref,
                                                         role_ref,
                                                         saveComment))

    def addUserRole(self, user, role, saveComment=""):
        user_ref = self.ref_or_raise(user)
        role_ref = self.ref_or_raise(role)
        payload = {
            "saveComment": saveComment
        }
        return self.client.put("{0}{1}/{2}".format(self.client.baseurl,
                                                   user_ref,
                                                   role_ref),
                               payload,
                               True)
