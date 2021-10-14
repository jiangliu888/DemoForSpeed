import HttpUtil
import os
import OsUtil
from erlang.libs.variables import InterfacePathVariables as Template
import urllib


class InsightRequest(object):

    token = ""

    @classmethod
    def post(cls, path, data):
        path = urllib.quote_plus(path, safe="/?=")
        return HttpUtil.post("{}{}{}".format(Template.INSIGHT_HOST, Template.INSIGHT_PORT, path), data, Template.INSIGHT_HEADERS)

    @classmethod
    def post_file(cls, path, file_path):
        md5 = OsUtil.get_md5(file_path)
        # open the file
        cmd = 'curl -X POST -H "Content-Type: multipart/form-data" '
        cmd += '-H "Authorization: Bearer ' + cls.token + '" '
        cmd += '-F md5=' + md5 + ' '
        cmd += '-F "file=@' + file_path
        cmd += ';filename=' + file_path + ';type=application/octet-stream" '
        cmd += "{}{}{}".format(Template.INSIGHT_HOST, Template.INSIGHT_PORT, path)
        res = os.popen(cmd).readlines()
        return res

    @classmethod
    def put(cls, path, data):
        path = urllib.quote_plus(path, safe="/?=")
        return HttpUtil.put("{}{}{}".format(Template.INSIGHT_HOST, Template.INSIGHT_PORT, path), data, Template.INSIGHT_HEADERS)

    @classmethod
    def patch(cls, path, data):
        path = urllib.quote_plus(path, safe="/?=")
        return HttpUtil.patch("{}{}{}".format(Template.INSIGHT_HOST, Template.INSIGHT_PORT, path), data, Template.INSIGHT_HEADERS)

    @classmethod
    def delete(cls, ref):
        ref = urllib.quote_plus(ref, safe="/?=")
        return HttpUtil.delete("{}{}{}".format(Template.INSIGHT_HOST, Template.INSIGHT_PORT, ref), Template.INSIGHT_HEADERS)

    @classmethod
    def get(cls, path, data=""):
        path = urllib.quote_plus(path, safe="/?=&")
        return HttpUtil.get("{}{}{}".format(Template.INSIGHT_HOST, Template.INSIGHT_PORT, path), Template.INSIGHT_HEADERS, data)
