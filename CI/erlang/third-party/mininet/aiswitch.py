from time import sleep
from core import ne
from client.uranus import UranusClient
from erlang.libs.configCenter.ConsulKeyword import ConsulKeyword
from core import settings
import docker
import copy
from threading import Thread

ne_list = {}
uranusClient = UranusClient()
DB_PORT = 3000
DB_REST_PORT = 3500
OFP_REST_PORT = 4000


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
                        "ip": settings.SWITCH_HOST,
                        "port": DB_PORT + int(ne_id),
                        "username": settings.SWITCH_NETCONF_USERNAME,
                        "password": settings.SWITCH_NETCONF_PASSWORD},
                    "ports": port_list[:port_num]}}

    routeCodeBody = {
        "cac": int(cac),
        "eac": int(eac)
    }
    ConsulKeyword.put_pop_all(ne_id, routeCodeBody) if ne_type != "CFP" else ConsulKeyword.put_cfp_all(ne_id, routeCodeBody)
    
    uranusClient.register(ne_body, "pop", str(ne_id))


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
            "type": "LAN",
            "mode": "FIA",
            "isEnabled": True,
            "pair": "enp0s3"
        },
        {
            "name": "enp0s9",
            "mac": "08:00:27:D1:70:42",
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
            "addrs": [{"ip": ip_prefix + "1","mode":"MIA"}],
            "type": "WAN",
            "mode": "MIA",
            "isEnabled": True
        },
        {
            "name": "enp0s4",
            "mac": "08:00:27:CF:EF:EB",
            "addrs": [{"ip": ip_prefix + "2","mode":"FIA"}],
            "type": "WAN",
            "mode": "FIA",
            "isEnabled": True
        },
        {
            "name": "enp0s5",
            "mac": "08:00:27:CF:EF:EC",
            "addrs": [{"ip": ip_prefix + "3","mode":"DIA"}],
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
                        "ip": settings.SWITCH_HOST,
                        "port": DB_PORT + int(ne_id),
                        "username": settings.SWITCH_NETCONF_USERNAME,
                        "password": settings.SWITCH_NETCONF_PASSWORD},
                    "ports": port_list_gw[:port_num] if int(modeId) == 2 else port_list[:port_num]}
               }

    def getPreferBody(portName, portAddr):
        Body = [{
            "portId":{
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
    preferenceBody = reduce(lambda x, y: x+y, pre_body)
    
    ConsulKeyword.put_cpe_all(ne_id, preferenceBody)
    return uranusClient.register(ne_body, "cpe", str(ne_id))


def add_pop(pop_type, ne_id, cac, eac, c_ip, c_port, port_num, use_group):
    info = {"type": pop_type, "neId": int(ne_id), "cac": int(cac), "eac": int(eac)}
    print 'controller info {}:{} are useless now'.format(c_ip, c_port)
    pop = ne.PopNode(info)
    pop.add_controller()
    pop.start_switch()
    sleep(1)
    pop_register(pop_type, ne_id, cac, eac, port_num, use_group)
    ne_list[ne_id] = pop


def add_cpe(ne_type, neid_str, cac, eac, c_ip, c_port, port_num, use_group):
    ne_id, modeId, wan_num = from_neid_get_mode_wanNum(neid_str)
    info = {"type": ne_type, "neId": int(ne_id), "cac": int(cac), "eac": int(eac)}
    print 'controller info {}:{} are useless now'.format(c_ip, c_port)
    cpe = ne.CpeNode(info)
    cpe.add_controller()
    cpe.start_switch()
    sleep(1)
    cpe_register(ne_id, cac, eac, port_num, modeId, wan_num, use_group)
    ne_list[ne_id] = cpe


def from_name_get_cac_eac(name):
    return name.split('-')


def from_name_get_type_neid(name):
    return name.split('_')

def from_neid_get_mode_wanNum(neid_str):
    neid_str_info = neid_str.split('.')
    return neid_str_info if len(neid_str_info) == 3 else [neid_str_info[0], 0, 1]


def get_switch(switch_type, ne_id, cac, eac, c_ip, c_port, port_num, use_group):
    match = \
        {
            'CR': add_pop,
            'ER': add_pop,
            'CFP': add_pop,
            'CPE': add_cpe
        }
    return match[switch_type](switch_type, ne_id, cac, eac, c_ip, c_port, port_num, use_group)


def start_aiswitch(full_name, c_ip, c_port, port_num, use_group):
    name, cac, eac = from_name_get_cac_eac(str(full_name))
    switch_type, ne_id = from_name_get_type_neid(name)
    t = Thread(target=get_switch, args=(switch_type, ne_id, cac, eac, c_ip, c_port, port_num, use_group))
    t.start()
    print 'finish thread start'


def get_docker_ip_from_ne_id(ne_id, ps_a=False):
    client = docker.from_env()
    if ne_id:
        new_id = int(ne_id) + 1000
    else:
        new_id = ne_id
    print 'uranus_pt_switch_{}'.format(str(new_id))
    return filter(lambda x: 'uranus_pt_switch_{}'.format(str(new_id)) in x.attrs['Name'], client.containers.list(all=ps_a))


def stop_aiswitch(full_name):
    name, _, _ = from_name_get_cac_eac(str(full_name))
    _, ne_id = from_name_get_type_neid(name)
    if ne_id in ne_list.keys():
        del ne_list[ne_id]
    else:
        print '{} not in the ne_list'.format(full_name)
    map(lambda x: x.remove(force=True), get_docker_ip_from_ne_id(ne_id))


def stop_all_ne():
    docker_list = get_docker_ip_from_ne_id('')
    print docker_list
    map(lambda x: x.stop(), docker_list)


def delete_all_ne():
    print 'delete_all_ne'
    map(lambda x: x.remove(force=True), get_docker_ip_from_ne_id('', True))
