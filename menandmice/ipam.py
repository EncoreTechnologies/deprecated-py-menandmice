import json

from menandmice.base import BaseObject
from menandmice.base import BaseService


class IPAMRecord(BaseObject):
    def __init__(self, **kwargs):
        self.addrRef = self.get_value('addrRef', kwargs)
        self.address = self.get_value('address', kwargs)
        self.claimed = self.get_value('claimed', kwargs)
        self.dnsHosts = self.get_value('dnsHosts', kwargs)
        self.dhcpReservations = self.get_value('dhcpReservations', kwargs)
        self.dhcpLeases = self.get_value('dhcpLeases', kwargs)
        self.discoveryType = self.get_value('discoveryType', kwargs)
        self.lastSeenDate = self.get_value('lastSeenDate', kwargs)
        self.lastDiscoveryDate = self.get_value('lastDiscoveryDate', kwargs)
        self.lastKnownClientIdentifier = self.get_value('lastKnownClientIdentifier', kwargs)
        self.device = self.get_value('device', kwargs)
        self.interface = self.get_value('interface', kwargs)
        self.ptrStatus = self.get_value('ptrStatus', kwargs)
        self.extraneousPTR = self.get_value('extraneousPTR', kwargs)
        self.customProperties = self.get_value('customProperties', kwargs)
        self.state = self.get_value('state', kwargs)
        self.usage = self.get_value('usage', kwargs)


class Range(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.name = self.get_value('name', kwargs)
        self.from_ = self.get_value('from', kwargs)
        self.to = self.get_value('to', kwargs)
        self.parentRef = self.get_value('parentRef', kwargs)
        self.adSiteRef = self.get_value('adSiteRef', kwargs)
        self.childRanges = self.get_value('childRanges', kwargs)
        self.dhcpScopes = self.get_value('dhcpScopes', kwargs)
        self.subnet = self.get_value('subnet', kwargs)
        self.locked = self.get_value('locked', kwargs)
        self.autoAssign = self.get_value('autoAssign', kwargs)
        self.hasSchedule = self.get_value('hasSchedule', kwargs)
        self.hasMonitor = self.get_value('hasMonitor', kwargs)
        self.customProperties = self.get_value('customProperties', kwargs)
        self.inheritAccess = self.get_value('inheritAccess', kwargs)
        self.isContainer = self.get_value('isContainer', kwargs)
        self.utilizationPercentage = self.get_value('utilizationPercentage', kwargs)
        self.hasRogueAddresses = self.get_value('hasRogueAddresses', kwargs)
        self.cloudNetworkRef = self.get_value('cloudNetworkRef', kwargs)
        self.cloudAllocationPools = self.get_value('cloudAllocationPools', kwargs)
        self.discoveredProperties = self.get_value('discoveredProperties', kwargs)
        self.creationTime = self.get_value('creationTime', kwargs)


class Discovery(BaseObject):
    def __init__(self, **kwargs):
        self.interval = self.get_value('interval', kwargs)
        self.unit = self.get_value('unit', kwargs)
        self.enabled = self.get_value('enabled', kwargs)
        self.startTime = self.get_value('startTime', kwargs)


class AddressBlock(BaseObject):
    def __init__(self, **kwargs):
        self.from_ = self.get_value('from', kwargs)
        self.to = self.get_value('to', kwargs)


class GetRangeStatisticsResponse(BaseObject):
    def __init__(self, **kwargs):
        self.used = self.get_value('used', kwargs)
        self.free = self.get_value('free', kwargs)
        self.numInSubranges = self.get_value('numInSubranges', kwargs)
        self.percentInSubranges = self.get_value('percentInSubranges', kwargs)


class Interface(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.name = self.get_value('name', kwargs)
        self.clientIdentifier = self.get_value('clientIdentifier', kwargs)
        self.addresses = self.get_value('addresses', kwargs)
        self.customProperties = self.get_value('customProperties', kwargs)
        self.deviceRef = self.get_value('deviceRef', kwargs)


class Device(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.name = self.get_value('name', kwargs)
        self.customProperties = self.get_value('customProperties', kwargs)
        self.interfaces = self.get_value('interfaces', kwargs)


class ChangeRequest(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.requester = self.get_value('requester', kwargs)
        self.state = self.get_value('state', kwargs)
        self.creationDate = self.get_value('creationDate', kwargs)
        self.objType = self.get_value('objType', kwargs)
        self.requestDate = self.get_value('requestDate', kwargs)
        self.customProperties = self.get_value('customProperties', kwargs)
        self.saveComment = self.get_value('saveComment', kwargs)
        self.processedDate = self.get_value('processedDate', kwargs)
        self.dnsZoneChanges = self.get_value('dnsZoneChanges', kwargs)
        self.dnsRecordChanges = self.get_value('dnsRecordChanges', kwargs)
        self.dhcpScopeChanges = self.get_value('dhcpScopeChanges', kwargs)
        self.dhcpReservationChanges = self.get_value('dhcpReservationChanges', kwargs)
        self.dhcpExclusionChanges = self.get_value('dhcpExclusionChanges', kwargs)
        self.dhcpAddressPoolChanges = self.get_value('dhcpAddressPoolChanges', kwargs)
        self.dhcpOptionChanges = self.get_value('dhcpOptionChanges', kwargs)
        self.customPropertyChanges = self.get_value('customPropertyChanges', kwargs)


class Folder(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.name = self.get_value('name', kwargs)
        self.contentType = self.get_value('contentType', kwargs)
        self.parentRef = self.get_value('parentRef', kwargs)


class IPAMRecords(BaseObject):
    def __init__(self, client):
        super(IPAMRecords, self).__init__(client=client,
                                          url_base="IPAMRecords",
                                          entity_class=IPAMRecord,
                                          get_response_entity_key="ipamRecord",
                                          get_response_all_key="ipamRecords",
                                          get_is_singular=True)

    def pingRecord(self, address_ref):
        return self.client.post("{0}{1}/Ping".format(self.client.baseurl, address_ref), "")

    def getRecordRange(self, address_ref):
        range_response = self.client.get("{0}{1}/Range".format(self.client.baseurl, address_ref))
        return Ranges(self.client).build(range_response['result']['range'])


class Ranges(BaseService):
    def __init__(self, client):
        super(Ranges, self).__init__(client=client,
                                     url_base="Ranges",
                                     entity_class=Range,
                                     get_response_entity_key="range",
                                     get_response_all_key="ranges")

    def buildAddressBlocks(self, json_input):
        return self.json_to_class(json_input, AddressBlock)

    def buildStatistics(self, json_input):
        return self.json_to_class(json_input, GetRangeStatisticsResponse)

    def add(self, range_input, discovery="", saveComment=""):
        if isinstance(range_input, Range):
            range_input = json.loads(range_input.to_json())
        if discovery:
            if isinstance(discovery, Discovery):
                discovery = json.loads(discovery.to_json())
        payload = {
            "discovery": discovery,
            "saveComment": saveComment,
            "range": range_input
        }
        range_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                      self.url_base),
                                      payload)
        range_return = self.get(range_json['result']['ref'])
        return range_return[0]

    def getZoneFolder(self, range_ref, **kwargs):
        query_string = self.make_query_str(**kwargs)
        folder_response = self.client.get("{0}{1}/Folders{2}".format(self.client.baseurl,
                                                                     range_ref,
                                                                     query_string))
        return Folders(self.client).get(folder_response['result']['folder'])

    def deleteZoneFromFolder(self, range_ref, folder_ref="", **kwargs):
        query_string = self.make_query_str(**kwargs)
        if folder_ref:
            url = "{0}{1}/{2}{3}".format(self.client.baseurl, range_ref, folder_ref, query_string)
        else:
            url = "{0}{1}/Folders{2}".format(self.client.baseurl, range_ref, query_string)
        return self.client.delete(url)

    def addZoneToFolder(self, range_ref, folder_ref, saveComment=""):
        return Folders(self.client).addToFolder(range_ref, folder_ref, saveComment)

    def getAddressBlocks(self, range_ref):
        all_blocks = []
        range_response = self.client.get("{0}{1}/AddressBlocks".format(self.client.baseurl,
                                                                       range_ref))
        for block in range_response['result']['addressBlocks']:
            all_blocks.append(self.buildAddressBlocks(block))
        return all_blocks

    def getAvailableAddressBlocks(self, range_ref, **kwargs):
        all_blocks = []
        query_string = self.make_query_str(**kwargs)
        range_response = self.client.get(
            "{0}{1}/AvailableAddressBlocks{2}".format(self.client.baseurl,
                                                      range_ref,
                                                      query_string))
        for block in range_response['result']['addressBlocks']:
            all_blocks.append(self.buildAddressBlocks(block))
        return all_blocks

    def getInheritAccess(self, range_ref):
        inherit_access_response = self.client.get(
            "{0}{1}/InheritAccess".format(self.client.baseurl,
                                          range_ref))
        return inherit_access_response['result']['inheritAccess']

    def getIpamRecords(self, range_ref, **kwargs):
        all_records = []
        query_string = self.make_query_str(**kwargs)
        record_response = self.client.get("{0}{1}/IPAMRecords{2}".format(self.client.baseurl,
                                                                         range_ref,
                                                                         query_string))
        for record in record_response['result']['ipamRecords']:
            all_records.append(IPAMRecords(self.client).build(record))
        return all_records

    def getNextFreeAddress(self, range_ref, **kwargs):
        query_string = ""
        query_string = self.make_query_str(**kwargs)
        address_response = self.client.get(
            "{0}{1}/NextFreeAddress{2}".format(self.client.baseurl,
                                               range_ref,
                                               query_string))
        return address_response['result']['address']

    def getStatistics(self, range_ref):
        statistics_response = self.client.get(
            "{0}{1}/Statistics".format(self.client.baseurl, range_ref))
        return self.buildStatistics(statistics_response['result'])

    def getSubranges(self, range_ref, **kwargs):
        all_ranges = []
        query_string = self.make_query_str(**kwargs)
        range_response = self.client.get(
            "{0}{1}/Subranges{2}".format(self.client.baseurl,
                                         range_ref,
                                         query_string))
        for range in range_response['result']['ranges']:
            all_ranges.append(self.build(range))
        return all_ranges


class Interfaces(BaseService):
    def __init__(self, client):
        super(Interfaces, self).__init__(client=client,
                                         url_base="Interfaces",
                                         entity_class=Interface,
                                         get_response_entity_key="interface",
                                         get_response_all_key="interfaces")

    def add(self, interface_input, saveComment=""):
        if isinstance(interface_input, Interface):
            interface_input = json.loads(interface_input.to_json())
        payload = {
            "saveComment": saveComment,
            "interface": interface_input
        }
        interface_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                          self.url_base),
                                          payload)
        interface_return = []
        for ref in interface_json['result']['objRefs']:
            interface_return.append(self.get(ref)[0])
        return interface_return


class Devices(BaseService):
    def __init__(self, client):
        super(Devices, self).__init__(client=client,
                                      url_base="Devices",
                                      entity_class=Device,
                                      get_response_entity_key="device",
                                      get_response_all_key="devices")

    def add(self, device_input, saveComment=""):
        if isinstance(device_input, Device):
            device_input = json.loads(device_input.to_json())
        payload = {
            "saveComment": saveComment,
            "device": device_input
        }
        device_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                       self.url_base),
                                       payload)
        device_return = []
        for ref in device_json['result']['objRefs']:
            device_return.append(self.get(ref)[0])
        return device_return


class ChangeRequests(BaseService):
    def __init__(self, client):
        super(ChangeRequests, self).__init__(client=client,
                                             url_base="ChangeRequests",
                                             entity_class=ChangeRequest,
                                             get_response_entity_key="changeRequest",
                                             get_response_all_key="changeRequests")

    def add(self, dnsZoneChanges="",
            dnsRecordChanges="",
            dhcpScopeChanges="",
            dhcpReservationChanges="",
            dhcpExclusionChanges="",
            dhcpAddressPoolChanges="",
            dhcpOptionChanges="",
            customPropertyChanges="",
            requestDate="",
            customProperties="",
            saveComment=""):
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
            "dnsZoneChanges": dnsZoneChanges,
            "dnsRecordChanges": dnsRecordChanges,
            "dhcpScopeChanges": dhcpScopeChanges,
            "dhcpReservationChanges": dhcpReservationChanges,
            "dhcpExclusionChanges": dhcpExclusionChanges,
            "dhcpAddressPoolChanges": dhcpAddressPoolChanges,
            "dhcpOptionChanges": dhcpOptionChanges,
            "customPropertyChanges": customPropertyChanges,
            "requestDate": requestDate,
            "customProperties": customProperties,
            "saveComment": saveComment,
        }
        change_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                       self.url_base),
                                       payload)
        change_return = []
        for ref in change_json['result']['objRefs']:
            change_return.append(self.get(ref)[0])
        return change_return


class Folders(BaseService):
    def __init__(self, client):
        super(Folders, self).__init__(client=client,
                                      url_base="Folders",
                                      entity_class=Folder,
                                      get_response_entity_key="folder",
                                      get_response_all_key="folders")

    def add(self, folder_input, saveComment=""):
        if isinstance(folder_input, Folder):
            folder_input = json.loads(folder_input.to_json())
        payload = {
            "saveComment": saveComment,
            "folder": folder_input
        }
        folder_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                       self.url_base),
                                       payload)
        folder_return = self.get(folder_json['result']['ref'])
        return folder_return[0]

    def getObjectFolder(self, ref, **kwargs):
        query_string = self.make_query_str(**kwargs)
        url = "{0}{1}/{2}/{3}{4}".format(self.client.baseurl,
                                         self.url_base,
                                         ref,
                                         self.url_base,
                                         query_string)
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
            "saveComment": saveComment
        }
        return self.client.put("{0}{1}/{2}".format(self.client.baseurl,
                                                   ref,
                                                   folder_ref),
                               payload,
                               True)

    def getAllObjects(self, folder_ref):
        object_json = self.client.get("{0}{1}/Objects".format(self.client.baseurl, folder_ref))
        all_objects = []
        for o in object_json['result']['objects']:
            all_objects.append(getattr(self.client, o['objType']).get(o['ref'])[0])
        return all_objects
