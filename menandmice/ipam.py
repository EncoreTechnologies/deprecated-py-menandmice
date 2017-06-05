import json

class IPAMRecord(object):
  def __init__(self, **kwargs):
    self.addrRef = self.getValue('addrRef', kwargs)
    self.address = self.getValue('address', kwargs)
    self.claimed = self.getValue('claimed', kwargs)
    self.dnsHosts = self.getValue('dnsHosts', kwargs)
    self.dhcpReservations = self.getValue('dhcpReservations', kwargs)
    self.dhcpLeases = self.getValue('dhcpLeases', kwargs)
    self.discoveryType = self.getValue('discoveryType', kwargs)
    self.lastSeenDate = self.getValue('lastSeenDate', kwargs)
    self.lastDiscoveryDate = self.getValue('lastDiscoveryDate', kwargs)
    self.lastKnownClientIdentifier = self.getValue('lastKnownClientIdentifier', kwargs)
    self.device = self.getValue('device', kwargs)
    self.interface = self.getValue('interface', kwargs)
    self.ptrStatus = self.getValue('ptrStatus', kwargs)
    self.extraneousPTR = self.getValue('extraneousPTR', kwargs)
    self.customProperties = self.getValue('customProperties', kwargs)
    self.state = self.getValue('state', kwargs)
    self.usage = self.getValue('usage', kwargs)
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class Range(object):
  def __init__(self, **kwargs):
    self.ref = self.getValue('ref', kwargs)
    self.name = self.getValue('name', kwargs)
    self.from_ = self.getValue('from', kwargs)
    self.to = self.getValue('to', kwargs)
    self.parentRef = self.getValue('parentRef', kwargs)
    self.adSiteRef = self.getValue('adSiteRef', kwargs)
    self.childRanges = self.getValue('childRanges', kwargs)
    self.dhcpScopes = self.getValue('dhcpScopes', kwargs)
    self.subnet = self.getValue('subnet', kwargs)
    self.locked = self.getValue('locked', kwargs)
    self.autoAssign = self.getValue('autoAssign', kwargs)
    self.hasSchedule = self.getValue('hasSchedule', kwargs)
    self.hasMonitor = self.getValue('hasMonitor', kwargs)
    self.customProperties = self.getValue('customProperties', kwargs)
    self.inheritAccess = self.getValue('inheritAccess', kwargs)
    self.isContainer = self.getValue('isContainer', kwargs)
    self.utilizationPercentage = self.getValue('utilizationPercentage', kwargs)
    self.hasRogueAddresses = self.getValue('hasRogueAddresses', kwargs)
    self.cloudNetworkRef = self.getValue('cloudNetworkRef', kwargs)
    self.cloudAllocationPools = self.getValue('cloudAllocationPools', kwargs)
    self.discoveredProperties = self.getValue('discoveredProperties', kwargs)
    self.creationTime = self.getValue('creationTime', kwargs)
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class Discovery(object):
  def __init__(self, **kwargs):
    self.interval = self.getValue('interval', kwargs)
    self.unit = self.getValue('unit', kwargs)
    self.enabled = self.getValue('enabled', kwargs)
    self.startTime = self.getValue('startTime', kwargs)
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class AddressBlock(object):
  def __init__(self, **kwargs):
    self.from_ = self.getValue('from', kwargs)
    self.to = self.getValue('to', kwargs)
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class GetRangeStatisticsResponse(object):
  def __init__(self, **kwargs):
    self.used = self.getValue('used', kwargs)
    self.free = self.getValue('free', kwargs)
    self.numInSubranges = self.getValue('numInSubranges', kwargs)
    self.percentInSubranges = self.getValue('percentInSubranges', kwargs)
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class Interface(object):
  def __init__(self, **kwargs):
    self.ref = self.getValue('ref', kwargs)
    self.name = self.getValue('name', kwargs)
    self.clientIdentifier = self.getValue('clientIdentifier', kwargs)
    self.addresses = self.getValue('addresses', kwargs)
    self.customProperties = self.getValue('customProperties', kwargs)
    self.deviceRef = self.getValue('deviceRef', kwargs)
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class Device(object):
  def __init__(self, **kwargs):
    self.ref = self.getValue('ref', kwargs)
    self.name = self.getValue('name', kwargs)
    self.customProperties = self.getValue('customProperties', kwargs)
    self.interfaces = self.getValue('interfaces', kwargs)
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class ChangeRequest(object):
  def __init__(self, **kwargs):
    self.ref = self.getValue('ref', kwargs)
    self.requester = self.getValue('requester', kwargs)
    self.state = self.getValue('state', kwargs)
    self.creationDate = self.getValue('creationDate', kwargs)
    self.objType = self.getValue('objType', kwargs)
    self.requestDate = self.getValue('requestDate', kwargs)
    self.customProperties = self.getValue('customProperties', kwargs)
    self.saveComment = self.getValue('saveComment', kwargs)
    self.processedDate = self.getValue('processedDate', kwargs)
    self.dnsZoneChanges = self.getValue('dnsZoneChanges', kwargs)
    self.dnsRecordChanges = self.getValue('dnsRecordChanges', kwargs)
    self.dhcpScopeChanges = self.getValue('dhcpScopeChanges', kwargs)
    self.dhcpReservationChanges = self.getValue('dhcpReservationChanges', kwargs)
    self.dhcpExclusionChanges = self.getValue('dhcpExclusionChanges', kwargs)
    self.dhcpAddressPoolChanges = self.getValue('dhcpAddressPoolChanges', kwargs)
    self.dhcpOptionChanges = self.getValue('dhcpOptionChanges', kwargs)
    self.customPropertyChanges = self.getValue('customPropertyChanges', kwargs)
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class Folder(object):
  def __init__(self, **kwargs):
    self.ref = self.getValue('ref', kwargs)
    self.name = self.getValue('name', kwargs)
    self.contentType = self.getValue('contentType', kwargs)
    self.parentRef = self.getValue('parentRef', kwargs)
  def getValue(self, key, kwargs):
    return_val = ""
    if key in kwargs:
      return_val = kwargs[key]
    return return_val
  def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__)


class IPAMRecords(object):
  def __init__(self, client):
    self.client = client
    self.url_base = "IPAMRecords"
  def build(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return IPAMRecord(**json_input)
  def get(self, address_ref, **kwargs):
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    ipam_record_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, address_ref, query_string))
    return self.build(ipam_record_response['result']['ipamRecord'])
  def update(self, address_ref, properties, objType="", saveComment="", deleteUnspecified=False):
    return self.client.updateItem(address_ref, properties, objType, saveComment, deleteUnspecified)
  def delete(self, address_ref, **kwargs):
    return self.client.deleteItem(address_ref, kwargs)
  def getAccess(self, address_ref, **kwargs):
    return self.client.getItemAccess(address_ref, kwargs)
  def setAccess(self, address_ref, identity_access, object_type="", saveComment=""):
    return self.client.setItemAccess(address_ref, identity_access, object_type, saveComment)
  def getHistory(self, address_ref, **kwargs):
    return self.client.getItemHistory(address_ref, kwargs)
  def getPropertyDefinition(self, address_ref, property_name=""):
    return self.client.getPropertyDefinitions(address_ref, property_name)
  def addNewPropertyDefinition(self, address_ref, property_definition, saveComment=""):
    return self.client.newCustomProperty(address_ref, property_definition, saveComment)
  def updatePropertyDefinition(self, address_ref, property_name, property_definition, updateExisting="", saveComment=""):
    return self.client.updatePropertyDefinitions(address_ref, property_name, property_definition, updateExisting, saveComment)
  def deletePropertyDefinition(self, address_ref, property_name, saveComment=""):
    return self.client.deletePropertyDefinition(address_ref, property_name, saveComment)
  def pingRecord(self, address_ref):
    return self.client.post("{0}{1}/Ping".format(self.client.baseurl, address_ref), "")
  def getRecordRange(self, address_ref):
    range_response = self.client.get("{0}{1}/Range".format(self.client.baseurl, address_ref))
    return Ranges(self.client).build(range_response['result']['range'])


class Ranges(object):
  def __init__(self, client):
    self.client = client
    self.url_base = "Ranges"
  def build(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return Range(**json_input)
  def buildAddressBlocks(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return AddressBlock(**json_input)
  def buildStatistics(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return GetRangeStatisticsResponse(**json_input)
  def get(self, range_ref="", **kwargs):
    all_ranges = []
    if not range_ref:
      query_string = ""
      if kwargs:
        for key, value in kwargs.items():
          if not query_string:
            query_string += "?{0}={1}".format(key, value)
          else:
            query_string += "&{0}={1}".format(key, value)
      range_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, self.url_base, query_string))
      for range_output in range_response['result']['ranges']:
        all_ranges.append(self.build(range_output))
    else:
      range_response = self.client.get("{0}{1}".format(self.client.baseurl, range_ref))
      all_ranges.append(self.build(range_response['result']['range']))
    return all_ranges
  def add(self, range_input, discovery="", saveComment=""):
    if isinstance(range_input, Range):
      range_input = json.loads(range_input.to_json())
    if discovery:
      if isinstance(discovery, Discovery):
        discovery = json.loads(discovery.to_json())
    payload = {
      "discovery" : discovery,
      "saveComment" : saveComment,
      "range" : range_input
    }
    range_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
    range_return = self.get(zone_json['result']['ref'])
    return range_return[0]
  def delete(self, range_ref, **kwargs):
    return self.client.deleteItem(range_ref, kwargs)
  def update(self, range_ref, properties, objType="", saveComment="", deleteUnspecified=False):
    return self.client.updateItem(range_ref, properties, objType, saveComment, deleteUnspecified)
  def getAccess(self, range_ref, **kwargs):
    return self.client.getItemAccess(range_ref, kwargs)
  def setAccess(self, range_ref, identity_access, object_type="", saveComment=""):
    return self.client.setItemAccess(range_ref, identity_access, object_type, saveComment)
  def getHistory(self, range_ref, **kwargs):
    return self.client.getItemHistory(range_ref, kwargs)
  def getPropertyDefinition(self, range_ref, property_name=""):
    return self.client.getPropertyDefinitions(range_ref, property_name)
  def addNewPropertyDefinition(self, range_ref, property_definition, saveComment=""):
    return self.client.newCustomProperty(range_ref, property_definition, saveComment)
  def updatePropertyDefinition(self, range_ref, property_name, property_definition, updateExisting="", saveComment=""):
    return self.client.updatePropertyDefinitions(range_ref, property_name, property_definition, updateExisting, saveComment)
  def deletePropertyDefinition(self, range_ref, property_name, saveComment=""):
    return self.client.deletePropertyDefinition(range_ref, property_name, saveComment)
  def getZoneFolder(self, range_ref, **kwargs):
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    folder_response = self.client.get("{0}{1}/Folders{2}".format(self.client.baseurl, range_ref, query_string))
    return Folders(self.client).get(folder_response['result']['folder'])
  def deleteZoneFromFolder(self, range_ref, folder_ref="", **kwargs):
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    if folder_ref:
      url = "{0}{1}/{2}{3}".format(self.client.baseurl, range_ref, folder_ref, query_string)
    else:
      url = "{0}{1}/Folders{2}".format(self.client.baseurl, range_ref, query_string)
    return self.client.delete(url)
  def addZoneToFolder(self, range_ref, folder_ref, saveComment=""):
    return Folders(self.client).addToFolder(range_ref, folder_ref, saveComment)
  def getAddressBlocks(self, range_ref):
    all_blocks = []
    range_response = self.client.get("{0}{1}/AddressBlocks".format(self.client.baseurl, range_ref))
    for block in range_response['result']['addressBlocks']:
      all_blocks.append(self.buildAddressBlocks(block))
    return all_blocks
  def getAvailableAddressBlocks(self, range_ref, **kwargs):
    all_blocks = []
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    range_response = self.client.get("{0}{1}/AvailableAddressBlocks{2}".format(self.client.baseurl, range_ref, query))
    for block in range_response['result']['addressBlocks']:
      all_blocks.append(self.buildAddressBlocks(block))
    return all_blocks
  def getInheritAccess(self, range_ref):
    inherit_access_response = self.client.get("{0}{1}/InheritAccess".format(self.client.baseurl, range_ref))
    return inherit_access_response['result']['inheritAccess']
  def getIpamRecords(self, range_ref, **kwargs):
    all_records = []
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    record_response = self.client.get("{0}{1}/IPAMRecords{2}".format(self.client.baseurl, range_ref, query))
    for record in record_response['result']['ipamRecords']:
      all_records.append(IPAMRecords(self.client).build(record))
    return all_records
  def getNextFreeAddress(self, range_ref, **kwargs):
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    address_response = self.client.get("{0}{1}/NextFreeAddress{2}".format(self.client.baseurl, range_ref, query))
    return address_response['result']['address']
  def getStatistics(self, range_ref):
    statistics_response = self.client.get("{0}{1}/Statistics".format(self.client.baseurl, range_ref))
    return self.buildStatistics(statistics_response['result'])
  def getSubranges(self, range_ref, **kwargs):
    all_ranges = []
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    rnage_response = self.client.get("{0}{1}/Subranges{2}".format(self.client.baseurl, range_ref, query))
    for range in range_response['result']['ranges']:
      all_ranges.append(self.build(range))
    return all_ranges


class Interfaces(object):
  def __init__(self, client):
    self.client = client
    self.url_base = "Interfaces"
  def build(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return Interface(**json_input)
  def get(self, interface_ref="", **kwargs):
    all_interfaces = []
    if not interface_ref:
      query_string = ""
      if kwargs:
        for key, value in kwargs.items():
          if not query_string:
            query_string += "?{0}={1}".format(key, value)
          else:
            query_string += "&{0}={1}".format(key, value)
      interface_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, self.url_base, query_string))
      for interface in interface_response['result']['interfaces']:
        all_interfaces.append(self.build(interface))
    else:
      interface_response = self.client.get("{0}{1}".format(self.client.baseurl, interface_ref))
      all_interfaces.append(self.build(interface_response['result']['interface']))
    return all_interfaces
  def add(self, interface_input, saveComment=""):
    if isinstance(interface_input, Interface):
      interface_input = json.loads(interface_input.to_json())
    payload = {
      "saveComment" : saveComment,
      "interface" : interface_input
    }
    interface_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
    interface_return = []
    for ref in interface_json['result']['objRefs']:
      interface_return.append(self.get(ref)[0])
    return interface_return
  def delete(self, interface_ref, **kwargs):
    return self.client.deleteItem(interface_ref, kwargs)
  def update(self, interface_ref, properties, objType="", saveComment="", deleteUnspecified=False):
    return self.client.updateItem(interface_ref, properties, objType, saveComment, deleteUnspecified)
  def getAccess(self, interface_ref, **kwargs):
    return self.client.getItemAccess(interface_ref, kwargs)
  def setAccess(self, interface_ref, identity_access, object_type="", saveComment=""):
    return self.client.setItemAccess(interface_ref, identity_access, object_type, saveComment)
  def getHistory(self, interface_ref, **kwargs):
    return self.client.getItemHistory(interface_ref, kwargs)
  def getPropertyDefinition(self, interface_ref, property_name=""):
    return self.client.getPropertyDefinitions(interface_ref, property_name)
  def addNewPropertyDefinition(self, interface_ref, property_definition, saveComment=""):
    return self.client.newCustomProperty(interface_ref, property_definition, saveComment)
  def updatePropertyDefinition(self, interface_ref, property_name, property_definition, updateExisting="", saveComment=""):
    return self.client.updatePropertyDefinitions(interface_ref, property_name, property_definition, updateExisting, saveComment)
  def deletePropertyDefinition(self, interface_ref, property_name, saveComment=""):
    return self.client.deletePropertyDefinition(interface_ref, property_name, saveComment)


class Devices(object):
  def __init__(self, client):
    self.client = client
    self.url_base = "Devices"
  def build(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return Device(**json_input)
  def get(self, device_ref="", **kwargs):
    all_devices = []
    if not device_ref:
      query_string = ""
      if kwargs:
        for key, value in kwargs.items():
          if not query_string:
            query_string += "?{0}={1}".format(key, value)
          else:
            query_string += "&{0}={1}".format(key, value)
      device_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, self.url_base, query_string))
      for device in device_response['result']['devices']:
        all_devices.append(self.build(device))
    else:
      device_response = self.client.get("{0}{1}".format(self.client.baseurl, device_ref))
      all_devices.append(self.build(device_response['result']['device']))
    return all_devices
  def add(self, device_input, saveComment=""):
    if isinstance(device_input, Device):
      device_input = json.loads(device_input.to_json())
    payload = {
      "saveComment" : saveComment,
      "device" : device_input
    }
    device_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
    device_return = []
    for ref in device_json['result']['objRefs']:
      device_return.append(self.get(ref)[0])
    return device_return
  def delete(self, device_ref, **kwargs):
    return self.client.deleteItem(device_ref, kwargs)
  def update(self, device_ref, properties, objType="", saveComment="", deleteUnspecified=False):
    return self.client.updateItem(device_ref, properties, objType, saveComment, deleteUnspecified)
  def getAccess(self, device_ref, **kwargs):
    return self.client.getItemAccess(device_ref, kwargs)
  def setAccess(self, device_ref, identity_access, object_type="", saveComment=""):
    return self.client.setItemAccess(device_ref, identity_access, object_type, saveComment)
  def getHistory(self, device_ref, **kwargs):
    return self.client.getItemHistory(device_ref, kwargs)
  def getPropertyDefinition(self, device_ref, property_name=""):
    return self.client.getPropertyDefinitions(device_ref, property_name)
  def addNewPropertyDefinition(self, device_ref, property_definition, saveComment=""):
    return self.client.newCustomProperty(device_ref, property_definition, saveComment)
  def updatePropertyDefinition(self, device_ref, property_name, property_definition, updateExisting="", saveComment=""):
    return self.client.updatePropertyDefinitions(device_ref, property_name, property_definition, updateExisting, saveComment)
  def deletePropertyDefinition(self, device_ref, property_name, saveComment=""):
    return self.client.deletePropertyDefinition(device_ref, property_name, saveComment)


class ChangeRequests(object):
  def __init__(self, client):
    self.client = client
    self.url_base = "ChangeRequests"
  def build(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return ChangeRequest(**json_input)
  def get(self, change_ref="", **kwargs):
    all_changes = []
    if not change_ref:
      query_string = ""
      if kwargs:
        for key, value in kwargs.items():
          if not query_string:
            query_string += "?{0}={1}".format(key, value)
          else:
            query_string += "&{0}={1}".format(key, value)
      change_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, self.url_base, query_string))
      for change in change_response['result']['changeRequests']:
        all_changes.append(self.build(change))
    else:
      change_response = self.client.get("{0}{1}".format(self.client.baseurl, change_ref))
      all_changes.append(self.build(change_response['result']['changeRequest']))
    return all_changes
  def add(self, dnsZoneChanges="", dnsRecordChanges="", dhcpScopeChanges="", dhcpReservationChanges="", dhcpExclusionChanges="", dhcpAddressPoolChanges="", dhcpOptionChanges="", customPropertyChanges="", requestDate="", customProperties="", saveComment=""):
    if isinstance(change_input, ChangeRequest):
      change_input = json.loads(change_input.to_json())
    if not isinstance(dnsZoneChanges, list):
      dnsZoneChanges = [dnsZoneChanges]
    if not isinstance(dnsRecordChanges, list):
      dnsRecordChanges = [dnsRecordChanges]
    if not isinstance(dhcpScopeChanges, list):
      dhcpScopeChanges = [dhcpScopeChanges]
    if not isinstance(dhcpReservationChanges, list):
      dhcpReservationChanges = [dhcpReservationChanges]
    if not isinstance(dhcpExclusionChanges, list):
      dhcpExclusionChanges = [dhcpExclusionChanges]
    if not isinstance(dhcpAddressPoolChanges, list):
      dhcpAddressPoolChanges = [dhcpAddressPoolChanges]
    if not isinstance(dhcpOptionChanges, list):
      dhcpOptionChanges = [dhcpOptionChanges]
    if not isinstance(customPropertyChanges, list):
      customPropertyChanges = [customPropertyChanges]
    if not isinstance(customProperties, list):
      customProperties = [customProperties]
    payload = {
      "dnsZoneChanges" : dnsZoneChanges,
      "dnsRecordChanges" : dnsRecordChanges,
      "dhcpScopeChanges" : dhcpScopeChanges,
      "dhcpReservationChanges" : dhcpReservationChanges,
      "dhcpExclusionChanges" : dhcpExclusionChanges,
      "dhcpAddressPoolChanges" : dhcpAddressPoolChanges,
      "dhcpOptionChanges" : dhcpOptionChanges,
      "customPropertyChanges" : customPropertyChanges,
      "requestDate" : requestDate,
      "customProperties" : customProperties,
      "saveComment" : saveComment,
    }
    change_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
    change_return = []
    for ref in change_json['result']['objRefs']:
      change_return.append(self.get(ref)[0])
    return change_return
  def delete(self, change_ref, **kwargs):
    return self.client.deleteItem(change_ref, kwargs)
  def update(self, change_ref, properties, objType="", saveComment="", deleteUnspecified=False):
    return self.client.updateItem(change_ref, properties, objType, saveComment, deleteUnspecified)
  def getAccess(self, change_ref, **kwargs):
    return self.client.getItemAccess(change_ref, kwargs)
  def setAccess(self, change_ref, identity_access, object_type="", saveComment=""):
    return self.client.setItemAccess(change_ref, identity_access, object_type, saveComment)
  def getHistory(self, change_ref, **kwargs):
    return self.client.getItemHistory(change_ref, kwargs)
  def getPropertyDefinition(self, change_ref, property_name=""):
    return self.client.getPropertyDefinitions(change_ref, property_name)
  def addNewPropertyDefinition(self, change_ref, property_definition, saveComment=""):
    return self.client.newCustomProperty(change_ref, property_definition, saveComment)
  def updatePropertyDefinition(self, change_ref, property_name, property_definition, updateExisting="", saveComment=""):
    return self.client.updatePropertyDefinitions(change_ref, property_name, property_definition, updateExisting, saveComment)
  def deletePropertyDefinition(self, change_ref, property_name, saveComment=""):
    return self.client.deletePropertyDefinition(change_ref, property_name, saveComment)


class Folders(object):
  def __init__(self, client):
    self.client = client
    self.url_base = "Folders"
  def build(self, json_input):
    if isinstance(json_input, basestring):
      json_input = json.loads(json_input)
    return Folder(**json_input)
  def get(self, folder_ref="", **kwargs):
    all_folders = []
    if not folder_ref:
      query_string = ""
      if kwargs:
        for key, value in kwargs.items():
          if not query_string:
            query_string += "?{0}={1}".format(key, value)
          else:
            query_string += "&{0}={1}".format(key, value)
      folder_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, self.url_base, query_string))
      for folder in folder_response['result']['folders']:
        all_folders.append(self.build(folder))
    else:
      folder_response = self.client.get("{0}{1}".format(self.client.baseurl, folder_ref))
      all_folders.append(self.build(folder_response['result']['folder']))
    return all_folders
  def add(self, folder_input, saveComment=""):
    print(folder_input)
    print(isinstance(folder_input, Folder))
    if isinstance(folder_input, Folder):
      folder_input = json.loads(folder_input.to_json())
    payload = {
      "saveComment" : saveComment,
      "folder" : folder_input
    }
    folder_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
    print(folder_json)
    folder_return = self.get(folder_json['result']['ref'])
    return folder_return[0]
  def delete(self, folder_ref, **kwargs):
    return self.client.deleteItem(folder_ref, kwargs)
  def update(self, folder_ref, properties, objType="Folder", saveComment="", deleteUnspecified=False):
    return self.client.updateItem(folder_ref, properties, objType, saveComment, deleteUnspecified)
  def getAccess(self, folder_ref, **kwargs):
    return self.client.getItemAccess(folder_ref, kwargs)
  def setAccess(self, folder_ref, identity_access, object_type="", saveComment=""):
    return self.client.setItemAccess("{0}/{1}".format(self.url_base, folder_ref), identity_access, object_type, saveComment)
  def getHistory(self, folder_ref, **kwargs):
    return self.client.getItemHistory(folder_ref, kwargs)
  def getObjectFolder(self, ref, **kwargs):
    query_string = ""
    if kwargs:
      for key, value in kwargs.items():
        if not query_string:
          query_string += "?{0}={1}".format(key, value)
        else:
          query_string += "&{0}={1}".format(key, value)
    url = "{0}{1}/{2}/{3}{4}".format(self.client.baseurl, self.url_base, ref, self.url_base, query_string)
    folder_response = self.client.get(url)
    return_val = ""
    if isinstance(folder_response, basestring):
      return_val = folder_response
    else:
      return_val = self.getFolder(folder_response['result']['folder'])
    return return_val
  def deleteObjectFolder(self, ref, folder_ref="", **kwargs):
    url = ""
    if not folder_ref:
      url = "{0}/{1}/{2}".format(self.url_base, ref, self.url_base)
    else:
      url = "{0}/{1}/{2}".format(self.url_base, ref, folder_ref)
    return self.client.deleteItem(url, kwargs)
  def addToFolder(self, ref, folder_ref, saveComment=""):
    payload = {
      "saveComment" : saveComment
    }
    return self.client.put("{0}{1}/{2}".format(self.client.baseurl, ref, folder_ref), payload, True)
  def getAllObjects(self, folder_ref):
    object_json = self.client.get("{0}{1}/Objects".format(self.client.baseurl, folder_ref))
    all_objects = []
    for o in object_json['result']['objects']:
      all_objects.append(getattr(self.client, o['objType']).get(o['ref'])[0])
    return all_objects
  def getPropertyDefinition(self, folder_ref, property_name=""):
    return self.client.getPropertyDefinitions(folder_ref, property_name)
  def addNewPropertyDefinition(self, folder_ref, property_definition, saveComment=""):
    return self.client.newCustomProperty(folder_ref, property_definition, saveComment)
  def updatePropertyDefinition(self, folder_ref, property_name, property_definition, updateExisting="", saveComment=""):
    return self.client.updatePropertyDefinitions(folder_ref, property_name, property_definition, updateExisting, saveComment)
  def deletePropertyDefinition(self, folder_ref, property_name, saveComment=""):
    return self.client.deletePropertyDefinition(folder_ref, property_name, saveComment)