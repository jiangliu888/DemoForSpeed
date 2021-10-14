from erlang.libs.variables import InterfacePathVariables
from base64 import b64encode


def set_host_ip_port(ip, port):
    InterfacePathVariables.HOST = "http://" + ip + ":"
    InterfacePathVariables.URANUS_PORT = port


def set_pontus_ip_port(ip, port):
    InterfacePathVariables.PONTUS_HOST = "http://" + ip + ":"
    InterfacePathVariables.PONTUS_PORT = port


def set_gaea_ip_port(ip, port):
    InterfacePathVariables.GAEA_HOST = "http://" + ip + ":"
    InterfacePathVariables.GAEA_PORT = port


def set_cli_ip_port(cli_ip, cli_port):
    InterfacePathVariables.URANUS_CLI_HOST = cli_ip
    InterfacePathVariables.URANUS_CLI_PORT = cli_port


def set_http_headers(headers):
    InterfacePathVariables.HEADERS = headers


def get_http_uranus_headers(user, password):
    user_and_password = b64encode('{}:{}'.format(user, password)).decode("ascii")
    return {'Content-Type': 'application/json',
            'Authorization': 'Basic {}'.format(user_and_password)}


def get_http_onos_headers(user, password):
    user_and_password = b64encode('{}:{}'.format(user, password)).decode("ascii")
    return {'Accept': 'application/json',
            'Authorization': 'Basic {}'.format(user_and_password)}


def set_ssh_user_password(user, password):
    InterfacePathVariables.URANUS_CLI_USER = user
    InterfacePathVariables.URANUS_CLI_PASSWORD = password


def set_es_ip_port(es_ip, es_port):
    InterfacePathVariables.ES_HOST = "http://" + es_ip + ":"
    InterfacePathVariables.ES_PORT = es_port


def set_insight_ip_port(ip, port):
    InterfacePathVariables.INSIGHT_HOST = "http://" + ip + ":"
    InterfacePathVariables.INSIGHT_PORT = port


def get_http_proxy_headers():
    return {'Content-Type': 'application/json'}


def set_influxdb_ip_port(ip, port):
    InterfacePathVariables.INFLUXDB_HOST = ip
    InterfacePathVariables.INFLUXDB_PORT = port


def set_manager_ip_port(ip, port):
    InterfacePathVariables.MANAGER_HOST = 'http://{}:'.format(ip)
    InterfacePathVariables.MANAGER_PORT = port


def set_alert_ip_port(ip, port):
    InterfacePathVariables.ALERT_HOST = 'http://{}:'.format(ip)
    InterfacePathVariables.ALERT_PORT = port


def set_http_onos_headers(headers):
    InterfacePathVariables.ONOS_HEADERS = headers


def set_onos_ip_port(ip, port):
    InterfacePathVariables.HOST = "http://" + ip + ":"
    InterfacePathVariables.ONOS_PORT = port


def set_consul_ip_port_token(ip, port, token):
    InterfacePathVariables.CONSUL_HOST = 'http://{}:'.format(ip)
    InterfacePathVariables.CONSUL_PORT = port
    InterfacePathVariables.CONSUL_HEADERS = {"X-Consul-Token": token}
