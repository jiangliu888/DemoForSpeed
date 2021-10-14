import HttpUtil
from erlang.libs.variables import InterfacePathVariables as Template


class ConsulRequest(object):

    @classmethod
    def put(cls, path, data):
        return HttpUtil.put("{}{}{}".format(Template.CONSUL_HOST, Template.CONSUL_PORT, path), data, Template.CONSUL_HEADERS)

    @classmethod
    def delete(cls, ref):
        return HttpUtil.delete("{}{}{}".format(Template.CONSUL_HOST, Template.CONSUL_PORT, ref), Template.CONSUL_HEADERS)

    @classmethod
    def get(cls, path):
        print Template.CONSUL_HOST + Template.CONSUL_PORT + path
        return HttpUtil.get("{}{}{}".format(Template.CONSUL_HOST, Template.CONSUL_PORT, path), Template.CONSUL_HEADERS)
