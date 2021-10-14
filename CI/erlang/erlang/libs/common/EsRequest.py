import HttpUtil
from erlang.libs.variables import InterfacePathVariables as Template


class EsRequest(object):

    @classmethod
    def post(cls, path, data):
        return HttpUtil.post("{}{}{}".format(Template.ES_HOST, Template.ES_PORT, path), data, Template.ES_HEADERS)

    @classmethod
    def put(cls, path, data):
        return HttpUtil.put("{}{}{}".format(Template.ES_HOST, Template.ES_PORT, path), data, Template.ES_HEADERS)

    @classmethod
    def delete(cls, ref):
        return HttpUtil.delete("{}{}{}".format(Template.ES_HOST, Template.ES_PORT, ref), Template.ES_HEADERS)

    @classmethod
    def get(cls, path, data=""):
        return HttpUtil.get("{}{}{}".format(Template.ES_HOST, Template.ES_PORT, path), Template.ES_HEADERS, data)
