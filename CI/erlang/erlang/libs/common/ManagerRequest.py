import HttpUtil
from erlang.libs.variables import InterfacePathVariables as Template


class ManagerRequest(object):

    @classmethod
    def post(cls, path, data):
        return HttpUtil.post("{}{}{}".format(Template.MANAGER_HOST, Template.MANAGER_PORT, path), data, Template.HEADERS)

    @classmethod
    def put(cls, path, data):
        return HttpUtil.put("{}{}{}".format(Template.MANAGER_HOST, Template.MANAGER_PORT, path), data, Template.HEADERS)

    @classmethod
    def delete(cls, path, data=''):
        return HttpUtil.delete("{}{}{}".format(Template.MANAGER_HOST, Template.MANAGER_PORT, path), Template.HEADERS, data)

    @classmethod
    def get(cls, path):
        return HttpUtil.get("{}{}{}".format(Template.MANAGER_HOST, Template.MANAGER_PORT, path), Template.HEADERS)
