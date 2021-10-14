def method(f, ttl, timestamp, jitter):
    return {
        0: get_loss_0_result,
        1: get_loss_1_result
    }[f](ttl, timestamp, jitter)


def topo(f):
    return {
        'CR20034_Loss_ER20001_tunnels': CR20034_ER20001_Net_links
    }[f]


def get_loss_1_result(ttl, timestamp, jitter):
    return \
        {"max": float(ttl),
         "avg": float(ttl),
         "sdev": float(jitter),
         "loss": 0.2,
         "timestamp": timestamp,
         "delays": [float(ttl) + jitter, float(ttl) - jitter, -1, float(ttl), float(ttl)]}


def get_loss_0_result(ttl, timestamp, jitter):
    return \
        {"max": float(ttl),
         "avg": float(ttl),
         "sdev": float(3 * jitter) / float(4),
         "loss": 0.0,
         "timestamp": timestamp,
         "delays": [float(ttl) + jitter, float(ttl) - jitter, float(ttl), float(ttl), float(ttl)]}


CR20034_ER20001_Net_links = \
    [{'netLink': {"srcNEId": 20034, "dstNEId": 20001, "srcIp": "30.4.1.1", "srcPort": 5801, "dstIp": "20.4.11.1", "dstPort": 5800},
      'jitter': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'loss': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 'ttl': 10},
     {'netLink': {"srcNEId": 20034, "dstNEId": 20001, "srcIp": "30.4.1.2", "srcPort": 5801, "dstIp": "20.4.11.2", "dstPort": 5800},
      'jitter': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'loss': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'ttl': 40},
     {'netLink': {"srcNEId": 20034, "dstNEId": 20001, "srcIp": "30.4.1.2", "srcPort": 5801, "dstIp": "20.4.11.1", "dstPort": 5800},
      'jitter': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'loss': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 'ttl': 20},
     {'netLink': {"srcNEId": 20034, "dstNEId": 20001, "srcIp": "30.4.1.1", "srcPort": 5801, "dstIp": "20.4.11.2", "dstPort": 5800},
      'jitter': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'loss': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 'ttl': 20}]
