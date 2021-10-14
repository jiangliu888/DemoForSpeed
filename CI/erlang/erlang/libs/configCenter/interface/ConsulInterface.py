from erlang.libs.common import JsonUtil
from erlang.libs.common.ConsulRequest import ConsulRequest
import base64


class ConsulInterface(object):
    CONSUL_PATH = "/v1/kv/configs/v1"
    CPE_PATH = "/ne/cpes"
    POP_PATH = "/ne/pops"
    CFP_PATH = "/ne/cfps"
    SERVICES_PATH = "/ne/services"
    ETC_PATH = "/etc"
    COMPANY_PATH = "/companies"
    GAEA_PATH = "/services/gaea"
    URANUS_PATH = "/services/uranus"
    DEVICE_PATH = "/devices"
    CPE_GLOBALCONFIG_PATH = "/cpeglobalconfig"
    MONITOR_DEVICE_PATH = "/monitor/devices"

    @classmethod
    def get_device_aiwan_info(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(dev_id) + "/aiwan/info")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def get_company_config_version(cls, company_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + "/{}/version".format(company_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_company_config_version(cls, company_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + "/{}/version".format(company_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_device_aiwan_startup(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(dev_id) + "/aiwan/startup")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_device_aiwan_startup(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(dev_id) + "/aiwan/startup", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_device_system_network(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(dev_id) + "/system/network")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def get_device_system_wifi(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(dev_id) + "/system/wifi")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def get_cpeGlobalConfig_ne(cls):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.CPE_GLOBALCONFIG_PATH + '/ne')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_cpeGlobalConfig_ne(cls, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.CPE_GLOBALCONFIG_PATH + "/ne", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def delete_all_consul_config(cls):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + "?recurse=true")
        return rcv.status_code

    @classmethod
    def put_services_gaea_saasSearchPattens(cls, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.GAEA_PATH + "/saasSearchPatterns", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_services_gaea_saasSearchPattens(cls):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.GAEA_PATH + "/saasSearchPatterns")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_services_company_saasSearchPattens(cls, company_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + "/{}/saasSearchPatterns".format(company_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_services_company_saasSearchPattens(cls, company_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + "/{}/saasSearchPatterns".format(company_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_services_gaea_anycastSearchPattens(cls, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.GAEA_PATH + "/anycastSearchPatterns", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_services_gaea_anycastSearchPattens(cls):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.GAEA_PATH + "/anycastSearchPatterns")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_services_gaea_openflowAddr(cls, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.GAEA_PATH + "/openflowAddrs", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_services_gaea_openflowAddr(cls):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.GAEA_PATH + "/openflowAddrs")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_services_gaea_netAlgConfig(cls, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.GAEA_PATH + "/netAlgConfig", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def delete_services_gaea_netAlgConfig(cls):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.GAEA_PATH + "/netAlgConfig")
        return rcv.status_code

    @classmethod
    def get_services_gaea_netAlgConfig(cls):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.GAEA_PATH + "/netAlgConfig")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_services_gaea_managers(cls, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.GAEA_PATH + "/managers", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_services_gaea_managers(cls):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.GAEA_PATH + "/managers")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_ne_services_proxy_preference(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.SERVICES_PATH + '/proxy/' + str(dev_id) + "/preference", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_ne_services_anycast_preference(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.SERVICES_PATH + '/anycast/' + str(dev_id) + "/preference", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_cpe_preference(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "/vport/preference", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_cpe_preference(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "/vport/preference")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_cpe_rateLimit(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "/vport/rateLimit", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_cpe_rateLimit(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "/vport/rateLimit")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_cpe_linkScoreAlgo(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "/linkScoreAlgo", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_cpe_linkScoreAlgo(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "/linkScoreAlgo")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_cpe_linkScoreAlgo(cls, dev_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "/linkScoreAlgo")
        return rcv.status_code

    @classmethod
    def put_cpe_netConfig(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "/netConfig", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def delete_cpe_netConfig(cls, dev_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "/netConfig")
        return rcv.status_code

    @classmethod
    def get_cpe_netConfig(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "/netConfig")
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_ne_cpe(cls, dev_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.CPE_PATH + '/' + str(dev_id) + "?recurse=true")
        return rcv.status_code

    @classmethod
    def put_pop_routecode(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.POP_PATH + '/' + str(dev_id) + '/routeCode', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_cfp_routecode(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.CFP_PATH + '/' + str(dev_id) + '/routeCode', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_pop_routecode(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.POP_PATH + '/' + str(dev_id) + '/routeCode')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_pop_status(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.POP_PATH + '/' + str(dev_id) + '/status', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_pop_status(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.POP_PATH + '/' + str(dev_id) + '/status')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_pop(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.POP_PATH + '/' + str(dev_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_pop_saasServices(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.POP_PATH + '/' + str(dev_id) + '/saasServices', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_pop_saasServices(cls, dev_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.POP_PATH + '/' + str(dev_id) + '/saasServices')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_ne_pop(cls, dev_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.POP_PATH + '/' + str(dev_id) + "?recurse=true")
        return rcv.status_code

    @classmethod
    def delete_ne_cfp(cls, dev_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.CFP_PATH + '/' + str(dev_id) + "?recurse=true")
        return rcv.status_code

    @classmethod
    def put_company_encryption(cls, company_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/encryption', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_encryption(cls, company_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/encryption')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_company(cls, company_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def delete_company(cls, company_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + "?recurse=true")
        return rcv.status_code

    @classmethod
    def put_etc_template_fw(cls, template_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.ETC_PATH + '/templates/fw/' + str(template_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_etc_template_fw(cls, template_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.ETC_PATH + '/templates/fw/' + str(template_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_etc_template_saas(cls, template_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.ETC_PATH + '/templates/saas/' + str(template_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_etc_template_saas(cls, template_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.ETC_PATH + '/templates/saas/' + str(template_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_etc_template_saas(cls, template_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.ETC_PATH + '/templates/saas/' + str(template_id))
        return rcv.status_code

    @classmethod
    def delete_etc_all_template_saas(cls):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.ETC_PATH + '/templates/saas' + "?recurse=true")
        return rcv.status_code

    @classmethod
    def get_company(cls, company_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_company_unions(cls, company_id, union_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/unions/' + str(union_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_unions(cls, company_id, union_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/unions/' + str(union_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_company_unions_rateLimit(cls, company_id, union_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/unions/' + str(union_id) + '/rateLimit', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_unions_rateLimit(cls, company_id, union_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/unions/' + str(union_id) + '/rateLimit')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_company_unions_rateLimit(cls, company_id, union_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/unions/' + str(union_id) + '/rateLimit')
        return rcv.status_code

    @classmethod
    def put_company_sites(cls, company_id, site_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_sites(cls, company_id, site_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_company_sites_fwGroups(cls, company_id, site_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/fwGroups', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_sites_fwGroups(cls, company_id, site_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/fwGroups')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_company_sites_fwGroups(cls, company_id, site_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/fwGroups')
        return rcv.status_code

    @classmethod
    def put_company_sites_saasGroups(cls, company_id, site_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/saasGroups', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_sites_saasGroups(cls, company_id, site_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/saasGroups')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_company_sites_saasGroups(cls, company_id, site_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/saasGroups')
        return rcv.status_code

    @classmethod
    def put_company_sites_spiGroups(cls, company_id, site_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/spiGroups', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_sites_spiGroups(cls, company_id, site_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/spiGroups')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_company_sites_spiGroups(cls, company_id, site_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/spiGroups')
        return rcv.status_code

    @classmethod
    def put_company_spiTags(cls, company_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/spiTags', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_spiTags(cls, company_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/spiTags')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_company_spiTags(cls, company_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/spiTags')
        return rcv.status_code

    @classmethod
    def put_company_sites_spiDispatches(cls, company_id, site_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/spiDispatches', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_sites_spiDispatches(cls, company_id, site_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/spiDispatches')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_company_sites_spiDispatches(cls, company_id, site_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/spiDispatches')
        return rcv.status_code

    @classmethod
    def put_company_sites_rateLimit(cls, company_id, site_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/rateLimit', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_sites_rateLimit(cls, company_id, site_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/rateLimit')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_company_sites_rateLimit(cls, company_id, site_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + '/rateLimit')
        return rcv.status_code

    @classmethod
    def put_etc_fwRules(cls, rule_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/fw/' + str(rule_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_etc_fwRules(cls, rule_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/fw/' + str(rule_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_etc_fwRules(cls, rule_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/fw/' + str(rule_id))
        return rcv.status_code

    @classmethod
    def put_etc_saasRules(cls, rule_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/saas/' + str(rule_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_etc_saasRules(cls, rule_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/saas/' + str(rule_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_etc_saasRules(cls, rule_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/saas/' + str(rule_id))
        return rcv.status_code

    @classmethod
    def delete_all_etc_saasRules(cls):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/saas' + "?recurse=true")
        return rcv.status_code

    @classmethod
    def put_etc_spiRules(cls, rule_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/spi/' + str(rule_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_etc_spiRules(cls, rule_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/spi/' + str(rule_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_etc_spiRules(cls, rule_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/spi/' + str(rule_id))
        return rcv.status_code

    @classmethod
    def delete_all_etc_spiRules(cls):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.ETC_PATH + '/rules/spi' + "?recurse=true")
        return rcv.status_code

    @classmethod
    def put_etc_template_spi(cls, template_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.ETC_PATH + '/templates/spi/' + str(template_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_etc_template_spi(cls, template_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.ETC_PATH + '/templates/spi/' + str(template_id))
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def delete_etc_template_spi(cls, template_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.ETC_PATH + '/templates/spi/' + str(template_id))
        return rcv.status_code

    @classmethod
    def delete_etc_all_template_spi(cls):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.ETC_PATH + '/templates/spi' + "?recurse=true")
        return rcv.status_code

    @classmethod
    def put_device_tunnel_config(cls, dev_id, body):
        return cls.put_cpe_netConfig(dev_id, body)

    @classmethod
    def put_cpe_vport_coreCode(cls, dev_id, body):
        return cls.put_cpe_preference(dev_id, body)

    @classmethod
    def put_controller_config(cls, body):
        return cls.put_services_gaea_openflowAddr(body)

    @classmethod
    def put_controller_config_specific(cls, body):
        return cls.put_services_gaea_openflowAddr(body)

    @classmethod
    def put_company_key(cls, company_id, body):
        return cls.put_company_encryption(company_id, body)

    @classmethod
    def delete_company_site(cls, company_id, site_id=''):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_id) + "?recurse=true")
        return rcv.status_code

    @classmethod
    def delete_all_site(cls, company_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/sites?recurse=true')
        return rcv.status_code

    @classmethod
    def put_ne_route_code(cls, dev_id, body):
        return cls.put_pop_routecode(dev_id, body)

    @classmethod
    def put_ne_home_code_prefer(cls, dev_id, body):
        return cls.put_cpe_preference(dev_id, body)

    @classmethod
    def delete_company_unions(cls, company_id, union_id=''):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/unions/' + str(union_id) + "?recurse=true")
        return rcv.status_code

    @classmethod
    def delete_all_unions(cls, company_id):
        rcv = ConsulRequest.delete(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/unions?recurse=true')
        return rcv.status_code

    @classmethod
    def put_cpe_wan_home_code_prefer(cls, dev_id, body):
        return cls.put_cpe_preference(dev_id, body)

    @classmethod
    def put_ne_status(cls, dev_id, body):
        return cls.put_pop_status(dev_id, body)

    @classmethod
    def put_cpe_address_groups(cls, dev_id, body):
        return cls.put_cpe_preference(dev_id, body)

    @classmethod
    def put_cpe_interface_bandwidth(cls, dev_id, iface_name, body):
        return cls.put_cpe_rateLimit(dev_id, body)

    @classmethod
    def put_cpe_wan_bandwidth(cls, dev_id, iface_name, index_v, body):
        return cls.put_cpe_rateLimit(dev_id, body)

    @classmethod
    def put_ne_measure_algo(cls, dev_id, body):
        return cls.put_cpe_linkScoreAlgo(dev_id, body)

    @classmethod
    def get_company_acls(cls, company_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/acls')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_company_acls(cls, company_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/acls', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_company_routes(cls, company_id):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/routes')
        rsp = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, rsp

    @classmethod
    def put_company_routes(cls, company_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.COMPANY_PATH + '/' + str(company_id) + '/routes', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_monitor_device_alert(cls, sn):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.MONITOR_DEVICE_PATH + '/' + str(sn) + '/alert')
        en = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, en

    @classmethod
    def get_device_auth(cls, sn):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(sn) + '/auth')
        print cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(sn) + '/auth'
        en = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, en

    @classmethod
    def put_device_auth(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(dev_id) + "/auth", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_device_audit(cls, dev_id, body):
        rcv = ConsulRequest.put(cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(dev_id) + "/audit", JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_device_audit(cls, sn):
        rcv = ConsulRequest.get(cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(sn) + '/audit')
        print cls.CONSUL_PATH + cls.DEVICE_PATH + '/' + str(sn) + '/audit'
        en = JsonUtil.i_eval(base64.b64decode(JsonUtil.load_json(rcv.content)[0]['Value'])) if rcv.status_code == 200 else ""
        return rcv.status_code, en
