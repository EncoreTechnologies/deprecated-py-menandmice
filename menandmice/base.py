

class BaseObject(object):
    
    def getValue(self, key, kwargs):
        return kwargs[key] if key in kwargs: else None

    def buildObj(self, clazz, kwargs):
        return clazz(**kwargs) if kwargs else None

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)



class BaseService(BaseObject):

    def __init__(self, client, url_base):
        self.client = client
        self.url_base = url_base
        
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
        return self.client.getItemAccess(ref, kwargs)

    def setAccess(self, ref, identity_access, object_type="", saveComment=""):
        return self.client.setItemAccess(ref, identity_access, object_type, saveComment)

    def getHistory(self, ref, **kwargs):
        return self.client.getItemHistory(ref, kwargs)

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

