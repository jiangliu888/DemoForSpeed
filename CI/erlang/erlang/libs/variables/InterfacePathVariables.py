HOST = "http://127.0.0.1:"
PONTUS_HOST = "http://127.0.0.1:"
PONTUS_PORT = "6226"
GAEA_HOST = "http://127.0.0.1:"
GAEA_PORT = "6126"
HEADERS = None
URANUS_PORT = "6116"
ONOS_PORT = '8181'
URANUS_SOUTH_PORT = "6116"
ES_HOST = 'http://172.17.0.1:'
ES_PORT = '9200'
URANUS_CLI_HOST = '127.0.0.1'
URANUS_CLI_PORT = "8101"
URANUS_CLI_USER = 'karaf'
URANUS_CLI_PASSWORD = 'karaf'
ES_HEADERS = {"content-type": "application/json"}
ONOS_HEADERS = {'Accept': 'application/json'}
INSIGHT_HOST = "http://10.192.20.18:"
INSIGHT_PORT = "8088"
INSIGHT_HEADERS = {"Content-Type": "application/json;charset=UTF-8"}
INSIGHT_USER = "admin"
INSIGHT_PASSWORD = 'AIRwalk2013!)'
AUTH_HOST = "https://10.192.20.95:"
AUTH_PORT = "8006"
AUDIT_HOST = "https://139.224.41.89:"
AUDIT_PORT = "3080"
AUTH_HEADERS = {"Content-Type": "application/json;charset=UTF-8"}
AUTH_APPID = 'PZL5LHABL001'
AUTH_VERSION = '1.0.1'
AUTH_SECRET = 'jeGJ4TWXmc1ymGDKutHlURNrZI1Hdolz'
INFLUXDB_HOST = '10.192.20.210'
INFLUXDB_PORT = 8086
INFLUXDB_USER = 'root'
INFLUXDB_PASSWORD = 'root'
INFLUXDB_DB = 'aiwan'
MANAGER_HOST = 'http://10.192.20.210:'
MANAGER_PORT = '9103'
PRISM_HOST = 'http://10.192.20.210:'
PRISM_PORT = '8001'
CONSUL_HOST = "http://10.192.20.18:"
CONSUL_PORT = "8500"
CONSUL_HEADERS = {"X-Consul-Token": "9673f18a-6ebc-cab6-e78f-6a343114ef52"}
CONTROLLER_PORT = "9095"
URANUS_HEALTH_PORT = "6061"
AUTHSERVER_PORT = "7000"
FAKE_NE_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VJZCI6Ik9wZW5XcnQiLCJleHAiOjE1OTQ2NzE2MTgsImlhdCI6MTU5NDY2ODAxOH0.BkEq0Ep6wgBFgUXUtBKFNQUKhAq9ePwXdbb6RlKHtLXh2jEwrfK_mTLyBu88O74PuYekOejFR1SZF-liIS08TetF-aHG9srH_SIXde4nlV4HWvfwi7fohemGxdYteXVIAhcswmhKNyQSxEM2X-RYRuocTCUqH_VKM7j-J7tKcwY"

flow_spec = \
    {
        "neId": 1,
        "priority": 1000,
        "tableId": 0,
        "timeout": 0,
        "matcher": {
            "inPort": 1,
            "ethType": 2048,
            "dstIp": "10.192.10.2/32"
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
                "srcDev": 0,
                "dstDev": 0
            },
            {
                "type": "GOTO_TABLE",
                "tableId": 1

            }
        ]
    }

dns_nat_flow_spec = \
    {
        "neId": 11,
        "priority": 1000,
        "tableId": 0,
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

route_flow_spec = \
    {
        "neId": 4387,
        "tableId": 1,
        "priority": 1500,
        "timeout": 0,
        "matcher": {"dcac": 4, "deac": 4, "dstDev": 1001},
        "actions": [{"type": "OUTPUT", "outPort": 3492}]
    }

pass_through_flow_sepc = \
    {'actions': [{'outPort': 4, 'type': 'OUTPUT'}],
     'matcher': {'inPort': 3},
     'neId': 10012,
     'priority': 20,
     'tableId': 0,
     'timeout': 0}

selector_filter = {1: [{"type": "IN_PORT", "port": 1},
                       {"type": "ETH_TYPE", "ethType": "0x800"}],
                   2: [{"type": "IN_PORT", "port": 2},
                       {"type": "ETH_TYPE", "ethType": "0x800"}]}


dns_to_tunnel_flow_spec = \
    {
        "neId": 1,
        "priority": 1000,
        "timeout": 0,
        "matcher": {
            "inPort": 1,
            "ethType": 2048,
            "ipProtocol": 17,
            "dstUdpPort": 53
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
                "srcDev": 0,
                "dstDev": 0
            },
            {
                "type": "GOTO_TABLE",
                "tableId": 1

            }
        ]
    }


def switch_type(ne_type):
    return {
        'CPE': 'cpe',
        'CFP': 'pop',
        'CR': 'pop',
        'ER': 'pop'
    }[ne_type]


pop_flow_spec = \
    {
        "neId": 389,
        "tableId": 1,
        "priority": 1200,
        "timeout": 0,
        "matcher": {
            "dcac": 4,
            "deac": 5
        },
        "actions": [
            {
                "type": "OUTPUT",
                "outPort": 8202
            }
        ]
    }
