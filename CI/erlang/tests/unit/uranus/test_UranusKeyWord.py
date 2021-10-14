import mock
import pytest
import json
from mock import call

from erlang.libs.uranus.UranusKeyword import UranusKeyword
from tests.data import Uranus_data


@pytest.mark.parametrize("device_ip, ssh_user, ssh_password, ssh_port, cmd_list, rtn_list, ck",
                         [("10.192.9.10", 'sdn', 'rocks', 22,
                           ['sysrepocfg -f json -X -x /aiwan-config:aiwan-switch/resource/net-measure-tasks//*'],
                           Uranus_data.cli_get_measure_task_netcfg, 2)])
@mock.patch('erlang.libs.uranus.interface.NeCli.SshUtil')
def test_get_device_net_measure_tasks(mock_cli, device_ip, ssh_user, ssh_password, ssh_port, cmd_list, rtn_list, ck):
    instance = mock_cli.return_value
    instance.ssh_cmd_list.return_value = [rtn_list]
    ret = UranusKeyword.get_device_net_measure_tasks(device_ip, ssh_port, ssh_user, ssh_password)
    instance.ssh_cmd_list.assert_called_with(cmd_list)
    assert len(ret) == ck


@pytest.mark.parametrize("cmd_list", [Uranus_data.set_es_ip_cmd])
@mock.patch('erlang.libs.uranus.interface.UranusCli.SshUtil')
def test_set_es_ip_to_controller(mock_cli, cmd_list):
    instance = mock_cli.return_value
    UranusKeyword.set_es_ip_to_controller()
    instance.ssh_cmd_list.assert_called_with(cmd_list)


@pytest.mark.parametrize("cmd_list2", [Uranus_data.set_manage_feq_cmd])
@mock.patch('erlang.libs.uranus.interface.UranusCli.SshUtil')
def test_set_measure_polling_freq_to_controller(mock_cli, cmd_list2):
    instance = mock_cli.return_value
    UranusKeyword.set_measure_polling_freq_to_controller('10')
    calls = [call(cmd_list2)]
    instance.ssh_cmd_list.assert_has_calls(calls)


@pytest.mark.parametrize("ne_id, tunnel, timestamp, mi, mx, avg, sdev, loss, payload",
                         [("89", Uranus_data.tunnel, 1542848545953, [0, 1], [0, 1], [0, 1], [0, 0],
                           0, Uranus_data.measure_task_result)])
@mock.patch('erlang.libs.uranus.interface.EsInterface.EsRequest')
def test_check_devices_measure_result(mock_request, ne_id, tunnel, timestamp, mi, mx, avg, sdev, loss, payload):
    mock_request.get.return_value.status_code = 200
    mock_request.get.return_value.content = json.dumps(payload)
    UranusKeyword.check_devices_measure_result(ne_id, tunnel, timestamp, mi, mx, avg, sdev, loss)


@pytest.mark.parametrize("cmd_list1", [Uranus_data.set_cr_area_select_delay])
@mock.patch('erlang.libs.uranus.interface.UranusCli.SshUtil')
def test_set_cr_area_select_delay(mock_cli, cmd_list1):
    instance = mock_cli.return_value
    UranusKeyword.set_cr_area_select_delay('10000')
    instance.ssh_cmd_list.assert_called_with(cmd_list1)


@pytest.mark.parametrize("device_ip, ssh_user, ssh_password, ssh_port, cmd_list, rtn_list, ck",
                         [("10.192.9.10", 'sdn', 'rocks', 22,
                           ['sysrepocfg -f json -X -x /aiwan-config:aiwan-switch/resource/ports//*'],
                           Uranus_data.cli_get_ports_netcfg, 1)])
@mock.patch('erlang.libs.uranus.interface.NeCli.SshUtil')
def test_get_ports_from_ne_side(mock_cli, device_ip, ssh_user, ssh_password, ssh_port, cmd_list, rtn_list, ck):
    instance = mock_cli.return_value
    instance.ssh_cmd_list.return_value = [rtn_list]
    ret = UranusKeyword.get_device_port_from_ne(device_ip, ssh_port, ssh_user, ssh_password)
    instance.ssh_cmd_list.assert_called_with(cmd_list)
    assert len(ret) == ck


@pytest.mark.parametrize("old_ip, new_ip, tunnels, ret_tunnels",
                         [('10.5.23.1', '9.5.23.1', Uranus_data.Test_Add_CPE10014_IN_ER10002_tunnels,
                           Uranus_data.Ret_Add_CPE10014_IN_ER10002_tunnels)])
def test_change_ne_ip(old_ip, new_ip, tunnels, ret_tunnels):
    ret = UranusKeyword.change_ne_ip(old_ip, new_ip, tunnels)
    assert ret == ret_tunnels
    assert tunnels != ret_tunnels


@pytest.mark.parametrize("cmd_list1, interval_time",
                         [(Uranus_data.set_flow_poll_frequency, 5)])
@mock.patch('erlang.libs.uranus.interface.UranusCli.SshUtil')
def test_set_flow_poll_frequency(mock_cli, cmd_list1, interval_time):
    instance = mock_cli.return_value
    UranusKeyword.set_flow_poll_frequency(interval_time)
    instance.ssh_cmd_list.assert_called_with(cmd_list1)


@pytest.mark.parametrize("device_ip, ssh_user, ssh_password, ssh_port, cmd_list, rtn_list, ck",
                         [("10.192.9.10", 'sdn', 'rocks', 22,
                           ['sysrepocfg -f json -X -x /aiwan-config:aiwan-switch/resource/net-measure-tasks//*'],
                           Uranus_data.cli_get_measure_task_config, 2)])
@mock.patch('erlang.libs.uranus.interface.NeCli.SshUtil')
def test_get_device_net_measure_config(mock_cli, device_ip, ssh_user, ssh_password, ssh_port, cmd_list, rtn_list, ck):
    instance = mock_cli.return_value
    instance.ssh_cmd_list.return_value = [rtn_list]
    ret = UranusKeyword.get_device_net_measure_config(device_ip, ssh_port, ssh_user, ssh_password)
    instance.ssh_cmd_list.assert_called_with(cmd_list)
    assert len(ret) == ck
