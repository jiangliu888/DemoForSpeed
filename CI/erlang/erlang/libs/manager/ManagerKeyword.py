import time
import json
import re
import copy
from datetime import datetime
from datetime import timedelta
from erlang.libs.manager.interface.ManagerInterface import ManagerInterface
from erlang.libs.common.InfluxdbUtil import InfluxdbUtil
from erlang.libs.variables import OpenwrtConfigVariable


class ManagerKeyword(object):
    def __init__(self):
        pass

    @staticmethod
    def get_ne_measure_result_counters_with_task(ne_id, task_id, b_time, e_time):
        ret = ManagerInterface.get_ne_measure_result_counter_with_task_id(ne_id, task_id, b_time, e_time)
        print ret
        return sum(map(lambda x: x['count'], ret[0]))

    @staticmethod
    def check_ne_measure_result_counters_with_task(ne_id, task_id, b_time, t_now):
        ret = ManagerKeyword.get_ne_measure_result_counters_with_task(ne_id, task_id, b_time, t_now)
        print ret
        print '{},expect{}'.format(ret, (t_now - b_time))
        assert ret in range((t_now - b_time) - 1, (t_now - b_time) + 2)

    @staticmethod
    def get_ne_metric_value(ne_id, metric_name, lable_names=[], lable_values=[]):
        samples = ManagerInterface.get_metrics_with_lable(ne_id, metric_name)
        for i in range(len(lable_names)):
            samples = filter(lambda x: x['labels'][lable_names[i]] == str(lable_values[i]), samples)
        return samples[0]['value']

    @staticmethod
    def get_ne_measure_result_value_with_task(ne_id, task_id, b_time, e_time=None):
        end_time = e_time if e_time else int(time.time())
        ret = ManagerInterface.get_ne_measure_result_value_with_task_id(ne_id, task_id, b_time, end_time)
        print ret
        return map(lambda x: x['value'], ret[0])

    @staticmethod
    def clean_measureData(ip, port):
        influx_c = InfluxdbUtil(ip, port, None, None, 'aiwan')
        res = influx_c.dropMeasurement('TaskResult')
        print res
