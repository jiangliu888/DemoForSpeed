from erlang.libs.common import JsonUtil
from erlang.libs.common.GaeaRequest import GaeaRequest


class GaeaInterface(object):
    CNF_PATH = "/api/v1/ne"
    COMPANY_PATH = "/api/v1/companies"
    CODE_AGENT_PATH = '/api/v1/config/location/code'

    @classmethod
    def get_company_key(cls, company_id):
        rcv = GaeaRequest.get(cls.COMPANY_PATH + '/' + str(company_id) + '/encryption')
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def get_cpe_global_bandwidth(cls, company_id, site_name):
        rcv = GaeaRequest.get(cls.COMPANY_PATH + '/{}/sites/{}/bandwidth'.format(company_id, site_name))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_company_unions_with_name(cls, company_id, union_name):
        rcv = GaeaRequest.get(cls.COMPANY_PATH + '/{}/unions/{}'.format(company_id, union_name))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_code_agent_search_pattern(cls):
        rcv = GaeaRequest.get(cls.CODE_AGENT_PATH + '/searchPatterns')
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_all_company_config(cls, skip=0, limit=10):
        rcv = GaeaRequest.get(cls.COMPANY_PATH + '?skip=' + str(skip) + '&limit=' + str(limit))
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def get_company_site(cls, company_id, skip=0, limit=0):
        rcv = GaeaRequest.get(cls.COMPANY_PATH + '/' + str(company_id) + '/sites?skip=' + str(skip) + '&limit=' + str(limit))
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def get_company_sites(cls, company_id, site_name):
        rcv = GaeaRequest.get(cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + site_name)
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def get_company_unions(cls, company_id):
        rcv = GaeaRequest.get(cls.COMPANY_PATH + '/{}/unions'.format(company_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp
