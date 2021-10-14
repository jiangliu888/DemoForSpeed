from erlang.libs.uranus.interface.GaeaInterface import GaeaInterface


class GaeaKeyword(object):
    def __init__(self):
        pass

    @staticmethod
    def get_company_key(company_id, field='key'):
        res_code, res_body = GaeaInterface.get_company_key(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return res_body[field]

    @staticmethod
    def get_cpe_global_bandwidth(company_id, site_id):
        res_code, body = GaeaInterface.get_cpe_global_bandwidth(company_id, site_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body['rateLimit']

    @staticmethod
    def check_cpe_global_bandwidth(company_id, site_id, bandwidth, burst, latency):
        body = GaeaKeyword.get_cpe_global_bandwidth(company_id, site_id)
        return True if(body["bandwidth"] == int(bandwidth) and body["burst"] == int(burst) and body["latency"] == int(latency)) else False

    @staticmethod
    def get_cpe_bond_bandwidth(company_id, union_id):
        res_code, body = GaeaInterface.get_company_unions_with_name(company_id, union_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body['rateLimit']

    @staticmethod
    def check_cpe_bond_bandwidth(company_id, union_id, bandwidth, burst, latency):
        body = GaeaKeyword.get_cpe_bond_bandwidth(company_id, union_id)
        return True if(body["bandwidth"] == int(bandwidth) and body["burst"] == int(burst) and body["latency"] == int(latency)) else False

    @staticmethod
    def check_code_agent_pattern(pop_id_list, region, country, area, district):
        cod, res = GaeaInterface.get_code_agent_search_pattern()
        assert cod == 200, '{} is not 200'.format(cod)
        bodys = res["results"]

        def find_match(matcher, region, country, area, district):
            return True if (matcher['region'] == region and matcher['country'] == country and matcher['area'] == area and matcher['district'] == district) else False

        body = filter(lambda x: find_match(x["matcher"], region, country, area, district), bodys)
        proxy_service = map(lambda x: x >> 4 << 4 | 8, pop_id_list)

        def in_list(proxyServices, proxyId):
            return True if proxyId in proxyServices else False

        if (len(body) != 0):
            results = map(lambda x: in_list(body[0]['proxyServices'], x), proxy_service)
            return all(results)
        return False

    @staticmethod
    def get_company_id(name):
        res_code, body = GaeaInterface.get_all_company_config(0, 0)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return filter(lambda x: name == x['name'], body['results'])[0]['id']

    @staticmethod
    def get_company_site(company_id, skip=0, limit=0):
        res_code, body = GaeaInterface.get_company_site(company_id, skip, limit)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body['results']

    @staticmethod
    def get_company_all_unions(company_id):
        res_code, rsp = GaeaInterface.get_company_unions(company_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return rsp["results"]

    @staticmethod
    def get_company_unions(company_id, unions_name):
        res_code, body = GaeaInterface.get_company_unions_with_name(company_id, unions_name)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body

    @staticmethod
    def get_company_sites_with_id(company_id, site_id):
        res_code, body = GaeaInterface.get_company_sites(company_id, site_id)
        assert res_code == 200, '{} is not 200'.format(res_code)
        return body

    @staticmethod
    def check_fwTemp_in_site(company_id, site_id, fwTemp_id):
        body = GaeaKeyword.get_company_sites_with_id(company_id, site_id)
        fwGroup = body["fwGroups"]
        return True if fwTemp_id in fwGroup else False

    @staticmethod
    def check_saasTemp_in_site(company_id, site_id, saasTemp_id):
        body = GaeaKeyword.get_company_sites_with_id(company_id, site_id)
        saasGroup = body["natGroups"]
        return True if saasTemp_id in saasGroup else False

    @staticmethod
    def check_spiTemp_in_site(company_id, site_id, spiTemp_id):
        body = GaeaKeyword.get_company_sites_with_id(company_id, site_id)
        spiGroup = body["spiGroups"]
        return True if spiTemp_id in spiGroup else False

    @staticmethod
    def check_none_saasTemp_in_site(company_id, site_id):
        body = GaeaKeyword.get_company_sites_with_id(company_id, site_id)
        assert 'natGroups' not in body.keys()

    @staticmethod
    def check_none_spiTemp_in_site(company_id, site_id):
        body = GaeaKeyword.get_company_sites_with_id(company_id, site_id)
        assert 'spiGroups' not in body.keys()
