from erlang.libs.common import JsonUtil
from erlang.libs.common.Request import Request


class UranusInterface(object):
    CNF_PATH = "/api/v1/ne"
    TUNNEL_CNF_PATH = "/netConfig"
    CONFIG_CNF_PATH = "/config"
    CONTROLLER_PATH = "/api/v1/config/openflow/controllers"
    NE_TUNNELS_PATH = "/tunnels"
    COMPANY_PATH = "/api/v1/companies"
    SAAS_PATH = '/service/saas'
    NAT_PATH = '/api/thea/nat'
    SOUTH_CPE_REG_PATH = '/api/v1/ne/cpe'
    SOUTH_POP_REG_PATH = '/api/v1/ne/pop'
    NETLINK_PATH = '/api/v1/netlink'
    TEMPLATE_PATH = '/api/v1/templates'
    NAT_TEMPLATE_PATH = TEMPLATE_PATH + '/nat'
    SPI_TEMPLATE_PATH = TEMPLATE_PATH + '/spi'
    FWRULES_PATH = TEMPLATE_PATH + '/fw/rules'
    FWGROUPS_PATH = TEMPLATE_PATH + '/fw/groups'
    VPORT = '/vport'
    MANAGER_PATH = '/api/v1/config/managers'
    NAT_AGENT_PATH = '/api/v1/config/nat/service'
    MEASURE_ALGO = '/measure/algo'
    VPORT_CORECODE = '/vport/coreCode'
    SAAS_PROXY_PATH = '/service/proxy'
    ANYCAST_PATH = '/service/anycast'
    NORTH_SAAS_PROXY_PATH = '/services/proxy'
    NORTH_ANYCAST_PATH = '/services/anycast'
    HOMECODE_SELECTION_PATH = '/homeCodeSelection'

    @classmethod
    def put_device_tunnel_config(cls, dev_id, body):
        rcv = Request.put(cls.CNF_PATH + '/' + str(dev_id) + cls.TUNNEL_CNF_PATH, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_device_tunnel_config(cls, dev_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(dev_id) + cls.TUNNEL_CNF_PATH)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_homeCodeSelection(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(ne_id) + cls.HOMECODE_SELECTION_PATH)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def put_device_vport_coreCode(cls, dev_id, body):
        rcv = Request.put(cls.CNF_PATH + '/' + str(dev_id) + cls.VPORT_CORECODE, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def post_ne_tunnels_config(cls, ne_id, body):
        rcv = Request.post(cls.CNF_PATH + '/' + str(ne_id) + cls.NE_TUNNELS_PATH, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_netcfg_ne_config(cls):
        rcv = Request.get(cls.CNF_PATH)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def put_controller_config(cls, body):
        rcv = Request.put(cls.CONTROLLER_PATH, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_controller_config_specific(cls, body):
        rcv = Request.put(cls.CONTROLLER_PATH + '/specific', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_controller_config(cls):
        rcv = Request.get(cls.CONTROLLER_PATH)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_controller_config_specific(cls):
        rcv = Request.get(cls.CONTROLLER_PATH + '/specific')
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def post_netcfg_er_config(cls, body):
        rcv = Request.post(cls.CNF_PATH + cls.CONFIG_CNF_PATH, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def post_company_config(cls, body):
        rcv = Request.post(cls.COMPANY_PATH, JsonUtil.dump_json(body))
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def patch_company_config(cls, company_id, body):
        rcv = Request.patch(cls.COMPANY_PATH + '/' + company_id, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_dedicate_company_config(cls, company_id):
        rcv = Request.get(cls.COMPANY_PATH + '/' + str(company_id) + '/config')
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def delete_dedicate_company_config(cls, company_id):
        rcv = Request.delete(cls.COMPANY_PATH + '/' + str(company_id))
        return rcv.status_code

    @classmethod
    def post_company_sites(cls, company_id, body):
        rcv = Request.post(cls.COMPANY_PATH + '/' + str(company_id) + '/sites', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def delete_company_site(cls, company_id, site_name):
        rcv = Request.delete(cls.COMPANY_PATH + '/' + str(company_id) + '/sites/' + str(site_name))
        return rcv.status_code

    @classmethod
    def put_ne_route_code(cls, ne_id, body):
        rcv = Request.put(cls.CNF_PATH + '/' + str(ne_id) + '/routeCode', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_ne_home_code_prefer(cls, ne_id, body):
        rcv = Request.put(cls.CNF_PATH + '/' + str(ne_id) + '/homeCode/prefer', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_ne_route_code(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(ne_id) + '/routeCode')
        rsp = JsonUtil.load_json(rcv.content)
        return rsp

    @classmethod
    def get_ne_tunnels_from_controller(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(ne_id) + '/tunnels')
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def delete_ne_tunnel(cls, ne_id, tunnel_id):
        rcv = Request.delete(cls.CNF_PATH + '/' + str(ne_id) + '/tunnel' + '/' + str(tunnel_id))
        return rcv.status_code

    @classmethod
    def get_ne_tasks_from_controller(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(ne_id) + '/task')
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def unregister_ne(cls, ne_id):
        rcv = Request.delete(cls.CNF_PATH + '/' + str(ne_id))
        return rcv.status_code

    @classmethod
    def post_pop_saas_config(cls, ne_id, body):
        rcv = Request.put(cls.CNF_PATH + '/' + str(ne_id) + cls.SAAS_PATH, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_pop_saas_config(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(ne_id) + cls.SAAS_PATH)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def delete_nat_agent_config(cls, ne_id, end_point):
        rcv = Request.delete(cls.NAT_AGENT_PATH + '/' + str(ne_id) + '/' + str(end_point) + '/config')
        return rcv.status_code

    @classmethod
    def post_nat_agent_search_pattern(cls, body):
        rcv = Request.post(cls.NAT_AGENT_PATH + '/searchPatterns', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def post_code_agent_search_pattern(cls, body):
        rcv = Request.post(cls.CODE_AGENT_PATH + '/searchPatterns', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def delete_nat_agent_search_pattern(cls, country, city, isp):
        rcv = Request.delete(cls.NAT_AGENT_PATH + '/searchPatterns?country={}&city={}&isp={}'.format(country, city, isp))
        return rcv.status_code

    @classmethod
    def get_nat_agent_search_pattern(cls):
        rcv = Request.get(cls.NAT_AGENT_PATH + '/searchPatterns')
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_netcfg_ne_config_with_id(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(ne_id))
        rsp = JsonUtil.load_json(rcv.content)
        rsp["pops"] = [] if 'pops' not in rsp.keys() else rsp["pops"]
        rsp["cpes"] = [] if 'cpes' not in rsp.keys() else rsp["cpes"]
        ne_list = rsp["cpes"] + rsp["pops"]
        return rcv.status_code, ne_list[0]

    @classmethod
    def cpe_reg_config(cls, device_id, body, token):
        rcv = Request.south_post(cls.SOUTH_CPE_REG_PATH + '/' + device_id, JsonUtil.dump_json(body), token)
        return rcv.status_code

    @classmethod
    def pop_reg_config(cls, device_id, body):
        rcv = Request.south_post(cls.SOUTH_POP_REG_PATH + '/' + device_id, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def post_ne_endpoints(cls, ne_id, body):
        rcv = Request.post(cls.CNF_PATH + '/' + str(ne_id) + '/endpoints', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def delete_ne_endpoints(cls, ne_id):
        rcv = Request.delete(cls.CNF_PATH + '/' + str(ne_id) + '/endpoints')
        return rcv.status_code

    @classmethod
    def delete_services_proxy(cls, service_id):
        rcv = Request.delete(cls.CNF_PATH + cls.NORTH_SAAS_PROXY_PATH + '/' + str(service_id))
        return rcv.status_code

    @classmethod
    def delete_services_anycast(cls, service_id):
        rcv = Request.delete(cls.CNF_PATH + cls.NORTH_ANYCAST_PATH + '/' + str(service_id))
        return rcv.status_code

    @classmethod
    def get_service_proxy(cls, service_id):
        rcv = Request.get(cls.SAAS_PROXY_PATH + '/' + str(service_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_service_anycast(cls, service_id):
        rcv = Request.get(cls.ANYCAST_PATH + '/' + str(service_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def put_measure_config(cls, body):
        rcv = Request.put(cls.MEASURE_CONFIG_PATH, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def post_site_isp(cls, company_id, site_id, body):
        rcv = Request.post(cls.COMPANY_PATH + '/{}/site/{}/isps'.format(company_id, site_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_site_isp(cls, company_id, site_id):
        rcv = Request.get(cls.COMPANY_PATH + '/{}/site/{}/isps'.format(company_id, site_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_site_port_isp(cls, company_id, site_id, port):
        rcv = Request.get(cls.COMPANY_PATH + '/{}/site/{}/isp/{}'.format(company_id, site_id, port))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def delete_site_isp(cls, company_id, site_id):
        rcv = Request.delete(cls.COMPANY_PATH + '/{}/site/{}/isps'.format(company_id, site_id))
        return rcv.status_code

    @classmethod
    def delete_site_isp_port(cls, company_id, site_id, port):
        rcv = Request.delete(cls.COMPANY_PATH + '/{}/site/{}/isp/{}'.format(company_id, site_id, port))
        return rcv.status_code

    @classmethod
    def post_company_unions(cls, company_id, body):
        rcv = Request.post(cls.COMPANY_PATH + '/{}/unions'.format(company_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def patch_company_unions(cls, company_id, union_name, body):
        rcv = Request.patch(cls.COMPANY_PATH + '/{}/unions/{}'.format(company_id, union_name), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_company_unions(cls, company_id, union_name, body):
        rcv = Request.put(cls.COMPANY_PATH + '/{}/unions/{}'.format(company_id, union_name), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def delete_company_unions(cls, company_id, unions_name):
        rcv = Request.delete(cls.COMPANY_PATH + '/{}/unions/{}'.format(company_id, unions_name))
        return rcv.status_code

    @classmethod
    def get_cpe_wan_home_code(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/{}/homeCode'.format(ne_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rsp["homeCodes"]

    @classmethod
    def delete_company_dedicate_union(cls, company_id, u_type, mem_a, mem_b):
        rcv = Request.delete(cls.COMPANY_PATH + '/{}/union?type={}&memA={}&memB={}'.format(company_id, u_type, mem_a, mem_b))
        return rcv.status_code

    @classmethod
    def get_cpe_wan_home_code_prefer(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/{}/homeCode/prefer'.format(ne_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rsp

    @classmethod
    def put_cpe_wan_home_code_prefer(cls, ne_id, body):
        rcv = Request.put(cls.CNF_PATH + '/{}/homeCode/prefer'.format(ne_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_ne_status(cls, ne_id, body):
        rcv = Request.put(cls.CNF_PATH + '/{}/status'.format(ne_id), JsonUtil.dump_json(body))
        return rcv.status_code, rcv.content

    @classmethod
    def get_cpe_status(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/{}/status'.format(ne_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rsp

    @classmethod
    def post_template_nat_groups(cls, body):
        rcv = Request.post(cls.NAT_TEMPLATE_PATH + '/groups', JsonUtil.dump_json(body))
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def put_template_nat_groups(cls, group_id, body):
        rcv = Request.put(cls.NAT_TEMPLATE_PATH + '/groups/{}'.format(group_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_template_nat_groups(cls):
        rcv = Request.get(cls.NAT_TEMPLATE_PATH + '/groups?skip=0&limit=0')
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_template_spi_groups(cls):
        rcv = Request.get(cls.SPI_TEMPLATE_PATH + '/groups?skip=0&limit=0')
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def delete_template_nat_groups(cls, group_id):
        rcv = Request.delete(cls.NAT_TEMPLATE_PATH + '/groups/{}'.format(group_id))
        return rcv.status_code

    @classmethod
    def post_template_nat_rules(cls, body):
        rcv = Request.post(cls.NAT_TEMPLATE_PATH + '/rules', JsonUtil.dump_json(body))
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def put_template_nat_rules(cls, rule_id, body):
        rcv = Request.put(cls.NAT_TEMPLATE_PATH + '/rules/{}'.format(rule_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_template_nat_rules(cls):
        rcv = Request.get(cls.NAT_TEMPLATE_PATH + '/rules?skip=0&limit=0')
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_template_spi_rules(cls):
        rcv = Request.get(cls.SPI_TEMPLATE_PATH + '/rules?skip=0&limit=0')
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def delete_template_nat_rules(cls, rule_id):
        rcv = Request.delete(cls.NAT_TEMPLATE_PATH + '/rules/{}'.format(rule_id))
        return rcv.status_code

    @classmethod
    def put_site_nat_rules(cls, company_id, site_name, body):
        rcv = Request.put(cls.COMPANY_PATH + '/{}/sites/{}/nats'.format(company_id, site_name), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_ne_route(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/{}/routes'.format(ne_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rsp

    @classmethod
    def get_ne_vport(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/{}'.format(ne_id) + cls.VPORT)
        rsp = JsonUtil.load_json(rcv.content)
        return rsp

    @classmethod
    def get_cpe_managers(cls):
        rcv = Request.get(cls.MANAGER_PATH)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_cpe_managers_specific(cls):
        rcv = Request.get(cls.MANAGER_PATH + "/specific")
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def put_cpe_managers(cls, body):
        rcv = Request.put(cls.MANAGER_PATH, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_cpe_interface_bandwidth(cls, ne_id, iface_name):
        rcv = Request.get(cls.CNF_PATH + '/{}/bandwidth/port/{}'.format(ne_id, iface_name))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def put_cpe_interface_bandwidth(cls, ne_id, iface_name, body):
        rcv = Request.put(cls.CNF_PATH + '/{}/bandwidth/port/{}'.format(ne_id, iface_name), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_cpe_wan_bandwidth(cls, ne_id, iface_name):
        rcv = Request.get(cls.CNF_PATH + '/{}/port/{}'.format(ne_id, iface_name))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_cpe_bond_bandwidth(cls, company_id, union_name, bond_number):
        rcv = Request.get(cls.COMPANY_PATH + '/{}/unions/{}/bond/{}/bandwidth'.format(company_id, union_name, bond_number))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def post_template_fw_groups(cls, body):
        rcv = Request.post(cls.FWGROUPS_PATH, JsonUtil.dump_json(body))
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def put_template_fw_groups(cls, group_id, body):
        rcv = Request.put(cls.FWGROUPS_PATH + '/{}'.format(group_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_template_fw_groups(cls, company_id):
        rcv = Request.get(cls.FWGROUPS_PATH + '?companyId={}&skip=0&limit=0'.format(company_id))
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def delete_template_fw_groups(cls, group_id):
        rcv = Request.delete(cls.FWGROUPS_PATH + '/{}'.format(group_id))
        return rcv.status_code

    @classmethod
    def post_template_fw_rule(cls, body):
        rcv = Request.post(cls.FWRULES_PATH, JsonUtil.dump_json(body))
        return rcv.status_code, JsonUtil.load_json(rcv.content)

    @classmethod
    def put_template_fw_rule(cls, rules_id, body):
        rcv = Request.put(cls.FWRULES_PATH + '/{}'.format(rules_id), JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_template_fw_rules(cls, company_id):
        rcv = Request.get(cls.FWRULES_PATH + '?companyId={}&skip=0&limit=0'.format(company_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def delete_template_fw_rule(cls, rules_id):
        rcv = Request.delete(cls.FWRULES_PATH + '/{}'.format(rules_id))
        return rcv.status_code

    @classmethod
    def put_ne_measure_algo(cls, ne_id, body):
        rcv = Request.put(cls.CNF_PATH + '/' + str(ne_id) + cls.MEASURE_ALGO, JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def get_ne_measure_algo(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(ne_id) + cls.MEASURE_ALGO)
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_e2e_links_from_controller(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(ne_id) + '/links')
        rsp = JsonUtil.load_json(rcv.content) if rcv.status_code != 404 else None
        return rcv.status_code, rsp

    @classmethod
    def get_e2e_bond_from_controller(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(ne_id) + '/bonds')
        rsp = JsonUtil.load_json(rcv.content) if rcv.status_code != 404 else None
        return rcv.status_code, rsp

    @classmethod
    def get_e2e_bond_from_controller_db(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/' + str(ne_id) + '/bonds/profile')
        rsp = JsonUtil.load_json(rcv.content) if rcv.status_code != 404 else None
        return rcv.status_code, rsp

    @classmethod
    def get_cpe_vports(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/{}/vport'.format(ne_id))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_controller_metric(cls):
        rcv = Request.get_metric("/metrics")
        return rcv.status_code, rcv.content

    @classmethod
    def get_pop_cpes(cls, ne_id):
        rcv = Request.get(cls.CNF_PATH + '/pop/' + str(ne_id) + '/cpes')
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def put_nes_control_state(cls, body):
        rcv = Request.put(cls.CNF_PATH + 's', JsonUtil.dump_json(body))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_nes_status(cls, status):
        rcv = Request.get(cls.CNF_PATH + 's?control='.format(status))
        rsp = JsonUtil.load_json(rcv.content)
        return rcv.status_code, rsp

    @classmethod
    def get_uranus_health(cls):
        rcv = Request.get_uranus_health()
        return rcv.status_code, rcv.content

    @classmethod
    def get_authserver_metrics(cls):
        rcv = Request.get_authserver_metric("/metrics")
        return rcv.status_code, rcv.content
