import mock
import pytest


from erlang.libs.manager.ManagerKeyword import ManagerKeyword
from tests.data import Manager_data


@pytest.mark.parametrize("ne_id, task_id, b_time, e_time, query_result",
                         [('1021', '11', 1557739990, 1557740118, Manager_data.measure_result)])
@mock.patch('erlang.libs.manager.interface.ManagerInterface.InfluxdbUtil')
def test_get_ne_measure_result_counters_with_task(mock_influxdb, ne_id, task_id, b_time, e_time, query_result):
    instance = mock_influxdb.return_value
    instance.query.return_value = query_result
    ret = ManagerKeyword.get_ne_measure_result_counters_with_task(ne_id, task_id, b_time, e_time)
    assert ret == 60


@pytest.mark.parametrize("ne_id, metric_name, metrics_result",
                         [('503', 'version', Manager_data.metrics_result)])
@mock.patch('erlang.libs.manager.interface.ManagerInterface.ManagerInterface.get_metrics_with_lable')
def test_get_ne_metric_value(mock_request, ne_id, metric_name, metrics_result):
    mock_request.return_value = metrics_result
    ret = ManagerKeyword.get_ne_metric_value(ne_id, metric_name)
    assert ret == 3997892608.0
