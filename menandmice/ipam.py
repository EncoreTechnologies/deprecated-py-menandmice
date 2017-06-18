from menandmice.base import BaseObject
from menandmice.base import BaseService


class IPAMRecord(BaseObject):
    def __init__(self, *args, **kwargs):
        super(IPAMRecord, self).__init__(*args, **kwargs)
        self.add_key('addrRef')
        self.add_key('address')
        self.add_key('claimed')
        self.add_key('dnsHosts')
        self.add_key('dhcpReservations')
        self.add_key('dhcpLeases')
        self.add_key('discoveryType')
        self.add_key('lastSeenDate')
        self.add_key('lastDiscoveryDate')
        self.add_key('lastKnownClientIdentifier')
        self.add_key('device')
        self.add_key('interface')
        self.add_key('ptrStatus')
        self.add_key('extraneousPTR')
        self.add_key('customProperties')
        self.add_key('state')
        self.add_key('usage')


class Range(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Range, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('from')
        self.add_key('to')
        self.add_key('parentRef')
        self.add_key('adSiteRef')
        self.add_key('childRanges')
        self.add_key('dhcpScopes')
        self.add_key('subnet')
        self.add_key('locked')
        self.add_key('autoAssign')
        self.add_key('hasSchedule')
        self.add_key('hasMonitor')
        self.add_key('customProperties')
        self.add_key('inheritAccess')
        self.add_key('isContainer')
        self.add_key('utilizationPercentage')
        self.add_key('hasRogueAddresses')
        self.add_key('cloudNetworkRef')
        self.add_key('cloudAllocationPools')
        self.add_key('discoveredProperties')
        self.add_key('creationTime')


class Discovery(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Discovery, self).__init__(*args, **kwargs)
        self.add_key('interval')
        self.add_key('unit')
        self.add_key('enabled')
        self.add_key('startTime')


class AddressBlock(BaseObject):
    def __init__(self, *args, **kwargs):
        super(AddressBlock, self).__init__(*args, **kwargs)
        self.add_key('from')
        self.add_key('to')


class GetRangeStatisticsResponse(BaseObject):
    def __init__(self, *args, **kwargs):
        super(GetRangeStatisticsResponse, self).__init__(*args, **kwargs)
        self.add_key('used')
        self.add_key('free')
        self.add_key('numInSubranges')
        self.add_key('percentInSubranges')


class Interface(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Interface, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('clientIdentifier')
        self.add_key('addresses')
        self.add_key('customProperties')
        self.add_key('deviceRef')


class Device(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Device, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('customProperties')
        self.add_key('interfaces')


class ChangeRequest(BaseObject):
    def __init__(self, *args, **kwargs):
        super(ChangeRequest, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('requester')
        self.add_key('state')
        self.add_key('creationDate')
        self.add_key('objType')
        self.add_key('requestDate')
        self.add_key('customProperties')
        self.add_key('saveComment')
        self.add_key('processedDate')
        self.add_key('dnsZoneChanges')
        self.add_key('dnsRecordChanges')
        self.add_key('dhcpScopeChanges')
        self.add_key('dhcpReservationChanges')
        self.add_key('dhcpExclusionChanges')
        self.add_key('dhcpAddressPoolChanges')
        self.add_key('dhcpOptionChanges')
        self.add_key('customPropertyChanges')


class Folder(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Folder, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('contentType')
        self.add_key('parentRef')


class IPAMRecords(BaseService):
    def __init__(self, client):
        super(IPAMRecords, self).__init__(client=client,
                                          url_base="IPAMRecords",
                                          entity_class=IPAMRecord,
                                          get_response_entity_key="ipamRecord",
                                          get_response_all_key="ipamRecords",
                                          get_is_singular=True,
                                          ref_key="addrRef")

    def pingRecord(self, ipam_record):
        addr_ref = self.ref_or_raise(ipam_record, key=self.ref_key)
        return self.client.post("{0}{1}/Ping".format(self.client.baseurl,
                                                     addr_ref),
                                "")

    def getRecordRange(self, ipam_record):
        addr_ref = self.ref_or_raise(ipam_record, key=self.ref_key)
        range_response = self.client.get("{0}{1}/Range".format(self.client.baseurl,
                                                               addr_ref))
        return Range(range_response['result']['range'])


class Ranges(BaseService):
    def __init__(self, client):
        super(Ranges, self).__init__(client=client,
                                     url_base="Ranges",
                                     entity_class=Range,
                                     get_response_entity_key="range",
                                     get_response_all_key="ranges")

    def add(self, range_, discovery="", saveComment=""):
        payload = {
            "discovery": discovery,
            "saveComment": saveComment,
            "range": range_
        }
        range_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                      self.url_base),
                                      payload)
        range_return = self.get(range_json['result']['ref'])
        return range_return[0]

    def getZoneFolder(self, range_, **kwargs):
        range_ref = self.ref_or_raise(range_)
        query_string = self.make_query_str(**kwargs)
        folder_response = self.client.get("{0}{1}/Folders{2}".format(self.client.baseurl,
                                                                     range_ref,
                                                                     query_string))
        return Folders(self.client).get(folder_response['result']['folder'])

    def deleteZoneFromFolder(self, range_, folder="", **kwargs):
        range_ref = self.ref_or_raise(range_)
        folder_ref = self.ref_or_raise(folder)
        query_string = self.make_query_str(**kwargs)
        if folder_ref:
            url = "{0}{1}/{2}{3}".format(self.client.baseurl,
                                         range_ref,
                                         folder_ref,
                                         query_string)
        else:
            url = "{0}{1}/Folders{2}".format(self.client.baseurl,
                                             range_ref,
                                             query_string)
        return self.client.delete(url)

    def addZoneToFolder(self, range_, folder, saveComment=""):
        range_ref = self.ref_or_raise(range_)
        folder_ref = self.ref_or_raise(folder)
        return Folders(self.client).addToFolder(range_ref, folder_ref, saveComment)

    def getAddressBlocks(self, range_):
        range_ref = self.ref_or_raise(range_)
        all_blocks = []
        range_response = self.client.get("{0}{1}/AddressBlocks".format(self.client.baseurl,
                                                                       range_ref))
        for block in range_response['result']['addressBlocks']:
            all_blocks.append(AddressBlock(block))
        return all_blocks

    def getAvailableAddressBlocks(self, range_, **kwargs):
        range_ref = self.ref_or_raise(range_)
        all_blocks = []
        query_string = self.make_query_str(**kwargs)
        range_response = self.client.get(
            "{0}{1}/AvailableAddressBlocks{2}".format(self.client.baseurl,
                                                      range_ref,
                                                      query_string))
        for block in range_response['result']['addressBlocks']:
            all_blocks.append(AddressBlock(block))
        return all_blocks

    def getInheritAccess(self, range_):
        range_ref = self.ref_or_raise(range_)
        inherit_access_response = self.client.get(
            "{0}{1}/InheritAccess".format(self.client.baseurl,
                                          range_ref))
        return inherit_access_response['result']['inheritAccess']

    def getIpamRecords(self, range_, **kwargs):
        range_ref = self.ref_or_raise(range_)
        all_records = []
        query_string = self.make_query_str(**kwargs)
        record_response = self.client.get("{0}{1}/IPAMRecords{2}".format(self.client.baseurl,
                                                                         range_ref,
                                                                         query_string))
        for record in record_response['result']['ipamRecords']:
            all_records.append(IPAMRecord(record))
        return all_records

    def getNextFreeAddress(self, range_, **kwargs):
        range_ref = self.ref_or_raise(range_)
        query_string = ""
        query_string = self.make_query_str(**kwargs)
        address_response = self.client.get(
            "{0}{1}/NextFreeAddress{2}".format(self.client.baseurl,
                                               range_ref,
                                               query_string))
        return address_response['result']['address']

    def getStatistics(self, range_):
        range_ref = self.ref_or_raise(range_)
        statistics_response = self.client.get(
            "{0}{1}/Statistics".format(self.client.baseurl, range_ref))
        return GetRangeStatisticsResponse(statistics_response['result'])

    def getSubranges(self, range_, **kwargs):
        range_ref = self.ref_or_raise(range_)
        all_ranges = []
        query_string = self.make_query_str(**kwargs)
        range_response = self.client.get(
            "{0}{1}/Subranges{2}".format(self.client.baseurl,
                                         range_ref,
                                         query_string))
        for range_ in range_response['result']['ranges']:
            all_ranges.append(Range(range_))
        return all_ranges


class Interfaces(BaseService):
    def __init__(self, client):
        super(Interfaces, self).__init__(client=client,
                                         url_base="Interfaces",
                                         entity_class=Interface,
                                         get_response_entity_key="interface",
                                         get_response_all_key="interfaces")

    def add(self, interface, saveComment=""):
        payload = {
            "saveComment": saveComment,
            "interface": interface
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

    def add(self, device, saveComment=""):
        payload = {
            "saveComment": saveComment,
            "device": device
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

    def add(self, folder, saveComment=""):
        payload = {
            "saveComment": saveComment,
            "folder": folder
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

    def deleteObjectFolder(self, ref, folder="", **kwargs):
        folder_ref = self.ref_or_raise(folder)
        url = ""
        if not folder_ref:
            url = "{0}/{1}/{2}".format(self.url_base, ref, self.url_base)
        else:
            url = "{0}/{1}/{2}".format(self.url_base, ref, folder_ref)
        return self.client.deleteItem(url, **kwargs)

    def addToFolder(self, ref, folder, saveComment=""):
        folder_ref = self.ref_or_raise(folder)
        payload = {
            "saveComment": saveComment
        }
        return self.client.put("{0}{1}/{2}".format(self.client.baseurl,
                                                   ref,
                                                   folder_ref),
                               payload,
                               True)

    def getAllObjects(self, folder):
        folder_ref = self.ref_or_raise(folder)
        object_json = self.client.get("{0}{1}/Objects".format(self.client.baseurl,
                                                              folder_ref))
        all_objects = []
        for o in object_json['result']['objects']:
            all_objects.append(getattr(self.client, o['objType']).get(o['ref'])[0])
        return all_objects
