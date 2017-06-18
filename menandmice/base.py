import json
import pprint


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
            for key, value in kwargs.items():
                if not query_string:
                    query_string += "?{0}={1}".format(key, value)
                else:
                    query_string += "&{0}={1}".format(key, value)
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

    def build(self, json_input):
        if isinstance(json_input, basestring):
            json_input = json.loads(json_input)
        return self.entity_class(**json_input)

    def get(self, obj_or_ref="", **kwargs):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        entities = []
        query_string = self.make_query_str(**kwargs)
        if self.get_is_singular or ref:
            response = self.client.get("{0}{1}{2}".format(self.client.baseurl,
                                                          ref,
                                                          query_string))
            pprint.pprint(response)
            entities.append(self.build(response['result'][self.get_response_entity_key]))
        else:
            response = self.client.get(
                "{0}{1}{2}".format(self.client.baseurl,
                                   self.url_base,
                                   query_string))
            pprint.pprint(response)
            for entity in response['result'][self.get_response_all_key]:
                entities.append(self.build(entity))
        return entities

    def delete(self, obj_or_ref, **kwargs):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.deleteItem(ref, **kwargs)

    def update(self,
               obj_or_ref,
               properties,
               objType="",
               saveComment="",
               deleteUnspecified=False):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.updateItem(ref,
                                      properties,
                                      objType,
                                      saveComment,
                                      deleteUnspecified)

    def getAccess(self, obj_or_ref, **kwargs):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.getItemAccess(ref, **kwargs)

    def setAccess(self, obj_or_ref, identity_access, object_type="", saveComment=""):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.setItemAccess(ref, identity_access, object_type, saveComment)

    def getHistory(self, obj_or_ref, **kwargs):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.getItemHistory(ref, **kwargs)

    def getPropertyDefinition(self, obj_or_ref, property_name=""):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.getPropertyDefinitions(ref, property_name)

    def addNewPropertyDefinition(self, obj_or_ref, property_definition, saveComment=""):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.newCustomProperty(ref, property_definition, saveComment)

    def updatePropertyDefinition(self,
                                 obj_or_ref,
                                 property_name,
                                 property_definition,
                                 updateExisting="",
                                 saveComment=""):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.updatePropertyDefinitions(ref,
                                                     property_name,
                                                     property_definition,
                                                     updateExisting,
                                                     saveComment)

    def deletePropertyDefinition(self, obj_or_ref, property_name, saveComment=""):
        ref = self.ref_or_raise(obj_or_ref, self.ref_key)
        return self.client.deletePropertyDefinition(ref, property_name, saveComment)

    def ref_or_raise(self, dict_or_ref, key="ref"):
        # is the object a string (ref)
        if isinstance(dict_or_ref, basestring):
            return dict_or_ref
        # is the object a dictionary (note, our objects are all dicts)
        elif isinstance(dict_or_ref, dict):
            return dict_or_ref[key]
        else:
            raise TypeError("Input must be of type basestring or dict")
