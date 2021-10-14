from erlang.libs.common import JsonUtil
from erlang.libs.common.AuditRequest import AuditRequest


class AuditInterface(object):

    PATH = "/pronline/Msg?"
    functionName = {'corp_delete': 'ncjk_del_corp',
                    'corp_query': 'ncjk_corp_list',
                    'corp_ap_query': 'ncjk_site_list'}

    @classmethod
    def get_function_info(cls, funName_action, params=''):
        rcv = AuditRequest.post(cls.PATH, cls.functionName[funName_action], params)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def delete_function_info(cls, funName_action, params):
        rcv = AuditRequest.post(cls.PATH, cls.functionName[funName_action], params)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp
