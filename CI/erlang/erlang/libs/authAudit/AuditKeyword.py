from erlang.libs.authAudit.interface.AuditInterface import AuditInterface


class AuditKeyword(object):
    def __init__(self):
        pass

    @staticmethod
    def delete_corp(company_name):
        res_code, rsp = AuditInterface.get_function_info('corp_query')
        assert res_code == 200, '{} is not 200'.format(res_code)
        print rsp
        corp_code = filter(lambda x: x['servicename'] == company_name, rsp['eimdata'])
        map(lambda x: AuditInterface.delete_function_info('corp_delete', '&servicecode@{}&servicename@{}'.format(x['servicecode'], company_name)), corp_code)

    @staticmethod
    def get_corp(company_name, corp_code):
        res_code, rsp = AuditInterface.get_function_info('corp_query', '&servicecode@{}&servicename@{}'.format(corp_code, company_name))
        assert res_code == 200, '{} is not 200'.format(res_code)
        print rsp
        return rsp

    @staticmethod
    def get_corp_ap(corp_code):
        res_code, rsp = AuditInterface.get_function_info('corp_ap_query', '&servicecode@{}'.format(corp_code))
        assert res_code == 200, '{} is not 200'.format(res_code)
        print rsp
        return rsp
