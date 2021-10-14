from erlang.libs.authAudit.interface.AuthInterface import AuthInterface


class AuthKeyword(object):
    def __init__(self):
        pass

    @staticmethod
    def get_raduis():
        res_code, rsp = AuthInterface.get_function_info('radius_query')
        assert res_code == 200, '{} is not 200'.format(res_code)
        print rsp
        return rsp

    @staticmethod
    def get_ldap():
        res_code, rsp = AuthInterface.get_function_info('ldap_query')
        assert res_code == 200, '{} is not 200'.format(res_code)
        print rsp
        return rsp

    @staticmethod
    def get_timeout():
        res_code, rsp = AuthInterface.get_function_info('timeout_query')
        assert res_code == 200, '{} is not 200'.format(res_code)
        print rsp
        return rsp

    @staticmethod
    def get_navUrl():
        res_code, rsp = AuthInterface.get_function_info('navurl_query')
        assert res_code == 200, '{} is not 200'.format(res_code)
        print rsp
        return rsp

    @staticmethod
    def get_black_white_list(blackList, nameType, content):
        res_code, rsp = AuthInterface.get_function_info('portaljk_whiteblank_query', '&wbflag@{}&nameType@{}&content@{}&limit@20&page@1'.format(blackList, nameType, content))
        assert res_code == 200, '{} is not 200'.format(res_code)
        print rsp
        return rsp
