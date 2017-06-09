import json

class DNSZone(object):
    def __init__(self, **kwargs):
        self.ref = self.getValue('ref', kwargs)
        self.name = self.getValue('name', kwargs)
        self.dnsScopeName = self.getValue('dnsScopeName', kwargs)
        self.dynamic = self.getValue('dynamic', kwargs)
        self.adIntegrated = self.getValue('adIntegrated', kwargs)
        self.adReplicationType = self.getValue('adReplicationType', kwargs)
        self.adPartition = self.getValue('adPartition', kwargs)
        self.dnsViewRef = self.getValue('dnsViewRef', kwargs)
        self.dnsViewRefs = self.getValue('dnsViewRefs', kwargs)
        self.authority = self.getValue('authority', kwargs)
        self.type = self.getValue('type', kwargs)
        self.dnssecSigned = self.getValue('dnssecSigned', kwargs)
        self.kskIDs = self.getValue('kskIDs', kwargs)
        self.zskIDs = self.getValue('zskIDs', kwargs)
        self.customProperties = self.getValue('customProperties', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class DNSZoneOptions(object):
    def __init__(self, **kwargs):
        self.zonetype = self.getValue('zonetype', kwargs)
        self.timestamp = self.getValue('timestamp', kwargs)
        self.masters = self.getValue('masters', kwargs)
        self.msSpecific = self.buildMsSpecific(self.getValue('msSpecific', kwargs))
        self.bindSpecific = self.buildBindSpecific(self.getValue('bindSpecific', kwargs))
        self.dnssec = self.buildDnsSec(self.getValue('dnssec', kwargs))
        self.additional = self.getValue('additional', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def buildMsSpecific(self, msSpecific):
        ms_return = ""
        if msSpecific:
            ms_return = MSSpecificDNSZoneOptions(**msSpecific)
        return ms_return

    def buildBindSpecific(self, bindSpecific):
        bind_return = ""
        if bindSpecific:
            bind_return = BINDSpecificDNSZoneOptions(**bindSpecific)
        return bind_return

    def buildDnsSec(self, dnssec):
        dns_return = ""
        if dnssec:
            dns_return = DNSSECZoneOptions(**dnssec)
        return dns_return

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class MSSpecificDNSZoneOptions(object):
    def __init__(self, notify="", allowTransferData="", allowUpdate="", scavenge="", replication="", **kwargs):
        self.notify = self.buildNotify(self.getValue('notify', kwargs))
        self.allowTransferData = self.buildTransferData(self.getValue('allowTransferData', kwargs))
        self.allowUpdate = self.getValue('allowUpdate', kwargs)
        self.scavenge = self.buildScavenge(self.getValue('scavenge', kwargs))
        self.replication = self.buildreplication(self.getValue('replication', kwargs))

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def buildNotify(self, notify):
        notify_return = ""
        if notify:
            notify_return = NotifyOption(**notify)
        return notify_return

    def buildTransferData(self, allowTransferData):
        tansfer_return = ""
        if allowTransferData:
            tansfer_return = AllowTransferOption(**allowTransferData)
        return tansfer_return

    def buildScavenge(self, scavenge):
        scavenge_return = ""
        if scavenge:
            scavenge_return = ScavengeOption(**scavenge)
        return scavenge_return

    def buildreplication(self, replication):
        replication_return = ""
        if replication:
            replication_return = ADReplicationOption(**replication)
        return replication_return

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class NotifyOption(object):
    def __init__(self, **kwargs):
        self.authoritative = self.getValue('authoritative', kwargs)
        self.alsoNotify = self.getValue('alsoNotify', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class AllowTransferOption(object):
    def __init__(self, **kwargs):
        self.allowTo = self.getValue('allowTo', kwargs)
        self.allowToServers = self.getValue('allowToServers', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class ScavengeOption(object):
    def __init__(self, **kwargs):
        self.noRefresh = self.getValue('noRefresh', kwargs)
        self.refresh = self.getValue('refresh', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class ADReplicationOption(object):
    def __init__(self, **kwargs):
        self.type = self.getValue('type', kwargs)
        self.partition = self.getValue('partition', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class BINDSpecificDNSZoneOptions(object):
    def __init__(self, **kwargs):
        self.allowQuery = self.getValue('allowQuery', kwargs)
        self.allowTransfer = self.getValue('allowTransfer', kwargs)
        self.zonefile = self.getValue('zonefile', kwargs)
        self.forwarders = self.getValue('forwarders', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class DNSSECZoneOptions(object):
    def __init__(self, **kwargs):
        self.SignWithNSEC3 = self.getValue('SignWithNSEC3', kwargs)
        self.NSEC3OptOut = self.getValue('NSEC3OptOut', kwargs)
        self.NSEC3RandomSaltLength = self.getValue('NSEC3RandomSaltLength', kwargs)
        self.NSEC3Iterations = self.getValue('NSEC3Iterations', kwargs)
        self.DSRecordSetTTL = self.getValue('DSRecordSetTTL', kwargs)
        self.DNSKEYRecordSetTTL = self.getValue('DNSKEYRecordSetTTL', kwargs)
        self.DsRecordAlgorithms = self.getValue('DsRecordAlgorithms', kwargs)
        self.MaintainTrustAnchor = self.getValue('MaintainTrustAnchor', kwargs)
        self.Keymaster = self.getValue('Keymaster', kwargs)
        self.ParentHasSecureDelegation = self.getValue('ParentHasSecureDelegation', kwargs)
        self.RFC5011KeyRollovers = self.getValue('RFC5011KeyRollovers', kwargs)
        self.SecureDelegationPollingPeriod = self.getValue('SecureDelegationPollingPeriod', kwargs)
        self.SignatureInceptionOffset = self.getValue('SignatureInceptionOffset', kwargs)
        self.NSEC3UserSalt = self.getValue('NSEC3UserSalt', kwargs)
        self.NSEC3CurrentSalt = self.getValue('NSEC3CurrentSalt', kwargs)
        self.NSEC3HashAlgorithm = self.getValue('NSEC3HashAlgorithm', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class DNSGenerateDirective(object):
    def __init__(self, **kwargs):
        self.ref = self.getValue('ref', kwargs)
        self.rangeStart = self.getValue('rangeStart', kwargs)
        self.rangeEnd = self.getValue('rangeEnd', kwargs)
        self.lhs = self.getValue('lhs', kwargs)
        self.dumbclass = self.getValue('dumbclass', kwargs)
        self.type = self.getValue('type', kwargs)
        self.rhs = self.getValue('rhs', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class DNSRecord(object):
    def __init__(self, **kwargs):
        self.ref = self.getValue('ref', kwargs)
        self.name = self.getValue('name', kwargs)
        self.type = self.getValue('type', kwargs)
        self.ttl = self.getValue('ttl', kwargs)
        self.data = self.getValue('data', kwargs)
        self.comment = self.getValue('comment', kwargs)
        self.enabled = self.getValue('enabled', kwargs)
        self.aging = self.getValue('aging', kwargs)
        self.dnsZoneRef = self.getValue('dnsZoneRef', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class DNSView(object):
    def __init__(self, **kwargs):
        self.ref = self.getValue('ref', kwargs)
        self.name = self.getValue('name', kwargs)
        self.dnsServerRef = self.getValue('dnsServerRef', kwargs)

    def getValue(self, key, kwargs):
        return_val = ""
        if key in kwargs:
            return_val = kwargs[key]
        return return_val

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class DNSZones(object):
    def __init__(self, client):
        self.client = client
        self.url_base = "DNSZones"

    def build(self, json_input):
        if isinstance(json_input, basestring):
            json_input = json.loads(json_input)
        return DNSZone(**json_input)

    def build_directive(self, json_input):
        if isinstance(json_input, basestring):
            json_input = json.loads(json_input)
        return DNSGenerateDirective(**json_input)

    def build_options(self, json_input):
        if isinstance(json_input, basestring):
            json_input = json.loads(json_input)
        return DNSZoneOptions(**json_input)

    def get(self, zone_ref="", **kwargs):
        all_zones = []
        if not zone_ref:
            query_string = ""
            if kwargs:
                for key, value in kwargs.items():
                    if not query_string:
                        query_string += "?{0}={1}".format(key, value)
                    else:
                        query_string += "&{0}={1}".format(key, value)
            dns_zone_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, self.url_base, query_string))
            for zone in dns_zone_response['result']['dnsZones']:
                all_zones.append(self.build(zone))
        else:
            dns_zone_response = self.client.get("{0}{1}".format(self.client.baseurl, zone_ref))
            all_zones.append(self.build(dns_zone_response['result']['dnsZone']))
        return all_zones

    def add(self, dnsZone_input, masterZones="", saveComment=""):
        if isinstance(dnsZone_input, DNSZone):
            dnsZone_input = json.loads(dnsZone_input.to_json())
        payload = {
            "masters" : masterZones,
            "saveComment" : saveComment,
            "dnsZone" : dnsZone_input
        }
        zone_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
        dns_zone_return = self.get(zone_json['result']['ref'])
        return dns_zone_return[0]

    def delete(self, zone_ref, **kwargs):
        return self.client.deleteItem(zone_ref, kwargs)

    def update(self, zone_ref, properties, objType="DNSZone", saveComment="", deleteUnspecified=False):
        return self.client.updateItem(zone_ref, properties, objType, saveComment, deleteUnspecified)

    def getRecords(self, zone_ref, **kwargs):
        all_records = []
        query_string = ""
        if kwargs:
            for key, value in kwargs.items():
                if not query_string:
                    query_string += "?{0}={1}".format(key, value)
                else:
                    query_string += "&{0}={1}".format(key, value)
        dns_record_response = self.client.get("{0}{1}/DNSRecords{2}".format(self.client.baseurl, zone_ref, query_string))
        for record in dns_record_response['result']['dnsRecords']:
            all_records.append(DNSRecords(self.client).build(record))
        return all_records

    def getAccess(self, zone_ref, **kwargs):
        return self.client.getItemAccess(zone_ref, kwargs)

    def setAccess(self, zone_ref, identity_access, object_type="", saveComment=""):
        return self.client.setItemAccess(zone_ref, identity_access, object_type, saveComment)

    def getHistory(self, zone_ref, **kwargs):
        return self.client.getItemHistory(zone_ref, kwargs)

    def getPropertyDefinition(self, zone_ref, property_name=""):
        return self.client.getPropertyDefinitions(zone_ref, property_name)

    def addNewPropertyDefinition(self, zone_ref, property_definition, saveComment=""):
        return self.client.newCustomProperty(zone_ref, property_definition, saveComment)

    def updatePropertyDefinition(self, zone_ref, property_name, property_definition, updateExisting="", saveComment=""):
        return self.client.updatePropertyDefinitions(zone_ref, property_name, property_definition, updateExisting, saveComment)

    def deletePropertyDefinition(self, zone_ref, property_name, saveComment=""):
        return self.client.deletePropertyDefinition(zone_ref, property_name, saveComment)

    def getZoneFolder(self, zone_ref, **kwargs):
        query_string = ""
        if kwargs:
            for key, value in kwargs.items():
                if not query_string:
                    query_string += "?{0}={1}".format(key, value)
                else:
                    query_string += "&{0}={1}".format(key, value)
        folder_response = self.client.get("{0}{1}/Folders{2}".format(self.client.baseurl, zone_ref, query_string))
        return Folders(self.client).get(folder_response['result']['folder'])

    def deleteZoneFromFolder(self, zone_ref, folder_ref="", **kwargs):
        query_string = ""
        if kwargs:
            for key, value in kwargs.items():
                if not query_string:
                    query_string += "?{0}={1}".format(key, value)
                else:
                    query_string += "&{0}={1}".format(key, value)
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
            all_directives.append(self.build_directive(directive_response['result']['dnsGenerateDirective']))
        return all_directives

    def deleteGenerateDirective(self, directive_ref, **kwargs):
        return self.client.deleteItem("{0}/{1}".format(self.url_base, directive_ref), kwargs)

    def addGenerateDirective(self, zone_ref, dnsGenerateDirective_input, saveComment=""):
        if isinstance(dnsZone_input, DNSGenerateDirective):
            dnsGenerateDirective_input = json.loads(dnsGenerateDirective_input.to_json())
        payload = {
            "saveComment" : saveComment,
            "dnsGenerateDirective" : dnsGenerateDirective_input
        }
        directive_json = self.client.post("{0}{1}/GenerateDirectives".format(self.client.baseurl, zone_ref), payload)
        directive_return = self.getGenerateDirective(directive_json['result']['ref'])
        return directive_return[0]

    def getKeyStorageProviders(self, zone_ref):
        providers_response = self.client.get("{0}{1}/KeyStorageProviders".format(self.client.baseurl, zone_ref))
        return providers_response['result']['keyStorageProviders']

    def getZoneOptions(self, zone_ref):
        options_response = self.client.get("{0}{1}/Options".format(self.client.baseurl, zone_ref))
        options_json = options_response['result']['dnsZoneOptions']
        return self.build_options(options_response['result']['dnsZoneOptions'])

    def updateZoneOptions(self, zone_ref, dns_options_input, saveComment=""):
        if isinstance(dns_options_input, DNSZoneOptions):
            dns_options_input = json.loads(dns_options_input.to_json())
        payload = {
            "saveComment" : saveComment,
            "dnsZoneOptions" : dns_options_input
        }
        return self.client.put("{0}{1}/Options".format(self.client.baseurl, zone_ref), payload)

    def getZoneScopes(self, zone_ref, **kwargs):
        query_string = ""
        if kwargs:
            for key, value in kwargs.items():
                if not query_string:
                    query_string += "?{0}={1}".format(key, value)
                else:
                    query_string += "&{0}={1}".format(key, value)
        dns_zone_response = self.client.get("{0}{1}/Scopes{2}".format(self.client.baseurl, zone_ref, query_string))
        return dns_zone_response['result']['dnsScopes']


class DNSRecords(object):
    def __init__(self, client):
        self.client = client
        self.url_base = "DNSRecords"

    def build(self, json_input):
        if isinstance(json_input, basestring):
            json_input = json.loads(json_input)
        return DNSRecord(**json_input)

    def get(self, record_ref):
        all_records = []
        dns_record_response = self.client.get("{0}{1}".format(self.client.baseurl, record_ref))
        all_records.append(self.build(dns_record_response['result']['dnsRecord']))
        return all_records

    def add(self, dnsRecord_input, saveComment="", autoAssignRangeRef="", dnsZoneRef="", forceOverride=""):
        if isinstance(dnsRecord_input, DNSRecord):
            dnsRecord_input = json.loads(dnsRecord_input.to_json())
        if not isinstance(dnsRecord_input, list):
            dnsRecord_input = [dnsRecord_input]
        payload = {
            "saveComment" : saveComment,
            "autoAssignRangeRef" : autoAssignRangeRef,
            "dnsZoneRef" : dnsZoneRef,
            "forceOverrideOfNamingConflictCheck" : forceOverride,
            "dnsRecords" : dnsRecord_input
        }
        record_json = self.client.post("{0}{1}".format(self.client.baseurl, self.url_base), payload)
        dns_record_return = []
        for ref in record_json['result']['objRefs']:
            dns_record_return.append(self.get(ref)[0])
        return dns_record_return

    def delete(self, record_ref, **kwargs):
        return self.client.deleteItem(record_ref, kwargs)

    def update(self, record_ref, properties, objType="DNSRecord", saveComment="", deleteUnspecified=False):
        return self.client.updateItem(record_ref, properties, objType, saveComment, deleteUnspecified)

    def getAccess(self, record_ref, **kwargs):
        return self.client.getItemAccess(record_ref, kwargs)

    def setAccess(self, record_ref, identity_access, object_type="", saveComment=""):
        return self.client.setItemAccess(record_ref, identity_access, object_type, saveComment)

    def getHistory(self, record_ref, **kwargs):
        return self.client.getItemHistory(record_ref, kwargs)

    def getPropertyDefinition(self, record_ref, property_name=""):
        return self.client.getPropertyDefinitions(record_ref, property_name)

    def addNewPropertyDefinition(self, record_ref, property_definition, saveComment=""):
        return self.client.newCustomProperty(record_ref, property_definition, saveComment)

    def updatePropertyDefinition(self, record_ref, property_name, property_definition, updateExisting="", saveComment=""):
        return self.client.updatePropertyDefinitions(record_ref, property_name, property_definition, updateExisting, saveComment)

    def deletePropertyDefinition(self, record_ref, property_name, saveComment=""):
        return self.client.deletePropertyDefinition(record_ref, property_name, saveComment)

    def getRelatedRecords(self, record_ref):
        all_records = []
        dns_record_response = self.client.get("{0}{1}/RelatedDNSRecords".format(self.client.baseurl, record_ref))
        for record in dns_record_response['result']['dnsRecords']:
                all_records.append(self.build(record))
        return all_records

    def deleteRelatedRecords(self, record_ref, **kwargs):
        query_string = ""
        if kwargs:
            for key, value in kwargs.items():
                if not query_string:
                    query_string += "?{0}={1}".format(key, value)
                else:
                    query_string += "&{0}={1}".format(key, value)
        return self.client.delete("{0}{1}/RelatedDNSRecords{2}".format(self.client.baseurl, record_ref, query_string))


class DNSViews(object):
    def __init__(self, client):
        self.client = client
        self.url_base = "DNSViews"

    def build(self, json_input):
        if isinstance(json_input, basestring):
            json_input = json.loads(json_input)
        return DNSView(**json_input)

    def get(self, view_ref="", **kwargs):
        all_views = []
        if not view_ref:
            query_string = ""
            if kwargs:
                for key, value in kwargs.items():
                    if not query_string:
                        query_string += "?{0}={1}".format(key, value)
                    else:
                        query_string += "&{0}={1}".format(key, value)
            dns_view_response = self.client.get("{0}{1}{2}".format(self.client.baseurl, self.url_base, query_string))
            for view in dns_view_response['result']['dnsViews']:
                all_views.append(self.build(view))
        else:
            dns_view_response = self.client.get("{0}{1}".format(self.client.baseurl, view_ref))
            all_views.append(self.build(dns_view_response['result']['dnsView']))
        return all_views

    def getZones(self, view_ref):
        all_zones = []
        dns_zone_response = self.client.get("{0}{1}/DNSZones".format(self.client.baseurl, view_ref))
        for zone in dns_zone_response['result']['dnsZones']:
            all_zones.append(DNSZones(self.client).build(zone))
        return all_zones