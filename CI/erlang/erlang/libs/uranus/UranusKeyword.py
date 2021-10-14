import re
import copy
from itertools import *
from copy import deepcopy
import time

from erlang.libs.uranus.interface.UranusInterface import UranusInterface
from erlang.libs.uranus.GaeaKeyword import GaeaKeyword
from erlang.libs.uranus.interface.UranusCli import UranusCli
from erlang.libs.uranus.interface.NeCli import NeCli
from erlang.libs.variables import InterfacePathVariables
from erlang.libs.uranus.interface.EsInterface import EsInterface
from erlang.libs.variables import FlowVariables
from erlang.libs.common.JsonUtil import are_same, load_json
from erlang.libs.uranus.interface.OnosInterface import OnosInterface


class UranusKeyword(object):
    def __init__(self):
        pass

    @staticmethod
    def get_available_devices(protocol):
        res_code, body = OnosInterface.get_devices()
        assert res_code == 200, '{} is not 200'.format(res_code)
        dev_list = filter(lambda x: (x["annotations"]["protocol"] == protocol) and x["available"], body["devices"])
        return len(dev_list), dev_list

    @staticmethod
    def check_device_status(ne_id, protocol):
        res_code, body = OnosInterface.get_devices()
        assert res_code == 200, '{} is not 200'.format(res_code)
        dev_list = filter(lambda x: (x["annotations"]["protocol"] == protocol), body["devices"])
        id = 'netconf:' + str(ne_id) if protocol == "NETCONF" else 'of:' + hex(int(ne_id))[2:].rjust(16, '0')
        dev = filter(lambda x: x['id'] == id, dev_list)
        return dev[0]["available"]

    @staticmethod
    def get_routeid_from_gneid(gneid, wan_id):
        ne_type = int(gneid) & 0x0f
        ne_id = int(gneid) >> 4
        numbers = {
            0: (ne_type << 20) + (ne_id << 4) + int(wan_id),
            1: (ne_type << 20) + (ne_id << 3) + int(wan_id),
            2: (ne_type << 20) + (ne_id << 2) + int(wan_id),
            3: (ne_type << 20) + (ne_id << 4) + int(wan_id),
            4: (ne_type << 20) + (ne_id << 3) + int(wan_id),
            5: (ne_type << 20) + (ne_id << 2) + int(wan_id),
            7: (ne_type << 20) + (ne_id << 10) + 0,
            8: (ne_type << 20) + (ne_id << 6) + 0
        }
        return numbers.get(ne_type, None)

    @staticmethod
    def get_device_dest_dev_flow_packets(ne_id, dest_dev, dest_dev_port):
        device_id = UranusKeyword.get_openflow_dev_id_from_ne_id(ne_id)
        res_code, body = OnosInterface.get_device_flow(device_id)
        assert res_code == 200, '{} is no 200'.format(res_code)
        selector_info_list = UranusCli.get_device_flows_selector_info(device_id,
                                                                      map(lambda x: format(int(x["id"]), 'x'),
                                                                          body["flows"]))
        print '{routeId=AiwanRouteId{id=0x%08x}' % UranusKeyword.get_routeid_from_gneid(dest_dev, dest_dev_port)
        flows = [body["flows"][i] for i in range(len(selector_info_list))
                 if '{routeId=AiwanRouteId{id=0x%08x}' % UranusKeyword.get_routeid_from_gneid(dest_dev, dest_dev_port)
                 in selector_info_list[i]]
        print flows
        high_priority_flow = sorted(flows, key=lambda k: k['priority'], reverse=True)[0]
        return high_priority_flow['packets']

    @staticmethod
    def get_device_id_by_ip(ip, ne_type):
        res_code, body = OnosInterface.get_devices()
        assert res_code == 200, '{} is not 200'.format(res_code)
        of_dev = filter(lambda x: (x["annotations"]["protocol"] == "OF_13"), body["devices"])
        try:
            chassis_id = UranusKeyword.get_chassis_id_from_cnf_by_ip(ip, ne_type)
            dev_of = filter(lambda x: (x["chassisId"] == format(chassis_id, 'x')), of_dev)[0]
            return dev_of["id"], chassis_id
        except IndexError:
            return None, None

    @staticmethod
    def get_device_id_from_cnf_with_type(ne_type):
        res_code, body = UranusInterface.get_netcfg_ne_config()
        assert res_code == 200, '{} is not 200'.format(res_code)
        ret = filter(lambda x: x["type"] == ne_type, body['{}s'.format(InterfacePathVariables.switch_type(ne_type))])
        return map(lambda x: x["neId"], ret)

    @staticmethod
    def get_all_device_id_from_cnf():
        res_code, body = UranusInterface.get_netcfg_ne_config()
        assert res_code == 200, '{} is not 200'.format(res_code)
        ret = body["cpes"] + body["pops"]
        return map(lambda x: x["neId"], ret)

    @staticmethod
    def get_device_tunnel_netcnf(device_ip, ssh_port, ssh_user, ssh_password):
        ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                       '/aiwan-config:aiwan-switch/resource/tunnels/tunnel//*')
        if ret:
            return ret['aiwan-config:aiwan-switch']['resource']['tunnels']['tunnel']
        else:
            return []

    @staticmethod
    def set_ne_tunnels_netcnf(ne_id, tunnel_id, srcIP, srcPort, mtu, dstNEId, dstIP, dstPort):
        body = {
            "tunnelId": tunnel_id,
            "srcIP": srcIP,
            "srcPort": srcPort,
            "mtu": mtu,
            "dstNEId": dstNEId,
            "dstIP": dstIP,
            "dstPort": dstPort
        }
        UranusInterface.post_ne_tunnels_config(ne_id, body)

    @staticmethod
    def get_chassis_id_from_cnf_by_ip(ip, ne_type):
        res_code, body = UranusInterface.get_netcfg_ne_config()
        assert res_code == 200, '{} is not 200'.format(res_code)
        return filter(lambda x: x["config"]["netconf"]['ip'] == ip, body['{}s'.format(ne_type)])[0]["neId"]

    @staticmethod
    def set_device_flow_spec(s_chassis_id, s_port, d_chassis_id, d_port, dest_host_ip, dcac, deac):
        body = InterfacePathVariables.flow_spec
        body['neId'] = s_chassis_id
        body['matcher']['inPort'] = s_port
        body['matcher']['dstIp'] = '{}/32'.format(dest_host_ip)
        body['actions'][0]['dcac'] = int(dcac)
        body['actions'][0]['deac'] = int(deac)
        body['actions'][1]['srcRouteId'] = int(s_chassis_id) * 16 + int(s_port)
        body['actions'][1]['dstRouteId'] = int(d_chassis_id) * 16 + int(d_port)
        res_code, ret = OnosInterface.post_cpe_flow_spec([body])
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body

    @staticmethod
    def all_cpe_get_cac_eac():
        dev_list = UranusKeyword.get_device_id_from_cnf_with_type('CPE')
        cac_eac_list = map(lambda x: UranusInterface.get_cpe_wan_home_code(x), dev_list)
        return all(map(lambda wan_cac_eac_list: all(map(lambda x: (x["cac"] != -1) and (x['eac'] != -1), wan_cac_eac_list)), cac_eac_list))

    @staticmethod
    def get_companies(skip=0, limit=10):
        res_code, body = UranusInterface.get_all_company_config(skip, limit)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return map(lambda x: x['id'], body['results'])

    @staticmethod
    def get_device_key_netcnf(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/secretKey//*')
            return ret['aiwan-config:aiwan-switch']['resource']['secretKey']['AES128'] if 'AES128' in ret[
                'aiwan-config:aiwan-switch']['resource']['secretKey'].keys() else \
                ret['aiwan-config:aiwan-switch']['resource']['secretKey']['AESKey']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_device_net_measure_tasks(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/net-measure-tasks//*')
            return ret['aiwan-config:aiwan-switch']['resource']['net-measure-tasks']['task']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def check_measure_tasks_over_tunnel(device_ip, ssh_port, ssh_user, ssh_password):
        tasks = UranusKeyword.get_device_net_measure_tasks('192.168.0.220', 22, 'sdn', 'rocks')
        tunnels = UranusKeyword.get_device_tunnel_netcnf('192.168.0.220', 22, 'sdn', 'rocks')
        for task in tasks:
            tunnel = filter(lambda x: x['number'] == task['tunnel-number'], tunnels)
            assert tunnel[0]['remote-id'] == task['remote-id']
        return map(lambda x: x['id'], tasks)

    @staticmethod
    def get_device_tunnel_fragment_strategy(device_ip, ssh_port, ssh_user, ssh_password, tunnels):
        ret_tunnel = UranusKeyword.get_device_tunnel_netcnf(device_ip, ssh_port, ssh_user, ssh_password)
        tunnel_id_c = map(lambda x: x["tunnelId"], tunnels)
        return map(lambda x: x['fragment-strategy'], filter(lambda x: x['number'] in tunnel_id_c, ret_tunnel))

    @staticmethod
    def set_es_ip_to_controller():
        UranusCli.set_es_server()

    @staticmethod
    def get_devices_status(device_id):
        res_code, body = OnosInterface.get_device_with_id(device_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body["available"]

    @staticmethod
    def check_devices_measure_result(ne_id, tunnel, timestamp, mi, mx, avg, sdev, loss):
        def not_bad(x):
            return all([float(mi[0]) <= x["min"] <= float(mi[1]), float(mx[0]) <= x["max"] <= float(mx[1]),
                        float(avg[0]) <= x["avg"] <= float(avg[1]), float(sdev[0]) <= x["sdev"] <= float(sdev[1]),
                        x["loss"] <= float(loss)])
        res_code, result = EsInterface.get_ne_tunnel_measure_result(ne_id, tunnel['local-ipv4-address'],
                                                                    tunnel['remote-ipv4-address'], timestamp * 1000 * 1000)
        assert res_code == 200, '{} is not 200'.format(res_code)
        assert result["hits"]["total"] > 0
        assert all(map(lambda x: not_bad(x["_source"]), result["hits"]["hits"]))

    @staticmethod
    def set_measure_polling_freq_to_controller(freq_time):
        UranusCli.set_controller_variable(UranusCli.pollFrequency, freq_time)

    @staticmethod
    def get_ne_tasks_from_controller(ne_id):
        res_code, body = UranusInterface.get_ne_tasks_from_controller(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body["content"]

    @staticmethod
    def get_ne_tasks_from_controller_with_dst_ne_id(ne_id, dst_ne_id):
        net_links = UranusKeyword.get_ne_tasks_from_controller(ne_id)
        return filter(lambda x: x["dstNeId"] == int(dst_ne_id), net_links)

    @staticmethod
    def get_ne_tunnels_from_controller(ne_id):
        res_code, body = UranusInterface.get_ne_tunnels_from_controller(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body

    @staticmethod
    def get_ne_tunnels_from_controller_with_dst_ne_id(ne_id, dst_ne_id):
        tunnels = UranusKeyword.get_ne_tunnels_from_controller(ne_id)
        return filter(lambda x: x["dstNEId"] == int(dst_ne_id), tunnels)

    @staticmethod
    def unregister_ne(ne_id):
        res_code = UranusInterface.unregister_ne(ne_id)
        assert res_code == 204, '{} is not 204'.format(res_code)

    @staticmethod
    def delete_proxy(service_id):
        res_code = UranusInterface.delete_services_proxy(service_id)
        assert res_code == 204, '{} is not 204'.format(res_code)

    @staticmethod
    def delete_anycast(service_id):
        res_code = UranusInterface.delete_services_anycast(service_id)
        assert res_code == 204, '{} is not 204'.format(res_code)

    @staticmethod
    def get_service_proxy(service_id):
        res_code, body = UranusInterface.get_service_proxy(service_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body

    @staticmethod
    def get_service_anycast(service_id):
        res_code, body = UranusInterface.get_service_anycast(service_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body

    @staticmethod
    def set_cr_area_select_delay(freq_time):
        UranusCli.set_controller_variable(UranusCli.area_selector_delay, freq_time)

    @staticmethod
    def set_net_measure_poll_delay(freq_time):
        UranusCli.set_controller_variable(UranusCli.netMeasurePollDelay, freq_time)

    @staticmethod
    def set_site_link_select_delay(freq_time):
        UranusCli.set_controller_variable(UranusCli.site_link_select_delay, freq_time)

    @staticmethod
    def create_nat_agent_pattern(pop_id, end_point, country, city, isp):
        body = \
            {
                "location": {"country": country, "province": city, "isp": isp},
                "services": [{
                    "neId": int(pop_id),
                    "serviceId": int(end_point)
                }]
            }
        res_code = UranusInterface.post_nat_agent_search_pattern(body)
        assert res_code == 201, '{} is not 201'.format(res_code)

    @staticmethod
    def delete_code_agent_pattern_by_service(pop_id, end_point):

        def delete_service(code_map, s):
            services = filter(lambda y: y != s, code_map["services"])
            code_map["services"] = services
            return code_map

        service = {"neId": int(pop_id), "serviceId": int(end_point)}
        cod, res = UranusInterface.get_code_agent_search_pattern()
        body = res["results"]
        new_body = map(lambda x: delete_service(x, service), body)
        res_code = UranusInterface.post_code_agent_search_pattern(new_body)
        assert res_code == 201, '{} is not 201'.format(res_code)

    @staticmethod
    def set_dns_nat_flow_spec(cpe_id):
        body = InterfacePathVariables.dns_nat_flow_spec
        body['neId'] = int(cpe_id)
        res_code, ret = OnosInterface.post_cpe_flow_spec([body])
        assert res_code == 200, '{} is not 200'.format(res_code)
        return ret[0]["flowId"]

    @staticmethod
    def set_pop_flow_spec(pop_id):
        body = InterfacePathVariables.pop_flow_spec
        body['neId'] = int(pop_id)
        res_code, ret = OnosInterface.post_cpe_flow_spec([body])
        assert res_code == 200, '{} is not 200'.format(res_code)
        return ret[0]["flowId"]

    @staticmethod
    def get_devices_measure_result(ne_id, timestamp):
        res_code, result = EsInterface.get_ne_all_measure_result(ne_id, timestamp * 1000 * 1000)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return result["hits"]

    @staticmethod
    def get_ne_cac_eac(ne_id):
        result = UranusInterface.get_ne_route_code(ne_id)
        return result

    @staticmethod
    def register_cpe_config_to_change_ip(ne_id, phy_port, ip_pre):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        port_list = body['config']['ports']

        def replace_prefix(port):
            if port['name'] == phy_port:
                port["addrs"][0]["ip"] = re.sub(r"^\d.", ip_pre, port["addrs"][0]["ip"])
            return port

        body['config']["ports"] = map(lambda x: replace_prefix(x), port_list)
        res_code = UranusInterface.cpe_reg_config(ne_id, body, InterfacePathVariables.FAKE_NE_TOKEN)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def register_cpe_config_to_change_wanType(ne_id, typeList, gw=False):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        port_list = body['config']['ports']

        def p_add_type_and_group(port_addr, type):
            port_addr['mode'] = type
            return port_addr

        def gw_add_type_and_group(port, type):
            port['addrs'][0]['mode'] = type
            return port

        if gw is False:
            body['config']["ports"][0]["addrs"] = map(lambda x, y: p_add_type_and_group(x, y), port_list[0]["addrs"], typeList)
        else:
            body['config']["ports"] = map(lambda x, y: gw_add_type_and_group(x, y), port_list, typeList)

        UranusKeyword.unregister_ne(ne_id)
        time.sleep(5)
        res_code = UranusInterface.cpe_reg_config(ne_id, body, InterfacePathVariables.FAKE_NE_TOKEN)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def register_cpe_config_to_change_4G_status(ne_id, status):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        port_list = body['config']['ports']

        def gw_change_4G_status(port):
            if port['addrs'][0]['mode'] == "MIA":
                port['isEnabled'] = status
            return port

        body['config']["ports"] = map(lambda x: gw_change_4G_status(x), port_list)

        res_code = UranusInterface.cpe_reg_config(ne_id, body, InterfacePathVariables.FAKE_NE_TOKEN)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def register_cpe_config_to_change_wanGroup(ne_id, groupList, gw=False):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        port_list = body['config']['ports']

        def p_add_type_and_group(port_addr, group):
            port_addr['groups'] = [group]
            return port_addr

        def gw_add_type_and_group(port, group):
            port['addrs'][0]['groups'] = [group]
            return port

        if gw is False:
            body['config']["ports"][0]["addrs"] = map(lambda x, y: p_add_type_and_group(x, y),
                                                      port_list[0]["addrs"], groupList)
        else:
            body['config']["ports"] = map(lambda x, y: gw_add_type_and_group(x, y), port_list,
                                          groupList)

        UranusKeyword.unregister_ne(ne_id)
        time.sleep(5)
        res_code = UranusInterface.cpe_reg_config(ne_id, body, InterfacePathVariables.FAKE_NE_TOKEN)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def register_pop_config_to_change_ip(ne_id, phy_port, ip_pre):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        port_list = body['config']['ports']

        def replace_prefix(port):
            if port['name'] == phy_port:
                port["addrs"][0]["ip"] = re.sub(r"^\d.", ip_pre, port["addrs"][0]["ip"])
            return port
        body['config']["ports"] = map(lambda x: replace_prefix(x), port_list)
        res_code = UranusInterface.pop_reg_config(ne_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def get_device_vport_from_ne(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/vports//*')
            return ret['aiwan-config:aiwan-switch']['resource']['vports']['vport']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_device_vpid2ip_from_ne(device_ip, ssh_port, ssh_user, ssh_password, interface, index=0):
        vports = UranusKeyword.get_device_vport_from_ne(device_ip, ssh_port, ssh_user, ssh_password)
        bin_vpid = bin(filter(lambda x: x['interface'] == interface, vports)[int(index)]['vpid'])
        return str(int(bin_vpid[2:10], 2)) + '.' + str(int(bin_vpid[10:18], 2)) + '.' + str(
            int(bin_vpid[18:26], 2)) + '.' + str(int(bin_vpid[26:34], 2))

    @staticmethod
    def get_device_port_from_ne(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/ports//*')
            return ret['aiwan-config:aiwan-switch']['resource']['ports']['port']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def delete_device_flow(body):
        res_code = OnosInterface.delete_cpe_flow_spe([body])
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def check_cpe_pass_through_flow(ne_id):
        expect_flows = FlowVariables.cpe_pass_through_flows
        flows = UranusKeyword.get_ne_route(ne_id)
        check_list = []
        for flow in expect_flows:
            flow['neId'] = int(ne_id)
            check_list.append(any(map(lambda x: are_same(flow, x, ["root['specId']", "root['priority']", "root['neId']"]), flows)))
        print check_list
        return all(check_list)

    @staticmethod
    def check_cpe_office_speed_up_flow(s_ne_id, d_ne_id, d_cac, d_eac, d_ip, header=0, tail=8):
        portNumber = UranusKeyword.get_e2e_dest_site_bond_portNumber(s_ne_id, d_ne_id)
        expect_flows = \
            [{u'matcher': {u'dstIp': u'{}/32'.format(d_ip), u'inPort': 1, u'ethType': 2048},
              u'actions': [{u"exLanMeta": -104, u"type": "PUSH_EX_LAN"}, {u"exLanId": 17, u"type": "SET_EX_LAN_ID"}, {u"outPort": portNumber, u"type": "EX_OUTPUT"}],
              u'priority': 500, u'tableId': 0, u'timeout': 0, "neId": int(s_ne_id)}]
        flows = UranusKeyword.get_ne_route(s_ne_id)
        check_list = []
        diff_ignore = ["root['specId']", "root['priority']"]
        print "expect_flow is ------{}".format(expect_flows)
        for flow in expect_flows:
            check_list.append(any(map(lambda x: are_same(flow, x, diff_ignore), flows)))
        print check_list
        return all(check_list)

    @staticmethod
    def check_not_series_cpe_office_speed_up_flow(s_ne_id, d_ne_id, d_cac, d_eac, d_net, header=0, tail=8, s_net=None):
        portNumber = UranusKeyword.get_e2e_dest_site_bond_portNumber(s_ne_id, d_ne_id)
        matcher = {u'dstIp': u'{}'.format(d_net), u'srcIp': u'{}'.format(s_net), u'inPort': 1, u'ethType': 2048} if s_net else {u'dstIp': u'{}'.format(d_net), u'inPort': 1, u'ethType': 2048}
        expect_flows = \
            [{u'matcher': matcher,
              u'actions': [{u"exLanMeta": -104, u"type": "PUSH_EX_LAN"}, {u"exLanId": 17, u"type": "SET_EX_LAN_ID"}, {u"outPort": portNumber, u"type": "EX_OUTPUT"}],
              u'priority': 500, u'tableId': 0, u'timeout': 0, "neId": int(s_ne_id)}]
        flows = UranusKeyword.get_ne_route(s_ne_id)
        check_list = []
        diff_ignore = ["root['specId']", "root['priority']"]
        for flow in expect_flows:
            check_list.append(any(map(lambda x: are_same(flow, x, diff_ignore), flows)))
        print check_list
        return all(check_list)

    @staticmethod
    def check_pop_2_cpe_flows(s_ne_id, d_ne_id, d_cac, d_eac, tunnel_id):
        expect_flows = FlowVariables.pop_to_cpe_flows
        expect_flows['neId'] = int(s_ne_id)
        expect_flows['actions'][0]['outPort'] = int(tunnel_id)
        expect_flows['matcher']['dcac'] = int(d_cac)
        expect_flows['matcher']['deac'] = int(d_eac)
        flows = UranusKeyword.get_ne_route(s_ne_id)
        print expect_flows
        return any(map(lambda x: are_same(expect_flows, x, ["root['specId']", "root['priority']", "root['matcher']"]), flows))

    @staticmethod
    def check_pop_2_cpe_next_pop_flows(s_ne_id, d_cac, d_eac, tunnel_id):
        expect_flows = FlowVariables.pop_to_pop_flows
        expect_flows['neId'] = int(s_ne_id)
        expect_flows['actions'][0]['outPort'] = int(tunnel_id)
        expect_flows['matcher']['dcac'] = int(d_cac)
        expect_flows['matcher']['deac'] = int(d_eac)
        flows = UranusKeyword.get_ne_route(s_ne_id)
        print expect_flows
        return any(map(lambda x: are_same(expect_flows, x, ["root['specId']", "root['priority']"]), flows))

    @staticmethod
    def check_pop_2_cpe_next_pop_flows_with_tunnel_list(s_ne_id, d_cac, d_eac, tunnel_list):
        return all(map(lambda tunnel: UranusKeyword.check_pop_2_cpe_next_pop_flows(s_ne_id, d_cac, d_eac, tunnel), tunnel_list))

    @staticmethod
    def get_flow_id_from_tunnel(s_ne_id, d_ne_id):
        tunnels = UranusKeyword.get_ne_tunnels_from_controller(s_ne_id)
        des_tunnels = filter(lambda x: x['dstNEId'] == int(d_ne_id), tunnels)
        return des_tunnels[0]['tunnelId'] if des_tunnels else None

    @staticmethod
    def change_ne_ip(old_ip, new_ip, tunnels):
        ret_tunnels = copy.deepcopy(tunnels)
        for tunnel in ret_tunnels:
            tunnel['peer'] = map(lambda x: [new_ip, x[1]] if x[0] == old_ip else [x[0], new_ip], tunnel['peer'])
        return ret_tunnels

    @staticmethod
    def delete_ne_tunnel(ne_id, tunnel_id):
        res_code = UranusInterface.delete_ne_tunnel(ne_id, tunnel_id)
        assert res_code == 204, '{} is not 204'.format(res_code)

    @staticmethod
    def get_device_flow_packets_by_flow_id(device_id, flow_id):
        hex_id = format(int(device_id), '04x')
        of_device_id = 'of:000000000000{}'.format(hex_id)
        ret_code, body = OnosInterface.get_device_flow_by_flow_id(of_device_id, flow_id)
        assert ret_code == 200, '{} is not 200'.format(ret_code)
        return body["flows"][0]['packets']

    @staticmethod
    def set_flow_poll_frequency(freq_time):
        UranusCli.set_controller_variable(UranusCli.flow_poll_frequency, freq_time)

    @staticmethod
    def get_device_net_measure_config(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/net-measure-tasks//*')
            return ret['aiwan-config:aiwan-switch']['resource']['net-measure-tasks']['task']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_device_of_controller_info(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/controllers//*')
            return ret['aiwan-config:aiwan-switch']['resource']['controllers']['controller']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_running_measure_config():
        res_code, body = UranusInterface.get_measure_config()
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body

    @staticmethod
    def get_pop_saas(ne_id, end_point):
        res_code, body = UranusInterface.get_pop_saas_config(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return filter(lambda x: x['serviceId'] == int(end_point), body)

    @staticmethod
    def delete_nat_agent_search_pattern(country, city, isp):
        res_code = UranusInterface.delete_nat_agent_search_pattern(country, city, isp)
        assert res_code == 204, '{} is not 204'.format(res_code)

    @staticmethod
    def delete_all_nat_agent_search_pattern():
        res_code, body = UranusInterface.get_nat_agent_search_pattern()
        assert res_code == 200, '{} is not 200'.format(res_code)
        map(lambda x: UranusKeyword.delete_nat_agent_search_pattern(x["location"]["country"],
                                                                    x["location"]["city"],
                                                                    x["location"]["isp"]), body["results"]) \
            if body["results"] else None

    @staticmethod
    def check_cpe_to_pop_flow(ne_id, tunnel):
        expect_flows = FlowVariables.cpe_to_pop_flows
        flows = UranusInterface.get_ne_route(ne_id)
        check_list = []
        for flow in expect_flows:
            flow['neId'] = int(ne_id)
            flow['actions'][0]['outPort'] = int(tunnel)
            check_list.append(any(map(lambda x: are_same(flow, x, ["root['specId']", "root['priority']"]), flows)))
        print check_list
        return all(check_list)

    @staticmethod
    def check_cpe_internet_table_2_flows(ne_id, dest_code, pri_range=range(496, 501)):
        flows = UranusKeyword.get_cpe_internet_table_2_code_flows(ne_id, dest_code, pri_range)
        return True if flows else False

    @staticmethod
    def get_cpe_internet_table_2_flows_bond_id(ne_id, dest_code, pri_range=range(496, 501)):
        flows = UranusKeyword.get_cpe_internet_table_2_code_flows(ne_id, dest_code, pri_range)
        return map(lambda x: x['extension']['Port'], flows[0]['treatment']['instructions'][2:]) if flows else []

    @staticmethod
    def get_cpe_internet_table_2_spi_flows_bond_id(ne_id, dest_spi, pri_range=range(700, 701)):
        flows = UranusKeyword.get_cpe_internet_table_2_spi_flows(ne_id, dest_spi, pri_range)
        return map(lambda x: x['extension']['Port'], flows[0]['treatment']['instructions'][2:]) if flows else []

    @staticmethod
    def get_cpe_internet_table_2_flows_packets(ne_id, dest_code, pri_range=range(496, 501)):
        flows = UranusKeyword.get_cpe_internet_table_2_code_flows(ne_id, dest_code, pri_range)
        return flows[0]['packets'] if flows else 0

    @staticmethod
    def get_cpe_internet_table_2_code_flows(ne_id, dest_code, pri_range=range(496, 501)):
        device_id = UranusKeyword.get_openflow_dev_id_from_ne_id(ne_id)
        res_code, body = OnosInterface.get_device_flow(device_id)
        assert res_code == 200, '{} is no 200'.format(res_code)
        table0_500_flows = filter(lambda x: str(x["tableId"]) == '2' and x["priority"] in pri_range, body["flows"])
        print table0_500_flows
        selector_info_list = UranusCli.get_device_flows_selector_info(device_id,
                                                                      map(lambda x: format(int(x["id"]), 'x'),
                                                                          table0_500_flows))
        print selector_info_list
        flows = [table0_500_flows[i] for i in range(len(selector_info_list))
                 if '{pktType=0x%08x}' % int(dest_code) in selector_info_list[i]]
        print flows
        return flows

    @staticmethod
    def get_cpe_internet_table_2_spi_flows(ne_id, dest_spi, pri_range=range(700, 701)):
        device_id = UranusKeyword.get_openflow_dev_id_from_ne_id(ne_id)
        res_code, body = OnosInterface.get_device_flow(device_id)
        assert res_code == 200, '{} is no 200'.format(res_code)
        table0_500_flows = filter(lambda x: str(x["tableId"]) == '2' and x["priority"] in pri_range, body["flows"])
        print table0_500_flows
        selector_info_list = UranusCli.get_device_flows_selector_info(device_id,
                                                                      map(lambda x: format(int(x["id"]), 'x'),
                                                                          table0_500_flows))
        print selector_info_list
        flows = [table0_500_flows[i] for i in range(len(selector_info_list))
                 if '{spiTag=0x%08x}' % int(dest_spi) in selector_info_list[i]]
        print flows
        return flows

    @staticmethod
    def check_cpe_internet_table_0_ip_flows(ne_id, dest_ip):
        device_id = UranusKeyword.get_openflow_dev_id_from_ne_id(ne_id)
        res_code, body = OnosInterface.get_device_flow(device_id)
        assert res_code == 200, '{} is no 200'.format(res_code)
        table0_flows = filter(lambda x: x["tableId"] == 0 and x["priority"] > 10, body["flows"])
        select_filter = copy.deepcopy(InterfacePathVariables.selector_filter[1])
        select_filter.append({"type": "IP_PROTO", "protocol": 17})
        select_filter.append({"type": "IPV4_DST",
                              "ip": "{}/32".format(dest_ip)})
        print select_filter
        flows = filter(lambda x: x["selector"]["criteria"] == select_filter, table0_flows)
        selector_info_list = UranusCli.get_device_flows_selector_info(device_id,
                                                                      map(lambda x: format(int(x["id"]), 'x'), flows))
        print selector_info_list
        return True if filter(lambda x: x["selector"]["criteria"] == select_filter, table0_flows) else False

    @staticmethod
    def get_nat_agent_config_from_pop(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/nat-agent-config//*')
            return ret['aiwan-config:aiwan-switch']['resource']['nat-agent-config']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def del_nat_agent_config(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_del_config(device_ip, ssh_user, ssh_password, ssh_port, 'domain-nat-patterns')
            return ret
        except (IndexError, KeyError, TypeError):
            return 'Error'

    @staticmethod
    def get_domain_nat_patterns_from_cpe(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/domain-nat-patterns//*')
            return ret['aiwan-config:aiwan-switch']['resource']['domain-nat-patterns']['domain-nat-pattern']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_spi_dispatch_from_cpe(device_ip, ssh_port, ssh_user, ssh_password, tag_id):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/spi-dispatches//*')
            return filter(lambda x: int(x['tag']) == int(tag_id), ret['aiwan-config:aiwan-switch']['resource']['spi-dispatches']['spi-dispatch'])[0]['action']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_spi_rule_from_cpe(device_ip, ssh_port, ssh_user, ssh_password, tag_id):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/spi-rules//*')
            return filter(lambda x: int(x['tag']) == int(tag_id), ret['aiwan-config:aiwan-switch']['resource']['spi-rules']['spi-rule'])
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_spi_nat_patterns_from_cpe(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/spi-rules//*')
            return ret['aiwan-config:aiwan-switch']['resource']['spi-rules']['spi-rule']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_device_fw_flow_packets(ne_id, type):
        device_id = UranusKeyword.get_openflow_dev_id_from_ne_id(ne_id)
        res_code, body = OnosInterface.get_device_flow(device_id)
        fw = filter(lambda flow: filter(lambda c: 'type' in c and type in c['type'], flow['selector']['criteria']),
                    body["flows"])
        return fw[0]['id'], fw[0]['packets']

    @staticmethod
    def get_device_fw_flow_num(device_id, type):
        res_code, body = OnosInterface.get_device_flow(device_id)
        fw = filter(lambda flow: filter(lambda c: 'type' in c and type in c['type'], flow['selector']['criteria']),
                    body["flows"])
        return str(len(fw))

    @staticmethod
    def cpe_selected_right_cac_eac(cpe_id, cac, eac, iface=None, index=None):
        cac_eacs = UranusKeyword.get_cpe_home_code(cpe_id)
        cac_eac_list = filter(lambda x: x["iface"] == iface and x["index"] == int(index), cac_eacs) if iface else cac_eacs
        return all(map(lambda cac_eac: cac_eac["cac"] == int(cac) and cac_eac["eac"] == int(eac), cac_eac_list)) if cac_eac_list else False

    @staticmethod
    def register_pop_config_to_change_group(ne_id, phy_port_list, group_list):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        port_list = body['config']['ports']

        def replace_group(port, phy_port, group_name):
            if port['name'] == phy_port:
                port["addrs"][0]["groups"] = group_name
            return port

        body['config']["ports"] = map(lambda x, y, z: replace_group(x, y, z), port_list, phy_port_list, group_list)
        res_code = UranusInterface.pop_reg_config(ne_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def unregister_and_register_cpe_config(ne_id):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        UranusKeyword.unregister_ne(ne_id)
        time.sleep(5)
        res_code = UranusInterface.cpe_reg_config(ne_id, body, InterfacePathVariables.FAKE_NE_TOKEN)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def unregister_and_register_pop_config(ne_id):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        UranusKeyword.unregister_ne(ne_id)
        res_code = UranusInterface.pop_reg_config(ne_id, body)
        assert res_code == 201, '{} is not 201'.format(res_code)

    @staticmethod
    def get_ip_from_cnf_by_id(chassis_id):
        return UranusKeyword.get_ip_from_cnf_by_id_port(chassis_id, 'enp1s0f0')

    @staticmethod
    def get_ip_from_cnf_by_id_port(chassis_id, port):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(chassis_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        ports = body["config"]["ports"]
        match_port = filter(lambda x: x["name"] == port, ports)[0]
        return match_port["addrs"][0]["ip"] if (match_port['proxy'] is False) else '169.254.1.2'

    @staticmethod
    def get_cpe_table0_dest_dev_flow_packets(ne_id, dest_dev, dest_dev_port, private_ip=None, nat_ip=None):
        device_id = UranusKeyword.get_openflow_dev_id_from_ne_id(ne_id)
        res_code, body = OnosInterface.get_device_flow(device_id)
        assert res_code == 200, '{} is no 200'.format(res_code)
        table0_flows = filter(lambda x: x["tableId"] == 0 and x["priority"] > 10, body["flows"])
        select_filter = copy.deepcopy(InterfacePathVariables.selector_filter[int(dest_dev_port)])
        if int(dest_dev_port) == 1:
            select_filter.append({"type": "IPV4_DST",
                                  "ip": "{}/32".format(nat_ip if nat_ip else UranusKeyword.get_ip_from_cnf_by_id(dest_dev))})
        if int(dest_dev_port) == 2:
            select_filter.append({"type": "IPV4_DST",
                                  "ip": "{}".format(private_ip)})
        print table0_flows
        print select_filter
        flows = filter(lambda x: x["selector"]["criteria"] == select_filter, table0_flows)
        return filter(lambda x: x["selector"]["criteria"] == select_filter, table0_flows)[0]['packets']

    @staticmethod
    def get_cpe_table0_dest_ip_flows(device_id, dest_dev, dest_ip=None):
        dst_ip = dest_ip if dest_ip else '{}/32'.format(UranusKeyword.get_ip_from_cnf_by_id(dest_dev))
        return UranusKeyword.get_cpe_table0_flows_with_ip_port(device_id, dst_ip, 1)

    @staticmethod
    def get_cpe_table0_private_ip_flows(device_id, company_id, site_id):
        body = GaeaKeyword.get_company_sites_with_id(company_id, site_id)
        dst_ip = body['config']["privateAddrs"] if body['config']['privateAddrs'] else None
        flows = map(lambda x: UranusKeyword.get_cpe_table0_flows_with_ip_port(device_id, '{}'.format(x), 2), dst_ip) if dst_ip else None
        return reduce(lambda z, y: z + y, flows) if flows else []

    @staticmethod
    def get_cpe_table0_flows_with_ip_port(ne_id, dest_ip, port):
        device_id = UranusKeyword.get_openflow_dev_id_from_ne_id(ne_id)
        res_code, body = OnosInterface.get_device_flow(device_id)
        assert res_code == 200, '{} is no 200'.format(res_code)
        table0_flows = filter(lambda x: str(x["tableId"]) == '0' and x["priority"] > 10, body["flows"])
        dst = {'ip': '{}'.format(dest_ip), 'type': 'IPV4_DST'}
        dst_p = {u'type': u'IN_PORT', u'port': port}
        print dst
        print dst_p
        print table0_flows
        return filter(lambda x: (dst in x["selector"]["criteria"]) and (dst_p in x["selector"]["criteria"]), table0_flows)

    @staticmethod
    def put_company_unions_route_strategy_value(company_id, union_name, perfer):
        body = UranusKeyword.get_company_unions(company_id, union_name)
        body["routeStrategy"] = perfer
        res_code = UranusInterface.put_company_unions(company_id, union_name, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def delete_company_all_unions(company_id):
        res_code, rsp = UranusInterface.get_company_unions(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        map(lambda x: UranusKeyword.delete_company_unions(company_id, x["name"]), rsp["results"])

    @staticmethod
    def get_dst_ne_tunnel_ids(s_ne_id, d_ne_id):
        tunnels = UranusKeyword.get_ne_tunnels_from_controller(s_ne_id)
        des_tunnels = filter(lambda x: x['dstNEId'] == int(d_ne_id), tunnels)
        return map(lambda x: x['tunnelId'], des_tunnels) if des_tunnels else None

    @staticmethod
    def get_dst_ne_tunnel_info_with_sip(s_ne_id, d_ne_id, sip):
        tunnels = UranusKeyword.get_ne_tunnels_from_controller(s_ne_id)
        des_tunnels = filter(lambda x: (x['dstNEId'] == int(d_ne_id)) and (x['srcIp'] == sip), tunnels)
        return (len(des_tunnels), des_tunnels[0]['tunnelId']) if des_tunnels else (0, None)

    @staticmethod
    def get_dst_ne_tunnel_info_with_dip(s_ne_id, d_ne_id, dip):
        tunnels = UranusKeyword.get_ne_tunnels_from_controller(s_ne_id)
        des_tunnels = filter(lambda x: (x['dstNEId'] == int(d_ne_id)) and (x['dstIp'] == dip), tunnels)
        return (len(des_tunnels), des_tunnels[0]['tunnelId'], des_tunnels[0]["quality"]['weight']) if des_tunnels else (0, None, None)

    @staticmethod
    def get_dst_ne_tunnel_info_with_sip_dip(s_ne_id, d_ne_id, sip, dip):
        tunnels = UranusKeyword.get_ne_tunnels_from_controller(s_ne_id)
        des_tunnels = filter(lambda x: (x['dstNEId'] == int(d_ne_id)) and (x['dstIp'] == dip) and (x['srcIp'] == sip), tunnels)
        return des_tunnels[0]['tunnelId'] if des_tunnels else (0, None, None)

    @staticmethod
    def get_pop_table_1_device_tunnel_packets(ne_id, tunnel_id):
        device_id = UranusKeyword.get_openflow_dev_id_from_ne_id(ne_id)
        res_code, body = OnosInterface.get_device_flow(device_id)
        assert res_code == 200, '{} is no 200'.format(res_code)
        flow = filter(lambda x: x['tableId'] == 1 and x['treatment']["instructions"] == [{"type": "OUTPUT", "port": str(tunnel_id)}], body["flows"])
        return flow[0]['packets'], flow[0]['priority']

    @staticmethod
    def get_site_tunnels_from_controller_for_destip(ne_id, peer_ip_pattern):
        body = UranusKeyword.get_ne_tunnels_from_controller(ne_id)
        return filter(lambda c: peer_ip_pattern in c['dstIp'], body)

    @staticmethod
    def get_cpe_end2end_measure_tasks(cpe_ip, peer_ip_pattern, ssh_port, ssh_user, ssh_password):
        try:
            tasks = NeCli.netconf_get_config(cpe_ip, ssh_user, ssh_password, ssh_port,
                                             '/aiwan-config:aiwan-switch/resource/net-measure-tasks//*')
            return filter(lambda c: peer_ip_pattern in c['remote-ipv4-address'], tasks['aiwan-config:aiwan-switch']['resource']['net-measure-tasks']['task'])
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_cpe_end2end_links(cpe_ip, remote_id, ssh_port, ssh_user, ssh_password):
        try:
            tasks = NeCli.netconf_get_config(cpe_ip, ssh_user, ssh_password, ssh_port,
                                             '/aiwan-config:aiwan-switch/resource/links//*')
            return filter(lambda c: int(remote_id) == int(c['remote-id']), tasks['aiwan-config:aiwan-switch']['resource']['links']['link'])
        except (IndexError, KeyError, TypeError):
            return []

    @staticmethod
    def get_cpe_end2end_bond(cpe_ip, remote_id, ssh_port, ssh_user, ssh_password):
        try:
            tasks = NeCli.netconf_get_config(cpe_ip, ssh_user, ssh_password, ssh_port,
                                             '/aiwan-config:aiwan-switch/resource/bonds//*')
            return filter(lambda c: int(remote_id) == int(c['remote-id']), tasks['aiwan-config:aiwan-switch']['resource']['bonds']['bond'])
        except (IndexError, KeyError, TypeError):
            return []

    @staticmethod
    def get_wan_if_name_from_reg_conf(ne_id):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return map(lambda y: y["name"], filter(lambda x: x["type"] == 'WAN' and x["mode"] != 'DIA', body['config']["ports"]))

    @staticmethod
    def get_wan_if_status_from_reg_conf_by_name(ne_id, wan_name):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return map(lambda y: y["isEnabled"], filter(lambda x: x["type"] == 'WAN' and x['name'] == wan_name, body['config']["ports"]))

    @staticmethod
    def get_vport_if_type_from_reg_conf_by_number(ne_id, vport_number):
        res_code, body = UranusInterface.get_cpe_vports(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return filter(lambda x: x["type"] == 'WAN' and x['vId'] == vport_number, body["ports"])[0]["mode"]

    @staticmethod
    def get_lan_if_num_from_reg_conf(ne_id):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return len(filter(lambda x: x["type"] == 'LAN', body['config']["ports"]))

    @staticmethod
    def get_cpe_home_code(cpe_id):
        return UranusInterface.get_cpe_wan_home_code(cpe_id)

    @staticmethod
    def get_cpe_end2end_measure_tunnels(cpe_ip, peer_ip_pattern, ssh_port, ssh_user, ssh_password):
        try:
            tunnels = NeCli.netconf_get_config(cpe_ip, ssh_user, ssh_password, ssh_port,
                                               '/aiwan-config:aiwan-switch/resource/tunnels//*')
            return filter(lambda c: peer_ip_pattern in c['remote-ipv4-address'], tunnels['aiwan-config:aiwan-switch']['resource']['tunnels']['tunnel'])
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_device_end2end_flow(ne_id, tunnel_id):
        device_id = UranusKeyword.get_openflow_dev_id_from_ne_id(ne_id)
        res_code, body = OnosInterface.get_device_flow(device_id)
        res = filter(
            lambda flow: filter(lambda c: 'port' in c and str(tunnel_id) in c['port'], flow['treatment']['instructions']),
            body["flows"])
        return len(res)

    @staticmethod
    def get_cpe_table1_des_link_des_dev_packets(ne_id, link_id, dest_dev):
        device_id = UranusKeyword.get_openflow_dev_id_from_ne_id(ne_id)
        res_code, body = OnosInterface.get_device_flow(device_id)
        assert res_code == 200, '{} is no 200'.format(res_code)
        flow = filter(lambda x: x['tableId'] == '1' and x['treatment']["instructions"] == [{"type": "OUTPUT", "port": str(link_id)}], body["flows"])
        selector_info_list = UranusCli.get_device_flows_selector_info(device_id,
                                                                      map(lambda x: format(int(x["id"]), 'x'), flow))
        flows = [flow[i] for i in range(len(selector_info_list))
                 if '{routeId=AiwanRouteId{id=%s}' % (int(dest_dev) * 64)
                 in selector_info_list[i]]
        return flows[0]['packets']

    @staticmethod
    def get_cpe_home_code_prefer(cpe_id, wan_if, index):
        wan_home_code_list = UranusInterface.get_cpe_wan_home_code_prefer(cpe_id)
        return filter(lambda y: y['iface'] == wan_if and y['index'] == index, wan_home_code_list["homeCodes"])[0]

    @staticmethod
    def get_ne_status(ne_id):
        ne_status = UranusInterface.get_cpe_status(ne_id)
        return ne_status["status"]

    @staticmethod
    def forbid_put_ne_status_maintain(ne_id):
        body = {"neId": ne_id,
                "status": "MAINTENANCE"}
        res_code, res_body = UranusInterface.put_ne_status(ne_id, body)
        assert res_code == 403, '{} is not 403'.format(res_code)
        res_bodyJson = load_json(res_body)
        return res_bodyJson["homeCodes"]

    @staticmethod
    def get_low_weight_tunnels(tunnel_list):
        tunnels_no_e2e_no_services = filter(lambda x: not ((x["dstNEId"] % 16 == 7) or (x["dstNEId"] % 16 == 8) or (x['dstPort'] == 6868 and x['srcPort'] == 6868)), tunnel_list)
        sort_t = sorted(tunnels_no_e2e_no_services, key=lambda x: x['dstNEId'])
        tunnel_group = groupby(sort_t, key=lambda x: x['dstNEId'])
        return map(lambda x: min(list(x[1]), key=lambda y: y['quality']['weight']), tunnel_group)

    @staticmethod
    def get_x_low_weight_tunnels(s_ne_id, d_ne_id, low_num):
        tunnels = UranusKeyword.get_ne_tunnels_from_controller(s_ne_id)
        des_tunnels = filter(lambda x: x['dstNEId'] == int(d_ne_id), tunnels)
        sort_t = sorted(des_tunnels, key=lambda x: x['quality']['weight'])
        return sort_t[:int(low_num)]

    @staticmethod
    def all_tunnels_have_quality(ne_id):
        tunnels = UranusKeyword.get_ne_tunnels_from_controller(ne_id)
        tunnels_no_e2e_no_services = filter(lambda x: not ((x["dstNEId"] % 16 == 7) or (x["dstNEId"] % 16 == 8) or (x['dstPort'][0] == 6868 and x['srcPort'][0] == 6868)), tunnels)
        return all(map(lambda x: 'quality' in x.keys(), tunnels_no_e2e_no_services))

    @staticmethod
    def get_ne_route(ne_id):
        route_info = UranusInterface.get_ne_route(ne_id)
        return route_info

    @staticmethod
    def check_pop_2_pop_next_pop_routes(s_ne_id, d_cac, d_eac, tunnel_id):
        expect_flows = FlowVariables.pop_to_pop_flows
        expect_flows['neId'] = int(s_ne_id)
        expect_flows['actions'][0]['outPort'] = int(tunnel_id)
        expect_flows['matcher']['dcac'] = int(d_cac)
        expect_flows['matcher']['deac'] = int(d_eac)
        flows = UranusKeyword.get_ne_route(s_ne_id)
        return any(map(lambda x: are_same(expect_flows, x, ["root['specId']", "root['priority']"]), flows))

    @staticmethod
    def check_pop_2_service_next_service_routes(s_ne_id, d_cac, d_eac, tunnel_id):
        expect_flows = FlowVariables.pop_to_pop_flows
        expect_flows['neId'] = int(s_ne_id)
        expect_flows['actions'][0]['outPort'] = int(tunnel_id)
        expect_flows['matcher']['dcac'] = int(d_cac)
        expect_flows['matcher']['deac'] = int(d_eac)
        flows = UranusKeyword.get_ne_route(s_ne_id)
        return any(map(lambda x: are_same(expect_flows, x, ["root['specId']", "root['priority']", "root['matcher']"]), flows))

    @staticmethod
    def check_pop_route_debar_maintain_pop(s_ne_id, m_ne_id):
        routes = UranusKeyword.get_ne_route(s_ne_id)
        route_code = UranusKeyword.get_ne_cac_eac(m_ne_id)
        len(filter(lambda x: (x['matcher']['dcac'] == route_code["routeCode"]['cac']) and (x['matcher']['deac'] == route_code["routeCode"]['eac']), routes))

    @staticmethod
    def get_cpe_address_group(ne_id, iface, index):
        ne_vport = UranusInterface.get_ne_vport(ne_id)
        return filter(lambda x: x["portId"]["iface"] == str(iface) and x["portId"]["index"] == int(index), ne_vport["ports"])[0]["addr"]["groups"]

    @staticmethod
    def in_bodys(bodys, ip, port):
        if bodys == "":
            return False
        tmp = filter(lambda body: True if (body["ip"] == ip and body["port"] == port) else False, bodys)
        return any(tmp)

    @staticmethod
    def check_ip_port_in_managers(ip_list, port_list):
        res_code, managers = UranusInterface.get_cpe_managers()
        assert res_code == 200, '{} is not 200'.format(res_code)
        results = map(lambda ip, port: UranusKeyword.in_bodys(managers["results"], ip, port), ip_list, port_list)
        return all(results)

    @staticmethod
    def check_ip_port_in_managers_specific(neid, ip_list, port_list):
        res_code, managers_specific = UranusInterface.get_cpe_managers_specific()
        assert res_code == 200, '{} is not 200'.format(res_code)
        if str(neid) in managers_specific["managers"].keys():
            results = map(lambda ip, port: UranusKeyword.in_bodys(managers_specific["managers"][str(neid)], ip, port), ip_list, port_list)
            return all(results)
        return False

    @staticmethod
    def check_ip_port_in_controllers(ip_list, port_list):
        res_code, controllers = UranusInterface.get_controller_config()
        assert res_code == 200, '{} is not 200'.format(res_code)
        results = map(lambda ip, port: UranusKeyword.in_bodys(controllers["results"], ip, port), ip_list, port_list)
        return all(results)

    @staticmethod
    def check_ip_port_in_controllers_specific(neid, ip_list, port_list):
        res_code, controllers_specific = UranusInterface.get_controller_config_specific()
        assert res_code == 200, '{} is not 200'.format(res_code)
        if str(neid) in controllers_specific["controllers"].keys():
            results = map(lambda ip, port: UranusKeyword.in_bodys(controllers_specific["controllers"][str(neid)], ip, port), ip_list, port_list)
            return all(results)
        return False

    @staticmethod
    def check_netConfig_with_value(neid, mtu, keepAlive, strategy):
        res_code, body = UranusInterface.get_device_tunnel_config(int(neid))
        assert res_code == 200, '{} is not 200'.format(res_code)
        return True if (body["netConfig"]['mtu'] == int(mtu) and body["netConfig"]['keepAlive'] == int(keepAlive) and body["netConfig"]['strategy'] == int(strategy)) else False

    @staticmethod
    def get_cpe_managers_startup(device_ip, ssh_port, ssh_user, ssh_password):
        try:
            ret = NeCli.netconf_get_config(device_ip, ssh_user, ssh_password, ssh_port,
                                           '/aiwan-config:aiwan-switch/resource/managers//*  --datastore=startup')
            return ret['aiwan-config:aiwan-switch']['resource']['managers']['manager']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_cpe_wan_bandwidth(ne_id, iface, index_v):
        res_code, body = UranusInterface.get_cpe_wan_bandwidth(ne_id, iface)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body[int(index_v)]['rateLimit']

    @staticmethod
    def check_cpe_wan_bandwidth(ne_id, iface_name, index_v, bandwidth, burst, latency, ratio):
        body = UranusKeyword.get_cpe_wan_bandwidth(int(ne_id), iface_name, int(index_v))
        return True if(body["bandwidth"] == int(bandwidth) and body["burst"] == int(burst) and body["latency"] == int(latency) and body["ratio"] == int(ratio)) else False

    @staticmethod
    def get_fw_group(company_id):
        res_code, rsp = UranusInterface.get_template_fw_groups(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return map(lambda x: x['id'], rsp['results'])

    @staticmethod
    def check_fwRule_in_fwTemp(company_id, fwRuleId, fwTempId):
        res_code, rsp = UranusInterface.get_template_fw_groups(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        rules = map(lambda x: x[9:][:-1], filter(lambda x: x['id'] == fwTempId, rsp['results'])[0]["rules"])
        print rules
        return True if fwRuleId in rules else False

    @staticmethod
    def check_saasRule_in_saasTemp(saasRuleId, saasTempId):
        res_code, rsp = UranusInterface.get_template_nat_groups()
        assert res_code == 200, '{} is not 200'.format(res_code)
        rules = map(lambda x: x[11:][:-1], filter(lambda x: x['id'] == saasTempId, rsp['results'])[0]["rules"])
        print rules
        return True if saasRuleId in rules else False

    @staticmethod
    def check_spiRule_in_saasTemp(spiRuleId, spiTempId):
        res_code, rsp = UranusInterface.get_template_spi_groups()
        assert res_code == 200, '{} is not 200'.format(res_code)
        rules = map(lambda x: x[11:][:-1], filter(lambda x: x['id'] == spiTempId, rsp['results'])[0]["rules"])
        print rules
        return True if spiRuleId in rules else False

    @staticmethod
    def check_None_saasTemp():
        res_code, rsp = UranusInterface.get_template_nat_groups()
        assert res_code == 200, '{} is not 200'.format(res_code)
        assert rsp['results'] == []

    @staticmethod
    def check_None_spiTemp_in_company(company_id):
        res_code, rsp = UranusInterface.get_template_spi_groups()
        assert res_code == 200, '{} is not 200'.format(res_code)
        assert rsp['results'] == []

    @staticmethod
    def check_None_saasRules():
        res_code, rsp = UranusInterface.get_template_nat_rules()
        assert res_code == 200, '{} is not 200'.format(res_code)
        assert rsp['results'] == []

    @staticmethod
    def check_None_spiRules_in_company(company_id):
        res_code, rsp = UranusInterface.get_template_spi_rules()
        assert res_code == 200, '{} is not 200'.format(res_code)
        assert rsp['results'] == []

    @staticmethod
    def check_fwRule(company_id, fwRule_id, rule_name, priority, protocol, srcIP, dstIP, srcPort=0, dstPort=0, icmpType=0, icmpCode=0):
        body = \
            {
                u'name': u'{}'.format(rule_name),
                u'priority': priority,
                u'protocol': protocol,
                u'srcIp': u'{}'.format(srcIP),
                u'srcPort': srcPort,
                u'dstIp': u'{}'.format(dstIP),
                u'dstPort': dstPort,
                u'icmpType': icmpType,
                u'icmpCode': icmpCode}
        res_code, rsp = UranusInterface.get_template_fw_rules(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        rule = filter(lambda x: x['id'] == fwRule_id, rsp['results'])[0]
        return are_same(body, rule, ["root['companyId']", "root['id']"])

    @staticmethod
    def check_saasRule(saasRule_id, domain_name, ttl, priority, name='default', agent=None, nat_type="DOMAIN"):
        body = \
            {
                u'saasType': u'{}'.format(nat_type),
                u'pattern': u'{}'.format(domain_name),
                u'ttl': int(ttl),
                u'priority': int(priority),
                u'name': u'{}'.format(name),
                u'agent': u'{}'.format(agent) if agent else u''
            }
        res_code, rsp = UranusInterface.get_template_nat_rules()
        assert res_code == 200, '{} is not 200'.format(res_code)
        rule = filter(lambda x: x['id'] == saasRule_id, rsp['results'])[0]
        return are_same(body, rule, ["root['companyId']", "root['id']"])

    @staticmethod
    def check_spiRule(spiRule_id, priority, tag, srcCIDR, dstCIDR, l4proto, srcPort, dstPort, dstDomain, srcMac=None, dstMac=None, vlanPri=None, vlanTag=None, diffServ=None, ifname=None, ifindex=None):
        body = {
            "spi": {
                "vport": {"iface": ifname, "index": ifindex} if ifname and ifindex else None,
                'srcMac': srcMac, 'dstMac': dstMac, 'vlanPri': vlanPri, 'vlanTag': vlanTag, 'diffServ': diffServ,
                'srcCIDR': srcCIDR, 'dstCIDR': dstCIDR, 'l4proto': l4proto,
                'srcPort': srcPort, 'dstPort': dstPort, 'dstDomain': dstDomain, 'dstPort': dstPort},
            "priority": priority, "tag": tag}
        res_code, rsp = UranusInterface.get_template_spi_rules()
        assert res_code == 200, '{} is not 200'.format(res_code)
        rule = filter(lambda x: x['id'] == spiRule_id, rsp['results'])[0]
        return are_same(body, rule, ["root['companyId']", "root['id']"])

    @staticmethod
    def delete_fw_rule(rule_id):
        res_code = UranusInterface.delete_template_fw_rule(rule_id)
        assert res_code == 204, '{} is not 204'.format(res_code)

    @staticmethod
    def get_fw_rules(company_id):
        res_code, rsp = UranusInterface.get_template_fw_rules(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return map(lambda x: x['id'], rsp['results'])

    @staticmethod
    def get_ne_measure_algo(ne_id):
        res_code, rsp = UranusInterface.get_ne_measure_algo(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return rsp["algo"]

    @staticmethod
    def check_ne_measure_algo(ne_id, delay=None, loss=None, stdev=None, m0=None, m1=None, m2=None, m3=None):
        algo = UranusKeyword.get_ne_measure_algo(ne_id)
        body = {
            "delay": int(delay) if delay else algo['delay'],
            "loss": int(loss) if loss else algo['loss'],
            "stdev": int(stdev) if stdev else algo['stdev'],
            "m0": int(m0) if m0 else algo['m0'],
            "m1": int(m1) if m1 else algo['m1'],
            "m2": int(m2) if m2 else algo['m2'],
            "m3": int(m3) if m3 else algo['m3']}
        return are_same(algo, body, [])

    @staticmethod
    def get_cpe_measure_algo(cpe_ip, ssh_port, ssh_user, ssh_password):
        try:
            algo = NeCli.netconf_get_config(cpe_ip, ssh_user, ssh_password, ssh_port,
                                            '/aiwan-config:aiwan-switch/resource/algo//*')
            return algo['aiwan-config:aiwan-switch']['resource']['algo']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def check_cpe_office_speed_up_flow_deleted(s_ne_id, d_ip):
        flows = UranusKeyword.get_ne_route(s_ne_id)
        dst_ip = "{}/32".format(d_ip)
        table_0_flows = filter(lambda x: x["tableId"] == 0 and 'matcher' in x.keys(), flows)
        table_0_flows_matcher = filter(lambda x: "dstIp" in x['matcher'].keys(), table_0_flows)
        res = filter(lambda x: x['matcher']["dstIp"] == dst_ip, table_0_flows_matcher) if table_0_flows_matcher else []
        return len(res) == 0

    @staticmethod
    def get_e2e_links_from_controller(ne_id, d_ne_id):
        res_code, body = UranusInterface.get_e2e_links_from_controller(ne_id)
        if res_code == 404:
            body = {"content": []}
        return filter(lambda x: x["dstId"] == int(d_ne_id), body["content"])

    @staticmethod
    def get_e2e_dest_site_bond(ne_id, d_ne_id):
        res_code, body = UranusInterface.get_e2e_bond_from_controller(ne_id)
        if res_code == 404:
            body = {"content": []}
        return filter(lambda x: x["dstId"] == int(d_ne_id), body["content"])

    @staticmethod
    def get_e2e_dest_site_bond_from_db(ne_id, d_ne_id):
        res_code, body = UranusInterface.get_e2e_bond_from_controller_db(ne_id)
        if res_code == 404:
            body = {"content": []}
        return filter(lambda x: x["dstId"] == int(d_ne_id), body["content"])

    @staticmethod
    def get_e2e_dest_site_bond_portNumber(ne_id, d_ne_id):
        body = UranusKeyword.get_e2e_dest_site_bond(ne_id, d_ne_id)
        return body[0]['portNumber'] if body else None

    @staticmethod
    def check_cpe_2_cpe_table1_flows(s_ne_id, d_ne_id):
        portNumber = UranusKeyword.get_e2e_dest_site_bond_portNumber(s_ne_id, d_ne_id)
        expect_flows = FlowVariables.cpe_2_cpe_table1_flows_with_bond(d_ne_id, portNumber)
        flows = UranusKeyword.get_ne_route(s_ne_id)
        return any(map(lambda x: are_same(expect_flows, x, ["root['specId']", "root['priority']", "root['neId']", "root['matcher']"]), flows))

    @staticmethod
    def get_ne_global_rate_limit(cpe_ip, ssh_port, ssh_user, ssh_password):
        try:
            tasks = NeCli.netconf_get_config(cpe_ip, ssh_user, ssh_password, ssh_port,
                                             '/aiwan-config:aiwan-switch/resource/global-rate-limit//*')
            return tasks['aiwan-config:aiwan-switch']['resource']['global-rate-limit']
        except (IndexError, KeyError, TypeError):
            return None

    @staticmethod
    def get_openflow_dev_id_from_ne_id(ne_id):
        id = str(hex(int(ne_id))).zfill(16).replace('x', '0')
        return 'of:' + id

    @staticmethod
    def get_cpe_type_from_ne_id(ne_id):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body["config"]["accessMode"] if "accessMode" in body["config"].keys() else "pop"

    @staticmethod
    def get_selecting_cpe_num():
        return UranusKeyword.get_controller_metric_with_key("sdwan_selecting_homecode_instance_count")

    @staticmethod
    def get_ne_homeCodeSelection(ne_id):
        res_code, body = UranusInterface.get_homeCodeSelection(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body

    @staticmethod
    def get_controller_metric_with_key(keyStr):
        res_code, body = UranusInterface.get_controller_metric()
        assert res_code == 200, '{} is not 200'.format(res_code)
        res = re.findall(keyStr + " (.*)\n", body)
        return int(eval(res[2]))

    @staticmethod
    def get_controller_metric_with_key_label_value(keyStr, label, value):
        res_code, body = UranusInterface.get_controller_metric()
        assert res_code == 200, '{} is not 200'.format(res_code)
        filterStr = keyStr + "{" + label + "=\"" + value + "\"} (.*)\n"
        print(filterStr)
        res = re.findall(filterStr, body)
        return int(eval(res[0]))

    @staticmethod
    def get_gaea_sevices_status():
        return UranusKeyword.get_controller_metric_with_key("ourea_health")

    @staticmethod
    def get_ne_netconf_config(ne_id):
        res_code, body = OnosInterface.get_ne_netconf_config(ne_id)
        return res_code, body

    @staticmethod
    def get_cpe_wanid(ne_id, iface, index):
        ne_vport = UranusInterface.get_ne_vport(ne_id)
        return filter(lambda x: x['type'] == 'WAN' and x['portId']['iface'] == iface and x['portId']['index'] == index, ne_vport['ports'])[0]['vId']

    @staticmethod
    def get_pop_cpes(ne_id):
        res_code, body = UranusInterface.get_pop_cpes(ne_id)
        assert res_code == 200, '{} is not 200 '.format(res_code)
        return body['cpes']

    @staticmethod
    def get_ne_control_status_from_ne_id(ne_id):
        res_code, body = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body["control"]

    @staticmethod
    def put_ne_control_status(ne_id, status):
        UranusKeyword.put_nes_control_status(status, [int(ne_id)])

    @staticmethod
    def put_nes_control_status(status, ne_id_list=[]):
        body = {"control": status,
                "neIds": ne_id_list}
        res_code, res_body = UranusInterface.put_nes_control_state(body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def get_control_status_nes(status, ne_type):
        res_code, body = UranusInterface.get_control_status_nes(status)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body["{}s".fromat(ne_type)]

    @staticmethod
    def get_uranus_health_code():
        res_code, body = UranusInterface.get_uranus_health()
        assert res_code == 200, '{} is not 200'.format(res_code)
        res = re.findall("aiwan_service_status (.*)\n", body)
        return int(eval(res[2]))

    @staticmethod
    def get_autherserver_statistics():
        res_code, body = UranusInterface.get_authserver_metrics()
        assert res_code == 200, '{} is not 200'.format(res_code)
        types = ["create nonce", "create token", "set secret", "verify token"]

        def get_value_by_key(key):
            countpatternSuss = re.compile('count.*200.*' + key + '\"} (.*)\n')
            count_resS_l = re.findall(countpatternSuss, body)
            sc = int(count_resS_l[0]) if len(count_resS_l) else 0
            countpatternFail = re.compile('count{Code=\"40.*' + key + '\"} (.*)\n')
            count_resF_l = re.findall(countpatternFail, body)
            fc = int(count_resF_l[0]) if len(count_resF_l) else 0
            timepatternSuss = re.compile('sum.*200.*' + key + '\"} (.*)\n')
            time_resS_l = re.findall(timepatternSuss, body)
            st = int(time_resS_l[0]) if len(time_resS_l) else 0
            timepatternFail = re.compile('sum{Code=\"40.*' + key + '\"} (.*)\n')
            time_resF_l = re.findall(timepatternFail, body)
            ft = int(time_resF_l[0]) if len(time_resF_l) else 0
            return [sc, fc, st, ft]
        return map(lambda x: get_value_by_key(x), types)
