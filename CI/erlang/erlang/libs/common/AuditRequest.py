import HttpUtil
import time
import OsUtil
from erlang.libs.variables import InterfacePathVariables as Template


class AuditRequest(object):

    @classmethod
    def post(cls, path, funName, otherParam="", data='{}'):
        timeStamp = str(int(time.time()))
        prosign = Template.AUTH_VERSION + Template.AUTH_APPID + timeStamp + funName + Template.AUTH_SECRET
        md5 = OsUtil.get_string_md5(prosign)
        param = 'FunName@{0}&appid@{1}&version@{2}&timestamp@{3}&prosign@{4}{5}'.format(funName, Template.AUTH_APPID, Template.AUTH_VERSION, timeStamp, md5, otherParam)
        print Template.AUDIT_HOST + Template.AUDIT_PORT + path + param
        return HttpUtil.post("{}{}{}{}".format(Template.AUDIT_HOST, Template.AUDIT_PORT, path, param), data, Template.AUTH_HEADERS)
