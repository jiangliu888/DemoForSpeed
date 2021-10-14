# coding=utf-8
url = "http://10.192.20.67:8089"
ssh_host = '10.192.20.67'
ssh_user = 'sdn'
ssh_psd = 'rocks'
portal_user = 'admin'
portal_psd = 'AIRwalk2013!)'

companyUrl = '/api/v1/companies'
userUrl = '/api/v1/users'
managerUrl = '/api/v1/controllerManagers/12'
openflowUrl = '/api/v1/controllerOpenflows/12'
netAlgConfigUrl = '/api/v1/controllerAlgorithms/pattern'
globalConfigUrl = '/api/v1/cpeGlobal'
saasSearchPattern = '/api/v1/saasSearchPatterns'
popConfigUrl = '/api/v1/popConfigs'
popUrl = '/api/v1/pops'
cpeGlobalConfUrl = '/api/v1/cpeGlobal'
mgrGroupUrl = '/api/v1/mgr/groups'
mgrRuleUrl = '/api/v1/mgr/rules'
siteUrl = '/api/v1/channel/configs/devices'
alarmUrl = '/api/v1/channel/alerts'
bwUrl = '/api/v1/channel/metrics/bandwidth'
deviceSysUrl = '/api/v1/channel/metrics/system'
networkUrl = '/api/v1/channel/metrics/network'
auth = '/api/v1/tokens'
roleUrl = '/api/v1/roles'

Company_body1 = {
    "name": "测试公司4", "address": "测试地址", "contact": "test-phone",
    "remark": "remark", "mail": "test-mail@test.com",
    "englishName": "test-Company", "city": ["中国", "上海市", "市辖区", "浦东新区"],
    "mobile": "18696198900", "englishAddress": "test-Address", "linkman": "test-Contact",
    "config": {"algorithms": "AES-128"}, "channel": "qudao"}

Company_body2 = {"name": "111@qq.com", "address": "", "contact": "", "remark": "", "mail": "",
                 "englishName": "", "city": ["中国", "山西省", "长治市", "襄垣县"], "mobile": "",
                 "englishAddress": "", "linkman": "", "config": {"algorithms": "AES-128"}, "channel": ""}

Account_body = \
    {"username": "11@qq.com", "password": "qq!!11", "company": "", "companyId": "80e485e7-6287-43ab-848a-27375d95bf24",
     "regions": ["all"], "scopes": [], "contact": "", "admin": 'true', "enabled": 'true', "version": 0, "role": "admin",
     "channel": "", "rolesId": [], "roles": []}

'''
Account_body = \
    {   "username":"11@qq.com","password":"111qq!","company":"","companyId":"80e485e7-6287-43ab-848a-27375d95bf24",
        "regions":["all"],
        "scopes":["0","0-0","0-0-0","0-0-1","0-1","0-1-0","0-1-1","0-2","0-2-0","0-2-1","0-3","0-4","0-4-0","0-4-1",
        "0-5","0-5-0","0-5-1", "0-6","0-6-0","0-6-1","0-7","0-8","0-9","0-10","1","1-0","1-0-0","1-0-1",
        "1-1","1-1-0","1-1-1","1-2"],
        "contact":"","admin":'true',"enabled":'true',"version":0,"role":"admin","channel":"","roles":[], "rolesId": ''
    }
'''

Site_body = \
    {"name": "xxxx", "engName": "", "remark": "", "companyId": "a692529a-9a0c-4a2c-89c2-977ff884651a",
     "city": "", "engLocation": "", "location": "", "ha": 'false',
     "config": {
         "privateAddrs": "", "seriesAddrs": "", "nets": [], "cpeType": "gateway", "mtu": 1400,
         "localPort": 8989, "enabled": 'true', "sn": ["2094"],
         "wan": [{"publicIp": "", "ipType": "dhcp", "ipAddress": "", "mask": "",
                  "ipmode": "FIA", "gateway": "", "bandwidth": 10, "logicName": "", "proxy": 'true'}],
         "lan": [{"lanIp": "1.1.1.1", "mask": "24", "ethNum": 1, "internet": 'true', "idc": 'true',
                  "dhcp": 'false', "gateway": "", "dhcpSever": 'false', "dhcpPool": ""}],
         "wifi": {"ssid": "", "encryption": ["none"], "network": "",
                  "password": "", "macCheck": "", "macArr": ""},
         "fwGroups": [], "natGroups": [], "bandwidth": 10},
     "haConfig": {
         "wanipAddress1": "", "wanipAddress2": "", "wanipAddress3": "", "wanipAddress4": "",
         "wanmask1": "", "wanmask2": "", "wanmask3": "", "wanmask4": "", "wangateway1": "",
         "wangateway2": "", "wangateway3": "", "wangateway4": "", "lanIp1": "", "lanIp2": "",
         "lanIpMask1": "", "lanIpMask2": "", "reportInterval": 60, "scoreInterval": 60,
         "enableLte": 'false', "lteName": "wwan0", "usage": "backup",
         "exportRule": [{"cidr": "", "action": "permit", "metric": 200}],
         "metric": 100, "importRuleCidr": ""},
     "sideHanging": 'false', "sideHangingSn": ""}

alarm_body = \
    {
        "alertId": "aaa100",
        "name": "NodeOffline", "code": "0108", "status": "firing", "severity": "Emergency",
        "startsAt": "2021-04-24T12:39:50.270397731+08:00", "updatesAt": "2021-04-24T12:40:30.275103409+08:00",
        "endsAt": "2021-04-24T12:50:22.07127243+08:00",
        "labels": {
            "companyId": "1793bde6-e667-4a96-b871-46801b0702be",
            "neId": "500", "severity": "Emergency",
            "siteName": "efg", "alertCode": "", "alertname": "NodeOffline",
            "companyName": "测试公司3", "deviceId": "2099"},
        "annotations": {"description": "site1-cpe : hardware self test fail, error code 1."},
        "url": "site1-cpe_CpeHardwareError", "companyId": "a692529a-9a0c-4a2c-89c2-977ff884651a", "deviceId": "2099"
    }

role_body = \
    {
        "roleId": "", "companyId": "80e485e7-6287-43ab-848a-27375d95bf24", "regions": [],
        "scopes": [
            "0", "0-0", "0-0-0", "0-0-1", "0-1", "0-1-0", "0-1-1", "0-2", "0-2-0", "0-2-1", "0-3",
            "0-4", "0-4-0", "0-4-1", "0-5", "0-5-0", "0-5-1", "0-6", "0-6-0", "0-6-1", "0-7", "0-8",
            "0-9", "0-10", "1", "1-0", "1-0-0", "1-0-1", "1-1", "1-1-0", "1-1-1", "1-2"
        ],
        "desc": "test", "extra": {}, "role": "test", "createdAt": "2021-07-01T03:24:29.394Z", "company": ""
    }
