from erlang.libs.common import JsonUtil
from erlang.libs.common.AuthRequest import AuthRequest


class AuthInterface(object):

    PATH = "/pronline/Msg?"
    functionName = {'radius_query': 'portaljk_radius_queryparams',
                    'whiteblank_query': 'portaljk_whiteblank_query',
                    'timeout_query': 'portaljk_timeout_query',
                    'navurl_query': 'portaljk_navurl_query',
                    'ldap_query': 'portaljk_ldappar_query'}

    @classmethod
    def get_function_info(cls, funName_action, params=''):
        rcv = AuthRequest.post(cls.PATH, cls.functionName[funName_action], params)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp
