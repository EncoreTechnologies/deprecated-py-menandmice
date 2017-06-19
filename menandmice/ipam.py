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

    def ping_record(self, ipam_record):
        addr_ref = self.ref_or_raise(ipam_record, key=self.ref_key)
        return self.client.post("{0}{1}/Ping".format(self.client.baseurl,
                                                     addr_ref),
                                "")

    def get_record_range(self, ipam_record):
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

    def add(self, range_, discovery="", save_comment=""):
        payload = {
            "discovery": discovery,
            "saveComment": save_comment,
            "range": range_
        }
        range_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                      self.url_base),
                                      payload)
        range_return = self.get(range_json['result']['ref'])
        return range_return[0]

    def get_range_folder(self, range_, **kwargs):
        range_ref = self.ref_or_raise(range_)
        query_string = self.make_query_str(**kwargs)
        folder_response = self.client.get("{0}{1}/Folders{2}".format(self.client.baseurl,
                                                                     range_ref,
                                                                     query_string))
        return Folders(self.client).get(folder_response['result']['folder'])

    def delete_range_from_folder(self, range_, folder="", **kwargs):
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

    def add_range_to_folder(self, range_, folder, save_comment=""):
        range_ref = self.ref_or_raise(range_)
        folder_ref = self.ref_or_raise(folder)
        return Folders(self.client).add_to_folder(range_ref, folder_ref, save_comment)

    def get_address_blocks(self, range_):
        range_ref = self.ref_or_raise(range_)
        all_blocks = []
        range_response = self.client.get("{0}{1}/AddressBlocks".format(self.client.baseurl,
                                                                       range_ref))
        for block in range_response['result']['addressBlocks']:
            all_blocks.append(AddressBlock(block))
        return all_blocks

    def get_available_address_blocks(self, range_, **kwargs):
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

    def get_inherit_access(self, range_):
        range_ref = self.ref_or_raise(range_)
        inherit_access_response = self.client.get(
            "{0}{1}/InheritAccess".format(self.client.baseurl,
                                          range_ref))
        return inherit_access_response['result']['inheritAccess']

    def get_ipam_records(self, range_, **kwargs):
        range_ref = self.ref_or_raise(range_)
        all_records = []
        query_string = self.make_query_str(**kwargs)
        record_response = self.client.get("{0}{1}/IPAMRecords{2}".format(self.client.baseurl,
                                                                         range_ref,
                                                                         query_string))
        for record in record_response['result']['ipamRecords']:
            all_records.append(IPAMRecord(record))
        return all_records

    def get_next_free_address(self, range_, **kwargs):
        range_ref = self.ref_or_raise(range_)
        query_string = ""
        query_string = self.make_query_str(**kwargs)
        address_response = self.client.get(
            "{0}{1}/NextFreeAddress{2}".format(self.client.baseurl,
                                               range_ref,
                                               query_string))
        return address_response['result']['address']

    def get_statistics(self, range_):
        range_ref = self.ref_or_raise(range_)
        statistics_response = self.client.get(
            "{0}{1}/Statistics".format(self.client.baseurl, range_ref))
        return GetRangeStatisticsResponse(statistics_response['result'])

    def get_subranges(self, range_, **kwargs):
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

    def add(self, interface, save_comment=""):
        payload = {
            "saveComment": save_comment,
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

    def add(self, device, save_comment=""):
        payload = {
            "saveComment": save_comment,
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

    def add(self,
            dns_zone_changes="",
            dns_record_changes="",
            dhcp_scope_changes="",
            dhcp_reservation_changes="",
            dhcp_exclusion_changes="",
            dhcp_address_pool_changes="",
            dhcp_option_changes="",
            custom_property_changes="",
            request_date="",
            custom_properties="",
            save_comment=""):
        if not isinstance(dns_zone_changes, list):
            dns_zone_changes = [dns_zone_changes]
        if not isinstance(dns_record_changes, list):
            dns_record_changes = [dns_record_changes]
        if not isinstance(dhcp_scope_changes, list):
            dhcp_scope_changes = [dhcp_scope_changes]
        if not isinstance(dhcp_reservation_changes, list):
            dhcp_reservation_changes = [dhcp_reservation_changes]
        if not isinstance(dhcp_exclusion_changes, list):
            dhcp_exclusion_changes = [dhcp_exclusion_changes]
        if not isinstance(dhcp_address_pool_changes, list):
            dhcp_address_pool_changes = [dhcp_address_pool_changes]
        if not isinstance(dhcp_option_changes, list):
            dhcp_option_changes = [dhcp_option_changes]
        if not isinstance(custom_property_changes, list):
            custom_property_changes = [custom_property_changes]
        if not isinstance(custom_properties, list):
            custom_properties = [custom_properties]
        payload = {
            "dnsZoneChanges": dns_zone_changes,
            "dnsRecordChanges": dns_record_changes,
            "dhcpScopeChanges": dhcp_scope_changes,
            "dhcpReservationChanges": dhcp_reservation_changes,
            "dhcpExclusionChanges": dhcp_exclusion_changes,
            "dhcpAddressPoolChanges": dhcp_address_pool_changes,
            "dhcpOptionChanges": dhcp_option_changes,
            "customPropertyChanges": custom_property_changes,
            "requestDate": request_date,
            "customProperties": custom_properties,
            "saveComment": save_comment,
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

    def add(self, folder, save_comment=""):
        payload = {
            "saveComment": save_comment,
            "folder": folder
        }
        folder_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                       self.url_base),
                                       payload)
        folder_return = self.get(folder_json['result']['ref'])
        return folder_return[0]

    def get_object_folder(self, ref, **kwargs):
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

    def delete_object_folder(self, ref, folder="", **kwargs):
        folder_ref = self.ref_or_raise(folder)
        url = ""
        if not folder_ref:
            url = "{0}/{1}/{2}".format(self.url_base, ref, self.url_base)
        else:
            url = "{0}/{1}/{2}".format(self.url_base, ref, folder_ref)
        return self.client.delete_item(url, **kwargs)

    def add_to_folder(self, ref, folder, save_comment=""):
        folder_ref = self.ref_or_raise(folder)
        payload = {
            "saveComment": save_comment
        }
        return self.client.put("{0}{1}/{2}".format(self.client.baseurl,
                                                   ref,
                                                   folder_ref),
                               payload,
                               True)

    def get_all_objects(self, folder):
        folder_ref = self.ref_or_raise(folder)
        object_json = self.client.get("{0}{1}/Objects".format(self.client.baseurl,
                                                              folder_ref))
        all_objects = []
        for o in object_json['result']['objects']:
            all_objects.append(getattr(self.client, o['objType']).get(o['ref'])[0])
        return all_objects
