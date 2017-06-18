from menandmice.ipam import Folders
from menandmice.base import BaseObject
from menandmice.base import BaseService


class DNSZone(BaseObject):
    def __init__(self, *args, **kwargs):
        super(DNSZone, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('dnsScopeName')
        self.add_key('dynamic')
        self.add_key('adIntegrated')
        self.add_key('adReplicationType')
        self.add_key('adPartition')
        self.add_key('dnsViewRef')
        self.add_key('dnsViewRefs')
        self.add_key('authority')
        self.add_key('type')
        self.add_key('dnssecSigned')
        self.add_key('kskIDs')
        self.add_key('zskIDs')
        self.add_key('customProperties')


class DNSZoneOptions(BaseObject):
    def __init__(self, *args, **kwargs):
        super(DNSZoneOptions, self).__init__(*args, **kwargs)
        self.add_key('zonetype')
        self.add_key('timestamp')
        self.add_key('masters')
        self.add_key('msSpecific', MSSpecificDNSZoneOptions())
        self.add_key('bindSpecific', BINDSpecificDNSZoneOptions())
        self.add_key('dnssec', DNSSECZoneOptions())
        self.add_key('additional')


class MSSpecificDNSZoneOptions(BaseObject):
    def __init__(self, *args, **kwargs):
        super(MSSpecificDNSZoneOptions, self).__init__(*args, **kwargs)
        self.add_key('notify', NotifyOption())
        self.add_key('allowTransferData', AllowTransferOption())
        self.add_key('allowUpdate')
        self.add_key('scavenge', ScavengeOption())
        self.add_key('replication', ADReplicationOption())


class NotifyOption(BaseObject):
    def __init__(self, *args, **kwargs):
        super(NotifyOption, self).__init__(*args, **kwargs)
        self.add_key('authoritative')
        self.add_key('alsoNotify')


class AllowTransferOption(BaseObject):
    def __init__(self, *args, **kwargs):
        super(AllowTransferOption, self).__init__(*args, **kwargs)
        self.add_key('allowTo')
        self.add_key('allowToServers')


class ScavengeOption(BaseObject):
    def __init__(self, *args, **kwargs):
        super(ScavengeOption, self).__init__(*args, **kwargs)
        self.add_key('noRefresh')
        self.add_key('refresh')


class ADReplicationOption(BaseObject):
    def __init__(self, *args, **kwargs):
        super(ADReplicationOption, self).__init__(*args, **kwargs)
        self.add_key('type')
        self.add_key('partition')


class BINDSpecificDNSZoneOptions(BaseObject):
    def __init__(self, *args, **kwargs):
        super(BINDSpecificDNSZoneOptions, self).__init__(*args, **kwargs)
        self.add_key('allowQuery')
        self.add_key('allowTransfer')
        self.add_key('zonefile')
        self.add_key('forwarders')


class DNSSECZoneOptions(BaseObject):
    def __init__(self, *args, **kwargs):
        super(DNSSECZoneOptions, self).__init__(*args, **kwargs)
        self.add_key('SignWithNSEC3')
        self.add_key('NSEC3OptOut')
        self.add_key('NSEC3RandomSaltLength')
        self.add_key('NSEC3Iterations')
        self.add_key('DSRecordSetTTL')
        self.add_key('DNSKEYRecordSetTTL')
        self.add_key('DsRecordAlgorithms')
        self.add_key('MaintainTrustAnchor')
        self.add_key('Keymaster')
        self.add_key('ParentHasSecureDelegation')
        self.add_key('RFC5011KeyRollovers')
        self.add_key('SecureDelegationPollingPeriod')
        self.add_key('SignatureInceptionOffset')
        self.add_key('NSEC3UserSalt')
        self.add_key('NSEC3CurrentSalt')
        self.add_key('NSEC3HashAlgorithm')


class DNSGenerateDirective(BaseObject):
    def __init__(self, *args, **kwargs):
        super(DNSGenerateDirective, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('rangeStart')
        self.add_key('rangeEnd')
        self.add_key('lhs')
        self.add_key('dumbclass')
        self.add_key('type')
        self.add_key('rhs')


class DNSRecord(BaseObject):
    def __init__(self, *args, **kwargs):
        super(DNSRecord, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('type')
        self.add_key('ttl')
        self.add_key('data')
        self.add_key('comment')
        self.add_key('enabled')
        self.add_key('aging')
        self.add_key('dnsZoneRef')


class DNSView(BaseObject):
    def __init__(self, *args, **kwargs):
        super(DNSView, self).__init__(*args, **kwargs)
        self.add_key('ref')
        self.add_key('name')
        self.add_key('dnsServerRef')


class DNSZones(BaseService):
    def __init__(self, client):
        super(DNSZones, self).__init__(client=client,
                                       url_base="DNSZones",
                                       entity_class=DNSZone,
                                       get_response_entity_key="dnsZone",
                                       get_response_all_key="dnsZones")

    def add(self, dns_zone, master_zones="", save_comment=""):
        payload = {
            "masters": master_zones,
            "saveComment": save_comment,
            "dnsZone": dns_zone
        }
        zone_json = self.client.post("{0}{1}".format(self.client.baseurl,
                                                     self.url_base),
                                     payload)
        dns_zone_return = self.get(zone_json['result']['ref'])
        return dns_zone_return[0]

    def get_records(self, dns_zone, **kwargs):
        zone_ref = self.ref_or_raise(dns_zone)
        all_records = []
        query_string = self.make_query_str(**kwargs)
        dns_record_response = self.client.get("{0}{1}/DNSRecords{2}".format(self.client.baseurl,
                                                                            zone_ref,
                                                                            query_string))
        for record in dns_record_response['result']['dnsRecords']:
            all_records.append(DNSRecord(record))
        return all_records

    def get_zone_folder(self, dns_zone, **kwargs):
        zone_ref = self.ref_or_raise(dns_zone)
        query_string = self.make_query_str(**kwargs)
        folder_response = self.client.get("{0}{1}/Folders{2}".format(self.client.baseurl,
                                                                     zone_ref,
                                                                     query_string))
        return Folders(self.client).get(folder_response['result']['folder'])

    def delete_zone_from_folder(self, dns_zone, folder="", **kwargs):
        zone_ref = self.ref_or_raise(dns_zone)
        folder_ref = self.ref_or_raise(folder)
        query_string = self.make_query_str(**kwargs)
        if folder_ref:
            url = "{0}{1}/{2}{3}".format(self.client.baseurl, zone_ref, folder_ref, query_string)
        else:
            url = "{0}{1}/Folders{2}".format(self.client.baseurl, zone_ref, query_string)
        return self.client.delete(url)

    def add_zone_to_folder(self, dns_zone, folder, save_comment=""):
        zone_ref = self.ref_or_raise(dns_zone)
        folder_ref = self.ref_or_raise(folder)
        return Folders(self.client).add_to_folder(zone_ref, folder_ref, save_comment)

    def get_generate_directive(self, dns_zone="", directive=""):
        zone_ref = self.ref_or_raise(dns_zone)
        directive_ref = self.ref_or_raise(directive)
        all_directives = []
        url = ""
        if zone_ref:
            url = "{0}{1}/GenerateDirectives".format(self.client.baseurl, zone_ref)
            directive_response = self.client.get(url)
            for directive in directive_response['result']['dnsGenerateDirectives']:
                all_directives.append(DNSGenerateDirective(directive))
        elif directive_ref:
            url = "{0}{1}{2}".format(self.client.baseurl, self.url_base, directive_ref)
            directive_response = self.client.get(url)
            all_directives.append(
                DNSGenerateDirective(directive_response['result']['dnsGenerateDirective']))
        return all_directives

    def delete_generate_directive(self, directive, **kwargs):
        directive_ref = self.ref_or_raise(directive)
        return self.client.delete_item("{0}/{1}".format(self.url_base, directive_ref),
                                      **kwargs)

    def add_aenerate_directive(self, dns_zone, dns_generate_directive, save_comment=""):
        zone_ref = self.ref_or_raise(dns_zone)
        payload = {
            "saveComment": save_comment,
            "dnsGenerateDirective": dns_generate_directive
        }
        directive_json = self.client.post("{0}{1}/GenerateDirectives".format(self.client.baseurl,
                                                                             zone_ref),
                                          payload)
        directive_return = self.getGenerateDirective(directive_json['result']['ref'])
        return directive_return[0]

    def get_ley_storage_providers(self, dns_zone):
        zone_ref = self.ref_or_raise(dns_zone)
        providers_response = self.client.get(
            "{0}{1}/KeyStorageProviders".format(self.client.baseurl, zone_ref))
        return providers_response['result']['keyStorageProviders']

    def get_zone_options(self, dns_zone):
        zone_ref = self.ref_or_raise(dns_zone)
        options_response = self.client.get("{0}{1}/Options".format(self.client.baseurl, zone_ref))
        return options_response['result']['dnsZoneOptions']

    def update_zone_options(self, dns_zone, dns_options_input, save_comment=""):
        zone_ref = self.ref_or_raise(dns_zone)
        payload = {
            "saveComment": save_comment,
            "dnsZoneOptions": dns_options_input
        }
        return self.client.put("{0}{1}/Options".format(self.client.baseurl, zone_ref),
                               payload)

    def get_zone_scopes(self, dns_zone, **kwargs):
        zone_ref = self.ref_or_raise(dns_zone)
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

    def add(self,
            dns_record,
            save_comment="",
            auto_assign_range_ref="",
            dns_zone_ref="",
            force_override=""):
        if not isinstance(dns_record, list):
            dns_record = [dns_record]
        payload = {
            "saveComment": save_comment,
            "autoAssignRangeRef": auto_assign_range_ref,
            "dnsZoneRef": dns_zone_ref,
            "forceOverrideOfNamingConflictCheck": force_override,
            "dnsRecords": dns_record
        }
        response = self.client.post("{0}{1}".format(self.client.baseurl,
                                                    self.url_base),
                                    payload)
        dns_record_return = []

        # POST /api/DNSRecords can return a valid (201) status but still not
        # create a record, in this case the 'errors' property is filled in
        # with an error about why the record couldn't be created
        if ('result' in response and response['result'] and
            'errors' in response['result'] and response['result']['errors']):  # noqa
            raise RuntimeError(response['result']['errors'])

        for ref in response['result']['objRefs']:
            dns_record_return.append(self.get(ref)[0])
        return dns_record_return

    def get_related_records(self, dns_record):
        record_ref = self.ref_or_raise(dns_record)
        all_records = []
        dns_record_response = self.client.get(
            "{0}{1}/RelatedDNSRecords".format(self.client.baseurl,
                                              record_ref))
        for record in dns_record_response['result']['dnsRecords']:
            all_records.append(DNSRecord(record))
        return all_records

    def delete_related_records(self, dns_record, **kwargs):
        record_ref = self.ref_or_raise(dns_record)
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

    def get_zones(self, dns_view):
        view_ref = self.ref_or_raise(dns_view)
        all_zones = []
        dns_zone_response = self.client.get("{0}{1}/DNSZones".format(self.client.baseurl,
                                                                     view_ref))
        for zone in dns_zone_response['result']['dnsZones']:
            all_zones.append(DNSZone(zone))
        return all_zones
