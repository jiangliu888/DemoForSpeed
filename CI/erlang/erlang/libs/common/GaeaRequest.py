import HttpUtil
from erlang.libs.variables import InterfacePathVariables as Template


class GaeaRequest(object):

    @classmethod
    def put(cls, path, data):
        return HttpUtil.put("{}{}{}".format(Template.GAEA_HOST, Template.GAEA_PORT, path), data, Template.HEADERS)

    @classmethod
    def delete(cls, ref):
        return HttpUtil.delete("{}{}{}".format(Template.GAEA_HOST, Template.GAEA_PORT, ref), Template.HEADERS)

    @classmethod
    def get(cls, path):
        return HttpUtil.get("{}{}{}".format(Template.GAEA_HOST, Template.GAEA_PORT, path), Template.HEADERS)
