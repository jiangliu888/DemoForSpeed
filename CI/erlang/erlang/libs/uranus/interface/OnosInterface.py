from erlang.libs.common import JsonUtil
from erlang.libs.common.OnosRequest import OnosRequest


class OnosInterface(object):
    V1_PATH = "/onos/v1"
    FLOWS_PATH = "/flows"
    DEVICE_PATH = "/devices"
    FLOW_SPEC_PATH = "/api/v1/flow/flowSpec"
    CNF_PATH = '/api/v1/ne'
    NETCONF_CONFIG = '/netconf/config'

    @classmethod
    def get_flows(cls):
        rcv = OnosRequest.get(cls.V1_PATH + cls.FLOWS_PATH)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_devices(cls):
        rcv = OnosRequest.get(cls.V1_PATH + cls.DEVICE_PATH)
        print rcv.content
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_device_flow(cls, device_id):
        rcv = OnosRequest.get(cls.V1_PATH + cls.FLOWS_PATH + '/' + device_id.replace(':', '%3A'))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_device_with_id(cls, device_id):
        rcv = OnosRequest.get(cls.V1_PATH + cls.DEVICE_PATH + '/' + device_id.replace(':', '%3A'))
        print rcv.content
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_device_flow_by_flow_id(cls, device_id, flow_id):
        rcv = OnosRequest.get(cls.V1_PATH + cls.FLOWS_PATH + '/' + device_id.replace(':', '%3A') + '/' + str(flow_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def post_cpe_flow_spec(cls, body):
        rcv = OnosRequest.post(cls.FLOW_SPEC_PATH + '/create', JsonUtil.dump_json(body))
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def delete_cpe_flow_spe(cls, body):
        rcv = OnosRequest.post(cls.FLOW_SPEC_PATH + '/remove', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_ne_netconf_config(cls, ne_id):
        rcv = OnosRequest.get(cls.CNF_PATH + '/' + str(ne_id) + cls.NETCONF_CONFIG)
        return rcv.status_code, rcv.content
