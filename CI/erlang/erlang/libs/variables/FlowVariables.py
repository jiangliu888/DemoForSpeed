cpe_pass_through_flows = \
    [{'actions': [{'tableId': 1, 'type': 'GOTO_TABLE'}],
      'neId': 20012, 'priority': 1, 'tableId': 0, 'timeout': 0},
     {'actions': [{"pop": True, "type": "POP_EX_LAN"}, {'outPort': 1, 'type': 'OUTPUT'}],
      'matcher': {"exLanId": 1, "exLanIdMask": 15, "exLanMeta": 8, "exLanMetaMask": 8},
      'neId': 20012, 'priority': 1100, 'tableId': 1, 'timeout': 0}]

pop_to_cpe_flows = \
    {u'matcher': {u'dcac': 4, u'deac': 1, u'dstRouteId': 20012, u'dstRouteIdMask': 16777208}, u'neId': 20034,
     u'actions': [{u'outPort': 20005, u'type': u'OUTPUT'}], u'priority': 1100, u'tableId': 1, u'timeout': 0}

pop_to_pop_flows = \
    {u'matcher': {u'dcac': 5, u'deac': 1},
     u'neId': 20034, u'actions': [{u'outPort': 38053, u'type': u'OUTPUT'}], u'priority': 1000, u'tableId': 1, u'timeout': 0}

cpe_office_speedup_flows = \
    [{u'matcher': {u'dstIp': u'10.6.22.1/32', u'inPort': 1, u'ethType': 2048}, u'neId': 20012,
      u'actions': [{u'dstRouteId': 320209, u'header': 0, u'tail': 128, u'type': u'PUSH_EX_VXLAN', u'srcRouteId': 320193},
                   {u'dcac': 6, u'deac': 1, u'scac': 0, u'ttl': 127, u'seac': 0, u'type': u'PUSH_EX_MPLS'}],
      u'priority': 500, u'tableId': 0, u'timeout': 0}]

cpe_nat_dns_to_controller = \
    [{"specId": 50102548204846610,
      "neId": 1001,
      "tableId": 0,
      "priority": 1000,
      "timeout": 0,
      "matcher": {
          "pktType": 1
      },
      "actions": [
          {
              "type": "OUTPUT",
              "outPort": -3
          }]
      }]

cpe_internet_table_0_flows = \
    [{
        "specId": 52917298660191704,
        "neId": 1002,
        "tableId": 0,
        "priority": 200,
        "timeout": 600,
        "matcher": {
            "inPort": 1,
            "ethType": 2048,
            "ipProtocol": 17,
            "dstIp": "192.168.0.8/32"
        },
        "actions": [
            {
                "type": "PUSH_EX_VXLAN",
                "header": 11,
                "tail": 0,
                "srcRouteId": 16033,
                "dstRouteId": 70202
            },
            {
                "type": "PUSH_EX_MPLS",
                "scac": 4,
                "dcac": 4,
                "seac": 4,
                "deac": 4,
                "ttl": 127
            },
            {
                "type": "GOTO_TABLE",
                "tableId": 1
            }
        ]
    },
        {
            "specId": 52917297578227680,
            "neId": 1002,
            "tableId": 0,
            "priority": 200,
            "timeout": 600,
            "matcher": {
                "inPort": 1,
                "ethType": 2048,
                "ipProtocol": 6,
                "dstIp": "192.168.0.8/32"
            },
            "actions": [
                {
                    "type": "PUSH_EX_VXLAN",
                    "header": 11,
                    "tail": 0,
                    "srcRouteId": 16033,
                    "dstRouteId": 70202
                },
                {
                    "type": "PUSH_EX_MPLS",
                    "scac": 4,
                    "dcac": 4,
                    "seac": 4,
                    "deac": 4,
                    "ttl": 127
                },
                {
                    "type": "GOTO_TABLE",
                    "tableId": 1
                }
            ]
        },
        {
            "specId": 52917298318349990,
            "neId": 1002,
            "tableId": 0,
            "priority": 200,
            "timeout": 600,
            "matcher": {
                "inPort": 1,
                "ethType": 2048,
                "ipProtocol": 1,
                "dstIp": "192.168.0.8/32"
            },
            "actions": [
                {
                    "type": "PUSH_EX_VXLAN",
                    "header": 11,
                    "tail": 0,
                    "srcRouteId": 16033,
                    "dstRouteId": 70202
                },
                {
                    "type": "PUSH_EX_MPLS",
                    "scac": 4,
                    "dcac": 4,
                    "seac": 4,
                    "deac": 4,
                    "ttl": 127
                },
                {
                    "type": "GOTO_TABLE",
                    "tableId": 1
                }
            ]
        }]

cpe_to_pop_flows = \
    [{
        "specId": 52354348306089380,
        "neId": 1001,
        "tableId": 1,
        "priority": 2999,
        "timeout": 0,
        "matcher": {
            "dcac": 4,
            "deac": 4
        },
        "actions": [
         {
            "type": "OUTPUT",
            "outPort": 59015
         }
         ]
    }]

cpe_fw_flows = \
    {
        "flows": [{
            "id": "50665498091268670",
            "tableId": "0",
            "appId": "com.wsds.aiwan.uranus.cronus.service.firewall.FirewallManager",
            "groupId": 0,
            "priority": 333,
            "timeout": 0,
            "isPermanent": 'true',
            "deviceId": "of:000000000001b669",
            "state": "ADDED",
            "life": 28,
            "packets": 29,
            "bytes": 2842,
            "liveType": "UNKNOWN",
            "lastSeen": 1548225717483,
            "treatment": {
                "instructions": [{
                    "type": "NOACTION"
                }],
                "deferred": []
            },
            "selector": {
                "criteria": [{
                    "type": "ETH_TYPE",
                    "ethType": "0x800"
                }, {
                    "type": "IP_PROTO",
                    "protocol": 1
                }, {
                    "type": "ICMPV4_TYPE",
                    "icmpType": 0
                }, {
                    "type": "ICMPV4_CODE",
                    "icmpCode": 0
                }]
            }
        }, {
            "id": "50384022008719632",
            "tableId": "1",
            "appId": "com.wsds.aiwan.uranus.gaea.service.TopologyManager",
            "groupId": 0,
            "priority": 1000,
            "timeout": 0,
            "isPermanent": 'true',
            "deviceId": "of:000000000001b669",
            "state": "ADDED",
            "life": 10226,
            "packets": 0,
            "bytes": 0,
            "liveType": "UNKNOWN",
            "lastSeen": 1548225717483,
            "treatment": {
                "instructions": [{
                    "type": "OUTPUT",
                    "port": "1"
                }],
                "deferred": []
            },
            "selector": {
                "criteria": [{
                    "type": "EXTENSION"
                }, {
                    "type": "EXTENSION"
                }, {
                    "type": "EXTENSION"
                }]
            }
        }, {
            "id": "51228447667998448",
            "tableId": "0",
            "appId": "com.wsds.aiwan.uranus.cronus.model.office.impl.OfficeServiceImpl",
            "groupId": 0,
            "priority": 500,
            "timeout": 0,
            "isPermanent": 'true',
            "deviceId": "of:000000000001b669",
            "state": "PENDING_ADD",
            "life": 0,
            "packets": 0,
            "bytes": 0,
            "liveType": "UNKNOWN",
            "lastSeen": 1548225719025,
            "treatment": {
                "instructions": [{
                    "type": "EXTENSION",
                    "extension": {
                        "type": "AIWAN_ACTION_PUSH_EX_VXLAN",
                        "ExVxlan": 800346132204437760
                    }
                }, {
                    "type": "EXTENSION",
                    "extension": {
                        "type": "AIWAN_ACTION_PUSH_EX_MPLS",
                        "ExMpls": 285745279
                    }
                }, {
                    "type": "TABLE",
                    "tableId": "1"
                }],
                "deferred": []
            },
            "selector": {
                "criteria": [{
                    "type": "IN_PORT",
                    "port": 1
                }, {
                    "type": "ETH_TYPE",
                    "ethType": "0x800"
                }, {
                    "type": "IPV4_DST",
                    "ip": "10.192.23.2/32"
                }]
            }
        }]
    }


def cpe_2_cpe_table1_flows(ne_id, tunnels):
    return \
        [{u'matcher': {u'dstRouteId': 64 * int(ne_id) + 1, u'dstRouteIdMask': 16777159}, u'neId': 20012, u'actions': [{u'outPort': tunnels[0], u'type': u'OUTPUT'}], u'priority': 2997, u'tableId': 1, u'timeout': 0},
         {u'matcher': {u'dstRouteId': 64 * int(ne_id) + 1, u'dstRouteIdMask': 16777159}, u'neId': 20012, u'actions': [{u'outPort': tunnels[0], u'type': u'OUTPUT'}], u'priority': 2998, u'tableId': 1, u'timeout': 0},
         {u'matcher': {u'dstRouteId': 64 * int(ne_id) + 2, u'dstRouteIdMask': 16777159}, u'neId': 20012, u'actions': [{u'outPort': tunnels[1], u'type': u'OUTPUT'}], u'priority': 2999, u'tableId': 1, u'timeout': 0},
         {u'matcher': {u'dstRouteId': 64 * int(ne_id) + 2, u'dstRouteIdMask': 16777159}, u'neId': 20012, u'actions': [{u'outPort': tunnels[1], u'type': u'OUTPUT'}], u'priority': 3000, u'tableId': 1, u'timeout': 0}]


def cpe_2_cpe_table1_flows_with_bond(ne_id, bondNumber):
    return \
        {u'matcher': {u'dstRouteId': 64 * int(ne_id), u'dstRouteIdMask': 16777159}, u'neId': 20012, u'actions': [{u"exLanMeta": -104, u"type": "PUSH_EX_LAN"}, {u"exLanId": 17, u"type": "SET_EX_LAN_ID"}, {u'outPort': bondNumber, u'type': u'OUTPUT'}], u'priority': 2997, u'tableId': 1, u'timeout': 0}
