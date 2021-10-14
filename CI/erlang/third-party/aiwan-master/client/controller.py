from client.rest import RestClient
from core import settings
import time
from infrastructure.logger import Logger
from client.consulClient import ConsulClient
from core.gneId import GNeId


class ControllerClient(object):
    southUrl = "http://" + settings.CONTROLLER_HOST + ":" + str(settings.GAEA_SOUTH_API_PORT)
    uranusUrl = "http://" + settings.CONTROLLER_HOST + ":" + "8181"
    netconfDevice = "http://" + settings.CONTROLLER_HOST + ":" + "6006"

    @classmethod
    def register(cls, data, type, neId, token=None):
        res = RestClient.post(cls.southUrl + "/api/v1/ne/" + type + "/" + neId, data, token)
        return RestClient.ok(res)

    @classmethod
    def register_saas_proxy(cls, saas_service_id, proxy):
        res = RestClient.post(cls.southUrl + "/api/v1/ne/service/proxy/" + str(saas_service_id), proxy)
        if RestClient.ok(res):
            return res.json()
        else:
            return {}

    @classmethod
    def register_anycast_proxy(cls, anycast_service_id, anycast):
        res = RestClient.post(cls.southUrl + "/api/v1/ne/service/anycast/" + str(anycast_service_id), anycast)
        if RestClient.ok(res):
            return res.json()
        else:
            return {}
