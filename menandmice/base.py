import json


class BaseObject(object):

    def get_value(self, key, **kwargs):
        return kwargs[key] if (key in kwargs) else None

    def build_obj(self, clazz, **kwargs):
        return clazz(**kwargs) if kwargs else None

    def build_obj_list(self, clazz, objects, **kwargs):
        obj_list = []
        if objects:
            if isinstance(objects, list):
                for obj in objects:
                    obj_list.append(clazz(**obj))
            else:
                obj_list.append(clazz(**objects))
        return obj_list

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def json_to_class(self, json_input, clazz):
        if isinstance(json_input, basestring):
            json_input = json.loads(json_input)
        return clazz(**json_input)

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
                 get_is_singular=False):
        self.client = client
        self.url_base = url_base
        self.entity_class = entity_class
        self.get_response_entity_key = get_response_entity_key
        self.get_response_all_key = get_response_all_key
        self.get_is_singular = get_is_singular

    def build(self, json_input):
        return self.json_to_class(json_input, self.entity_class)

    def get(self, ref="", **kwargs):
        entities = []
        query_string = self.make_query_str(**kwargs)
        if self.get_is_singular or ref:
            entity_response = self.client.get("{0}{1}{2}".format(self.client.baseurl,
                                                                 ref,
                                                                 query_string))
            entities.append(self.build(entity_response['result'][self.get_response_entity_key]))
        else:
            entity_response = self.client.get(
                "{0}{1}{2}".format(self.client.baseurl,
                                   self.url_base,
                                   query_string))
            for entity in entity_response['result'][self.get_response_all_key]:
                entities.append(self.build(entity))
        return entities

    def delete(self, ref, **kwargs):
        return self.client.deleteItem(ref, kwargs)

    def update(self,
               ref,
               properties,
               objType="",
               saveComment="",
               deleteUnspecified=False):
        return self.client.updateItem(ref,
                                      properties,
                                      objType,
                                      saveComment,
                                      deleteUnspecified)

    def getAccess(self, ref, **kwargs):
        return self.client.getItemAccess(ref, **kwargs)

    def setAccess(self, ref, identity_access, object_type="", saveComment=""):
        return self.client.setItemAccess(ref, identity_access, object_type, saveComment)

    def getHistory(self, ref, **kwargs):
        return self.client.getItemHistory(ref, **kwargs)

    def getPropertyDefinition(self, ref, property_name=""):
        return self.client.getPropertyDefinitions(ref, property_name)

    def addNewPropertyDefinition(self, ref, property_definition, saveComment=""):
        return self.client.newCustomProperty(ref, property_definition, saveComment)

    def updatePropertyDefinition(self,
                                 ref,
                                 property_name,
                                 property_definition,
                                 updateExisting="",
                                 saveComment=""):
        return self.client.updatePropertyDefinitions(ref,
                                                     property_name,
                                                     property_definition,
                                                     updateExisting,
                                                     saveComment)

    def deletePropertyDefinition(self, ref, property_name, saveComment=""):
        return self.client.deletePropertyDefinition(ref, property_name, saveComment)
