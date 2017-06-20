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

import requests
import pprint
import json
import logging

from menandmice.base import BaseObject

from menandmice.dns import DNSGenerateDirective
from menandmice.dns import DNSRecord
from menandmice.dns import DNSRecords
from menandmice.dns import DNSView
from menandmice.dns import DNSViews
from menandmice.dns import DNSZone
from menandmice.dns import DNSZoneOptions
from menandmice.dns import DNSZones

from menandmice.ipam import AddressBlock
from menandmice.ipam import ChangeRequest
from menandmice.ipam import ChangeRequests
from menandmice.ipam import Device
from menandmice.ipam import Devices
from menandmice.ipam import Discovery
from menandmice.ipam import Folder
from menandmice.ipam import Folders
from menandmice.ipam import GetRangeStatisticsResponse
from menandmice.ipam import Interface
from menandmice.ipam import Interfaces
from menandmice.ipam import IPAMRecord
from menandmice.ipam import IPAMRecords
from menandmice.ipam import Range
from menandmice.ipam import Ranges

from menandmice.users import Group
from menandmice.users import Groups
from menandmice.users import Role
from menandmice.users import Roles
from menandmice.users import User
from menandmice.users import Users


class AccessEntry(BaseObject):
    def __init__(self, *args, **kwargs):
        super(AccessEntry, self).__init__(*args, **kwargs)
        self.add_key('name')
        self.add_key('access')


class IdentityAccess(BaseObject):
    def __init__(self, *args, **kwargs):
        super(IdentityAccess, self).__init__(*args, **kwargs)
        self.add_key('identityRef')
        self.add_key('identityName')
        self.add_key('accessEntries', [AccessEntry()])


class ObjectAccess(BaseObject):
    def __init__(self, *args, **kwargs):
        super(ObjectAccess, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('identityAccess', [IdentityAccess()])


class Event(BaseObject):
    def __init__(self, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)
        self.add_key('eventType')
        self.add_key('objType')
        self.add_key('objRef')
        self.add_key('objName')
        self.add_key('timestamp')
        self.add_key('username')
        self.add_key('saveComment')
        self.add_key('eventText')


class PropertyDefinition(BaseObject):
    def __init__(self, *args, **kwargs):
        super(PropertyDefinition, self).__init__(*args, **kwargs)
        self.add_key('name')
        self.add_key('type')
        self.add_key('system')
        self.add_key('mandatory')
        self.add_key('readOnly')
        self.add_key('multiLine')
        self.add_key('defaultValue')
        self.add_key('listItems')
        self.add_key('parentProperty')


class Client(BaseObject):
    def __init__(self, server, username, password):
        self.baseurl = "http://{0}/mmws/api/".format(server)
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.DNSZones = DNSZones(self)
        self.DNSRecords = DNSRecords(self)
        self.DNSViews = DNSViews(self)
        self.Folders = Folders(self)
        self.Users = Users(self)
        self.Groups = Groups(self)
        self.Roles = Roles(self)
        self.IPAMRecords = IPAMRecords(self)
        self.Ranges = Ranges(self)
        self.Interfaces = Interfaces(self)
        self.Devices = Devices(self)
        self.ChangeRequests = ChangeRequests(self)
        self.logger = logging.getLogger('menandmice.client.Client')

    def new_dns_zone(self, *args, **kwargs):
        return DNSZone(*args, **kwargs)

    def new_dns_record(self, *args, **kwargs):
        return DNSRecord(*args, **kwargs)

    def new_dns_view(self, *args, **kwargs):
        return DNSView(*args, **kwargs)

    def new_dns_generate_directive(self, *args, **kwargs):
        return DNSGenerateDirective(*args, **kwargs)

    def new_dns_zone_options(self, *args, **kwargs):
        return DNSZoneOptions(*args, **kwargs)

    def new_folder(self, *args, **kwargs):
        return Folder(*args, **kwargs)

    def new_object_access(self, *args, **kwargs):
        return ObjectAccess(*args, **kwargs)

    def new_identity_access(self, *args, **kwargs):
        return IdentityAccess(*args, **kwargs)

    def new_access_entry(self, *args, **kwargs):
        return AccessEntry(*args, **kwargs)

    def new_event(self, *args, **kwargs):
        return Event(*args, **kwargs)

    def new_property_definition(self, *args, **kwargs):
        return PropertyDefinition(*args, **kwargs)

    def new_role(self, *args, **kwargs):
        return Role(*args, **kwargs)

    def new_group(self, *args, **kwargs):
        return Group(*args, **kwargs)

    def new_user(self, *args, **kwargs):
        return User(*args, **kwargs)

    def new_ipam_record(self, *args, **kwargs):
        return IPAMRecord(*args, **kwargs)

    def new_range(self, *args, **kwargs):
        return Range(*args, **kwargs)

    def new_discovery(self, *args, **kwargs):
        return Discovery(*args, **kwargs)

    def new_address_block(self, *args, **kwargs):
        return AddressBlock(*args, **kwargs)

    def new_range_statistics_response(self, *args, **kwargs):
        return GetRangeStatisticsResponse(*args, **kwargs)

    def new_interface(self, *args, **kwargs):
        return Interface(*args, **kwargs)

    def new_device(self, *args, **kwargs):
        return Device(*args, **kwargs)

    def new_change_request(self, *args, **kwargs):
        return ChangeRequest(*args, **kwargs)

    def sanitize_list(self, dirty_list):
        for idx, value in enumerate(dirty_list):
            if isinstance(value, list):
                dirty_list[idx] = self.sanitize_list(value)
            elif isinstance(value, dict):
                dirty_list[idx] = self.sanitize_dict(value)

        # remove all None and empty elements
        dirty_list = [x for x in dirty_list if x]
        return dirty_list

    def sanitize_dict(self, dirty_dict):
        for k, v in dirty_dict.items():
            if not v:
                del dirty_dict[k]
            elif isinstance(v, list):
                dirty_dict[k] = self.sanitize_list(v)
            elif isinstance(v, dict):
                dirty_dict[k] = self.sanitize_dict(v)
        return dirty_dict

    def get(self, url):
        self.logger.debug("GET " + url)
        response = self.session.get(url)
        return_val = ""
        self.logger.debug(response.status_code)
        if response.status_code == 200:
            return_val = response.json()
        elif response.status_code == 204:
            return_val = "No data to display"
        else:
            error_json = response.json()
            if error_json:
                code = error_json['error']['code']
                message = error_json['error']['message']
                raise requests.exceptions.HTTPError(
                    "{0}: {1}".format(code, message))
            else:
                response.raise_for_status()
        return return_val

    def post(self, url, payload):
        self.logger.debug("POST " + url)
        sanitized_payload = self.sanitize_dict(payload)
        self.logger.debug(sanitized_payload)
        self.logger.debug(json.dumps(sanitized_payload))
        response = self.session.post(url, json=sanitized_payload)
        self.logger.debug(response.status_code)
        if response.status_code != 201:
            error_json = response.json()
            if error_json:
                code = error_json['error']['code']
                message = error_json['error']['message']
                raise requests.exceptions.HTTPError(
                    "{0}: {1}".format(code, message))
            else:
                response.raise_for_status()
        return response.json()

    def delete(self, url):
        self.logger.debug("DELETE " + url)
        response = self.session.delete(url)
        return_status = ""
        self.logger.debug(response.status_code)
        if response.status_code == 204:
            return_status = "Successfully removed!"
        else:
            error_json = response.json()
            if error_json:
                code = error_json['error']['code']
                message = error_json['error']['message']
                raise requests.exceptions.HTTPError(
                    "{0}: {1}".format(code, message))
            else:
                response.raise_for_status()
        return return_status

    def put(self, url, payload, sanitize_override=False):
        self.logger.debug("PUT " + url)
        if not sanitize_override:
            payload = self.sanitize_dict(payload)
        self.logger.debug(payload)
        response = self.session.put(url, json=payload)
        return_status = ""
        self.logger.debug(response.status_code)
        if response.status_code == 204:
            return_status = "Successfully updated!"
        else:
            error_json = response.json()
            if error_json:
                code = error_json['error']['code']
                message = error_json['error']['message']
                raise requests.exceptions.HTTPError(
                    "{0}: {1}".format(code, message))
            else:
                response.raise_for_status()
        return return_status

    def delete_item(self, ref, **kwargs):
        self.logger.debug("Delete item  " + ref)
        query_string = self.make_query_str(**kwargs)
        self.logger.debug(query_string)
        response = self.delete("{0}{1}{2}".format(self.baseurl, ref, query_string))
        return response

    def update_item(self, ref, properties, obj_type, save_comment, delete_unspecified):
        if not isinstance(properties, list):
            properties = [properties]
        payload = {
            "ref": ref,
            "objType": obj_type,
            "saveComment": save_comment,
            "deleteUnspecified": delete_unspecified,
            "properties": properties
        }
        response = self.put("{0}{1}".format(self.baseurl, ref), payload)
        return response

    def get_item_access(self, ref, **kwargs):
        query_string = self.make_query_str(**kwargs)
        access_response_json = self.get(
            "{0}{1}/Access{2}".format(self.baseurl, ref, query_string))
        self.logger.debug(pprint.pformat(access_response_json['result']))
        access_object = ObjectAccess(access_response_json['result']['objectAccess'])
        return access_object

    def set_item_access(self, ref, identity_access, object_type, save_comment):
        if not isinstance(identity_access, list):
            identity_access = [identity_access]
        payload = {
            "objType": object_type,
            "saveComment": save_comment,
            "identityAccess": identity_access
        }
        self.logger.debug(payload)
        return self.put("{0}{1}/Access".format(self.baseurl, ref), payload)

    def get_item_history(self, ref, **kwargs):
        query_string = self.make_query_str(**kwargs)
        history_response_json = self.get(
            "{0}{1}/History{2}".format(self.baseurl, ref, query_string))
        all_events = []
        for event in history_response_json['result']['events']:
            all_events.append(Event(event))
        return all_events

    def get_property_definitions(self, ref, property_name):
        url = ""
        if property_name:
            url = "{0}{1}/PropertyDefinitions/{2}".format(
                self.baseurl, ref, property_name)
        else:
            url = "{0}{1}/PropertyDefinitions".format(self.baseurl, ref)
        property_definitions_json = self.get(url)
        property_definitions = []
        for definition in property_definitions_json['result']['propertyDefinitions']:
            property_definitions.append(PropertyDefinition(definition))
        return property_definitions

    def add_property_definition(self, ref, property_definition, save_comment):
        url = "{0}{1}/PropertyDefinitions".format(self.baseurl, ref)
        payload = {
            'saveComment': save_comment,
            'propertyDefinition': property_definition
        }
        return self.post(url, payload)

    def update_property_definition(self, ref,
                                   property_name,
                                   property_definition,
                                   update_existing,
                                   save_comment):
        payload = {
            'updateExisting': update_existing,
            'saveComment': save_comment,
            'propertyDefinition': property_definition
        }
        return self.put("{0}{1}/PropertyDefinitions/{2}".format(self.baseurl,
                                                                ref,
                                                                property_name),
                        payload)

    def delete_property_definition(self, ref, property_name, save_comment):
        query_string = ""
        if save_comment:
            query_string = self.make_query_str(**{"saveComment": save_comment})
        return self.delete("{0}{1}/PropertyDefinitions/{2}{3}".format(self.baseurl,
                                                                      ref,
                                                                      property_name,
                                                                      query_string))
