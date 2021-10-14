from erlang.libs.common.NetmikoUtil import NetmikoUtil
from erlang.libs.common.NetmikoUtil import NetmikoTelnet
from erlang.libs.variables import SwitchVariable


class SwitchKeyword(object):
    connect_list = {}
    telnet_list = {}
    current_connect = ''

    def __init__(self):
        pass

    @staticmethod
    def connect_switch(device_type, host_ip, port, user, password):
        connect_index = '{}_{}_{}'.format(device_type, host_ip, port)
        SwitchKeyword.connect_list[connect_index] = NetmikoUtil(device_type, host_ip, port, user, password)
        return connect_index

    @staticmethod
    def no_shutdown_interface(connect_index, interface):
        device_type = SwitchKeyword.connect_list[connect_index].get_device_type()
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.no_shutdown_if(device_type, interface))

    @staticmethod
    def shutdown_interface(connect_index, interface):
        device_type = SwitchKeyword.connect_list[connect_index].get_device_type()
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.shutdown_if(device_type, interface))

    @staticmethod
    def change_interface_access_vlan(connect_index, interface, vlan):
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.change_interface_access_vlan_huawei(interface, vlan))

    @staticmethod
    def close_all_connect():
        map(lambda x: SwitchKeyword.connect_list[x].net_connect_close(), SwitchKeyword.connect_list.keys())

    @staticmethod
    def close_connect(connect_index):
        SwitchKeyword.connect_list[connect_index].net_connect_close()

    @staticmethod
    def enable_interface_acl(connect_index, interface, acl_name):
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.enable_interface_acl(interface, acl_name))

    @staticmethod
    def disable_interface_acl(connect_index, interface, acl_name):
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.disable_interface_acl(interface, acl_name))

    @staticmethod
    def config_interface_address(connect_index, interface, address):
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.config_if_address(interface, address))

    @staticmethod
    def telnet_switch(device_type, host_ip, user, password):
        connect_index = '{}_{}_{}'.format(device_type, host_ip, 21)
        SwitchKeyword.telnet_list[connect_index] = NetmikoTelnet(device_type, host_ip, user, password)
        return connect_index

    @staticmethod
    def close_all_telnet_connect():
        map(lambda x: SwitchKeyword.telnet_list[x].net_connect_close(), SwitchKeyword.telnet_list.keys())

    @staticmethod
    def port_speed_limit(connect_index, interface, speed):
        return SwitchKeyword.telnet_list[connect_index].send_config_cmd_list(SwitchVariable.config_if_speed_limit(interface, speed))

    @staticmethod
    def add_route_static(connect_index, nets, mask, interface, gateway):
        return SwitchKeyword.telnet_list[connect_index].send_config_cmd_list(SwitchVariable.add_route_static(nets, mask, interface, gateway))

    @staticmethod
    def delete_route_static(connect_index, nets, mask, interface, gateway):
        return SwitchKeyword.telnet_list[connect_index].send_config_cmd_list(SwitchVariable.delete_route_static(nets, mask, interface, gateway))

    @staticmethod
    def ping_from_gw(connect_index, peer_ip):
        return SwitchKeyword.telnet_list[connect_index].send_config_cmd_list(SwitchVariable.ping_from_gw(peer_ip))

    @staticmethod
    def disable_port_speed_limit(connect_index, interface):
        return SwitchKeyword.telnet_list[connect_index].send_config_cmd_list(
            SwitchVariable.disable_if_speed_limit(interface))

    @staticmethod
    def port_traffic_filter(connect_index, interface, acl_name):
        return SwitchKeyword.telnet_list[connect_index].send_config_cmd_list(SwitchVariable.config_traffic_filter(interface, acl_name))

    @staticmethod
    def disable_port_traffic_filter(connect_index, interface):
        return SwitchKeyword.telnet_list[connect_index].send_config_cmd_list(SwitchVariable.disable_traffic_filter(interface))

    @staticmethod
    def port_packet_filter(connect_index, interface, acl_name):
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.config_packet_filter(interface, acl_name))

    @staticmethod
    def disable_port_packet_filter(connect_index, interface, acl_name):
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.disable_packet_filter(interface, acl_name))

    @staticmethod
    def disable_pppoe_server(connect_index, num):
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.disable_pppoe_server(num))

    @staticmethod
    def enable_pppoe_server(connect_index, num):
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.enable_pppoe_server(num))

    @staticmethod
    def print_pppoe_server(connect_index):
        return SwitchKeyword.connect_list[connect_index].send_config_cmd_list(SwitchVariable.print_pppoe_server())

    @staticmethod
    def no_shutdown_interface_telnet(connect_index, interface):
        return SwitchKeyword.telnet_list[connect_index].send_config_cmd_list(SwitchVariable.no_shutdown_if('huawei', interface))

    @staticmethod
    def shutdown_interface_telnet(connect_index, interface):
        return SwitchKeyword.telnet_list[connect_index].send_config_cmd_list(SwitchVariable.shutdown_if('huawei', interface))
