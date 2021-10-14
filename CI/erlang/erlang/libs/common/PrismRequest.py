import HttpUtil
from erlang.libs.variables import InterfacePathVariables as Template


class PrismRequest(object):

    @classmethod
    def post(cls, path, data):
        return HttpUtil.post("{}{}{}".format(Template.PRISM_HOST, Template.PRISM_HOST, path), data, Template.HEADERS)

    @classmethod
    def put(cls, path, data):
        return HttpUtil.put("{}{}{}".format(Template.PRISM_HOST, Template.PRISM_PORT, path), data, Template.HEADERS)

    @classmethod
    def delete(cls, ref):
        return HttpUtil.delete("{}{}{}".format(Template.PRISM_HOST, Template.PRISM_PORT, ref), Template.HEADERS)

    @classmethod
    def get(cls, path):
        return HttpUtil.get("{}{}{}".format(Template.PRISM_HOST, Template.PRISM_PORT, path), Template.HEADERS)
