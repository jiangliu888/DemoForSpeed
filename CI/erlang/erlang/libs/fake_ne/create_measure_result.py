import time
import sys
import requests
from influxdb import InfluxDBClient
import datetime
from interface.FakeNeKeyword import FakeNeKeyword


class InfluxClient(object):
    def __init__(self):
        self.client = InfluxDBClient('127.0.0.1', '8086', timeout=10)
        print('use database aiwan')
        self.client.create_database('aiwan')
        self.client.switch_database('aiwan')

    def write_measure_data(self, delays, task_info, tunnel):
        measure_data = self.gene_data_to_influx(delays, task_info, tunnel)
        self.client.write_points(measure_data)

    def gene_data_to_influx(self, delays, task_info, tunnel):
        measure_datas = []
        for delay in delays:
            for i in range(30):
                measure_data = {
                    "measurement": "TaskResult",
                    "tags": {
                        "DeviceId": task_info["neId"],
                        "LocalId": task_info["neId"],
                        "LocalIp": tunnel["srcIp"],
                        "RemoteId": task_info["dstNeId"],
                        "RemoteIp": tunnel["dstIp"],
                        "TaskId": task_info['id'],
                    },
                    "time": datetime.datetime.utcnow().isoformat("T"),
                    "fields": {
                        "value": delay
                    },
                }
                measure_datas.append(measure_data)
        return measure_datas


class NetConfClient(object):
    def __init__(self, neid):
        self.neid = neid

    def __del__(self):
        self.neid = None

    def get_measure_tasks(self):
        return FakeNeKeyword.get_fake_ne_measure_tasks(self.neid)

    def get_tunnels(self):
        return FakeNeKeyword.get_fake_ne_measure_tunnels(self.neid)

    def get_tunnel_by_task(self, task):
        tunnels = self.get_tunnels()
        return filter(lambda x: x["portNumber"] == task["tunnelNumber"], tunnels)

    def close(self):
        pass


if __name__ == "__main__":
    input_arg = sys.argv[1:]
    is_cpe = 1 if input_arg[0] != "measure" else 0
    neid = int(input_arg[1]) >> 4
    jitter = map(int, input_arg[2:6]) if len(input_arg) > 2 else [0, 0, 0, 0]
    loss = map(int, input_arg[6:10]) if len(input_arg) > 6 else [0, 0, 0, 0]
    delay = map(int, input_arg[10:14]) if len(input_arg) > 10 else [0, 0, 0, 0]
    loss_target = map(int, input_arg[14:]) if len(input_arg) > 14 else None
    fakeneClient = NetConfClient(neid)
    influxClient = InfluxClient()
    print 'jitter is {}'.format(str(jitter))
    print 'delay  is {}'.format(str(delay))
    print 'loss is {}'.format(str(loss))
    print 'loss_target is {}'.format(str(loss_target))
    while True:
        tasks = fakeneClient.get_measure_tasks()
        if tasks:
            for task in tasks:
                print 'task is {}'.format(task)
                print 'tunnel number is {}'.format(task["tunnelNumber"])
                print 'time {} to check tunnel by tasks : '.format(datetime.datetime.utcnow())
                tunnel = fakeneClient.get_tunnel_by_task(task)
                if not tunnel:
                    print 'due to tunnel is null. do not generate task result--------------'
                else:
                    remote_ip_address = tunnel[0]['dstIp']
                    local_ip_address = input_arg[0] if (tunnel[0]['srcIp'] == "0.0.0.0" or "169.254" in tunnel[0]['srcIp']) else tunnel[0]['srcIp']
                    local_cac = int(local_ip_address.split('.')[1])
                    local_eac = int(local_ip_address.split('.')[2])
                    not_cr = (local_eac != 1)
                    remote_cac = int(remote_ip_address.split('.')[1])
                    remote_eac = int(remote_ip_address.split('.')[2])
                    local_port = int(local_ip_address.split('.')[3])
                    remote_port = int(remote_ip_address.split('.')[3])
                    port_inf = 0.5 if local_port < remote_port else 0
                    port_jitter = int(jitter[remote_port - 1]) * remote_port
                    port_loss = int(loss[remote_port - 1])
                    result = int((local_port * remote_port - port_inf + abs(local_cac - remote_cac) * 5 * int(not_cr) + abs(local_eac - remote_eac) * int(is_cpe)) * 10)
                    print 'local_ip is {}'.format(local_ip_address)
                    print 'remote_ip is {}'.format(remote_ip_address)
                    print 'result is {}'.format(result)
                    if loss_target:
                        if remote_cac in loss_target:
                            target_index = loss_target.index(remote_cac)
                            target_delay = int(delay[target_index])
                            measure_result = [(result + port_jitter + target_delay) * 1000, (result - port_jitter + target_delay) * 1000,
                                              (result + port_jitter + target_delay) * 1000,
                                              (result - port_jitter + target_delay) * 1000, result * 1000 if port_loss == 0 else -1]
                        else:
                            measure_result = [result * 1000, result * 1000, result * 1000, result * 1000, result * 1000]
                    else:
                        measure_result = [(result + port_jitter) * 1000, (result - port_jitter) * 1000, (result + port_jitter) * 1000,
                                          (result - port_jitter) * 1000, result * 1000 if port_loss == 0 else -1]
                    print 'measure_result is {}'.format(str(measure_result))
                    influxClient.write_measure_data(measure_result, task, tunnel[0])
        time.sleep(2)
