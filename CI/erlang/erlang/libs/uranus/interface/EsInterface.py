import time

from erlang.libs.common import JsonUtil
from erlang.libs.common.EsRequest import EsRequest
from erlang.libs.variables import MeasureResultVariables


class EsInterface(object):
    MEAURE_PATH = "/netmeasure"

    @classmethod
    def get_ne_measure_result(cls, ne_id):
        rcv = EsRequest.get(cls.MEAURE_PATH + time.strftime("%Y-%m-%d", time.localtime()) + '/{}/_search'.format(ne_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_ne_tunnel_measure_result(cls, ne_id, src_ip, dst_ip, timestamp):
        t_now = int(time.time() * 1000 * 1000)
        data = \
            {"query":
                {"bool":
                    {"must": [
                        {"match": {"srcNEId": ne_id}},
                        {"match": {"dstIp": dst_ip}},
                        {"match": {"srcIp": src_ip}},
                        {"range": {"timestamp": {"from": timestamp, "to": t_now}}
                         }
                    ]
                    }}}
        d = JsonUtil.dump_json(data)
        url = cls.MEAURE_PATH + '_' + time.strftime("%Y-%m-%d", time.localtime()) + '/_search?pretty'
        rcv = EsRequest.get(url, d)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_ne_all_measure_result(cls, ne_id, timestamp):
        t_now = int(time.time() * 1000 * 1000)
        data = \
            {"query":
                {"bool":
                    {"must": [
                        {"match": {"srcNEId": ne_id}},
                        {"range": {"timestamp": {"from": timestamp, "to": t_now}}
                         }
                    ]
                    }}}
        d = JsonUtil.dump_json(data)
        url = cls.MEAURE_PATH + '_' + time.strftime("%Y-%m-%d", time.localtime()) + '/_search?pretty'
        rcv = EsRequest.get(url, d)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def bulk_insert_12_measure_results(cls, net_link, ttl, jitter, loss):
        bulk_body = ''
        t_now = int(time.time() * 1000 * 1000)
        for i in range(12):
            t = t_now - i * 5 * 1000 * 1000
            bulk_body += '{"index":{}}\n'
            bulk_body += JsonUtil.dump_json(net_link).replace('}', '') + ', ' + JsonUtil.dump_json(MeasureResultVariables.method(loss[i], ttl, t, jitter[i])).replace('{', '') + '\n'

        url = cls.MEAURE_PATH + '_' + time.strftime("%Y-%m-%d", time.localtime()) + '/netmeasure/_bulk'
        rcv = EsRequest.post(url, bulk_body)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def bulk_delete_1day_measure_result(cls):
        data = \
            {
                "query": {
                    "match_all": {}
                }
            }
        d = JsonUtil.dump_json(data)
        url = cls.MEAURE_PATH + '_' + time.strftime("%Y-%m-%d", time.localtime()) + '/netmeasure/_delete_by_query'
        rcv = EsRequest.post(url, d)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp
