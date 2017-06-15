import json

from menandmice.ipam import Folders
from menandmice.base import BaseObject
from menandmice.base import BaseService


class DNSZone(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.name = self.get_value('name', kwargs)
        self.dnsScopeName = self.get_value('dnsScopeName', kwargs)
        self.dynamic = self.get_value('dynamic', kwargs)
        self.adIntegrated = self.get_value('adIntegrated', kwargs)
        self.adReplicationType = self.get_value('adReplicationType', kwargs)
        self.adPartition = self.get_value('adPartition', kwargs)
        self.dnsViewRef = self.get_value('dnsViewRef', kwargs)
        self.dnsViewRefs = self.get_value('dnsViewRefs', kwargs)
        self.authority = self.get_value('authority', kwargs)
        self.type = self.get_value('type', kwargs)
        self.dnssecSigned = self.get_value('dnssecSigned', kwargs)
        self.kskIDs = self.get_value('kskIDs', kwargs)
        self.zskIDs = self.get_value('zskIDs', kwargs)
        self.customProperties = self.get_value('customProperties', kwargs)


class DNSZoneOptions(BaseObject):
    def __init__(self, **kwargs):
        self.zonetype = self.get_value('zonetype', kwargs)
        self.timestamp = self.get_value('timestamp', kwargs)
        self.masters = self.get_value('masters', kwargs)
        self.msSpecific = self.build_obj(MSSpecificDNSZoneOptions,
                                        self.get_value('msSpecific', kwargs))
        self.bindSpecific = self.build_obj(BINDSpecificDNSZoneOptions,
                                          self.get_value('bindSpecific', kwargs))
        self.dnssec = self.build_obj(DNSSECZoneOptions,
                                    self.get_value('dnssec', kwargs))
        self.additional = self.get_value('additional', kwargs)


class MSSpecificDNSZoneOptions(BaseObject):
    def __init__(self, **kwargs):
        self.notify = self.build_obj(NotifyOption,
                                    self.get_value('notify', kwargs))
        self.allowTransferData = self.build_obj(AllowTransferOption,
                                               self.get_value('allowTransferData', kwargs))
        self.allowUpdate = self.get_value('allowUpdate', kwargs)
        self.scavenge = self.build_obj(ScavengeOption,
                                      self.get_value('scavenge', kwargs))
        self.replication = self.build_obj(ADReplicationOption,
                                         self.get_value('replication', kwargs))


class NotifyOption(BaseObject):
    def __init__(self, **kwargs):
        self.authoritative = self.get_value('authoritative', kwargs)
        self.alsoNotify = self.get_value('alsoNotify', kwargs)


class AllowTransferOption(BaseObject):
    def __init__(self, **kwargs):
        self.allowTo = self.get_value('allowTo', kwargs)
        self.allowToServers = self.get_value('allowToServers', kwargs)


class ScavengeOption(BaseObject):
    def __init__(self, **kwargs):
        self.noRefresh = self.get_value('noRefresh', kwargs)
        self.refresh = self.get_value('refresh', kwargs)


class ADReplicationOption(BaseObject):
    def __init__(self, **kwargs):
        self.type = self.get_value('type', kwargs)
        self.partition = self.get_value('partition', kwargs)


class BINDSpecificDNSZoneOptions(BaseObject):
    def __init__(self, **kwargs):
        self.allowQuery = self.get_value('allowQuery', kwargs)
        self.allowTransfer = self.get_value('allowTransfer', kwargs)
        self.zonefile = self.get_value('zonefile', kwargs)
        self.forwarders = self.get_value('forwarders', kwargs)


class DNSSECZoneOptions(BaseObject):
    def __init__(self, **kwargs):
        self.SignWithNSEC3 = self.get_value('SignWithNSEC3', kwargs)
        self.NSEC3OptOut = self.get_value('NSEC3OptOut', kwargs)
        self.NSEC3RandomSaltLength = self.get_value('NSEC3RandomSaltLength', kwargs)
        self.NSEC3Iterations = self.get_value('NSEC3Iterations', kwargs)
        self.DSRecordSetTTL = self.get_value('DSRecordSetTTL', kwargs)
        self.DNSKEYRecordSetTTL = self.get_value('DNSKEYRecordSetTTL', kwargs)
        self.DsRecordAlgorithms = self.get_value('DsRecordAlgorithms', kwargs)
        self.MaintainTrustAnchor = self.get_value('MaintainTrustAnchor', kwargs)
        self.Keymaster = self.get_value('Keymaster', kwargs)
        self.ParentHasSecureDelegation = self.get_value('ParentHasSecureDelegation', kwargs)
        self.RFC5011KeyRollovers = self.get_value('RFC5011KeyRollovers', kwargs)
        self.SecureDelegationPollingPeriod = self.get_value('SecureDelegationPollingPeriod', kwargs)
        self.SignatureInceptionOffset = self.get_value('SignatureInceptionOffset', kwargs)
        self.NSEC3UserSalt = self.get_value('NSEC3UserSalt', kwargs)
        self.NSEC3CurrentSalt = self.get_value('NSEC3CurrentSalt', kwargs)
        self.NSEC3HashAlgorithm = self.get_value('NSEC3HashAlgorithm', kwargs)


class DNSGenerateDirective(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.rangeStart = self.get_value('rangeStart', kwargs)
        self.rangeEnd = self.get_value('rangeEnd', kwargs)
        self.lhs = self.get_value('lhs', kwargs)
        self.dumbclass = self.get_value('dumbclass', kwargs)
        self.type = self.get_value('type', kwargs)
        self.rhs = self.get_value('rhs', kwargs)


class DNSRecord(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.name = self.get_value('name', kwargs)
        self.type = self.get_value('type', kwargs)
        self.ttl = self.get_value('ttl', kwargs)
        self.data = self.get_value('data', kwargs)
        self.comment = self.get_value('comment', kwargs)
        self.enabled = self.get_value('enabled', kwargs)
        self.aging = self.get_value('aging', kwargs)
        self.dnsZoneRef = self.get_value('dnsZoneRef', kwargs)


class DNSView(BaseObject):
    def __init__(self, **kwargs):
        self.ref = self.get_value('ref', kwargs)
        self.name = self.get_value('name', kwargs)
        self.dnsServerRef = self.get_value('dnsServerRef', kwargs)


class DNSZones(BaseService):
    def __init__(self, client):
        super(DNSZones, self).__init__(client=client,
                                       url_base="DNSZones",
                                       entity_class=DNSZone,
                                       get_response_entity_key="dnsZone",
                                       get_response_all_key="dnsZones")

    def build_directive(self, json_input):
        return self.json_to_clazz(json_input, DNSGenerateDirective)

    def build_options(self, json_input):
        return self.json_to_clazz(json_input, DNSZoneOptions)

    def add(self, dnsZone_input, masterZones="", saveComment=""):
        if isinstance(dnsZone_input, DNSZone):
            dnsZone_input = json.loads(dnsZone_input.to_json())
        payload = {
            "masters": masterZones,
            "saveComment": saveComment,
            "dnsZone": dnsZone_input
        }
        zone_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                     self.url_base),
                                     payload)
        dns_zone_return = self.get(zone_json['result']['ref'])
        return dns_zone_return[0]

    def getRecords(self, zone_ref, **kwargs):
        all_records = []
        query_string = self.make_query_str(**kwargs)
        dns_record_response = self.client.get("{0}{1}/DNSRecords{2}".format(self.client.baseurl,
                                                                            zone_ref,
                                                                            query_string))
        for record in dns_record_response['result']['dnsRecords']:
            all_records.append(DNSRecords(self.client).build(record))
        return all_records

    def getZoneFolder(self, zone_ref, **kwargs):
        query_string = self.make_query_str(**kwargs)
        folder_response = self.client.get("{0}{1}/Folders{2}".format(self.client.baseurl,
                                                                     zone_ref,
                                                                     query_string))
        return Folders(self.client).get(folder_response['result']['folder'])

    def deleteZoneFromFolder(self, zone_ref, folder_ref="", **kwargs):
        query_string = self.make_query_str(**kwargs)
        if folder_ref:
            url = "{0}{1}/{2}{3}".format(self.client.baseurl, zone_ref, folder_ref, query_string)
        else:
            url = "{0}{1}/Folders{2}".format(self.client.baseurl, zone_ref, query_string)
        return self.client.delete(url)

    def addZoneToFolder(self, zone_ref, folder_ref, saveComment=""):
        return Folders(self.client).addToFolder(zone_ref, folder_ref, saveComment)

    def getGenerateDirective(self, zone_ref="", directive_ref=""):
        all_directives = []
        url = ""
        if zone_ref:
            url = "{0}{1}/GenerateDirectives".format(self.client.baseurl, zone_ref)
            directive_response = self.client.get(url)
            for directive in directive_response['result']['dnsGenerateDirectives']:
                all_directives.append(self.build_directive(directive))
        elif directive_ref:
            url = "{0}{1}{2}".format(self.client.baseurl, self.url_base, directive_ref)
            directive_response = self.client.get(url)
            all_directives.append(
                self.build_directive(directive_response['result']['dnsGenerateDirective']))
        return all_directives

    def deleteGenerateDirective(self, directive_ref, **kwargs):
        return self.client.deleteItem("{0}/{1}".format(self.url_base, directive_ref), kwargs)

    def addGenerateDirective(self, zone_ref, dnsGenerateDirective_input, saveComment=""):
        if isinstance(dnsGenerateDirective_input, DNSGenerateDirective):
            dnsGenerateDirective_input = json.loads(dnsGenerateDirective_input.to_json())
        payload = {
            "saveComment": saveComment,
            "dnsGenerateDirective": dnsGenerateDirective_input
        }
        directive_json = self.client.post("{0}{1}/GenerateDirectives".format(self.client.baseurl,
                                                                             zone_ref),
                                          payload)
        directive_return = self.getGenerateDirective(directive_json['result']['ref'])
        return directive_return[0]

    def getKeyStorageProviders(self, zone_ref):
        providers_response = self.client.get(
            "{0}{1}/KeyStorageProviders".format(self.client.baseurl, zone_ref))
        return providers_response['result']['keyStorageProviders']

    def getZoneOptions(self, zone_ref):
        options_response = self.client.get("{0}{1}/Options".format(self.client.baseurl, zone_ref))
        options_json = options_response['result']['dnsZoneOptions']
        return self.build_options(options_json)

    def updateZoneOptions(self, zone_ref, dns_options_input, saveComment=""):
        if isinstance(dns_options_input, DNSZoneOptions):
            dns_options_input = json.loads(dns_options_input.to_json())
        payload = {
            "saveComment": saveComment,
            "dnsZoneOptions": dns_options_input
        }
        return self.client.put("{0}{1}/Options".format(self.client.baseurl, zone_ref), payload)

    def getZoneScopes(self, zone_ref, **kwargs):
        query_string = self.make_query_str(**kwargs)
        dns_zone_response = self.client.get("{0}{1}/Scopes{2}".format(self.client.baseurl,
                                                                      zone_ref,
                                                                      query_string))
        return dns_zone_response['result']['dnsScopes']


class DNSRecords(BaseService):
    def __init__(self, client):
        super(DNSRecords, self).__init__(client=client,
                                         url_base="DNSRecords",
                                         entity_class=DNSRecord,
                                         get_response_entity_key="dnsRecord",
                                         get_response_all_key="dnsRecords",
                                         get_is_singular=True)

    def add(self, dnsRecord_input,
            saveComment="",
            autoAssignRangeRef="",
            dnsZoneRef="",
            forceOverride=""):
        if isinstance(dnsRecord_input, DNSRecord):
            dnsRecord_input = json.loads(dnsRecord_input.to_json())
        if not isinstance(dnsRecord_input, list):
            dnsRecord_input = [dnsRecord_input]
        payload = {
            "saveComment": saveComment,
            "autoAssignRangeRef": autoAssignRangeRef,
            "dnsZoneRef": dnsZoneRef,
            "forceOverrideOfNamingConflictCheck": forceOverride,
            "dnsRecords": dnsRecord_input
        }
        record_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                       self.url_base),
                                       payload)
        dns_record_return = []
        for ref in record_json['result']['objRefs']:
            dns_record_return.append(self.get(ref)[0])
        return dns_record_return

    def getRelatedRecords(self, record_ref):
        all_records = []
        dns_record_response = self.client.get(
            "{0}{1}/RelatedDNSRecords".format(self.client.baseurl,
                                              record_ref))
        for record in dns_record_response['result']['dnsRecords']:
            all_records.append(self.build(record))
        return all_records

    def deleteRelatedRecords(self, record_ref, **kwargs):
        query_string = self.make_query_str(**kwargs)
        return self.client.delete(
            "{0}{1}/RelatedDNSRecords{2}".format(self.client.baseurl,
                                                 record_ref,
                                                 query_string))


class DNSViews(BaseService):
    def __init__(self, client):
        super(DNSViews, self).__init__(client=client,
                                       url_base="DNSViews",
                                       entity_class=DNSView,
                                       get_response_entity_key="dnsView",
                                       get_response_all_key="dnsViews")

    def getZones(self, view_ref):
        all_zones = []
        dns_zone_response = self.client.get("{0}{1}/DNSZones".format(self.client.baseurl,
                                                                     view_ref))
        for zone in dns_zone_response['result']['dnsZones']:
            all_zones.append(DNSZones(self.client).build(zone))
        return all_zones
