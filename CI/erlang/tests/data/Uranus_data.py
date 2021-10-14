# coding=utf-8
cnf_devices = {"devices": [
    {"id": "netconf:10.192.12.2:830", "type": "SWITCH", "available": True, "role": "MASTER", "mfr": "unknown",
     "hw": "unknown", "sw": "unknown", "serial": "unknown", "driver": "default", "chassisId": "0",
     "lastUpdate": "1541078979632", "humanReadableLastUpdate": "connected 13h9m ago",
     "annotations": {"ipaddress": "10.192.12.2", "port": "830", "protocol": "NETCONF"}},
    {"id": "netconf:10.192.10.2:830", "type": "SWITCH", "available": True, "role": "MASTER", "mfr": "unknown",
     "hw": "unknown", "sw": "unknown", "serial": "unknown", "driver": "default", "chassisId": "0",
     "lastUpdate": "1541078978717", "humanReadableLastUpdate": "connected 13h9m ago",
     "annotations": {"ipaddress": "10.192.10.2", "port": "830", "protocol": "NETCONF"}},
    {"id": "netconf:10.192.1.2:830", "type": "SWITCH", "available": True, "role": "MASTER", "mfr": "unknown",
     "hw": "unknown", "sw": "unknown", "serial": "unknown", "driver": "default", "chassisId": "0",
     "lastUpdate": "1541052113995", "humanReadableLastUpdate": "connected 20h37m ago",
     "annotations": {"ipaddress": "10.192.1.2", "port": "830", "protocol": "NETCONF"}}]}

devices = {"devices": [
    {"id": "netconf:10.192.12.2:830", "type": "SWITCH", "available": True, "role": "MASTER", "mfr": "unknown",
     "hw": "unknown", "sw": "unknown", "serial": "unknown", "driver": "default", "chassisId": "0",
     "lastUpdate": "1541078979632", "humanReadableLastUpdate": "connected 13h9m ago",
     "annotations": {"ipaddress": "10.192.12.2", "port": "830", "protocol": "NETCONF"}},
    {"id": "of:00000000000003e9", "type": "SWITCH", "available": True, "role": "MASTER", "mfr": "aiwan", "hw": "",
     "sw": "", "serial": "1", "driver": "aiwan-switch", "chassisId": "3e9", "lastUpdate": "1541079065065",
     "humanReadableLastUpdate": "connected 13h8m ago",
     "annotations": {"channelId": "10.192.12.2:33698", "managementAddress": "10.192.12.2", "protocol": "OF_13"}},
    {"id": "netconf:10.192.10.2:830", "type": "SWITCH", "available": True, "role": "MASTER", "mfr": "unknown",
     "hw": "unknown", "sw": "unknown", "serial": "unknown", "driver": "default", "chassisId": "0",
     "lastUpdate": "1541078978717", "humanReadableLastUpdate": "connected 13h9m ago",
     "annotations": {"ipaddress": "10.192.10.2", "port": "830", "protocol": "NETCONF"}},
    {"id": "of:00000000000003ea", "type": "SWITCH", "available": True, "role": "MASTER", "mfr": "aiwan", "hw": "",
     "sw": "", "serial": "1", "driver": "aiwan-switch", "chassisId": "3ea", "lastUpdate": "1541079063970",
     "humanReadableLastUpdate": "connected 13h8m ago",
     "annotations": {"channelId": "10.192.10.2:52654", "managementAddress": "10.192.10.2", "protocol": "OF_13"}},
    {"id": "of:0000000000001123", "type": "SWITCH", "available": True, "role": "MASTER", "mfr": "aiwan", "hw": "",
     "sw": "", "serial": "11235813213455", "driver": "aiwan-switch", "chassisId": "1123", "lastUpdate": "1541052116068",
     "humanReadableLastUpdate": "connected 20h37m ago",
     "annotations": {"channelId": "10.192.1.2:34088", "managementAddress": "10.192.1.2", "protocol": "OF_13"}},
    {"id": "netconf:10.192.1.2:830", "type": "SWITCH", "available": True, "role": "MASTER", "mfr": "unknown",
     "hw": "unknown", "sw": "unknown", "serial": "unknown", "driver": "default", "chassisId": "0",
     "lastUpdate": "1541052113995", "humanReadableLastUpdate": "connected 20h37m ago",
     "annotations": {"ipaddress": "10.192.1.2", "port": "830", "protocol": "NETCONF"}}]}

of_devices_num = 3

flows_selector_cmd_list = ['flows -f b300000f760d50 any of:000000000000162f',
                           'flows -f b30000872eaf18 any of:000000000000162f',
                           'flows -f b30000880b6fa5 any of:000000000000162f']

flows_selector_rnt_list = [[u'deviceId=of:000000000000162f, flowRuleCount=1\n',
                            u'    id=b30000880b6fa5, state=ADDED, bytes=1989651801, packets=2398991, duration=351198, liveType=UNKNOWN, priority=1000, tableId=1, appId=com.wsds.aiwan.uranus.gaea.model.net.topology.impl.TopologyServiceImpl, payLoad=null, selector=[EXTENSION:of:000000000000162f/OFOxmDcacMatch{dcac=1}, EXTENSION:of:000000000000162f/OFOxmDeacMatch{deac=1}, EXTENSION:of:000000000000162f/OFOxmDstDevMatch{dstDevId=AiwanServiceId{id=70204, neId=NEId{id=4387}, endpointId=EndpointId{id=12}}}], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:102], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}\n'],
                           [u'deviceId=of:000000000000162f, flowRuleCount=1\n',
                            u'    id=b300000f760d50, state=ADDED, bytes=0, packets=0, duration=351198, liveType=UNKNOWN, priority=1000, tableId=1, appId=com.wsds.aiwan.uranus.gaea.model.net.topology.impl.TopologyServiceImpl, payLoad=null, selector=[EXTENSION:of:000000000000162f/OFOxmDcacMatch{dcac=3}, EXTENSION:of:000000000000162f/OFOxmDeacMatch{deac=3}, EXTENSION:of:000000000000162f/OFOxmDstDevMatch{dstDevId=AiwanServiceId{id=70214, neId=NEId{id=1001}, endpointId=EndpointId{id=1}}}], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:102], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}\n'],
                           [u'deviceId=of:000000000000162f, flowRuleCount=1\n',
                            u'    id=b30000872eaf18, state=ADDED, bytes=1196957847, packets=2602385, duration=351198, liveType=UNKNOWN, priority=1000, tableId=1, appId=com.wsds.aiwan.uranus.gaea.model.net.topology.impl.TopologyServiceImpl, payLoad=null, selector=[EXTENSION:of:000000000000162f/OFOxmDcacMatch{dcac=2}, EXTENSION:of:000000000000162f/OFOxmDeacMatch{deac=2}, EXTENSION:of:000000000000162f/OFOxmDstDevMatch{dstDevId=AiwanServiceId{id=73204, neId=NEId{id=1002}, endpointId=EndpointId{id=1}}}], treatment=DefaultTrafficTreatment{immediate=[OUTPUT:101], deferred=[], transition=None, meter=[], cleared=false, StatTrigger=null, metadata=null}\n']]

test_flows_seletor_rtn_flow = {
    "id": "50384023113658277",
    "tableId": "1",
    "appId": "com.wsds.aiwan.uranus.gaea.model.net.topology.impl.TopologyServiceImpl",
    "groupId": 0,
    "priority": 1000,
    "timeout": 0,
    "isPermanent": True,
    "deviceId": "of:000000000000162f",
    "state": "ADDED",
    "life": 350043,
    "packets": 2398991,
    "bytes": 1989651801,
    "liveType": "UNKNOWN",
    "lastSeen": 1541396679539,
    "treatment": {
        "instructions": [
            {
                "type": "OUTPUT",
                "port": "102"
            }
        ],
        "deferred": []
    },
    "selector": {
        "criteria": [
            {
                "type": "EXTENSION"
            },
            {
                "type": "EXTENSION"
            },
            {
                "type": "EXTENSION"
            }
        ]
    }
}

device_flows = {
    "flows": [
        {
            "id": "50384021090602320",
            "tableId": "1",
            "appId": "com.wsds.aiwan.uranus.gaea.model.net.topology.impl.TopologyServiceImpl",
            "groupId": 0,
            "priority": 1000,
            "timeout": 0,
            "isPermanent": True,
            "deviceId": "of:000000000000162f",
            "state": "ADDED",
            "life": 350043,
            "packets": 0,
            "bytes": 0,
            "liveType": "UNKNOWN",
            "lastSeen": 1541396679539,
            "treatment": {
                "instructions": [
                    {
                        "type": "OUTPUT",
                        "port": "102"
                    }
                ],
                "deferred": []
            },
            "selector": {
                "criteria": [
                    {
                        "type": "EXTENSION"
                    },
                    {
                        "type": "EXTENSION"
                    },
                    {
                        "type": "EXTENSION"
                    }
                ]
            }
        },
        {
            "id": "50384023099191064",
            "tableId": "1",
            "appId": "com.wsds.aiwan.uranus.gaea.model.net.topology.impl.TopologyServiceImpl",
            "groupId": 0,
            "priority": 1000,
            "timeout": 0,
            "isPermanent": True,
            "deviceId": "of:000000000000162f",
            "state": "ADDED",
            "life": 350043,
            "packets": 2602385,
            "bytes": 1196957847,
            "liveType": "UNKNOWN",
            "lastSeen": 1541396679539,
            "treatment": {
                "instructions": [
                    {
                        "type": "OUTPUT",
                        "port": "101"
                    }
                ],
                "deferred": []
            },
            "selector": {
                "criteria": [
                    {
                        "type": "EXTENSION"
                    },
                    {
                        "type": "EXTENSION"
                    },
                    {
                        "type": "EXTENSION"
                    }
                ]
            }
        },
        {
            "id": "50384023113658277",
            "tableId": "1",
            "appId": "com.wsds.aiwan.uranus.gaea.model.net.topology.impl.TopologyServiceImpl",
            "groupId": 0,
            "priority": 1000,
            "timeout": 0,
            "isPermanent": True,
            "deviceId": "of:000000000000162f",
            "state": "ADDED",
            "life": 350043,
            "packets": 2398991,
            "bytes": 1989651801,
            "liveType": "UNKNOWN",
            "lastSeen": 1541396679539,
            "treatment": {
                "instructions": [
                    {
                        "type": "OUTPUT",
                        "port": "102"
                    }
                ],
                "deferred": []
            },
            "selector": {
                "criteria": [
                    {
                        "type": "EXTENSION"
                    },
                    {
                        "type": "EXTENSION"
                    },
                    {
                        "type": "EXTENSION"
                    }
                ]
            }
        }
    ]}

ne_configs = \
    [
        {
            "deviceId": 4387,
            "type": "ER",
            "version": "1.3.0",
            "os": {
                "name": "Linux",
                "version": "#161-Ubuntu SMP Mon Aug 27 10:45:01 UTC 2018"
            },
            "netconf": {
                "ip": "10.192.1.2",
                "port": 830,
                "username": "netconfuser",
                "password": "1234"
            },
            "portList": [
                {
                    "name": "eno1",
                    "mac": "24:6e:96:b1:16:ae",
                    "ip": "10.192.1.2",
                    "speed": "1000Mbps",
                    "type": "GENERAL",
                    "isEnabled": True
                },
                {
                    "name": "eno2",
                    "mac": "24:6e:96:b1:16:b0",
                    "ip": "10.192.2.2",
                    "speed": "1000Mbps",
                    "type": "GENERAL",
                    "isEnabled": True
                }
            ]
        },
        {
            "deviceId": 89,
            "type": "CFP",
            "version": "1.3.0",
            "os": {
                "name": "Linux",
                "version": "#25-Ubuntu SMP Wed May 23 18:02:16 UTC 2018"
            },
            "netconf": {
                "ip": "172.17.0.1",
                "port": 830,
                "username": "netconfuser",
                "password": "1234"
            },
            "portList": [
                {
                    "name": "eth2",
                    "mac": "aa:bb:cc:11:22:33",
                    "ip": "10.192.9.8",
                    "speed": "1000Mbps",
                    "type": "GENERAL",
                    "isEnabled": True
                }
            ]
        },
        {
            "deviceId": 1001,
            "type": "CPE",
            "version": "0.0.1",
            "os": {
                "name": "Linux",
                "version": "#46~16.04.1-Ubuntu SMP Thu May 3 10:06:43 UTC 2018"
            },
            "netconf": {
                "ip": "10.192.12.2",
                "port": 830,
                "username": "air",
                "password": "Passw0rd"
            },
            "portList": [
                {
                    "name": "enp1s0",
                    "mac": "08:cb:40:77:d1:3c",
                    "ip": "10.192.12.2",
                    "speed": "1000Mb/s",
                    "type": "WAN",
                    "isEnabled": True
                },
                {
                    "name": "enp2s0",
                    "mac": "E4:F0:04:6F:4C:AC",
                    "ip": "10.192.1.2",
                    "speed": "1000Mb/s",
                    "type": "LAN",
                    "isEnabled": True
                },
                {
                    "name": "enp3s0",
                    "mac": "00:E0:67:08:6A:AE",
                    "speed": "100Mb/s",
                    "type": "GENERAL",
                    "isEnabled": True
                },
                {
                    "name": "enp4s0",
                    "mac": "00:E0:67:08:6A:AF",
                    "ip": "10.192.9.28",
                    "speed": "1000Mb/s",
                    "type": "GENERAL",
                    "isEnabled": True
                }
            ]
        },
        {
            "deviceId": 1002,
            "type": "CPE",
            "version": "0.0.1",
            "os": {
                "name": "Linux",
                "version": "#46~16.04.1-Ubuntu SMP Thu May 3 10:06:43 UTC 2018"
            },
            "netconf": {
                "ip": "10.192.10.2",
                "port": 830,
                "username": "air",
                "password": "Passw0rd"
            },
            "portList": [
                {
                    "name": "enp1s0",
                    "mac": "78:44:fd:cb:06:eb",
                    "ip": "10.192.10.2",
                    "speed": "1000Mb/s",
                    "type": "WAN",
                    "isEnabled": True
                },
                {
                    "name": "enp2s0",
                    "mac": "00:E0:67:0E:6C:E5",
                    "speed": "1000Mb/s",
                    "type": "LAN",
                    "isEnabled": True
                },
                {
                    "name": "enp3s0",
                    "mac": "00:E0:67:0E:6C:E6",
                    "speed": "1000Mb/s",
                    "type": "GENERAL",
                    "isEnabled": True
                },
                {
                    "name": "enp4s0",
                    "mac": "00:E0:67:0E:6C:E7",
                    "type": "GENERAL",
                    "isEnabled": True
                },
                {
                    "name": "enp6s0",
                    "mac": "00:E0:67:0E:6C:E9",
                    "ip": "10.192.9.10",
                    "speed": "1000Mb/s",
                    "type": "GENERAL",
                    "isEnabled": True
                }
            ]
        }
    ]

set_controller_body = {"controllers": [{"ip": "10.192.9.8", "port": 6633}]}

cli_get_tunnel_netcfg = [u'{\n', u'  "aiwan-config:aiwan-switch": {\n', u'    "resource": {\n', u'      "tunnels": {\n',
                         u'        "tunnel": [\n', u'          {\n', u'            "id": 67165,\n',
                         u'            "number": 58947,\n', u'            "mtu": 1500,\n',
                         u'            "fragment-strategy": 1,\n', u'            "keepalive": 60,\n',
                         u'            "local-ipv4-address": "10.192.10.2",\n',
                         u'            "local-ipv4-ports": 1000,\n', u'            "remote-ipv4-ports": 4789,\n',
                         u'            "remote-ipv4-address": "10.192.2.2"\n', u'          }\n', u'        ]\n',
                         u'      }\n', u'    }\n', u'  }\n', u'}\n']

cli_get_key_netcfg = [u'{\n', u'  "aiwan-config:aiwan-switch": {\n', u'    "resource": {\n', u'      "secretKey": {\n',
                      u'        "AES128": "AAAAB3NzaC1yc2EA"\n', u'      }\n', u'    }\n', u'  }\n', u'}\n']

cli_get_measure_task_netcfg = [u'{\n', u' "aiwan-config:aiwan-switch": {\n', u' "resource": {\n',
                               u' "net-measure-tasks": {\n', u' "task": [\n', u' {\n', u' "id": 2084647767,\n',
                               u' "result-max": 3600,\n', u' "timeout": 3000,\n', u' "interval": 1,\n',
                               u' "local-ipv4-address": "10.192.10.2",\n', u' "local-ipv4-ports": 831,\n',
                               u' "remote-ipv4-address": "10.192.1.2",\n', u' "remote-ipv4-ports": 5800\n', u' },\n',
                               u' {\n', u' "id": 2084677558,\n', u' "result-max": 3600,\n', u' "timeout": 3000,\n',
                               u' "interval": 1,\n', u' "local-ipv4-address": "10.192.10.2",\n',
                               u' "local-ipv4-ports": 831,\n', u' "remote-ipv4-address": "10.192.2.2",\n',
                               u' "remote-ipv4-ports": 5800\n', u' }\n', u' ]\n', u' }\n', u' }\n', u' }\n', u'}\n']

cli_get_ports_netcfg = [u'{\n', u'  "aiwan-config:aiwan-switch": {\n', u'    "resource": {\n', u'      "ports": {\n',
                        u'        "port": [\n', u'          {\n', u'            "id": 485565000,\n',
                        u'            "number": 2,\n', u'            "interface": "enp1s0"\n', u'          }\n',
                        u'        ]\n', u'      }\n', u'    }\n', u'  }\n', u'}\n']

cli_get_measure_task_config = [u'{\n', u' "aiwan-config:aiwan-switch": {\n', u' "resource": {\n',
                               u' "net-measure-tasks": {\n', u' "task": [\n', u' {\n', u' "id": 72991851,\n',
                               u' "local-ipv4-address": "10.192.1.2",\n', u' "local-ipv4-ports": 5800\n', u' },\n',
                               u' {\n', u' "id": -193432375,\n', u' "local-ipv4-address": "10.192.2.2",\n',
                               u' "local-ipv4-ports": 5800\n', u' }\n', u' ]\n', u' }\n', u' }\n', u' }\n', u'}\n']
set_tunnel_config_check_body = \
    {
        "strategy": 2,
        "mtu": 1400,
        "keepAlive": 30
    }

flow_spec = \
    {
        "neId": 1001,
        "priority": 1000,
        "timeout": 0,
        "matcher": {
            "inPort": 1,
            "ethType": 2048,
            "dstIp": "172.19.42.2/32"
        },
        "actions": [
            {
                "type": "PUSH_EX_MPLS",
                "scac": 4,
                "seac": 4,
                "dcac": 4,
                "deac": 4,
                "ttl": 127
            },
            {
                "type": "PUSH_EX_VXLAN",
                "header": 11,
                "srcDev": 16017,
                "dstDev": 16033
            },
            {
                "type": "GOTO_TABLE",
                "tableId": 1

            }
        ]
    }

company_config = \
    [{
        "id": 1234,
        "name": "subao",
        "ability": 0
    }]

company_key = \
    [{
        "name": "subao",
        "content": "AAAAB3NzaC1yc2EA"
    }]

company_site = \
    [{
        "id": 111,
        "name": "shanghai",
        "neId": 1001,
        "mode": "OFFICE"
    }]

set_es_ip_cmd = [
    'cfg set com.wsds.aiwan.uranus.gaea.provider.es.impl.EsProviderImpl aiwanEsUrls http://172.17.0.1:9200']
set_node_feq_cmd = ['cfg set com.wsds.aiwan.uranus.gaea.service.NodeSelector netMeasurePollFrequency 30']
set_manage_feq_cmd = ['cfg set org.onosproject.provider.netconf.device.impl.NetconfDeviceProvider pollFrequency 10']
set_cr_area_select_delay = [
    'cfg set com.wsds.aiwan.uranus.gaea.model.area.impl.AreaSelectorImpl areaSelectorDelay 10000']
set_flow_poll_frequency = [
    'cfg set com.wsds.aiwan.uranus.cronus.model.stats.flow.impl.FlowStatsProvider aiwanFlowPollFrequency 5']

tunnel = {'id': -909037387, 'interval': 1, 'local-ipv4-address': '10.192.9.8', 'local-ipv4-ports': 5801,
          'remote-ipv4-address': '10.192.2.2', 'remote-ipv4-ports': 5800, 'result-max': 3600, 'timeout': 3000}

measure_task_result = {"took": 6, "timed_out": False,
                       "shards": {"total": 5, "successful": 5, "skipped": 0, "failed": 0},
                       "hits": {"total": 1, "max_score": 0.5753642, "hits": [
                           {"index": "netmeaure_2018-11-22", "type": "89", "id": "PS_wOGcBeD5lwZaOh-gb",
                            "score": 0.5753642,
                            "_source": {"srcNEId": 89, "dstNEId": 4387, "srcIp": "10.192.9.8", "dstIp": "10.192.1.2",
                                        "srcPort": 5801, "dstPort": 5800, "min": 1.0, "max": 1.0, "avg": 1.0,
                                        "sdev": 0.0, "loss": 0.0, "timestamp": 1542848543953}}]}}

ret_cac_eac = {"cac": 4, "eac": 4}
ret_without_cac_eac = {"cac": -1, "eac": -1}

ret_ne_tunnels = \
    [
        {
            "tunnelId": 64901,
            "srcIP": "10.192.2.2",
            "srcPort": 4789,
            "dstNEId": 1002,
            "dstIP": "10.192.10.2",
            "dstPort": 1000,
            "weight": 5000
        },
        {
            "tunnelId": 58947,
            "srcIP": "10.192.2.2",
            "srcPort": 4789,
            "dstNEId": 1001,
            "dstIP": "10.192.12.2",
            "dstPort": 1000,
            "weight": 5000
        }
    ]

ret_ne_netlinks = \
    [
        {
            "srcNEId": 89,
            "dstNEId": 4387,
            "srcIp": "10.192.9.8",
            "srcPort": 5801,
            "dstIp": "10.192.2.2",
            "dstPort": 5800
        },
        {
            "srcNEId": 89,
            "dstNEId": 1002,
            "srcIp": "10.192.9.8",
            "srcPort": 5801,
            "dstIp": "10.192.1.2",
            "dstPort": 5800
        }
    ]

post_nat_agent = \
    {
        "dev": 33,
        "endpoint": 11,
        "ifAddr": "eth0",
        "startNatPort": 1000,
        "endNatPort": 5000,
        "tcpNatTimeout": 1000,
        "udpNatTimeout": 2000
    }

post_nat_agent_pattern = \
    {
        "type": "REGEX",
        "pattern": "*",
        "devs": [{
            "neId": 33,
            "endpoint": 11
        }]
    }

post_nat_pattern = \
    {
        "dev": 11,
        "type": "DOMAIN",
        "pattern": ".*google.*",
        "ttl": 600,
        "priority": 1000,
        "desc": "desc"
    }

post_dns_nat_flow = \
    {
        "neId": 11,
        "priority": 1000,
        "timeout": 0,
        "matcher": {
            "pktType": 1
        },
        "actions": [
            {
                "type": "OUTPUT",
                "outPort": -3
            }
        ]
    }

get_all_device_flows_info = \
    [
        {
            "specId": 51509922430687460,
            "neId": 1001,
            "tableId": 1,
            "priority": 1000,
            "timeout": 0,
            "matcher": {
                "dcac": 4,
                "deac": 4,
                "dstDev": 1002
            },
            "actions": [
                {
                    "type": "OUTPUT",
                    "outPort": 49764
                }
            ]
        },
        {
            "specId": 52354348889935460,
            "neId": 1001,
            "tableId": 0,
            "priority": 10,
            "timeout": 0,
            "matcher": {
                "inPort": 2
            },
            "actions": [
                {
                    "type": "OUTPUT",
                    "outPort": 1
                }
            ]
        },
        {
            "specId": 52635820675601220,
            "neId": 1002,
            "tableId": 0,
            "priority": 1,
            "timeout": 0,
            "matcher": {},
            "actions": [
                {
                    "type": "GOTO_TABLE",
                    "tableId": 1
                }
            ]
        },
        {
            "specId": 51509922385247544,
            "neId": 4387,
            "tableId": 1,
            "priority": 1000,
            "timeout": 0,
            "matcher": {
                "dcac": 4,
                "deac": 4,
                "dstDev": 1002
            },
            "actions": [
                {
                    "type": "OUTPUT",
                    "outPort": 9446
                }
            ]
        },
        {
            "specId": 51509923915173370,
            "neId": 4387,
            "tableId": 1,
            "priority": 1000,
            "timeout": 0,
            "matcher": {
                "dcac": 4,
                "deac": 4,
                "dstDev": 1001
            },
            "actions": [
                {
                    "type": "OUTPUT",
                    "outPort": 3492
                }
            ]
        },
        {
            "specId": 51509923209190430,
            "neId": 1002,
            "tableId": 1,
            "priority": 1000,
            "timeout": 0,
            "matcher": {
                "dcac": 4,
                "deac": 4,
                "dstDev": 1001
            },
            "actions": [
                {
                    "type": "OUTPUT",
                    "outPort": 4390
                }
            ]
        },
        {
            "specId": 52354349676824940,
            "neId": 1002,
            "tableId": 0,
            "priority": 10,
            "timeout": 0,
            "matcher": {
                "inPort": 1
            },
            "actions": [
                {
                    "type": "OUTPUT",
                    "outPort": 2
                }
            ]
        }
    ]

Test_Add_CPE10014_IN_ER10002_tunnels = \
    [{'local': 10014, 'peer': [['20.5.12.1', '10.5.23.1']]},
     {'local': 10002, 'peer': [['10.5.23.1', '20.5.12.1'], ['10.5.23.1', '30.5.1.1'], ['10.5.23.1', '30.5.1.2']]}]

Ret_Add_CPE10014_IN_ER10002_tunnels = \
    [{'local': 10014, 'peer': [['20.5.12.1', '9.5.23.1']]},
     {'local': 10002, 'peer': [['9.5.23.1', '20.5.12.1'], ['9.5.23.1', '30.5.1.1'], ['9.5.23.1', '30.5.1.2']]}]

Post_Wan_MPLS_Tunnel = \
    [
        {
            "tunnelId": 9999,
            "srcIP": '169.254.100.102',
            "srcPort": 4799,
            "dstNEId": 1001,
            "dstIP": '169.254.100.101',
            "dstPort": 4799
        }
    ]

Post_route_flow_spec = \
    {
        "neId": 4387,
        "tableId": 1,
        "priority": 1500,
        "timeout": 0,
        "matcher": {"dcac": 4, "deac": 4, "dstDev": 16017},
        "actions": [{"type": "OUTPUT", "outPort": 3492}]
    }

test_get_flows_with_id = \
    {
        "flows": [
            {
                "id": "50384023267965790",
                "tableId": "1",
                "appId": "com.wsds.aiwan.uranus.gaea.model.net.topology.impl.TopologyServiceImpl",
                "groupId": 0,
                "priority": 1000,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003e9",
                "state": "ADDED",
                "life": 12330,
                "packets": 4488,
                "bytes": 0,
                "liveType": "UNKNOWN",
                "lastSeen": 1545374556884,
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "59015"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "EXTENSION"
                        },
                        {
                            "type": "EXTENSION"
                        },
                        {
                            "type": "EXTENSION"
                        }
                    ]
                }
            }
        ]
    }

test_pass_through_flows = \
    {'actions': [{'outPort': 4, 'type': 'OUTPUT'}],
     'matcher': {'inPort': 3},
     'neId': 10012, 'priority': 20,
     'tableId': 0, 'timeout': 0}

running_measure_config = \
    {"upperBandwidth": 100.0, "lowerBandwidth": 2.5,
     "upperBwPercent": 300.0, "lowBwPercent": 20.0,
     "maxLossIn15Min": 0.8, "avgLossIn60Min": 0.4,
     "maxLossRatio": 1.0}

test_get_nat_agent_list = \
    [{"dev": 4387, "endpoint": 11, "ifAddr": "eno2", "startNatPort": 1000,
      "endNatPort": 5000, "tcpNatTimeout": 1000, "udpNatTimeout": 2000},
     {"dev": 4387, "endpoint": 10, "ifAddr": "eno1", "startNatPort": 1000,
      "endNatPort": 5000, "tcpNatTimeout": 1000, "udpNatTimeout": 2000}]

running_measure_config_modified = \
    {"upperBandwidth": 100.0, "lowerBandwidth": 2.5,
     "upperBwPercent": 300.0, "lowBwPercent": 20.0,
     "maxLossIn15Min": 0.8, "avgLossIn60Min": 0.4,
     "maxLossRatio": 5.0}

test_site_isps = \
    [
        {
            "name": "eth0",
            "isp": "" 'CMCC'
        },
        {
            "name": "eth1",
            "isp": "" 'CUCC'
        }
    ]

cpe_flows = \
    {
        "flows": [
            {
                "id": "50384023287578292",
                "tableId": "1",
                "appId": "com.wsds.aiwan.uranus.gaea.service.TopologyManager",
                "groupId": 0,
                "priority": 1100,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "PENDING_ADD",
                "life": 0,
                "packets": 0,
                "bytes": 0,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184152475,
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "3"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "EXTENSION"
                        },
                        {
                            "type": "EXTENSION"
                        },
                        {
                            "type": "EXTENSION"
                        }
                    ]
                }
            },
            {
                "id": "50384020965518663",
                "tableId": "1",
                "appId": "com.wsds.aiwan.uranus.gaea.service.TopologyManager",
                "groupId": 0,
                "priority": 999,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "ADDED",
                "life": 444,
                "packets": 0,
                "bytes": 0,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184153583,
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "7714"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "EXTENSION"
                        },
                        {
                            "type": "EXTENSION"
                        }
                    ]
                }
            },
            {
                "id": "50384023772786327",
                "tableId": "1",
                "appId": "com.wsds.aiwan.uranus.gaea.service.TopologyManager",
                "groupId": 0,
                "priority": 1000,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "ADDED",
                "life": 478,
                "packets": 114666,
                "bytes": 145303716,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184153583,
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "7519"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "EXTENSION"
                        },
                        {
                            "type": "EXTENSION"
                        }
                    ]
                }
            },
            {
                "id": "51509923622037242",
                "tableId": "0",
                "appId": "com.wsds.aiwan.uranus.cronus.model.office.impl.OfficeServiceImpl",
                "groupId": 0,
                "priority": 10,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "ADDED",
                "life": 525,
                "packets": 270,
                "bytes": 29831,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184153583,
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "1"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "IN_PORT",
                            "port": 2
                        }
                    ]
                }
            },
            {
                "id": "51228447368390562",
                "tableId": "0",
                "appId": "com.wsds.aiwan.uranus.cronus.service.intranet.IntranetManager",
                "groupId": 0,
                "priority": 500,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "ADDED",
                "life": 1,
                "packets": 1,
                "bytes": 356,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184153583,
                "treatment": {
                    "instructions": [
                        {
                            "type": "EXTENSION",
                            "extension": {
                                "type": "AIWAN_ACTION_PUSH_EX_VXLAN",
                                "ExVxlan": 792702404221899600
                            }
                        },
                        {
                            "type": "EXTENSION",
                            "extension": {
                                "type": "AIWAN_ACTION_PUSH_EX_MPLS",
                                "ExMpls": -3969
                            }
                        },
                        {
                            "type": "TABLE",
                            "tableId": "1"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "IN_PORT",
                            "port": 3
                        }
                    ]
                }
            },
            {
                "id": "51509922231193335",
                "tableId": "0",
                "appId": "com.wsds.aiwan.uranus.cronus.model.office.impl.OfficeServiceImpl",
                "groupId": 0,
                "priority": 500,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "ADDED",
                "life": 1,
                "packets": 0,
                "bytes": 0,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184153583,
                "treatment": {
                    "instructions": [
                        {
                            "type": "EXTENSION",
                            "extension": {
                                "type": "AIWAN_ACTION_PUSH_EX_VXLAN",
                                "ExVxlan": 792702395631976700
                            }
                        },
                        {
                            "type": "EXTENSION",
                            "extension": {
                                "type": "AIWAN_ACTION_PUSH_EX_MPLS",
                                "ExMpls": 1141915775
                            }
                        },
                        {
                            "type": "TABLE",
                            "tableId": "1"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "IN_PORT",
                            "port": 1
                        },
                        {
                            "type": "ETH_TYPE",
                            "ethType": "0x800"
                        },
                        {
                            "type": "IPV4_DST",
                            "ip": "10.1.13.2/32"
                        }
                    ]
                }
            },
            {
                "id": "51509923146633854",
                "tableId": "0",
                "appId": "com.wsds.aiwan.uranus.cronus.model.office.impl.OfficeServiceImpl",
                "groupId": 0,
                "priority": 500,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "ADDED",
                "life": 1,
                "packets": 0,
                "bytes": 0,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184153583,
                "treatment": {
                    "instructions": [
                        {
                            "type": "EXTENSION",
                            "extension": {
                                "type": "AIWAN_ACTION_PUSH_EX_VXLAN",
                                "ExVxlan": 792702395631972600
                            }
                        },
                        {
                            "type": "EXTENSION",
                            "extension": {
                                "type": "AIWAN_ACTION_PUSH_EX_MPLS",
                                "ExMpls": 1141915775
                            }
                        },
                        {
                            "type": "TABLE",
                            "tableId": "1"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "IN_PORT",
                            "port": 1
                        },
                        {
                            "type": "ETH_TYPE",
                            "ethType": "0x800"
                        },
                        {
                            "type": "IPV4_DST",
                            "ip": "10.192.11.48/32"
                        }
                    ]
                }
            },
            {
                "id": "51509924746692974",
                "tableId": "0",
                "appId": "com.wsds.aiwan.uranus.cronus.model.office.impl.OfficeServiceImpl",
                "groupId": 0,
                "priority": 10,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "ADDED",
                "life": 525,
                "packets": 1506,
                "bytes": 456272,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184153583,
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "2"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "IN_PORT",
                            "port": 1
                        }
                    ]
                }
            },
            {
                "id": "51509923795591536",
                "tableId": "0",
                "appId": "com.wsds.aiwan.uranus.cronus.model.office.impl.OfficeServiceImpl",
                "groupId": 0,
                "priority": 500,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "ADDED",
                "life": 1,
                "packets": 0,
                "bytes": 0,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184153583,
                "treatment": {
                    "instructions": [
                        {
                            "type": "EXTENSION",
                            "extension": {
                                "type": "AIWAN_ACTION_PUSH_EX_VXLAN",
                                "ExVxlan": 792702395631964400
                            }
                        },
                        {
                            "type": "EXTENSION",
                            "extension": {
                                "type": "AIWAN_ACTION_PUSH_EX_MPLS",
                                "ExMpls": 1141915775
                            }
                        },
                        {
                            "type": "TABLE",
                            "tableId": "1"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "IN_PORT",
                            "port": 1
                        },
                        {
                            "type": "ETH_TYPE",
                            "ethType": "0x800"
                        },
                        {
                            "type": "IPV4_DST",
                            "ip": "10.192.12.2/32"
                        }
                    ]
                }
            },
            {
                "id": "50384023916421667",
                "tableId": "1",
                "appId": "com.wsds.aiwan.uranus.gaea.service.TopologyManager",
                "groupId": 0,
                "priority": 1100,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "ADDED",
                "life": 525,
                "packets": 66941,
                "bytes": 23302590,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184153583,
                "treatment": {
                    "instructions": [
                        {
                            "type": "OUTPUT",
                            "port": "1"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": [
                        {
                            "type": "EXTENSION"
                        },
                        {
                            "type": "EXTENSION"
                        },
                        {
                            "type": "EXTENSION"
                        }
                    ]
                }
            },
            {
                "id": "52635820675601219",
                "tableId": "0",
                "appId": "com.wsds.aiwan.uranus.gaea.service.FlowSpecProvider",
                "groupId": 0,
                "priority": 1,
                "timeout": 0,
                "isPermanent": True,
                "deviceId": "of:00000000000003ea",
                "state": "ADDED",
                "life": 525,
                "packets": 67578,
                "bytes": 23529362,
                "liveType": "UNKNOWN",
                "lastSeen": 1551184153583,
                "treatment": {
                    "instructions": [
                        {
                            "type": "TABLE",
                            "tableId": "1"
                        }
                    ],
                    "deferred": []
                },
                "selector": {
                    "criteria": []
                }
            }
        ]
    }

ret_site_netlinks = \
    [
        {
            "srcNEId": 1003,
            "dstNEId": 1002,
            "srcIp": "10.192.11.27",
            "srcPort": 831,
            "dstIp": "10.192.10.2",
            "dstPort": 5800
        },
        {
            "srcNEId": 1003,
            "dstNEId": 1004,
            "srcIp": "10.192.11.27",
            "srcPort": 831,
            "dstIp": "10.1.13.2",
            "dstPort": 5800
        },
        {
            "srcNEId": 1003,
            "dstNEId": 1002,
            "srcIp": "10.192.11.27",
            "srcPort": 831,
            "dstIp": "10.192.10.2",
            "dstPort": 5800
        }
    ]

ret_site_tunnels = \
    [
        {
            "tunnelId": 10242,
            "srcCac": 0,
            "srcEac": 0,
            "srcIP": "10.192.11.27",
            "srcPort": 1000,
            "dstNEId": 0,
            "dstCac": 0,
            "dstEac": 0,
            "dstIP": "10.192.10.2",
            "dstPort": 4789,
            "weight": 0.002336
        }, {
            "tunnelId": 36455,
            "srcCac": 0,
            "srcEac": 0,
            "srcIP": "10.192.11.27",
            "srcPort": 1000,
            "dstNEId": 0,
            "dstCac": 0,
            "dstEac": 0,
            "dstIP": "10.1.13.2",
            "dstPort": 4789,
            "weight": 0.002336
        }
    ]

ne_1001_config = \
    {
        "deviceId": 1001,
        "type": "CPE",
        "version": "2.4.0",
        "os": {
            "name": "Linux",
            "version": "#46~16.04.1-Ubuntu SMP Thu May 3 10:06:43 UTC 2018"
        },
        "netconf": {
            "ip": "10.192.12.2",
            "port": 830,
            "username": "netconfuser",
            "password": "1234"
        },
        "portList": [
            {
                "name": "enp1s0f0",
                "mac": "88:66:39:2a:6a:51",
                "ip": "10.192.12.2",
                "type": "WAN",
                "mode": "FIA",
                "pair": "enp1s0f1",
                "isEnabled": True
            },
            {
                "name": "enp1s0f1",
                "mac": "A0:36:9F:85:AB:65",
                "type": "LAN",
                "mode": "FIA",
                "pair": "enp1s0f0",
                "isEnabled": True
            },
            {
                "name": "enp1s0f2",
                "mac": "A0:36:9F:85:AB:66",
                "type": "LAN",
                "mode": "DIA",
                "isEnabled": True
            }
        ]
    }
