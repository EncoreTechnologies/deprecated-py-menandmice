import json

class Role(object):
  def __init__(self, **kwargs):
    self.ref = self.getValue('ref', kwargs)
    self.name = self.getValue('name', kwargs)
    self.description = self.getValue('description', kwargs)
    self.users = self.build_users(self.getValue('users', kwargs))
    self.groups = self.build_groups(self.getValue('groups', kwargs))
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def build_groups(self, groups):
    groups_return = []
    if groups:
      if isinstance(groups, list):
        for group in groups:
          groups_return.append(Group(**group))
      else:
        groups_return.append(Group(**groups))
    return groups_return
  def build_users(self, users):
    users_return = []
    if users:
      if isinstance(users, list):
        for user in users:
          users_return.append(User(**user))
      else:
        users_return.append(User(**users))
    return users_return
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class User(object):
  def __init__(self, **kwargs):
    self.ref = self.getValue('ref', kwargs)
    self.name = self.getValue('name', kwargs)
    self.password = self.getValue('password', kwargs)
    self.fullName = self.getValue('fullName', kwargs)
    self.description = self.getValue('description', kwargs)
    self.email = self.getValue('email', kwargs)
    self.authenticationType = self.getValue('authenticationType', kwargs)
    self.roles = self.build_roles(self.getValue('roles', kwargs))
    self.groups = self.build_groups(self.getValue('groups', kwargs))
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def build_groups(self, groups):
    groups_return = []
    if groups:
      if isinstance(groups, list):
        for group in groups:
          groups_return.append(Group(**group))
      else:
        groups_return.append(Group(**groups))
    return groups_return
  def build_roles(self, roles):
    roles_return = []
    if roles:
      if isinstance(roles, list):
        for role in roles:
          roles_return.append(Role(**role))
      else:
        roles_return.append(Role(**roles))
    return roles_return
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class Group(object):
  def __init__(self, **kwargs):
    self.ref = self.getValue('ref', kwargs)
    self.name = self.getValue('name', kwargs)
    self.description = self.getValue('description', kwargs)
    self.adIntegrated = self.getValue('adIntegrated', kwargs)
    self.groupMembers = self.build_users(self.getValue('groupMembers', kwargs))
    self.roles = self.build_roles(self.getValue('roles', kwargs))
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def build_roles(self, roles):
    roles_return = []
    if roles:
      if isinstance(roles, list):
        for role in roles:
          roles_return.append(Role(**role))
      else:
        roles_return.append(Role(**roles))
    return roles_return
  def build_users(self, users):
    users_return = []
    if users:
      if isinstance(users, list):
        for user in users:
          users_return.append(User(**user))
      else:
        users_return.append(User(**users))
    return users_return
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class Groups(object):
  def __init__(self, client):
    self.client = client
    self.url_base = "Groups"
  def build(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return Group(**json_input)
  def get(self, group_ref="", **kwargs):
    all_groups = []
    if not group_ref:
      query_string = ""
      if kwargs:
        for key, value in kwargs.items():
          if not query_string:
            query_string += "?{0}={1}".format(key, value)
          else:
            query_string += "&{0}={1}".format(key, value)
      group_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, self.url_base, query_string))
      for group in group_response['result']['groups']:
        all_groups.append(self.build(group))
    else:
      group_response = self.client.get("{0}{1}".format(self.client.baseurl, group_ref))
      all_groups.append(self.build(group_response['result']['group']))
    return all_groups
  def add(self, group_input, saveComment=""):
    if isinstance(group_input, Group):
      group_input = json.loads(group_input.to_json())
    payload = {
      "saveComment" : saveComment,
      "group" : group_input
    }
    group_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
    group_return = []
    for ref in group_json['result']['objRefs']:
      group_return.append(self.get(ref)[0])
    return group_return
  def delete(self, group_ref, **kwargs):
    return self.client.deleteItem(group_ref, kwargs)
  def update(self, group_ref, properties, objType="", saveComment="", deleteUnspecified=False):
    return self.client.updateItem(group_ref, properties, objType, saveComment, deleteUnspecified)
  def getAccess(self, group_ref, **kwargs):
    return self.client.getItemAccess(group_ref, kwargs)
  def setAccess(self, group_ref, identity_access, object_type="", saveComment=""):
    return self.client.setItemAccess(group_ref, identity_access, object_type, saveComment)
  def getHistory(self, group_ref, **kwargs):
    return self.client.getItemHistory(group_ref, kwargs)
  def getPropertyDefinition(self, group_ref, property_name=""):
    return self.client.getPropertyDefinitions(group_ref, property_name)
  def addNewPropertyDefinition(self, group_ref, property_definition, saveComment=""):
    return self.client.newCustomProperty(group_ref, property_definition, saveComment)
  def updatePropertyDefinition(self, group_ref, property_name, property_definition, updateExisting="", saveComment=""):
    return self.client.updatePropertyDefinitions(group_ref, property_name, property_definition, updateExisting, saveComment)
  def deletePropertyDefinition(self, group_ref, property_name, saveComment=""):
    return self.client.deletePropertyDefinition(group_ref, property_name, saveComment)
  def getGroupRoles(self, group_ref, **kwargs):
    all_roles = []
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    role_response = self.client.get("{0}{1}/Roles{2}".format(self.client.baseurl, group_ref, query_string))
    for role in role_response['result']['roles']:
      all_roles.append(Roles(self.client).build(role))
    return all_roles
  def deleteGroupRole(self, group_ref, role_ref, saveComment=""):
    if saveComment:
      saveComment = "?{0}".format(saveComment)
    return self.client.delete("{0}{1}/{2}{3}".format(self.client.baseurl, group_ref, role_ref, saveComment))
  def addGroupRole(self, group_ref, role_ref, saveComment=""):
    payload = {
      "saveComment" : saveComment
    }
    return self.client.put("{0}{1}/{2}".format(self.client.baseurl, group_ref, role_ref), payload, True)
  def getUserRoles(self, group_ref, **kwargs):
    all_users = []
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    role_response = self.client.get("{0}{1}/Users{2}".format(self.client.baseurl, group_ref, query_string))
    for user in role_response['result']['users']:
      all_users.append(User(self.client).build(user))
    return all_users
  def deleteUserRole(self, group_ref, user_ref, saveComment=""):
    if saveComment:
      saveComment = "?{0}".format(saveComment)
    return self.client.delete("{0}{1}/{2}{3}".format(self.client.baseurl, group_ref, user_ref, saveComment))
  def addUserRole(self, group_ref, user_ref, saveComment=""):
    payload = {
      "saveComment" : saveComment
    }
    return self.client.put("{0}{1}/{2}".format(self.client.baseurl, group_ref, user_ref), payload, True)


class Roles(object):
  def __init__(self, client):
    self.client = client
    self.url_base = "Roles"
  def build(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return Role(**json_input)
  def get(self, role_ref="", **kwargs):
    all_roles = []
    if not role_ref:
      query_string = ""
      if kwargs:
        for key, value in kwargs.items():
          if not query_string:
            query_string += "?{0}={1}".format(key, value)
          else:
            query_string += "&{0}={1}".format(key, value)
      role_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, self.url_base, query_string))
      for role in role_response['result']['roles']:
        all_roles.append(self.build(role))
    else:
      role_response = self.client.get("{0}{1}".format(self.client.baseurl, role_ref))
      all_roles.append(self.build(role_response['result']['role']))
    return all_roles
  def add(self, role_input, saveComment=""):
    if isinstance(role_input, Role):
      role_input = json.loads(role_input.to_json())
    payload = {
      "saveComment" : saveComment,
      "role" : role_input
    }
    role_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
    role_return = []
    for ref in role_json['result']['objRefs']:
      role_return.append(self.get(ref)[0])
    return role_return
  def delete(self, role_ref, **kwargs):
    return self.client.deleteItem(role_ref, kwargs)
  def update(self, role_ref, properties, objType="", saveComment="", deleteUnspecified=False):
    return self.client.updateItem(role_ref, properties, objType, saveComment, deleteUnspecified)
  def getAccess(self, role_ref, **kwargs):
    return self.client.getItemAccess(role_ref, kwargs)
  def setAccess(self, role_ref, identity_access, object_type="", saveComment=""):
    return self.client.setItemAccess(role_ref, identity_access, object_type, saveComment)
  def getHistory(self, role_ref, **kwargs):
    return self.client.getItemHistory(role_ref, kwargs)
  def getPropertyDefinition(self, role_ref, property_name=""):
    return self.client.getPropertyDefinitions(role_ref, property_name)
  def addNewPropertyDefinition(self, role_ref, property_definition, saveComment=""):
    return self.client.newCustomProperty(role_ref, property_definition, saveComment)
  def updatePropertyDefinition(self, role_ref, property_name, property_definition, updateExisting="", saveComment=""):
    return self.client.updatePropertyDefinitions(role_ref, property_name, property_definition, updateExisting, saveComment)
  def deletePropertyDefinition(self, role_ref, property_name, saveComment=""):
    return self.client.deletePropertyDefinition(role_ref, property_name, saveComment)
  def getRoleGroups(self, role_ref, **kwargs):
    all_groups = []
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    group_response = self.client.get("{0}{1}/Groups{2}".format(self.client.baseurl, role_ref, query_string))
    for group in group_response['result']['groups']:
      all_groups.append(Group(self.client).build(group))
    return all_groups
  def getRoleUsers(self, role_ref, **kwargs):
    all_users = []
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    user_response = self.client.get("{0}{1}/Users{2}".format(self.client.baseurl, role_ref, query_string))
    for user in user_response['result']['users']:
      all_users.append(User(self.client).build(user))
    return all_users



class Users(object):
  def __init__(self, client):
    self.client = client
    self.url_base = "Users"
  def build(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return User(**json_input)
  def get(self, user_ref="", **kwargs):
    all_users = []
    if not user_ref:
      query_string = ""
      if kwargs:
        for key, value in kwargs.items():
          if not query_string:
            query_string += "?{0}={1}".format(key, value)
          else:
            query_string += "&{0}={1}".format(key, value)
      user_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, self.url_base, query_string))
      for user in user_response['result']['users']:
        all_users.append(self.build(user))
    else:
      user_response = self.client.get("{0}{1}".format(self.client.baseurl, user_ref))
      all_users.append(self.build(user_response['result']['user']))
    return all_users
  def add(self, user_input, saveComment=""):
    if isinstance(user_input, User):
      user_input = json.loads(user_input.to_json())
    payload = {
      "saveComment" : saveComment,
      "user" : user_input
    }
    user_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
    user_return = []
    for ref in user_json['result']['objRefs']:
      user_return.append(self.get(ref)[0])
    return user_return
  def delete(self, user_ref, **kwargs):
    return self.client.deleteItem(user_ref, kwargs)
  def update(self, user_ref, properties, objType="", saveComment="", deleteUnspecified=False):
    return self.client.updateItem(user_ref, properties, objType, saveComment, deleteUnspecified)
  def getAccess(self, user_ref, **kwargs):
    return self.client.getItemAccess(user_ref, kwargs)
  def setAccess(self, user_ref, identity_access, object_type="", saveComment=""):
    return self.client.setItemAccess(user_ref, identity_access, object_type, saveComment)
  def getHistory(self, user_ref, **kwargs):
    return self.client.getItemHistory(user_ref, kwargs)
  def getPropertyDefinition(self, user_ref, property_name=""):
    return self.client.getPropertyDefinitions(user_ref, property_name)
  def addNewPropertyDefinition(self, user_ref, property_definition, saveComment=""):
    return self.client.newCustomProperty(user_ref, property_definition, saveComment)
  def updatePropertyDefinition(self, user_ref, property_name, property_definition, updateExisting="", saveComment=""):
    return self.client.updatePropertyDefinitions(user_ref, property_name, property_definition, updateExisting, saveComment)
  def deletePropertyDefinition(self, user_ref, property_name, saveComment=""):
    return self.client.deletePropertyDefinition(user_ref, property_name, saveComment)
  def getUsersGroups(self, user_ref, **kwargs):
    all_groups = []
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    group_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, user_ref, query_string))
    for group in group_response['result']['groups']:
      all_groups.append(Groups(self.client).build(group))
    return all_groups
  def getUserRoles(self, user_ref, **kwargs):
    all_roles = []
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    role_response = self.client.get("{0}{1}/Roles{2}".format(self.client.baseurl, user_ref, query_string))
    for role in role_response['result']['roles']:
      all_roles.append(Roles(self.client).build(role))
    return all_roles
  def deleteUserRole(self, user_ref, role_ref, saveComment=""):
    if saveComment:
      saveComment = "?{0}".format(saveComment)
    return self.client.delete("{0}{1}/{2}{3}".format(self.client.baseurl, user_ref, role_ref, saveComment))
  def addUserRole(self, user_ref, role_ref, saveComment=""):
    payload = {
      "saveComment" : saveComment
    }
    return self.client.put("{0}{1}/{2}".format(self.client.baseurl, user_ref, role_ref), payload, True)