import HttpUtil
from erlang.libs.variables import InterfacePathVariables as Template


class PontusRequest(object):

    @classmethod
    def put(cls, path, data):
        return HttpUtil.put("{}{}{}".format(Template.PONTUS_HOST, Template.PONTUS_PORT, path), data, Template.HEADERS)

    @classmethod
    def delete(cls, ref):
        return HttpUtil.delete("{}{}{}".format(Template.PONTUS_HOST, Template.PONTUS_PORT, ref), Template.HEADERS)

    @classmethod
    def get(cls, path):
        return HttpUtil.get("{}{}{}".format(Template.PONTUS_HOST, Template.PONTUS_PORT, path), Template.HEADERS)
