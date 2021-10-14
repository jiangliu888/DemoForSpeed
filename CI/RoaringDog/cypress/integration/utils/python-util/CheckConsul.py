# -*- coding: UTF-8 -*-
import sys
import ast
import json
import io
import body_check
from erlang.libs.configCenter.interface.ConsulInterface import ConsulInterface
from erlang.libs.common.JsonUtil import are_same



def check_company(argList):
    companyId = argList[0]
    companyName = argList[1]
    print u'{}'.format(companyName)
    expectBody = body_check.companyBody[companyName]
    res_code, body = ConsulInterface.get_company(companyId)
    assert res_code == 200, '{} is not 200,body is {}'.format(res_code,body)
    print "company consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, ["root['tunnelControlSwitch']"]) == True
    check_company_encryption([companyId])

def check_company_encryption(argList):
    companyId = argList[0]
    expectBody = {"key": "", "algorithm": argList[1], "format": "256"} if len(argList) >= 2 else body_check.companyEncryptionBody
    expectKeyLen = argList[2] if len(argList) >=3 else 16
    res_code, body = ConsulInterface.get_company_encryption(companyId)
    assert res_code == 200, '{} is not 200,body is {}'.format(res_code,body)
    print "company encryption consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, ["root['key']"]) == True
    assert len(body["key"]) == int(expectKeyLen)

def check_site(argList):
    companyId = argList[0]
    siteId = argList[1]
    siteName = argList[2]
    neId = argList[3]
    expectBody = body_check.siteBody[siteName]
    expectBody['config']['neId'] = int(neId)
    res_code, body = ConsulInterface.get_company_sites(companyId,siteId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "site consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, ["root['id']"]) == True

def check_siteRateLimit(argList):
    companyId = argList[0]
    siteId = argList[1]
    siteName = argList[2]
    expectBody = body_check.siteRateLimitBody[siteName]
    res_code, body = ConsulInterface.get_company_sites_rateLimit(companyId,siteId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "siteRate consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, ["root['burst']"]) == True

def check_union(argList):
    companyId = argList[0]
    unionId = argList[1]
    unionName = argList[2]
    expectBody = body_check.unionBody[unionName]
    res_code, body = ConsulInterface.get_company_unions(companyId,unionId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "union consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, ["root['siteA']", "root['siteB']"]) == True

def check_unionRateLimit(argList):
    companyId = argList[0]
    unionId = argList[1]
    unionName = argList[2]
    expectBody = body_check.unionRateLimitBody[unionName]
    res_code, body = ConsulInterface.get_company_unions_rateLimit(companyId,unionId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "unionRate consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, []) == True

def check_nePreference(argList):
    neId = argList[0]
    siteName = argList[1]
    preference_expectBody = body_check.vportPreferenceBody[siteName]
    res_code, preference_bodys = ConsulInterface.get_cpe_preference(neId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "preference consul is {}\nand expect is {}".format(preference_bodys, preference_expectBody)
    check_list = []
    for body in preference_expectBody:
        check_list.append(any([are_same(body, x, []) for x in preference_bodys]))
    print check_list
    assert all(check_list) == True

def check_neRateLimit(argList):
    neId = argList[0]
    siteName = argList[1]
    rateLimit_expectBody = body_check.vportRateLimitBody[siteName]
    res_code, rateLimit_bodys = ConsulInterface.get_cpe_rateLimit(neId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "rateLimit consul is {}\nand expect is {}".format(rateLimit_bodys, rateLimit_expectBody)
    check_list = []
    for body in rateLimit_expectBody:
        check_list.append(any([are_same(body, x, []) for x in rateLimit_bodys]))
    print check_list
    assert all(check_list) == True

def check_neNetConfig(argList):
    neId = argList[0]
    siteName = argList[1]
    netConfig_expectBody = body_check.netConfigBody[siteName]
    res_code, netConfig_body = ConsulInterface.get_cpe_netConfig(neId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "netConfig consul is {}\nand expect is {}".format(netConfig_body, netConfig_expectBody)
    assert are_same(netConfig_expectBody, netConfig_body, []) == True

def check_device_aiwan_info(argList):
    deviceId = argList[0]
    #neid = argList[1]
    companyId = argList[2]
    expectBody = {"company": companyId}
    res_code, body = ConsulInterface.get_device_aiwan_info(deviceId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "aiwan info consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(body, expectBody, ["root['companyName']", "root['siteId']", "root['siteName']", "root['isHA']", "root['isHub']"]) == True

def check_device_aiwan_startup(argList):
    deviceId = argList[0]
    expectBody = body_check.startupBody[deviceId]
    res_code, body = ConsulInterface.get_device_aiwan_startup(deviceId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "aiwan startup consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(body, expectBody, []) == True

def check_device_system_network(argList):
    deviceId = argList[0]
    expectBody = body_check.networkBody[deviceId]
    res_code, body = ConsulInterface.get_device_system_network(deviceId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "aiwan  consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(body, expectBody, []) == True

def check_device_system_wifi(argList):
    deviceId = argList[0]
    expectBody = body_check.wifiBody[deviceId]
    res_code, body = ConsulInterface.get_device_system_wifi(deviceId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "aiwan startup consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(body, expectBody, []) == True

def check_cpeglobalconfigne():
    expectBody = body_check.cpeglobalconfigneBody
    res_code, body = ConsulInterface.get_cpeGlobalConfig_ne()
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "globalNe consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(body, expectBody, []) == True

def check_spiTag(argList):
    companyId = argList[0]
    tagsName = argList[1]
    expectBody = body_check.spiTagsBody[tagsName]
    res_code, body = ConsulInterface.get_company_spiTags(companyId)
    for i in body:
        for x in i['rules']:
            del x['id']
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "spitags consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, ["root['spiTags']"]) == True

def check_spiDispatch(argList):
    companyId = argList[0]
    siteName = argList[1]
    siteId = argList[2]
    expectBody = body_check.spiDispatchBody[siteName]
    res_code, body = ConsulInterface.get_company_sites_spiDispatches(companyId,siteId)
    for i in body:
        del i['tag']
        for x in i['actions']:
            for y in x['param']:
                if "id" in y:
                    del y['id']
    if (siteName == 'Empty'):
        assert res_code == 404, '{} is not 404'.format(res_code)
    else:
        assert res_code == 200, '{} is not 200'.format(res_code)
        print "spidispatch consul is {}\nand expect is {}".format(body, expectBody)
        assert are_same(expectBody, body, ["root['spiDispatch']"]) == True

def check_manager():
    expectBody = body_check.managerBody
    res_code, body = ConsulInterface.get_services_gaea_managers()
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "manager consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, []) == True

def check_openflow():
    expectBody = body_check.openflowBody
    res_code, body = ConsulInterface.get_services_gaea_openflowAddr()
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "openflow consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, []) == True

def check_saasSearchPattern(argList):
    code = argList[0]
    expectBody = body_check.saasSearchPattern[code]
    res_code, bodys = ConsulInterface.get_services_gaea_saasSearchPattens()
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "saasSearchPattern consul is {}\nand expect is {}".format(bodys, expectBody)
    assert expectBody in bodys

def check_companySaasSearchPattern(argList):
    company = argList[0]
    code = argList[1]
    expectBody = body_check.companySaasSearchPattern[code]
    res_code, bodys = ConsulInterface.get_services_company_saasSearchPattens(company)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "saasSearchPattern consul is {}\nand expect is {}".format(bodys, expectBody)
    assert expectBody in bodys

def check_companyAcls(argList):
    company = argList[0]
    site_id = argList[1]
    acl_name = argList[2]
    expectBody = body_check.companyAcls[acl_name]
    if ('siteId' in expectBody.keys()):
        expectBody['siteId'] = site_id
    res_code, bodys = ConsulInterface.get_company_acls(company)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "acls consul is {}\nand expect is {}".format(bodys, expectBody)
    assert expectBody in bodys

def check_companyRouters(argList):
    company = argList[0]
    site_id = argList[1]
    router_name = argList[2]
    next_hop = argList[3]
    expectBody = body_check.companyRouters[router_name]
    if ('siteId' in expectBody.keys()):
        expectBody['siteId'] = site_id
    expectBody['nextHop'] = next_hop
    res_code, bodys = ConsulInterface.get_company_routes(company)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "routers consul is {}\nand expect is {}".format(bodys, expectBody)
    assert expectBody in bodys

def check_anycastSearchPattern(argList):
    code = argList[0]
    expectBody = body_check.anycastSearchPattern[code]
    res_code, bodys = ConsulInterface.get_services_gaea_anycastSearchPattens()
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "anycastSearchPattern consul is {}\nand expect is {}".format(bodys, expectBody)
    assert expectBody in bodys

def check_netAlgConfig():
    expectBody = body_check.netAlgConfigBody
    res_code, body = ConsulInterface.get_services_gaea_netAlgConfig()
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "netalg consul is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, []) == True

def check_pop(argList):
    popId = argList[0]
    neId = argList[1]
    pop_expectBody = body_check.popBody[popId]
    res_code, routeCode_body = ConsulInterface.get_pop_routecode(neId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "routeCode consul is {}\nand expect is {}".format(routeCode_body, pop_expectBody["routeCode"])
    assert routeCode_body == pop_expectBody["routeCode"]
    res_code, status_body = ConsulInterface.get_pop_status(neId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "status consul is {}\nand expect is {}".format(status_body, pop_expectBody["status"])
    assert status_body == pop_expectBody["status"]

def check_pop_status(argList):
    neId = argList[0]
    status = argList[1]
    res_code, status_body = ConsulInterface.get_pop_status(neId)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "status consul is {}\nand expect is {}".format(status_body, status)
    assert status_body['status'] == status

def check_monitor_alert(argList):
    sn = argList[0]
    expected = bool(int(argList[1]))
    res_code, status_body = ConsulInterface.get_monitor_device_alert(sn)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "monitor device {} alert enable is {}\nand expect is {}".format(sn, status_body['enable'], expected)
    assert status_body['enable'] == expected

def check_cpe_auth_audit(argList):
    sn = argList[0]
    auth = argList[1]
    audit = argList[2]
    expectAuditBody = body_check.cpeAuditBody[audit]
    expectAuthBody = body_check.cpeAuthBody[auth]
    res_code, auth_body = ConsulInterface.get_device_auth(sn)
    assert res_code == 200, '{} is not 200'.format(res_code)
    res_code, audit_body = ConsulInterface.get_device_audit(sn)
    assert res_code == 200, '{} is not 200'.format(res_code)
    print "device {} auth is {} audit is {}\nand expect is auth {}audit {}".format(sn, auth_body, audit_body, expectAuthBody, expectAuditBody)
    assert are_same(expectAuthBody, auth_body, []) == True
    assert are_same(expectAuditBody, audit_body, []) == True

def check_json_file(argList):
    f1_path = argList[0]
    f2_path = argList[1]
    print "checkFile is {} and expectFile is {}".format(f1_path, f2_path)
    with io.open(f1_path, encoding='utf-8') as f1:
        f1_data = json.load(f1)
    with io.open(f2_path, encoding='utf-8') as f2:
        f2_data = json.load(f2)
    assert are_same(f1_data, f2_data, ["root['isHA']", "root['isHub']"]) == True

def call_funcion(matchFunction):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    funList = ast.literal_eval(sys.argv[1])
    for func in funList:
        if len(sys.argv) >= 3:
            matchFunction[func](sys.argv[2:])
        else:
            matchFunction[func]()

if __name__ == "__main__":
    match = \
        {
            'company': check_company,
            'encryption': check_company_encryption,
            'site': check_site,
            'siteRateLimit': check_siteRateLimit,
            'union': check_union,
            'unionRateLimit': check_unionRateLimit,
            'nePreference': check_nePreference,
            'neRateLimit':check_neRateLimit,
            'neNetConfig':check_neNetConfig,
            'wifi': check_device_system_wifi,
            'network': check_device_system_network,
            'spiTag': check_spiTag,
            'spiDispatch': check_spiDispatch,
            'manager': check_manager,
            'openflow': check_openflow,
            'saasSearchPattern': check_saasSearchPattern,
            'companySaasSearchPattern': check_companySaasSearchPattern,
            'anycastSearchPattern': check_anycastSearchPattern,
            'netAlgConfig': check_netAlgConfig,
            'pop': check_pop,
            'pop_status': check_pop_status,
            'info': check_device_aiwan_info,
            'startup': check_device_aiwan_startup,
            'acls': check_companyAcls,
            'routers': check_companyRouters,
            'cpeglobalconfigne': check_cpeglobalconfigne,
            'neAlert': check_monitor_alert,
            'neAuditAuth': check_cpe_auth_audit,
            'checkJsonFile':check_json_file
        }
    call_funcion(match)
