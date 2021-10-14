from prometheus_client.parser import text_string_to_metric_families
from erlang.libs.common import JsonUtil
from erlang.libs.common import HttpUtil
from erlang.libs.common.InfluxdbUtil import InfluxdbUtil
from erlang.libs.common.ManagerRequest import ManagerRequest
from erlang.libs.variables import InterfacePathVariables as Temple


class ManagerInterface(object):
    Measure_Counter_Sql = "SELECT COUNT(value) FROM TaskResult WHERE time >= {}s AND time < {}s AND DeviceId = '{}' AND TaskId = '{}' GROUP BY time(1m)"
    Measure_Value_Sql = "SELECT value FROM TaskResult WHERE time >= {}s AND time < {}s AND DeviceId = '{}' AND TaskId = '{}'"
    METRICS = '/metrics'

    @classmethod
    def get_ne_measure_result_counter_with_task_id(cls, ne_id, task_id, b_time, e_time):
        influx_c = InfluxdbUtil(Temple.INFLUXDB_HOST, Temple.INFLUXDB_PORT, Temple.INFLUXDB_USER,
                                Temple.INFLUXDB_PASSWORD, Temple.INFLUXDB_DB)
        return list(influx_c.query(cls.Measure_Counter_Sql.format(b_time, e_time, ne_id, task_id)))

    @classmethod
    def get_metrics_with_lable(cls, ne_id, metric_name):
        metrics = ManagerRequest.get("device/{}".format(ne_id)).content
        print map(lambda x: x.name, text_string_to_metric_families(metrics))
        samples = filter(lambda x: x.name == metric_name, text_string_to_metric_families(metrics))[0].samples
        print map(lambda x: {'labels': x.labels, 'value': x.value}, samples)
        return map(lambda x: {'labels': x.labels, 'value': x.value}, samples)

    @classmethod
    def get_ne_measure_result_value_with_task_id(cls, ne_id, task_id, b_time, e_time):
        influx_c = InfluxdbUtil(Temple.INFLUXDB_HOST, Temple.INFLUXDB_PORT, Temple.INFLUXDB_USER,
                                Temple.INFLUXDB_PASSWORD, Temple.INFLUXDB_DB)
        return list(influx_c.query(cls.Measure_Value_Sql.format(b_time, e_time, ne_id, task_id)))
