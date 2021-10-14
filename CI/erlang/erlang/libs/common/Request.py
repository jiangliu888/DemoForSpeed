import HttpUtil
from erlang.libs.variables import InterfacePathVariables as Template


class Request(object):

    @classmethod
    def post(cls, path, data):
        return HttpUtil.post(Template.HOST + Template.URANUS_PORT + path, data, Template.HEADERS)

    @classmethod
    def put(cls, path, data):
        return HttpUtil.put(Template.HOST + Template.URANUS_PORT + path, data, Template.HEADERS)

    @classmethod
    def delete(cls, ref):
        return HttpUtil.delete(Template.HOST + Template.URANUS_PORT + ref, Template.HEADERS)

    @classmethod
    def get(cls, path):
        return HttpUtil.get(Template.HOST + Template.URANUS_PORT + path, Template.HEADERS)

    @classmethod
    def south_post(cls, path, data, token=None):
        headers = Template.HEADERS
        if token:
            headers["Authorization"] = "Bearer {}".format(token)
        return HttpUtil.post(Template.HOST + Template.URANUS_SOUTH_PORT + path, data, headers)

    @classmethod
    def patch(cls, path, data):
        return HttpUtil.patch(Template.HOST + Template.URANUS_PORT + path, data, Template.HEADERS)

    @classmethod
    def get_metric(cls, path):
        return HttpUtil.get(Template.HOST + Template.CONTROLLER_PORT + path, Template.HEADERS)

    @classmethod
    def get_uranus_health(cls):
        return HttpUtil.get(Template.HOST + Template.URANUS_HEALTH_PORT, Template.HEADERS)

    @classmethod
    def get_authserver_metric(cls, path):
        return HttpUtil.get(Template.HOST + Template.AUTHSERVER_PORT + path, Template.HEADERS)
