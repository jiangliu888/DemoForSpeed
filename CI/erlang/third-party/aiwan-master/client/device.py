from client.rest import RestClient
from core import settings


class DeviceClient(object):
    netconfUrl = "http://"
    openflowUrl = "http://" + settings.OPENFLOW_SWITCH + ":" + "6007"
    switchUrl = "http://" + settings.CONTROLLER_HOST + ":" + "6008"

    @classmethod
    def get_device_config(cls, neId, type):
        ipAndPort = settings.NETCONF_SWITCH[0] if int(neId) < 1000 else settings.NETCONF_SWITCH[1]
        data = {
            'neId': neId,
            'type': type
        }
        res = RestClient.post(cls.netconfUrl + ipAndPort + "/netconf", data)
        if RestClient.ok(res):
            return res.json()
        else:
            return []

    @classmethod
    def create_openflow_device(cls, switchType, neId, ip=settings.CONTROLLER_HOST, port=settings.URANUS_OPENFLOW_PORT):
        data = {}
        data['type'] = switchType
        data['neId'] = neId
        data['ip'] = ip
        data['port'] = port
        res = RestClient.post(cls.openflowUrl + "/api/switch/create", data)
        if RestClient.ok(res):
            return True
        else:
            return False

    @classmethod
    def start_openflow(cls, neId):
        data = {}
        data['neId'] = neId
        res = RestClient.post(cls.openflowUrl + "/api/switch/start", data)
        if RestClient.ok(res):
            return res.json()['result']
        else:
            return False
    
    @classmethod
    def stop_openflow(cls, neId):
        data = {}
        data['neId'] = neId
        res = RestClient.post(cls.openflowUrl + "/api/switch/stop", data)
        if RestClient.ok(res):
            return res.json()['result']
        else:
            return False

    @classmethod
    def start_call_home_dev(cls, neId, netype="CPE"):
        ipAndPort = settings.NETCONF_SWITCH[0] if int(neId) < 1000 else settings.NETCONF_SWITCH[1]
        data = {}
        data["neId"] = neId
        data["type"] = netype
        res = RestClient.post(cls.netconfUrl + ipAndPort + "/callhome/start", data)
        if RestClient.ok(res):
            return res.json()
        else:
            return False

    @classmethod
    def get_routes(cls, neId):
        data = {}
        data['neId'] = neId
        res = RestClient.post(cls.openflowUrl + "/api/switch/routes", data)
        print res
        if RestClient.ok(res):
            return res.json()['result']
        else:
            return []

