def shutdown_if(device_type, interface):
    return {
        'dell_os10': shutdown_interface,
        'huawei': shutdown_interface_huawei
    }[device_type](interface)


def no_shutdown_if(device_type, interface):
    return {
        'dell_os10': no_shutdown_interface,
        'huawei': no_shutdown_interface_huawei
    }[device_type](interface)


def no_shutdown_interface(interface):
    return ['interface {}'.format(interface), 'no shutdown', 'exit']


def shutdown_interface(interface):
    return ['interface {}'.format(interface), 'shutdown', 'exit']


def no_shutdown_interface_huawei(interface):
    return ['interface {}'.format(interface), 'undo shutdown', 'quit']


def shutdown_interface_huawei(interface):
    return ['interface {}'.format(interface), 'shutdown', 'quit']


def change_interface_access_vlan_huawei(interface, vlan):
    return ['interface {}'.format(interface), 'port access vlan {}'.format(vlan), 'quit']


def enable_interface_acl(interface, acl_name):
    return ['interface {}'.format(interface), 'ip access-group {} in'.format(acl_name), 'ip access-group {} out'.format(acl_name), 'quit']


def disable_interface_acl(interface, acl_name):
    return ['interface {}'.format(interface), 'no ip access-group {} in'.format(acl_name), 'no ip access-group {} out'.format(acl_name), 'quit']


def config_if_address(interface, address):
    return ['/ ip address set interface={} address={} netmask=255.255.255.0 numbers=1'.format(interface, address)]


def ping_from_gw(ip):
    return ['ping {}'.format(ip)]


def config_if_speed_limit(interface, speed):
    return ['interface {}'.format(interface),
            'qos car inbound cir {}'.format(speed), 'quit']


def add_route_static(nets, mask, interface, gateway):
    return ['ip route-static {} {} {} {}'.format(nets, mask, interface, gateway),
            'quit']


def delete_route_static(nets, mask, interface, gateway):
    return ['undo ip route-static {} {} {} {}'.format(nets, mask, interface, gateway),
            'quit']


def disable_if_speed_limit(interface):
    return ['interface {}'.format(interface), 'undo qos car inbound', 'quit']


def config_traffic_filter(interface, acl_name):
    return ['interface {}'.format(interface), 'traffic-filter inbound acl name {}'.format(acl_name), 'quit']


def disable_traffic_filter(interface):
    return ['interface {}'.format(interface), 'undo traffic-filter inbound', 'quit']


def config_packet_filter(interface, acl_name):
    return ['interface {}'.format(interface), 'packet-filter name {} inbound'.format(acl_name), 'quit']


def disable_packet_filter(interface, acl_name):
    return ['interface {}'.format(interface), 'undo packet-filter name {} inbound'.format(acl_name), 'quit']


def disable_pppoe_server(if_num):
    return ['/ interface pppoe-server server disable numbers={}'.format(if_num)]


def enable_pppoe_server(if_num):
    return ['/ interface pppoe-server server enable numbers={}'.format(if_num)]


def print_pppoe_server():
    return ['/ interface pppoe-server server print']
