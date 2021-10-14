from time import sleep
from client.controller import ControllerClient
from client.authServerClient import AuthClient
from erlang.libs.configCenter.ConsulKeyword import ConsulKeyword
from erlang.libs.insight.InsightKeyword import InsightKeyword
from core import settings
import copy
import json
import io
import os
from threading import Thread
from client.device import DeviceClient


fake_ne_list = []


class loadTopo(object):

    def __init__(self):
        pass

    @staticmethod
    def start_topo(topoPath):
        with io.open(topoPath, encoding='utf-8') as f:
            topo_data = json.load(f)
        for fakeNe in topo_data:
            start_aiswitch(fakeNe['name'], fakeNe['port_num'], fakeNe['use_group'])
            fake_ne_list.append(fakeNe['name'])
        print fake_ne_list

    @staticmethod
    def start_a_fakene(name, port_num, use_group=False):
        start_aiswitch(name, port_num, use_group)
        fake_ne_list.append(name)

    @staticmethod
    def stop_topo():
        for fakeNe in fake_ne_list:
            stop_aiswitch(fakeNe)

    @staticmethod
    def stop_a_fakene(name):
        stop_aiswitch(name)
        fake_ne_list.pop(fake_ne_list.index(name))


def add_pop(pop_type, ne_id, cac, eac, port_num, use_group):
    DeviceClient.create_openflow_device(pop_type, int(ne_id))
    DeviceClient.start_openflow(int(ne_id))
    sleep(1)
    pop_register(pop_type, ne_id, cac, eac, port_num, use_group)


def add_saas(saas_type, ne_id, cac, eac, port_num, use_group):
    saas_register(ne_id)


def add_anycast(anycast_type, ne_id, cac, eac, port_num, use_group):
    anycast_register(ne_id)


def add_cpe(ne_type, neid_str, cac, eac, port_num, use_group):
    ne_id, modeId, wan_num = from_neid_get_mode_wanNum(neid_str)
    DeviceClient.create_openflow_device(ne_type, int(ne_id))
    DeviceClient.start_openflow(int(ne_id))
    sleep(1)
    cpe_register(ne_id, cac, eac, port_num, modeId, wan_num, use_group)


def from_name_get_cac_eac(name):
    return name.split('-')


def from_name_get_type_neid(name):
    return name.split('_')


def from_neid_get_mode_wanNum(neid_str):
    neid_str_info = neid_str.split('.')
    return neid_str_info if len(neid_str_info) == 3 else [neid_str_info[0], 0, 1]


def get_switch(switch_type, ne_id, cac, eac, port_num, use_group):
    match = \
        {
            'CR': add_pop,
            'ER': add_pop,
            'SAAS': add_saas,
            'ANYCAST': add_anycast,
            'CPE': add_cpe
        }
    return match[switch_type](switch_type, ne_id, cac, eac, port_num, use_group)


def start_aiswitch(full_name, port_num, use_group):
    name, cac, eac = from_name_get_cac_eac(str(full_name))
    switch_type, ne_id = from_name_get_type_neid(name)
    t = Thread(target=get_switch, args=(switch_type, ne_id, cac, eac, port_num, use_group))
    t.start()
    print 'finish thread start'


def stop_aiswitch(full_name):
    name, _, _ = from_name_get_cac_eac(str(full_name))
    ne_Type, neid_str = from_name_get_type_neid(name)
    ne_id, _, _ = from_neid_get_mode_wanNum(neid_str) if ne_Type == "CPE" else [neid_str, 0, 0]
    DeviceClient.stop_openflow(int(ne_id))
    cmd = "ps -ef |grep create_measure|grep {} |awk {}|xargs sudo kill -9".format(ne_id, r"'{print $2}'")
    ret = os.system(cmd)
    if ret == 0:
        return True
    else:
        return False


def saas_register(proxyId):
    proxy = {
        "version": "1.0.0",
        "tunnelAddrs": [
            {
                "addr": "192.168.0.22",
                "port": 4792,
                "groups": ["group1", "group2"]
            }
        ]
    }
    ControllerClient.register_saas_proxy(int(proxyId), proxy)


def anycast_register(serviceId):
    anycast = {
        "version": "1.0.0",
        "tunnelAddrs": [
            {
                "addr": "192.168.0.22",
                "port": 4792,
                "groups": ["group1", "group2"]
            }
        ]
    }
    ControllerClient.register_anycast_proxy(int(serviceId), anycast)


def pop_register(ne_type, ne_id, cac, eac, port_num, use_group):
    if ne_type == "CR":
        ip_prefix = "30" + "." + str(cac) + "." + str(eac) + "."
    else:
        ip_prefix = "20" + "." + str(cac) + "." + str(eac) + "."

    port_list = [
        {
            "name": "eth0",
            "mac": "08:00:27:3f:30:7b",
            "addrs": [{"ip": ip_prefix + "1"}],
            "speed": "1000Mb/s",
            "type": "GENERAL",
            "mode": "FIA",
            "pair": "no",
            "isEnabled": True
        },
        {
            "name": "eth1",
            "mac": "08:00:27:CF:EF:EB",
            "addrs": [{"ip": ip_prefix + "2"}],
            "speed": "1000Mb/s",
            "type": "GENERAL",
            "mode": "FIA",
            "pair": "no",
            "isEnabled": True
        },
        {
            "name": "eth2",
            "mac": "08:00:27:C3:DF:54",
            "addrs": [{"ip": ip_prefix + "3"}],
            "speed": "1000Mb/s",
            "type": "GENERAL",
            "mode": "FIA",
            "pair": "no",
            "isEnabled": True
        }
    ]
    if use_group:
        port_list[1]["addrs"][0]['groups'] = ['group2']
        port_list[2]["addrs"][0]['groups'] = ['group3']

    ne_body = {"model": "x300",
               "type": ne_type,
               "version": {"planet": "1.0.0"},
               "system": {},
               "config":
                   {"netconf": {
                        "ip": settings.CONTROLLER_HOST,
                        "port": settings.POP_NETCONF_START_PORT + (int(ne_id) >> 4) - 500,
                        "username": settings.SWITCH_NETCONF_USERNAME,
                        "password": settings.SWITCH_NETCONF_PASSWORD},
                    "ports": port_list[:int(port_num)]}}

    routeCodeBody = {"cac": int(cac),
                     "eac": int(eac)}
    ConsulKeyword.put_pop_all(ne_id, routeCodeBody) if ne_type != "CFP" else ConsulKeyword.put_cfp_all(ne_id, routeCodeBody)
    start_measure("measure", ne_id)
    ControllerClient.register(ne_body, "pop", ne_id)
    DeviceClient.start_call_home_dev(int(ne_id) >> 4, "POP")


def start_measure(info, ne_id):
    cmd = "sh -c 'mkdir -p logs;python erlang/libs/fake_ne/create_measure_result.py {} {} > logs/{}measure.log &'".format(info, int(ne_id), int(ne_id))
    ret = os.system(cmd)
    if ret == 0:
        return True
    else:
        return False


def cpe_register(ne_id, cac, eac, port_num, modeId, wan_num, use_group):
    ip_prefix = "10" + "." + str(cac) + "." + str(eac) + "."
    addr_list = [{"ip": ip_prefix + "1"}, {"ip": ip_prefix + "2"}, {"ip": ip_prefix + "3"}]
    accessModeList = ['SERIES', 'PARALLEL', 'GATEWAY']
    if use_group:
        addr_list[0]['groups'] = ['group1']
        addr_list[1]['groups'] = ['group2']
        addr_list[2]['groups'] = ['group3']
    port_list = [
        {
            "name": "enp0s3",
            "mac": "08:00:27:3f:30:7b",
            "addrs": addr_list[:int(wan_num)],
            "type": "WAN",
            "mode": "FIA",
            "isEnabled": True
        },
        {
            "name": "enp0s8",
            "mac": "08:00:27:CF:EF:EB",
            "addrs": [{"ip": ip_prefix + "1", "mode": "FIA"}],
            "type": "LAN",
            "mode": "FIA",
            "isEnabled": True,
            "pair": "enp0s3"
        },
        {
            "name": "enp0s9",
            "mac": "08:00:27:D1:70:42",
            "addrs": [{"ip": ip_prefix + "2", "mode": "DIA"}],
            "type": "LAN",
            "mode": "DIA",
            "isEnabled": True
        }
    ]

    port_list_gw = [
        {
            "name": "tun1",
            "mac": "08:00:27:D1:70:42",
            "addrs": [{"ip": ip_prefix + "9", "mode": "FIA"}],
            "type": "LAN",
            "mode": "FIA",
            "isEnabled": True
        },
        {
            "name": "enp0s3",
            "mac": "08:00:27:3f:30:7b",
            "addrs": [{"ip": ip_prefix + "1", "mode": "MIA"}],
            "type": "WAN",
            "mode": "MIA",
            "isEnabled": True
        },
        {
            "name": "enp0s4",
            "mac": "08:00:27:CF:EF:EB",
            "addrs": [{"ip": ip_prefix + "2", "mode": "FIA"}],
            "type": "WAN",
            "mode": "FIA",
            "isEnabled": True
        },
        {
            "name": "enp0s5",
            "mac": "08:00:27:CF:EF:EC",
            "addrs": [{"ip": ip_prefix + "3", "mode": "DIA"}],
            "type": "WAN",
            "mode": "DIA",
            "isEnabled": True
        }
    ]
    if use_group:
        port_list_gw[1]["addrs"][0]['groups'] = ['group1']
        port_list_gw[2]["addrs"][0]['groups'] = ['group2']
        port_list_gw[3]["addrs"][0]['groups'] = ['group3']

    ne_body = {"model": "x300",
               "type": 'CPE',
               "version": {"satellite": "1.0.0"},
               "system": {},
               "config":
                   {"accessMode": accessModeList[int(modeId)],
                    "netconf": {
                        "ip": settings.CONTROLLER_HOST,
                        "port": settings.CPE_NETCONF_START_PORT + (int(ne_id) >> 4) - 1000,
                        "username": settings.SWITCH_NETCONF_USERNAME,
                        "password": settings.SWITCH_NETCONF_PASSWORD},
                    "ports": port_list_gw[:int(port_num)] if int(modeId) == 2 else port_list[:int(port_num)]}
               }

    def getPreferBody(portName, portAddr):
        Body = [{
                "portId": {
                    "iface": portName,
                    "index": 0
                    }
                }]
        PBody = copy.deepcopy(Body)
        if len(portAddr) == 1:
            if "groups" in portAddr[0].keys():
                PBody[0]["preferGroups"] = portAddr[0]["groups"]
        else:
            PBody = [copy.deepcopy(Body[0]) for i in range(len(portAddr))]
            for i in range(len(portAddr)):
                PBody[i]["portId"]["index"] = i
                if "groups" in portAddr[i].keys():
                    PBody[i]["preferGroups"] = portAddr[i]["groups"]
        return PBody

    pre_body = map(lambda x: getPreferBody(x['name'], x['addrs']) if x['type'] == "WAN" else [], ne_body["config"]["ports"])
    preferenceBody = reduce(lambda x, y: x + y, pre_body)
    ConsulKeyword.put_cpe_all(ne_id, preferenceBody)
    start_measure(ip_prefix + "1", ne_id)
    ControllerClient.register(ne_body, "cpe", ne_id, AuthClient.get_token())
    DeviceClient.start_call_home_dev(int(ne_id) >> 4)
