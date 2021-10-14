session_request = \
    {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "call",
        "params": [
            "00000000000000000000000000000000",
            "session",
            "login",
            {
                "username": "root",
                "password": "rocks"
            }
        ]
    }

dnsmasq_request = \
    {"jsonrpc": "2.0",
     "id": 3,
     "method": "call",
     "params": ["3cddb1661d0b5ebc937d5b094cc7fa1a",
                "file",
                "write",
                {"path": "/etc/dnsmasq.d/ipset_dnsmasq.conf",
                 "data": "111\n222",
                 "mode": 420}]
     }

dnsmasq_restart = \
    {
        "jsonrpc": "2.0",
        "id": 4,
        "method": "call",
        "params": ["4e06e1ab252168c6312494bc8ad988a3",
                   "file",
                   "exec",
                   {"command": "/etc/init.d/dnsmasq",
                    "params": ["restart"],
                    "env": None}]
    }

dnsmasq_delete = \
    {"jsonrpc": "2.0",
     "id": 3,
     "method": "call",
     "params": ["3cddb1661d0b5ebc937d5b094cc7fa1a",
                "file",
                "remove",
                {"path": "/etc/dnsmasq.d/ipset_dnsmasq.conf"}]
     }

pppoe_set = \
    {"jsonrpc": "2.0",
     "id": 5,
     "method": "call",
     "params": ["3cddb1661d0b5ebc937d5b094cc7fa1a",
                "uci",
                "set",
                {
                    "config": "network",
                    "section": "interface_name",
                    "values": {
                        "username": "123",
                        "proto": "pppoe",
                        "password": "123",
                        "ipv6": "auto"
                    }
                }]
     }

pppoe_add = \
    {
        "jsonrpc": "2.0",
        "id": 627,
        "method": "call",
        "params": [
            "bc7d45e1edcfadfbee493327767d0612",
            "uci",
            "add",
            {
                "config": "network",
                "type": "interface",
                "name": "wan2",
                "values": {
                    "ifname": "eth2",
                    "proto": "pppoe",
                    "username": "123",
                    "password": "123",
                    "ipv6": "auto"
                }
            }
        ]
    }

get_section = \
    {"jsonrpc": "2.0",
     "id": 5,
     "method": "call",
     "params": ["3cddb1661d0b5ebc937d5b094cc7fa1a",
                "uci",
                "get",
                {
                    "config": "network",
                    "section": "ifname",
                }]
     }

dhcp_add = \
    {"jsonrpc": "2.0",
     "id": 8,
     "method": "call",
     "params": ["3cddb1661d0b5ebc937d5b094cc7fa1a",
                "uci",
                "add",
                {
                    "config": "dhcp",
                    "type": "dhcp",
                    "name": "dhcp-server",
                    "values": {
                        "start": 100,
                        "limit": 150,
                        "leasetime": "12h",
                        "serveraddress": "12.1.1.1"
                    }
                }]
     }

staticrt_add = \
    {"jsonrpc": "2.0",
     "id": 11,
     "method": "call",
     "params": ["3cddb1661d0b5ebc937d5b094cc7fa1a",
                "uci",
                "add",
                {
                    "config": "network",
                    "type": "route",
                    "name": "testrt",
                    "values": {
                        "interface": "1234",
                        "target": "13.16.19.1",
                        "netmask": "255.0.0.0",
                        "gateway": "192.168.0.1"
                    }
                }]
     }

acl_add = \
    {"jsonrpc": "2.0",
     "id": 14,
     "method": "call",
     "params": ["3cddb1661d0b5ebc937d5b094cc7fa1a",
                "uci",
                "add",
                {
                    "config": "firewall",
                    "type": "rule",
                    "name": "acl_test",
                    "values": {
                    }
                }]
     }

nat_add = \
    {"jsonrpc": "2.0",
     "id": 17,
     "method": "call",
     "params": ["3cddb1661d0b5ebc937d5b094cc7fa1a",
                "uci",
                "add",
                {
                    "config": "firewall",
                    "type": "redirect",
                    "name": "dnat1",
                    "values": {
                        "target": "DNAT",
                    }

                }]
     }

add_ip_rule = \
    {"jsonrpc": "2.0",
     "id": 3,
     "method": "call",
     "params": ["3cddb1661d0b5ebc937d5b094cc7fa1a",
                "uci",
                "add",
                {"config": "network",
                 "type": "rule",
                 "name": "ipsaas",
                 "values": {"src": "10.184.16.2/32",
                            "lookup": "10"}
                 }]
     }

delete_ip_rule = \
    {"jsonrpc": "2.0",
     "id": 3,
     "method": "call",
     "params": ["3cddb1661d0b5ebc937d5b094cc7fa1a",
                "uci",
                "delete",
                {"config": "network",
                 "type": "rule",
                 "name": "ipsaas"
                 }]
     }
