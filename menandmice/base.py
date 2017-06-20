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

import json

# Python 2 and 3 compatible
from future.standard_library import install_aliases
install_aliases()
from urllib.parse import urlencode


class BaseObject(dict):

    def add_key(self, key, default=None):
        if key not in self:
            self[key] = default

    def to_json(self):
        return json.dumps(self)

    def from_json(self, string):
        return json.loads(string)

    def make_query_str(self, **kwargs):
        query_string = ""
        if kwargs:
            query_string = "?{0}".format(urlencode(kwargs))
        return query_string


class BaseService(BaseObject):

    def __init__(self,
                 client=None,
                 url_base="",
                 entity_class=None,
                 get_response_entity_key="",
                 get_response_all_key="",
                 get_is_singular=False,
                 ref_key="ref"):
        self.client = client
        self.url_base = url_base
        self.entity_class = entity_class
        self.get_response_entity_key = get_response_entity_key
        self.get_response_all_key = get_response_all_key
        self.get_is_singular = get_is_singular
        self.ref_key = ref_key

    def build(self, json_or_dict):
        if isinstance(json_or_dict, basestring):
            json_or_dict = json.loads(json_or_dict)
        return self.entity_class(**json_or_dict)

    def get(self, obj_or_ref="", **kwargs):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        entities = []
        query_string = self.make_query_str(**kwargs)
        if self.get_is_singular or ref:
            response = self.client.get("{0}{1}{2}".format(self.client.baseurl,
                                                          ref,
                                                          query_string))
            entities.append(self.build(response['result'][self.get_response_entity_key]))
        else:
            response = self.client.get(
                "{0}{1}{2}".format(self.client.baseurl,
                                   self.url_base,
                                   query_string))
            for entity in response['result'][self.get_response_all_key]:
                entities.append(self.build(entity))
        return entities

    def delete(self, obj_or_ref, **kwargs):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.delete_item(ref, **kwargs)

    def update(self,
               obj_or_ref,
               properties,
               obj_type="",
               save_comment="",
               delete_unspecified=False):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.update_item(ref,
                                       properties,
                                       obj_type,
                                       save_comment,
                                       delete_unspecified)

    def get_access(self, obj_or_ref, **kwargs):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.get_item_access(ref, **kwargs)

    def set_access(self,
                   obj_or_ref,
                   identity_access,
                   obj_type="",
                   save_comment=""):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        # this code allows a user to call get_access() which returns an ObjectAccess
        # object, and then pass it to this set_access() function.
        # Note: 'identityAccess' is a member of ObjectAccess that we will use
        #        for setting this object's access
        if isinstance(identity_access, dict) and 'identityAccess' in identity_access:
            identity_access = identity_access['identityAccess']
        return self.client.set_item_access(ref, identity_access, obj_type, save_comment)

    def get_history(self, obj_or_ref, **kwargs):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.get_item_history(ref, **kwargs)

    def get_property_definition(self, obj_or_ref, property_name=""):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.get_property_definitions(ref, property_name)

    def add_property_definition(self, obj_or_ref, property_definition, save_comment=""):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.add_property_definition(ref, property_definition, save_comment)

    def update_property_definition(self,
                                   obj_or_ref,
                                   property_name,
                                   property_definition,
                                   update_existing=None,  # boolean
                                   save_comment=""):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.update_property_definition(ref,
                                                      property_name,
                                                      property_definition,
                                                      update_existing,
                                                      save_comment)

    def delete_property_definition(self, obj_or_ref, property_name, save_comment=""):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.delete_property_definition(ref, property_name, save_comment)

    def ref_or_raise(self, dict_or_ref, key="ref"):
        # is the object a string (ref)
        if isinstance(dict_or_ref, basestring):
            return dict_or_ref
        # is the object a dictionary (note, our objects are all dicts)
        elif isinstance(dict_or_ref, dict):
            return dict_or_ref[key]
        else:
            raise TypeError("Input must be of type basestring or dict")
