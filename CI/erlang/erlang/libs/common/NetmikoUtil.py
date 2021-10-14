from netmiko import ConnectHandler
from netmiko import Netmiko


class NetmikoUtil(object):
    def __init__(self, device_type, host_ip, port, user, password):
        self.config = {
            'device_type': device_type,
            'ip': host_ip,
            'username': user,
            'password': password,
            'port': int(port),  # optional, defaults to 22
            'secret': '',  # optional, defaults to ''
            'verbose': False,  # optional, defaults to False
        }
        self.net_connect = ConnectHandler(**self.config)

    def send_config_cmd_list(self, cmd_list):
        return self.net_connect.send_config_set(cmd_list)

    def net_connect_close(self):
        self.net_connect.disconnect()

    def get_device_type(self):
        return self.config['device_type']


class NetmikoTelnet(object):
    def __init__(self, device_type, host_ip, user, password):
        self.config = {
            'device_type': device_type,
            'host': host_ip,
            'username': user,
            'password': password
        }
        self.net_connect = Netmiko(**self.config)

    def send_config_cmd_list(self, cmd_list):
        return self.net_connect.send_config_set(cmd_list)

    def net_connect_close(self):
        self.net_connect.disconnect()

    def get_device_type(self):
        return self.config['device_type']
