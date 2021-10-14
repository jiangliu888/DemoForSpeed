import HttpUtil
from erlang.libs.variables import InterfacePathVariables as Template


class OnosRequest(object):

    @classmethod
    def post(cls, path, data):
        return HttpUtil.post("{}{}{}".format(Template.HOST, Template.ONOS_PORT, path), data, Template.ONOS_HEADERS)

    @classmethod
    def put(cls, path, data):
        return HttpUtil.put("{}{}{}".format(Template.HOST, Template.ONOS_PORT, path), data, Template.ONOS_HEADERS)

    @classmethod
    def delete(cls, ref):
        return HttpUtil.delete("{}{}{}".format(Template.HOST, Template.ONOS_PORT, ref), Template.ONOS_HEADERS)

    @classmethod
    def get(cls, path, data=""):
        return HttpUtil.get("{}{}{}".format(Template.HOST, Template.ONOS_PORT, path), Template.ONOS_HEADERS, data)
