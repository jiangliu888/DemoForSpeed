from erlang.libs.common import JsonUtil
from erlang.libs.common.PontusRequest import PontusRequest


class PontusInterface(object):
    CNF_PATH = "/api/v1/net"
    TUNNEL_CNF_PATH = "/topology/tunnels"
    MEASURE_CONFIG_PATH = '/api/v1/config/routing/algorithm'

    @classmethod
    def get_pop_running_tunnels_from_controller(cls, dev_id):
        rcv = PontusRequest.get(cls.CNF_PATH + cls.TUNNEL_CNF_PATH + '?src=' + str(dev_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_measure_config(cls):
        rcv = PontusRequest.get(cls.MEASURE_CONFIG_PATH)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp
