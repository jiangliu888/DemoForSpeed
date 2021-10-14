import copy
import uuid
import re

from erlang.libs.configCenter.interface.ConsulInterface import ConsulInterface


class ConsulKeyword(object):
    def __init__(self):
        pass

    @staticmethod
    def genUuid():
        return str(uuid.uuid1())

    @staticmethod
    def create_company(name, contact="", remark=""):
        body = {'name': name, 'contact': contact, 'remark': remark}
        companyId = ConsulKeyword.genUuid()
        res_code = ConsulInterface.put_company(companyId, body)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return companyId

    @staticmethod
    def update_company(company_id, name, contact="", remark=""):
        body = {'name': name, 'contact': contact, 'remark': remark}
        res_code = ConsulInterface.put_company(company_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_company(company_id):
        res_code = ConsulInterface.delete_company(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_company_sites(company_id, site_name, ne_id, private_addr=None, nets=None, public_if=None, public_addr=None):
        siteId = ConsulKeyword.genUuid()
        config = {"neId": int(ne_id), "nets": [nets] if nets else [],
                  "privateAddrs": [private_addr] if private_addr else [],
                  "publicAddrs": [{"iface": public_if[0], "index":0, "publicIp":public_addr[0]}, {"iface": public_if[1], "index":1, "publicIp":public_addr[1]}] if public_addr else []}

        body = {'id': siteId, 'name': site_name, 'config': config}
        res_code = ConsulInterface.put_company_sites(company_id, siteId, body)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return siteId

    @staticmethod
    def patch_company_sites(company_id, site_id, site_name, ne_id, private_addr=None, nets=None, public_if=None, public_addr=None, dynamicEnable=False):
        config = {"neId": int(ne_id), "nets": [nets] if nets else [],
                  "privateAddrs": private_addr if private_addr else [],
                  "dynamicEnable": dynamicEnable,
                  "publicAddrs": [{"iface": public_if[0], "index":0, "publicIp":public_addr[0]}, {"iface": public_if[1], "index":1, "publicIp":public_addr[1]}] if public_addr else []}

        res_code, body = ConsulInterface.get_company_sites(company_id, site_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        body['config'] = config
        res_code = ConsulInterface.put_company_sites(company_id, site_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_company_unions(company_id, name, private, siteAId, siteBId, officeNet=True, transportMode=1):
        unionId = ConsulKeyword.genUuid()
        body = {'name': name,
                "siteA": str(siteAId),
                "siteB": str(siteBId),
                "officeNet": officeNet,
                "transportMode": transportMode,
                "privateNet": private}
        res_code = ConsulInterface.put_company_unions(company_id, unionId, body)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return unionId

    @staticmethod
    def patch_company_union(company_id, union_id, name, private, siteAId, siteBId, officeNet=True, transportMode=1):
        body = {'name': name,
                "siteA": str(siteAId),
                "siteB": str(siteBId),
                "officeNet": officeNet,
                "transportMode": transportMode,
                "privateNet": private}
        res_code = ConsulInterface.put_company_unions(company_id, union_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_company_unions_private_value(company_id, union_id, is_private):
        res_code, body = ConsulInterface.get_company_unions(company_id, union_id)
        body["privateNet"] = is_private
        res_code = ConsulInterface.put_company_unions(company_id, union_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_company_unions_flow_value(company_id, union_id, transport_mode):
        res_code, body = ConsulInterface.get_company_unions(company_id, union_id)
        body["transportMode"] = int(transport_mode)
        res_code = ConsulInterface.put_company_unions(company_id, union_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_etc_fwRules(rule_name, priority, protocol, srcIP, dstIP, srcPort=0, dstPort=0, icmpType=0, icmpCode=0):
        body = {'name': rule_name, 'priority': priority, 'protocol': protocol,
                'srcIp': srcIP, 'srcPort': srcPort, 'dstIp': dstIP, 'dstPort': dstPort,
                'icmpType': icmpType, 'icmpCode': icmpCode}
        fwRuleId = ConsulKeyword.genUuid()
        res_code = ConsulInterface.put_etc_fwRules(fwRuleId, body)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return fwRuleId

    @staticmethod
    def update_etc_fw_rule(rule_id, rule_name, priority, protocol, srcIP, dstIP, srcPort=0, dstPort=0, icmpType=0, icmpCode=0, enabled=True, remark=''):
        body = {'name': rule_name, 'enabled': enabled, 'remark': remark, 'priority': priority,
                'protocol': protocol, 'srcIp': srcIP, 'srcPort': srcPort, 'dstIp': dstIP, 'dstPort': dstPort,
                'icmpType': icmpType, 'icmpCode': icmpCode}
        res_code = ConsulInterface.put_etc_fwRules(rule_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_etc_spiRules(priority, tag, srcCIDR, dstCIDR, l4proto, srcPort, dstPort, srcMac=None, dstMac=None, vlanPri=None, vlanTag=None, diffServ=None, ifname=None, ifindex=None):
        body = {
            'spi': {
                'vport': {'iface': ifname, 'index': ifindex} if ifname and ifindex else None,
                'srcMac': srcMac, 'dstMac': dstMac, 'vlanPri': vlanPri, 'vlanTag': vlanTag, 'diffServ': diffServ},
            'priority': priority, 'tag': int(tag)}
        if srcCIDR != 'any':
            body['spi']['srcCIDR'] = srcCIDR
        if dstCIDR != 'any':
            body['spi']['dstCIDR'] = dstCIDR
        if l4proto != 'any':
            body['spi']['l4proto'] = l4proto
        if srcPort != 'any':
            body['spi']['srcPort'] = srcPort
        if dstPort != 'any':
            body['spi']['dstPort'] = dstPort
        spiRuleId = ConsulKeyword.genUuid()
        res_code = ConsulInterface.put_etc_spiRules(spiRuleId, body)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return spiRuleId

    @staticmethod
    def create_etc_domain_spiRules(priority, tag, l4proto, dstDomain):
        body = {
            'spi': {'l4proto': l4proto, 'dstDomain': dstDomain},
            'priority': priority, 'tag': int(tag)}
        spiRuleId = ConsulKeyword.genUuid()
        res_code = ConsulInterface.put_etc_spiRules(spiRuleId, body)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return spiRuleId

    @staticmethod
    def update_etc_spi_rule(rule_id, rule_name, priority, protocol, srcIP, dstIP, srcPort=0, dstPort=0, icmpType=0, icmpCode=0, enabled=True, remark=''):
        body = {'name': rule_name, 'enabled': enabled, 'remark': remark, 'priority': priority,
                'protocol': protocol, 'srcIp': srcIP, 'srcPort': srcPort, 'dstIp': dstIP, 'dstPort': dstPort,
                'icmpType': icmpType, 'icmpCode': icmpCode}
        res_code = ConsulInterface.put_etc_fwRules(rule_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_etc_saasRules(domain_name, ttl, priority, name='default', agent=None, nat_type="DOMAIN"):
        body = \
            {
                "saasType": nat_type,
                "pattern": domain_name,
                "ttl": int(ttl),
                "priority": int(priority),
                "name": name,
                "agent": agent if agent else ""
            }
        saasRuleId = ConsulKeyword.genUuid()
        res_code = ConsulInterface.put_etc_saasRules(saasRuleId, body)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return saasRuleId

    @staticmethod
    def update_etc_saas_rule(rule_id, domain_name, ttl, priority, name='default', agent=None, nat_type="DOMAIN"):
        body = \
            {
                "saasType": nat_type,
                "pattern": domain_name,
                "ttl": int(ttl),
                "priority": int(priority),
                "name": name,
                "agent": agent if agent else ""
            }
        res_code = ConsulInterface.put_etc_saasRules(rule_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_all_nat_rules():
        res_code = ConsulInterface.delete_all_etc_saasRules()
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_all_spi_rules():
        res_code = ConsulInterface.delete_all_etc_spiRules()
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_etc_template_fw(fwRules=[]):
        fw_templateId = ConsulKeyword.genUuid()
        res_code = ConsulInterface.put_etc_template_fw(fw_templateId, fwRules)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return fw_templateId

    @staticmethod
    def create_etc_template_saas(saasRules=[]):
        saas_templateId = ConsulKeyword.genUuid()
        res_code = ConsulInterface.put_etc_template_saas(saas_templateId, saasRules)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return saas_templateId

    @staticmethod
    def create_etc_template_spi(spiRules=[]):
        spi_templateId = ConsulKeyword.genUuid()
        res_code = ConsulInterface.put_etc_template_spi(spi_templateId, spiRules)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return spi_templateId

    @staticmethod
    def delete_nat_pattern_groups(company_id, template_id):
        res_code = ConsulInterface.delete_company_template_saas(company_id, template_id)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_all_nat_groups():
        res_code = ConsulInterface.delete_etc_all_template_saas()
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_all_spi_groups():
        res_code = ConsulInterface.delete_etc_all_template_spi()
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_nat_pattern_rule(rule_id):
        res_code = ConsulInterface.delete_etc_saasRules(rule_id)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_saas_template(template_id):
        res_code = ConsulInterface.delete_etc_template_saas(template_id)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_company_site_fwGroup(company_id, site_id, fw_templates=[]):
        res_code = ConsulInterface.put_company_sites_fwGroups(company_id, site_id, fw_templates)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_company_site_saasGroups(company_id, site_id, saas_templates=[]):
        res_code = ConsulInterface.put_company_sites_saasGroups(company_id, site_id, saas_templates)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_company_site_spiGroups(company_id, site_id, spi_templates=[]):
        res_code = ConsulInterface.put_company_sites_spiGroups(company_id, site_id, spi_templates)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_company_site_bandwidth(company_id, site_id, bandwidth, burst, latency):
        body = {"bandwidth": int(bandwidth),
                "burst": int(burst),
                "latency": int(latency)}
        res_code = ConsulInterface.put_company_sites_rateLimit(company_id, site_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_company_union_bandwidth(company_id, union_id, bandwidth, burst, latency):
        body = {"bandwidth": int(bandwidth),
                "burst": int(burst),
                "latency": int(latency)}
        res_code = ConsulInterface.put_company_unions_rateLimit(company_id, union_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_company_sites(company_id, site_id=None):
        res_code = ConsulInterface.delete_company_site(company_id, site_id) if site_id else ConsulInterface.delete_all_site(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_company_unions(company_id, union_id=None):
        res_code = ConsulInterface.delete_company_unions(company_id, union_id) if union_id else ConsulInterface.delete_all_unions(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_cpe_all(dev_id, preferenceBody):
        preference_rcode = ConsulInterface.put_cpe_preference(dev_id, preferenceBody)
        assert preference_rcode == 200, '{} is not 200'.format(preference_rcode)

    @staticmethod
    def put_pop_all(dev_id, routeCodeBody):
        routeCode_rcode = ConsulInterface.put_pop_routecode(dev_id, routeCodeBody)
        assert routeCode_rcode == 200, '{} is not 200'.format(routeCode_rcode)

    @staticmethod
    def put_cfp_all(dev_id, routeCodeBody):
        routeCode_rcode = ConsulInterface.put_cfp_routecode(dev_id, routeCodeBody)
        assert routeCode_rcode == 200, '{} is not 200'.format(routeCode_rcode)

    @staticmethod
    def delete_ne(dev_id, ne_type):
        res_code = 0
        if (ne_type == "CR" or ne_type == "ER"):
            res_code = ConsulInterface.delete_ne_pop(dev_id)
        elif ne_type == "CFP":
            res_code = ConsulInterface.delete_ne_cfp(dev_id)
        elif ne_type == "CPE":
            res_code = ConsulInterface.delete_ne_cpe(dev_id)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_gaea_config():
        res_saas = ConsulInterface.put_services_gaea_saasSearchPattens([])
        res_con = ConsulInterface.put_services_gaea_openflowAddr({"global": [], "specific": {}})
        res_alg = ConsulInterface.delete_services_gaea_netAlgConfig()
        res_ma = ConsulInterface.put_services_gaea_managers({"global": [], "specific": {}})
        assert all(map(lambda x: True if x == 200 else False, [res_saas, res_con, res_alg, res_ma]))

    @staticmethod
    def delete_all_config():
        res_code = ConsulInterface.delete_all_consul_config()
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_gaea_openflow_config():
        res_code = ConsulInterface.put_services_gaea_openflowAddr({})
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_ne_cac_eac(ne_id, cac, eac, ne_type='pop'):
        data = {"cac": int(cac), "eac": int(eac)}
        res_code = ConsulInterface.put_ne_route_code(ne_id, data) if ne_type == 'pop' else ConsulInterface.put_cfp_routecode(ne_id, data)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_er_cac_eac(device_id_list, cac_list, eac_list):
        assert len(device_id_list) == len(eac_list)
        map(lambda x, y, z: ConsulKeyword.put_ne_cac_eac(x, y, z), device_id_list, cac_list, eac_list)

    @staticmethod
    def put_cpe_home_code_prefer(cpe_id, wan_if_list, cac_list, eac_list, prefer_ip=None, index_list=None):
        res_code, rsp = ConsulInterface.get_cpe_preference(cpe_id)
        index_l = index_list if index_list else range(len(wan_if_list))
        all_list = zip(wan_if_list, index_l, cac_list, eac_list, prefer_ip) if prefer_ip else zip(wan_if_list, index_l, cac_list, eac_list)

        def set_if_prefer(elem):
            tmpelem = copy.deepcopy(elem)

            def updatePreferBody(allInfo, elem):
                body = copy.deepcopy(elem)
                if (body['portId']['iface'] == allInfo[0] and body['portId']['index'] == int(allInfo[1])):
                    homeCodeBody = {"cac": int(allInfo[2]),
                                    "eac": int(allInfo[3])}
                    if len(allInfo) == 5:
                        homeCodeBody["preferIp"] = allInfo[4]
                    body['preferHomeCode'] = homeCodeBody
                return body
            tmpbodys = filter(lambda x: x != tmpelem, map(lambda x: updatePreferBody(x, tmpelem), all_list))
            return tmpbodys[0] if len(tmpbodys) != 0 else tmpelem
        bodys = map(lambda x: set_if_prefer(x), rsp)
        res_code = ConsulInterface.put_cpe_wan_home_code_prefer(cpe_id, bodys)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_ne_coreCode(ne_id, wan_if_list, cac_list, index_list=None):
        res_code, rsp = ConsulInterface.get_cpe_preference(ne_id)
        index_l = index_list if index_list else range(len(wan_if_list))
        all_list = zip(wan_if_list, index_l, cac_list)

        def set_if_prefer(elem):
            tmpelem = copy.deepcopy(elem)

            def updatePreferBody(allInfo, elem):
                body = copy.deepcopy(elem)
                if (body['portId']['iface'] == allInfo[0] and body['portId']['index'] == int(allInfo[1])):
                    body['preferCac'] = int(allInfo[2])
                return body
            tmpbodys = filter(lambda x: x != tmpelem, map(lambda x: updatePreferBody(x, tmpelem), all_list))
            return tmpbodys[0] if len(tmpbodys) != 0 else tmpelem
        bodys = map(lambda x: set_if_prefer(x), rsp)
        res_code = ConsulInterface.put_cpe_vport_coreCode(ne_id, bodys)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_cpe_home_code_prefer(cpe_id, wan_if_list, index_list=None):
        res_code, rsp = ConsulInterface.get_cpe_preference(cpe_id)
        index_l = index_list if index_list else range(len(wan_if_list))
        all_list = zip(wan_if_list, index_l)

        def set_if_prefer(elem):
            tmpelem = copy.deepcopy(elem)

            def updatePreferBody(allInfo, elem):
                body = copy.deepcopy(elem)
                if (body['portId']['iface'] == allInfo[0] and body['portId']['index'] == int(allInfo[1])):
                    if 'preferHomeCode' in body.keys():
                        body.pop('preferHomeCode')
                return body
            tmpbodys = filter(lambda x: x != tmpelem, map(lambda x: updatePreferBody(x, tmpelem), all_list))
            return tmpbodys[0] if len(tmpbodys) != 0 else tmpelem
        bodys = map(lambda x: set_if_prefer(x), rsp)
        res_code = ConsulInterface.put_cpe_preference(cpe_id, bodys)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_ne_status(ne_id, status):
        body = {"status": status}
        res_code = ConsulInterface.put_pop_status(ne_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_proxy_prefer_pop(service_id, prefer_pop_id):
        body = {"accessNode": int(prefer_pop_id)}
        res_code = ConsulInterface.put_ne_services_proxy_preference(service_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_anycast_prefer_pop(service_id, prefer_pop_id):
        body = {"accessNode": int(prefer_pop_id)}
        res_code = ConsulInterface.put_ne_services_anycast_preference(service_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_cpe_address_group(ne_id, iface, index, groups):
        res_code, rsp = ConsulInterface.get_cpe_preference(ne_id)

        def set_if_prefer(elem, iface, index, groups):
            tmpelem = copy.deepcopy(elem)
            if (tmpelem['portId']['iface'] == iface and tmpelem['portId']['index'] == int(index)):
                tmpelem['preferGroups'] = groups
            return tmpelem
        bodys = map(lambda x: set_if_prefer(x, iface, index, groups), rsp)
        res_code = ConsulInterface.put_cpe_preference(ne_id, bodys)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_ne_measure_algo(ne_id, delay=None, loss=None, stdev=None, m0=None, m1=None, m2=None, m3=None):
        res_code, rsp = ConsulInterface.get_cpe_linkScoreAlgo(int(ne_id))
        body = {
            "delay": int(delay) if delay else 100,
            "loss": int(loss) if loss else 100,
            "stdev": int(stdev) if stdev else 100,
            "m0": int(m0) if m0 else 70,
            "m1": int(m1) if m0 else 20,
            "m2": int(m2) if m0 else 10,
            "m3": int(m3) if m0 else 5}
        if res_code != 404:
            body = {
                "delay": int(delay) if delay else rsp['delay'],
                "loss": int(loss) if loss else rsp['loss'],
                "stdev": int(stdev) if stdev else rsp['stdev'],
                "m0": int(m0) if m0 else rsp['m0'],
                "m1": int(m1) if m1 else rsp['m1'],
                "m2": int(m2) if m2 else rsp['m2'],
                "m3": int(m3) if m3 else rsp['m3']}
        res_code = ConsulInterface.put_cpe_linkScoreAlgo(ne_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_cpe_linkscoreAlgo(neid):
        res_code = ConsulInterface.delete_cpe_linkScoreAlgo(int(neid))
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def change_running_measure_config(key, value):
        body = {
            "upperBandwidth": 100.0,
            "lowerBandwidth": 2.5,
            "upperBwPercent": 300.0,
            "lowBwPercent": 20.0,
            "maxLossIn15Min": 0.8,
            "avgLossIn60Min": 0.4,
            "maxLossRatio": 20.0
        }
        res_code, rsp = ConsulInterface.get_services_gaea_netAlgConfig()
        if res_code == 404:
            body[key] = float(value)
        else:
            rsp[key] = float(value)
            body = rsp
        res_code = ConsulInterface.put_services_gaea_netAlgConfig(body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_gaea_managers_global_config(ip_list, port_list):
        body = {}

        def global_key(ip, port):
            return {"ip": ip, "port": port}
        global_body = map(lambda ip, port: global_key(ip, port), ip_list, port_list)
        res_code, rsp = ConsulInterface.get_services_gaea_managers()
        if res_code == 404:
            body["global"] = global_body
        else:
            rsp["global"] = global_body
            body = rsp
        res_code = ConsulInterface.put_services_gaea_managers(body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def clear_managers():
        res_code = ConsulInterface.put_services_gaea_managers({"global": [], "specific": {}})
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def append_managers(manager_ip, manager_port):
        body = {}
        ipPortBody = {"ip": manager_ip, "port": manager_port}
        res_code, rsp = ConsulInterface.get_services_gaea_managers()
        if res_code == 404:
            body["global"] = [ipPortBody]
        else:
            if "global" in rsp.keys():
                rsp["global"].append(ipPortBody) if (ipPortBody not in rsp["global"]) else None
            else:
                rsp["global"] = [ipPortBody]
            body = rsp
        res_code = ConsulInterface.put_services_gaea_managers(body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_gaea_managers_specific_config(ne_id, ip_list, port_list):
        body = {}

        def global_key(ip, port):
            return {"ip": ip, "port": port}
        specific_body = map(lambda ip, port: global_key(ip, port), ip_list, port_list)
        res_code, rsp = ConsulInterface.get_services_gaea_managers()
        if res_code == 404:
            body["specific"] = {int(ne_id): specific_body}
        else:
            if "specific" in rsp.keys():
                rsp["specific"][int(ne_id)] = specific_body
            else:
                rsp["specific"] = {int(ne_id): specific_body}
            body = rsp
        res_code = ConsulInterface.put_services_gaea_managers(body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_gaea_openflow_global_config(ip_list, port_list):
        body = {}

        def global_key(ip, port):
            return {"ip": ip, "port": port}
        global_body = map(lambda ip, port: global_key(ip, port), ip_list, port_list)
        res_code, rsp = ConsulInterface.get_services_gaea_openflowAddr()
        if res_code == 404:
            body["global"] = global_body
        else:
            rsp["global"] = global_body
            body = rsp
        res_code = ConsulInterface.put_services_gaea_openflowAddr(body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_ne_controller_config():
        body = {}
        res_code, rsp = ConsulInterface.get_services_gaea_openflowAddr()
        if res_code == 404:
            body = {"global": [], "specific": {}}
        else:
            rsp["global"] = []
            body = rsp
        res_code = ConsulInterface.put_services_gaea_openflowAddr(body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_gaea_openflow_specific_config(ne_id, ip_list, port_list):
        body = {}

        def global_key(ip, port):
            return {"ip": ip, "port": port}
        specific_body = map(lambda ip, port: global_key(ip, port), ip_list, port_list)
        res_code, rsp = ConsulInterface.get_services_gaea_openflowAddr()
        if res_code == 404:
            body["specific"] = {int(ne_id): specific_body}
        else:
            if "specific" in rsp.keys():
                rsp["specific"][int(ne_id)] = specific_body
            else:
                rsp["specific"] = {int(ne_id): specific_body}
            body = rsp
        res_code = ConsulInterface.put_services_gaea_openflowAddr(body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_code_agent_pattern(pop_id_list, region, country=0, area=0, district=0, serviceType="saas", carrier=0):
        ConsulKeyword.modify_code_agent_pattern(pop_id_list, region, country, area, district, serviceType, carrier)

    @staticmethod
    def modify_code_agent_pattern(pop_id_list, region, country, area, district, serviceType, carrier=0):
        bodys = []
        res_code, rsp = ConsulInterface.get_services_gaea_saasSearchPattens() if serviceType == "saas" else ConsulInterface.get_services_gaea_anycastSearchPattens()

        def find_match(matcher, region, country, area, district):
            return True if (matcher['region'] == region and matcher['country'] == country and matcher['area'] == area and matcher['district'] == district) else False

        proxy_service = map(lambda x: int(x), pop_id_list)
        body = {
            "matcher": {"region": int(region),
                        "country": int(country),
                        "area": int(area),
                        "district": int(district),
                        "carrier": int(carrier)},
            "proxyServices": proxy_service
        }
        if res_code == 404:
            bodys.append(body)
        else:
            except_exsit = filter(lambda x: not find_match(x['matcher'], int(region), int(country), int(area), int(district)), rsp)
            bodys = except_exsit + [body]
        res_code = ConsulInterface.put_services_gaea_saasSearchPattens(bodys) if serviceType == "saas" else ConsulInterface.put_services_gaea_anycastSearchPattens(bodys)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_code_agent_pattern_by_code(region, country=0, area=0, district=0, carrier=0):
        res_code, rsp = ConsulInterface.get_services_gaea_saasSearchPattens()

        def find_match(matcher, region, country, area, district, carrier):
            return True if (matcher['region'] == region and matcher['country'] == country and matcher['area'] == area and matcher['district'] == district and matcher['carrier'] == carrier) else False

        body = filter(lambda x: not find_match(x['matcher'], int(region), int(country), int(area), int(district), int(carrier)), rsp)
        res_code = ConsulInterface.put_services_gaea_saasSearchPattens(body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_all_agent_pattern():
        res_code = ConsulInterface.put_services_gaea_saasSearchPattens([])
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def refresh_cpe_config(neid, key):
        match_get = {
            "preference": ConsulInterface.get_cpe_preference,
            "rateLimit": ConsulInterface.get_cpe_rateLimit,
            "Algo": ConsulInterface.get_cpe_linkScoreAlgo,
            "netConfig": ConsulInterface.get_cpe_netConfig
        }
        match_put = {
            "preference": ConsulInterface.put_cpe_preference,
            "rateLimit": ConsulInterface.put_cpe_rateLimit,
            "Algo": ConsulInterface.put_cpe_linkScoreAlgo,
            "netConfig": ConsulInterface.put_cpe_netConfig
        }
        res_code, rsp = match_get[key](int(neid))
        assert res_code == 200, '{} is not 200'.format(res_code)
        res_code = match_put[key](int(neid), rsp)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def change_cpe_netConfig(neid, mtu, keepAlive, strategy):
        netConfigBody = {
            "mtu": int(mtu),
            "keepAlive": int(keepAlive),
            "strategy": int(strategy)
        }
        res_code = ConsulInterface.put_cpe_netConfig(int(neid), netConfigBody)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_cpe_netConfig(neid):
        res_code = ConsulInterface.delete_cpe_netConfig(int(neid))
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_cpe_wan_bandwidth(ne_id, iface_name, index_v, bandwidth, burst, latency, ratio):
        vportBody = {
            "portId": {
                "iface": str(iface_name),
                "index": int(index_v)
                },
            "rateLimit": {
                "bandwidth": int(bandwidth),
                "burst": int(burst),
                "latency": int(latency),
                "ratio": int(ratio)
                }
            }
        res_code, rsp = ConsulInterface.get_cpe_rateLimit(int(ne_id))
        body = filter(lambda x: not (x["portId"]['iface'] == str(iface_name) and x["portId"]['index'] == int(index_v)), rsp) if res_code != 404 else []
        body.append(vportBody)
        res_code = ConsulInterface.put_cpe_rateLimit(int(ne_id), body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_cpe_wan_bandwidth(ne_id, iface_name, index_v):
        res_code, rsp = ConsulInterface.get_cpe_rateLimit(int(ne_id))
        assert res_code == 200, '{} is not 200'.format(res_code)
        body = filter(lambda x: not (x["portId"]['iface'] == str(iface_name) and x["portId"]['index'] == int(index_v)), rsp)
        res_code = ConsulInterface.put_cpe_rateLimit(int(ne_id), body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_company_site_bandwidth(company_id, site_id, bandwidth, burst, latency):
        body = {"bandwidth": int(bandwidth),
                "burst": int(burst),
                "latency": int(latency)}
        res_code = ConsulInterface.put_company_sites_rateLimit(company_id, site_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_company_union_bandwidth(company_id, union_id, bandwidth, burst, latency):
        body = {"bandwidth": int(bandwidth),
                "burst": int(burst),
                "latency": int(latency)}
        res_code = ConsulInterface.put_company_unions_rateLimit(company_id, union_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_company_site_bandwidth(company_id, site_id):
        res_code = ConsulInterface.delete_company_sites_rateLimit(company_id, site_id)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_company_union_bandwidth(company_id, union_id):
        res_code = ConsulInterface.delete_company_unions_rateLimit(company_id, union_id)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_pop_saas(ne_id):
        res_code = ConsulInterface.put_pop_saasServices(ne_id, [])
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_pop_saas(pop_id, end_point, phy_port):
        body = \
            {
                "serviceId": int(end_point),
                "iface": phy_port
            }
        res_code = ConsulInterface.put_pop_saasServices(str(pop_id), [body])
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def add_more_pop_saas(pop_id, end_point, phy_port):
        body = \
            {
                "serviceId": int(end_point),
                "iface": phy_port
             }
        res_code, saas_list = ConsulInterface.get_pop_saasServices(pop_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        saas_list.append(body)
        res_code = ConsulInterface.put_pop_saasServices(str(pop_id), saas_list)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_pop_saas_with_service_id(ne_id, service_id):
        res_code, service_list = ConsulInterface.get_pop_saasServices(ne_id)
        body = filter(lambda x: x["serviceId"] != int(service_id), service_list)
        res_code = ConsulInterface.put_pop_saasServices(ne_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def put_company_key(company_id, algorithm="", format="", key=""):
        body = {'algorithm': algorithm, 'format': format, 'key': key}
        res_code = ConsulInterface.put_company_encryption(company_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def set_device_tunnel_netcnf(neid, strategy, mtu):
        body = {"mtu": int(mtu), "keepAlive": 10, "strategy": int(strategy)}
        res_code = ConsulInterface.put_cpe_netConfig(int(neid), body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def set_wrong_cpe_home_code_prefer(cpe_id):
        res_code, rsp = ConsulInterface.get_cpe_preference(cpe_id)
        reset_body = map(lambda x: {'portId': x["portId"], 'preferHomeCode': {'cac': 15, 'eac': 63,
                                    'preferIp': x['preferHomeCode']['preferIp']}}, rsp)
        res_code = ConsulInterface.put_cpe_wan_home_code_prefer(cpe_id, reset_body)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return rsp

    @staticmethod
    def retore_cpe_home_code_prefer(cpe_id, body):
        res_code = ConsulInterface.put_cpe_wan_home_code_prefer(cpe_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def create_code_agent_pattern_company(company_id, pop_id_list, region, country=0, area=0, district=0):
        ConsulKeyword.modify_code_agent_pattern_company(company_id, pop_id_list, region, country, area, district)

    @staticmethod
    def modify_code_agent_pattern_company(company_id, pop_id_list, region, country, area, district):
        bodys = []
        res_code, rsp = ConsulInterface.get_services_company_saasSearchPattens(company_id)

        def find_match(matcher, region, country, area, district):
            return True if (matcher['region'] == region and matcher['country'] == country and matcher['area'] == area and matcher['district'] == district) else False

        proxy_service = map(lambda x: int(x), pop_id_list)
        body = {
            "matcher": {"region": int(region),
                        "country": int(country),
                        "area": int(area),
                        "district": int(district)},
            "proxyServices": proxy_service
        }
        if res_code == 404:
            bodys.append(body)
        else:
            except_exsit = filter(lambda x: not find_match(x['matcher'], int(region), int(country), int(area), int(district)), rsp)
            bodys = except_exsit + [body]
        res_code = ConsulInterface.put_services_company_saasSearchPattens(company_id, bodys)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_code_agent_pattern_by_code_company(company_id, region, country=0, area=0, district=0):
        res_code, rsp = ConsulInterface.get_services_company_saasSearchPattens(company_id)

        def find_match(matcher, region, country, area, district):
            return True if (matcher['region'] == region and matcher['country'] == country and matcher['area'] == area and matcher['district'] == district) else False

        bodys = filter(lambda x: not find_match(x['matcher'], int(region), int(country), int(area), int(district)), rsp)
        res_code = ConsulInterface.put_services_company_saasSearchPattens(company_id, bodys)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_all_agent_pattern_company(company_id):
        res_code = ConsulInterface.put_services_company_saasSearchPattens(company_id, [])
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_all_company_routes(company_id):
        res_code = ConsulInterface.put_company_routes(company_id, [])
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_all_company_acls(company_id):
        res_code = ConsulInterface.put_company_acls(company_id, [])
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_company_route(company_id, route_name):
        ret_code, routes = ConsulInterface.get_company_routes(company_id)
        body = filter(lambda x: x['name'] != route_name, routes)
        res_code = ConsulInterface.put_company_routes(company_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_company_acl(company_id, acl_name):
        ret_code, acls = ConsulInterface.get_company_acls(company_id)
        body = filter(lambda x: x['name'] != acl_name, acls)
        res_code = ConsulInterface.put_company_acls(company_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def add_company_route(company_id, route_name, priority, nextHop, dstCIDR=None, srcCIDR=None, protocol=None, srcPort=None, dstPort=None, domain=None, site_id=None):
        nextHops = [nextHop] if type(nextHop) is not list else nextHop
        site_ids = [site_id] if type(site_id) is not list else site_id
        route_body = {"name": route_name,
                      "priority": priority,
                      "nextHops": nextHops,
                      "srcCIDR": srcCIDR,
                      "dstCIDR": dstCIDR,
                      "protocol": protocol,
                      "srcPort": srcPort,
                      "dstPort": dstPort,
                      "domain": domain,
                      "siteIds": site_ids}

        for key, value in route_body.items():
            if value is None:
                del route_body[key]
        ret_code, body = ConsulInterface.get_company_routes(company_id)
        routes = [] if ret_code == 404 else body
        routes.append(route_body)
        res_code = ConsulInterface.put_company_routes(company_id, routes)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def add_company_acl(company_id, acl_name, siteId, priority, strategy, srcCIDR=None, dstCIDR=None, protocol=None, srcPort=None, dstPort=None):
        acl_body = {"name": acl_name,
                    "siteId": siteId,
                    "priority": priority,
                    "strategy": strategy,
                    "srcCIDR": srcCIDR,
                    "dstCIDR": dstCIDR,
                    "protocol": protocol,
                    "srcPort": srcPort,
                    "dstPort": dstPort}

        for key, value in acl_body.items():
            if value is None:
                del acl_body[key]
        ret_code, body = ConsulInterface.get_company_acls(company_id)
        acls = [] if ret_code == 404 else body
        acls.append(acl_body)
        res_code = ConsulInterface.put_company_acls(company_id, acls)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def modify_cpe_tunnel_port(dev_id, tunnel_port):
        res_code, body = ConsulInterface.get_device_aiwan_startup(dev_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        body["tunnelPort"] = int(tunnel_port)
        res_code = ConsulInterface.put_device_aiwan_startup(dev_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def update_cpe_startup_wan(dev_id, action, wan_name, insert_id=-1, mode='FIA', usage='normal'):
        res_code, startup = ConsulInterface.get_device_aiwan_startup(dev_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        if action == 'del':
            startup["interface"] = filter(lambda x: x['name'] != wan_name, startup['interface'])
        else:
            startup['interface'].insert(insert_id,
                                        {'usage': usage, 'proxy': True, 'type': 'WAN', 'name': wan_name, 'mode': mode})
        res_code = ConsulInterface.put_device_aiwan_startup(dev_id, startup)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def modify_company_version(company_id):
        res_code, body = ConsulInterface.get_company_config_version(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        body["version"] = body["version"] + 1
        body["updatetime"] = body["updatetime"] + 10
        res_code = ConsulInterface.put_company_config_version(company_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def get_company_spi_tag_id_by_name(company_id, name):
        status_code, rsp = ConsulInterface.get_company_spiTags(company_id)
        assert status_code == 200, '{} is not 200'.format(status_code)
        tag_id = map(lambda y: y['tag'], filter(lambda x: x['name'] == name, rsp))
        return tag_id[0]

    @staticmethod
    def add_company_spi_tag(company_id, name, rules=[]):
        tag_id = 1
        status_code, body = ConsulInterface.get_company_spiTags(company_id)
        if status_code == 200 and body != []:
            tag_ids = map(lambda x: x['tag'], body)
            tag_names = map(lambda x: x['name'], body)
            tag_id = max(tag_ids) + 1
            if name in tag_names:
                tag_id = ConsulKeyword.get_company_spi_tag_id_by_name(company_id, name)
                body = filter(lambda x: x['name'] != name, body)
        body = list(body)
        tag_body = {"tag": int(tag_id), "name": name, "rules": rules}
        body.append(tag_body)
        res_code = ConsulInterface.put_company_spiTags(company_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return tag_id

    @staticmethod
    def append_company_spi_tag_rules(company_id, domain_name_ip, name):
        pattern = re.compile('[a-zA-Z]')
        rule = {"dstDomain": domain_name_ip} if re.search(pattern, domain_name_ip) else {"dstCIDR": domain_name_ip}
        ConsulKeyword.append_company_spi_tag_rule_by_name(company_id, name, rule)

    @staticmethod
    def append_company_spi_Qos_tag_rules(company_id, protocol, src_ip, src_port, dst_ip, dst_port, tag_name):
        temp_rule = {"srcCIDR": src_ip, "dstCIDR": dst_ip, "l4proto": protocol, "srcPort": src_port, "dstPort": dst_port}
        rule = {key: val for key, val in temp_rule.items() if val != '*'}
        ConsulKeyword.append_company_spi_tag_rule_by_name(company_id, tag_name, rule)

    @staticmethod
    def append_company_spi_Fec_tag_rules(company_id, protocol, src_ip, src_port, dst_ip, dst_port, tag_name):
        temp_rule = {"srcCIDR": src_ip, "dstCIDR": dst_ip, "l4proto": protocol, "srcPort": src_port, "dst_port": dst_port}
        rule = {key: val for key, val in temp_rule.items() if val != '*'}
        ConsulKeyword.append_company_spi_tag_rule_by_name(company_id, tag_name, rule)

    @staticmethod
    def append_company_spi_tag_rule_by_name(company_id, tag_name, rule):
        ret_code, tags = ConsulInterface.get_company_spiTags(company_id)
        assert ret_code == 200, '{} is not 200'.format(ret_code)
        assert tag_name in map(lambda x: x['name'], tags)

        def append_rule(tag, tag_name, rule):
            tag['rules'].append(rule) if tag['name'] == tag_name else None

        def insert_rule_id(tag, rule):
            ids = map(lambda y: y['id'], filter(lambda x: 'id' in x, tag['rules']))
            rule["id"] = max(ids) + 1 if len(ids) else 0

        insert_rule_id(filter(lambda x: x['name'] == tag_name, tags)[0], rule)
        map(lambda x: append_rule(x, tag_name, rule), tags)
        res_code = ConsulInterface.put_company_spiTags(company_id, tags)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def update_company_spi_tag_rule(company_id, tag_id, rule_id, update_field, update_value):
        rule_id = int(rule_id)
        ret_code, tags = ConsulInterface.get_company_spiTags(company_id)
        assert ret_code == 200, '{} is not 200'.format(ret_code)
        assert tag_id in map(lambda x: x['tag'], tags)
        if update_value is None:
            if update_field in filter(lambda x: x['tag'] == tag_id, tags)[0]['rules'][rule_id]:
                filter(lambda x: x['tag'] == tag_id, tags)[0]['rules'][rule_id].pop(update_field)
        elif len(filter(lambda x: x['id'] == rule_id, filter(lambda x: x['tag'] == tag_id, tags)[0]['rules'])) > 0:
            filter(lambda x: x['tag'] == tag_id, tags)[0]['rules'][rule_id][update_field] = update_value
        else:
            filter(lambda x: x['tag'] == tag_id, tags)[0]['rules'].append({"id": int(rule_id), update_field: update_value})
        res_code = ConsulInterface.put_company_spiTags(company_id, tags)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_company_spi_tag(company_id, spi_tag_name):
        ret_code, tags = ConsulInterface.get_company_spiTags(company_id)
        tags_body = filter(lambda x: x['name'] != spi_tag_name, tags)
        res_code = ConsulInterface.put_company_spiTags(company_id, tags_body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_all_company_spi_tags(company_id):
        res_code = ConsulInterface.put_company_spiTags(company_id, [])
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def add_site_spi_dispatch(company_id, site_id, tag_id, priority, actions=[]):
        ret_code, body = ConsulInterface.get_company_sites_spiDispatches(company_id, site_id)
        dispatches = [] if ret_code == 404 else body
        spi_dispatch_body = {"tag": int(tag_id), "priority": int(priority), "actions": actions}
        dispatches.append(spi_dispatch_body)
        res_code = ConsulInterface.put_company_sites_spiDispatches(company_id, site_id, dispatches)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def get_appointment_param_with_port(saas_list, port_list):
        saas_port_list = zip(saas_list, port_list)
        return [{"serviceId": int(x[0]), "carrierId": int(x[1])} for x in saas_port_list]

    @staticmethod
    def config_saas_params_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, agent_codes, indexes, ttls,
                                                 nuwa_type=None, max_time=None, max_pkt=None, appointment=None):
        params = list()

        def form_dispatch_param(agent_code, index, ttl):
            pattern = re.compile(r'\D')
            return [{"agent": agent_code, "id": int(index), "ttl": int(ttl)}] if (re.search(pattern, str(agent_code)) or agent_code == '') else [{"code": str(agent_code), "id": int(index), "ttl": int(ttl)}]

        def get_appointment_param(pop_list):
            return [{"serviceId": int(x), "carrierId": 13} for x in pop_list]

        for agent_code, index, ttl in zip(agent_codes, indexes, ttls):
            params += form_dispatch_param(agent_code, index, ttl)
        saas_action = [{'name': "saas", 'param': params, "appointment": get_appointment_param(appointment)}] if appointment else [{'name': "saas", 'param': params}]
        if nuwa_type == "partialReliable":
            assert max_time is not None
            assert max_pkt is not None
        nuwa_action = [{'name': "transportPolicy", 'param': [{"policy": nuwa_type,
                                                              "waitParam": {"maxTime": int(max_time), "maxPktNum": int(
                                                                  max_pkt)}}]}] if nuwa_type == "partialReliable" else [
            {'name': "transportPolicy", 'param': [{"policy": nuwa_type}]}]
        saas_nuwa_actions = saas_action + nuwa_action if nuwa_type is not None else saas_action
        ret_code, body = ConsulInterface.get_company_sites_spiDispatches(company_id, site_id)
        dispatches = [] if ret_code == 404 else body
        dispatches_body = filter(lambda x: x['tag'] != tag_id, dispatches)
        this_dispatches = filter(lambda x: x['tag'] == tag_id, dispatches)
        if len(this_dispatches):
            other_actions = filter(lambda x: x['name'] != 'saas' and x['name'] != 'transportPolicy', this_dispatches[0]['actions'])
            this_dispatches[0]['actions'] = saas_nuwa_actions + other_actions
            this_dispatches[0]['priority'] = int(priority)
        else:
            this_dispatches = [{"tag": int(tag_id), "priority": int(priority), "actions": saas_nuwa_actions}]
        res_code = ConsulInterface.put_company_sites_spiDispatches(company_id, site_id, dispatches_body + this_dispatches)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_site_spi_dispatch(company_id, site_id, tag_id):
        ret_code, dispatches = ConsulInterface.get_company_sites_spiDispatches(company_id, site_id)
        dispatchs_body = filter(lambda x: int(x['tag']) != int(tag_id), dispatches)
        res_code = ConsulInterface.put_company_sites_spiDispatches(company_id, site_id, dispatchs_body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_all_site_spi_dispatches(company_id, site_id):
        res_code = ConsulInterface.put_company_sites_spiDispatches(company_id, site_id, [])
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def config_transport_params_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, policy, max_time=100, max_pks=0):
        action = {"name": "transportPolicy", "param": [{"policy": policy}]}
        if policy == "partialReliable":
            action["param"] = [{"policy": policy, "waitParam": {"maxTime": max_time, "maxPktNum": max_pks}}]
        ConsulKeyword.append_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, action)

    @staticmethod
    def config_pri_params_to_site_qos_spi_dispatchs(company_id, site_id, tag_id, priority, pri_level):
        action = {"name": "priority", "param": [{"level": pri_level}]}
        ConsulKeyword.append_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, action)

    @staticmethod
    def config_wan_params_to_site_qos_spi_dispatchs(company_id, site_id, tag_id, priority, poli, ports=[]):
        action = {"name": "wan", "param": [{"policy": poli, "ports": ports}]}
        ConsulKeyword.append_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, action)

    @staticmethod
    def update_wan_params_to_site_qos_spi_dispatchs(company_id, site_id, tag_id, priority, poli, ports=[]):
        action = {"name": "wan", "param": [{"policy": poli, "ports": ports}]}
        ConsulKeyword.update_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, action)

    @staticmethod
    def config_fec_params_to_site_fec_spi_dispatchs(company_id, site_id, tag_id, priority, policy="always", period=None, trigger=None, recovery=None):
        action_fec = {"name": "fec", "param": [{"policy": 'always'}]} if policy == "always" else {"name": "fec",
                                                                                                  "param": [{"policy": 'dynamic',
                                                                                                             "dynamicParam": {"period": int(period), "trigger": int(trigger), "recovery": int(recovery)}}]}
        ConsulKeyword.append_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, action_fec)

    @staticmethod
    def append_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, action):
        ret_code, body = ConsulInterface.get_company_sites_spiDispatches(company_id, site_id)
        dispatches = [] if ret_code == 404 else body
        dispatch_tags = map(lambda x: x['tag'], dispatches)

        def append_action(dispatch, tag_id, act):
            if dispatch['tag'] == int(tag_id):
                tmp = filter(lambda x: x['name'] != act['name'], dispatch['actions']) if len(filter(lambda x: x['name'] == act['name'], dispatch['actions'])) == 1 else dispatch['actions']
                tmp.append(act)
                dispatch['actions'] = tmp

        if (int(tag_id) in dispatch_tags):
            map(lambda x: append_action(x, tag_id, action), dispatches)
        else:
            dispatches.append({"tag": int(tag_id), "priority": int(priority), "actions": [action]})
        res_code = ConsulInterface.put_company_sites_spiDispatches(company_id, site_id, dispatches)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_action_to_site_spi_dispatchs(company_id, site_id, tag_id, action):
        ret_code, body = ConsulInterface.get_company_sites_spiDispatches(company_id, site_id)
        dispatches = [] if ret_code == 404 else body
        dispatch_tags = map(lambda x: x['tag'], dispatches)

        def del_action(dispatch, tag_id, act):
            new_action = filter(lambda x: x['name'] != act, dispatch['actions']) if dispatch['tag'] == int(tag_id) else dispatch['actions']
            dispatch['actions'] = new_action

        if (int(tag_id) in dispatch_tags):
            map(lambda x: del_action(x, tag_id, action), dispatches)
        res_code = ConsulInterface.put_company_sites_spiDispatches(company_id, site_id, dispatches)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def append_office_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, dc_site_id, dns_server=None, id=None, ttl=None):
        action = {"name": "office", "param": [{"nextHop": dc_site_id}]} if dns_server is None else {"name": "office",
                                                                                                    "param": [{"nextHop": dc_site_id,
                                                                                                               "dnsParam": [{"agent": dns_server, "id": int(id), "ttl": int(ttl)}]}]}
        ConsulKeyword.append_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, action)

    @staticmethod
    def append_analyze_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority):
        action = {"name": "analyze"}
        ConsulKeyword.append_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, action)

    @staticmethod
    def update_action_to_site_spi_dispatchs(company_id, site_id, tag_id, priority, action):
        ret_code, body = ConsulInterface.get_company_sites_spiDispatches(company_id, site_id)
        dispatches = [] if ret_code == 404 else body
        dispatch_tags = map(lambda x: x['tag'], dispatches)

        def update_action(dispatch, tag_id, act):
            wan_param = filter(lambda x: x['name'] == 'wan', dispatch['actions'])[0]
            dispatch['actions'].remove(wan_param)
            dispatch['actions'].append(act) if dispatch['tag'] == int(tag_id) else None

        if (int(tag_id) in dispatch_tags):
            map(lambda x: update_action(x, tag_id, action), dispatches)
        res_code = ConsulInterface.put_company_sites_spiDispatches(company_id, site_id, dispatches)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def update_appointment_to_site_saas_spi_dispatchs(company_id, site_id, tag_id, saas_list, port_list):
        ret_code, body = ConsulInterface.get_company_sites_spiDispatches(company_id, site_id)
        dispatches = [] if ret_code == 404 else body
        dispatch_tags = map(lambda x: x['tag'], dispatches)

        def add_appoitment_in_saas_action(dispatch, tag_id, saas_l, port_l):
            if dispatch['tag'] == int(tag_id):
                saas_param = filter(lambda x: x['name'] == 'saas', dispatch['actions'])[0]
                dispatch['actions'].remove(saas_param)
                if saas_l == [] and 'appointment' in saas_param.keys():
                    del saas_param['appointment']
                if saas_l != []:
                    saas_param['appointment'] = ConsulKeyword.get_appointment_param_with_port(saas_l, port_l)
                dispatch['actions'].append(saas_param)

        if (int(tag_id) in dispatch_tags):
            map(lambda x: add_appoitment_in_saas_action(x, tag_id, saas_list, port_list), dispatches)
        res_code = ConsulInterface.put_company_sites_spiDispatches(company_id, site_id, dispatches)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_fec_params_to_site_fec_spi_dispatchs(company_id, site_id, tag_id):
        action_fec = {"name": "fec", "param": [{"policy": 'always'}]}
        ConsulKeyword.delete_action_to_site_spi_dispatchs(company_id, site_id, tag_id, action_fec)

    @staticmethod
    def update_cpeGlobalConfig_ne_controllers(domain):
        ret_code, body = ConsulInterface.get_cpeGlobalConfig_ne()
        for index in range(len(body['controllers'])):
            body['controllers'][index]['domain'] = domain
        res_code = ConsulInterface.put_cpeGlobalConfig_ne(body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def get_alert_enable(sn):
        status_code, rsp = ConsulInterface.get_monitor_device_alert(sn)
        assert status_code == 200, '{} is not 200'.format(status_code)
        return rsp['enable']

    @staticmethod
    def set_device_auth_audit(sn, auth, audit):
        status_code, body = ConsulInterface.get_device_auth(sn)
        assert status_code == 200, '{} is not 200'.format(status_code)
        body['enable'] = auth
        ConsulInterface.put_device_auth(sn, body)
        status_code, body = ConsulInterface.get_device_audit(sn)
        assert status_code == 200, '{} is not 200'.format(status_code)
        body['enable'] = audit
        ConsulInterface.put_device_audit(sn, body)

    @staticmethod
    def set_device_auth_audit_config(sn, authServer, auth, auditServer, audit):
        body = {'authServer': authServer, "enable": auth}
        status_code = ConsulInterface.put_device_auth(sn, body)
        assert status_code == 200, '{} is not 200'.format(status_code)
        body = {'auditServer': auditServer, "enable": audit}
        status_code = ConsulInterface.put_device_audit(sn, body)
        assert status_code == 200, '{} is not 200'.format(status_code)
