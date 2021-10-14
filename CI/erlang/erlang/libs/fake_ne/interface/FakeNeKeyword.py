import os
from client.device import DeviceClient
from erlang.libs.uranus.interface.EsInterface import EsInterface
from erlang.libs.uranus.interface.UranusInterface import UranusInterface
from erlang.libs.variables import MeasureResultVariables


class FakeNeKeyword(object):
    DB_PORT = 3000
    DB_REST_PORT = 3500
    OFP_REST_PORT = 4000
    fake_ne_list = {}

    def __init__(self):
        pass

    @staticmethod
    def get_fake_ne_measure_tunnels(neid):
        return DeviceClient.get_device_config(int(neid), "TUNNEL")

    @staticmethod
    def get_fake_ne_measure_tasks(neid):
        return DeviceClient.get_device_config(int(neid), "MEASURE")

    @staticmethod
    def get_fake_ne_measure_task_with_address(ne_id, local_ip, remote_ip):
        tasks = FakeNeKeyword.get_fake_ne_measure_tasks(ne_id)
        print tasks
        return filter(lambda x: (x["remote-ipv4-address"] == remote_ip) and (x["local-ipv4-address"] == local_ip), tasks)

    @staticmethod
    def get_fake_ne_tunnels_with_dstNeId(local_NeId, dstNeId):
        s_id = int(local_NeId) >> 4
        tunnels = FakeNeKeyword.get_fake_ne_measure_tunnels(s_id)
        print tunnels
        return filter(lambda x: x["dst"] == dstNeId, tunnels)

    @staticmethod
    def get_fake_ne_measure_tasks_with_dstNeId(local_NeId, dstNeId):
        s_id = int(local_NeId) >> 4
        tasks = FakeNeKeyword.get_fake_ne_measure_tasks(s_id)
        print tasks
        return filter(lambda x: x["dstNeId"] == dstNeId, tasks)

    @staticmethod
    def get_fake_ne_flows_id(ne_id):
        res = DeviceClient.get_routes(int(ne_id))
        return map(int, res) if res else []

    @staticmethod
    def change_ne_link_measure_result(ne_id, jitter, loss, delay=[0, 0, 0, 0], loss_target=[]):
        cmd = "ps -ef |grep create_measure|grep {} |awk {}".format(ne_id, r"'{print $10}'")
        r = os.popen(cmd)
        info = r.read().split('\n')[0]
        print 'info is {}'.format(info)
        cmd = "ps -ef |grep create_measure|grep {} |awk {}|xargs sudo kill -9".format(ne_id, r"'{print $2}'")
        ret = os.system(cmd)
        print 'cmd is {} and ret is {}'.format(cmd, ret)
        cmd = "sh -c 'python erlang/libs/fake_ne/create_measure_result.py {} {} {} {} {} {} >> logs/{}measure.log &'".format(info, int(ne_id), ' '.join(jitter), ' '.join(loss), ' '.join(delay), ' '.join(loss_target), int(ne_id))
        print cmd
        ret = os.system(cmd)
        assert ret == 0

    @staticmethod
    def export_data_to_es(topo_name):
        for es_data in MeasureResultVariables.topo(topo_name):
            EsInterface.bulk_insert_12_measure_results(es_data['netLink'], es_data['ttl'], es_data['jitter'], es_data['loss'])

    @staticmethod
    def get_fake_ne_type(ne_id):
        rec, ne_info = UranusInterface.get_netcfg_ne_config_with_id(ne_id)
        ne_type = ne_info["type"]
        return ne_type
