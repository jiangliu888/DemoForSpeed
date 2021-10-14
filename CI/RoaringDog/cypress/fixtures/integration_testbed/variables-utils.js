const default_bandwidth = 1000
const pop1_cac = "7"
const pop1_eac = "10"
const pop1_ip = "10.192.11.2"
const setupSites = ['testSTBeijing', 'testSTShanghai', 'testSTGuangzhou', 'testSTNanjing', 'testSTWuhan']
const testSiteBody = {
  testSTBeijing:{"name":"beijing","sn":"2560","tunnelNum":"4000","nets": "","location":"beijing","reportInterval":"10","scoreInterval":"10","enablePrivate":false,
  "private":["10.191.0.15/32"],"longitude":"116.352963","latitude":"40.409079",
  "type":"串联","HA":false,
  "wans":[{"name":"WAN1","mtu":"1380","bandwidth":default_bandwidth, "prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip,"staticIp":'10.192.1.15',"proxy":false, "ifname": "enp1s0f0",'ip_mode':'FIA'}],
  "lans":[{"IDC":true, 'pair': 'enp1s0f0', 'ifname': 'enp1s0f1', 'ip_mode': 'FIA'}]},
  testSTShanghai:{"name":"shanghai","sn":"2004","tunnelNum":"6868","nets": "","location":"shanghai","reportInterval":"10","scoreInterval":"10","enablePrivate":false,
  "type":"串联","HA":false,"natNet":"100.64.0.0/16","longitude":"121.48789949","latitude":"31.24916171",
  "private":["10.191.0.100/32"],
  "wans":[{"name":"WAN1","mtu":"1380","bandwidth":default_bandwidth,"prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip,"proxy":false}],
  "lans":[]},
  testSTNanjing:{"name":"nanjing","sn":"2000","tunnelNum":"8989","nets": ["172.28.42.0/24"],"location":"nanjing","reportInterval":"10","scoreInterval":"10","longitude":"118.802422","latitude":"32.064653",
  "type":"旁挂","HA":false,
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"10.192.10.2","ip_mode":"FIA","ip_type":"静态ip地址","ip":'172.31.42.5',"mask":'24',"gateway":"172.31.42.1","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip,'ifname':'enp1s0f0'}],
  "lans":[{"name":"LAN1","ip_addr":"172.30.42.5","mask":"24","gateway":"172.30.42.1","IDC":true, 'ifname': 'enp1s0f1', 'pair': 'enp1s0f0', 'ip_mode': 'FIA'}]
  },
  testSTWuhan:{"name":"wuhan","sn":"2002","tunnelNum":"0","nets": ["172.19.42.0/24"],"location":"wuhan","reportInterval":"10","scoreInterval":"10",
  "type":"旁挂","HA":false,"longitude":"114.311582","latitude":"30.598467",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"静态ip地址","ip":'172.21.42.5',"mask":'24',"gateway":"172.21.42.1","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip}],
  "lans":[{"name":"LAN1","ip_addr":"172.20.42.5","mask":"24","gateway":"172.20.42.1"}]
  },
  testSTGuangzhou:{"name":"guangzhou","sn":"2008","tunnelNum":"6868","nets": ["172.32.42.0/24"],"location":"guangzhou","reportInterval":"10","scoreInterval":"10",
  "type":"网关","HA":false,"longitude":"113.374375","latitude":"23.368923",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"静态ip地址","ip":'10.192.5.2',"mask":'24',"gateway":"10.192.5.1","bandwidth":default_bandwidth,"proxy":true,
  "prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip}],
  "lans":[{"name":"LAN1","ip_addr":"172.32.42.1","mask":"24","DHCP":false,"internet":true,"IDC":true}],
  "wifi":{"ssid":"testwifi", "network":"lan1", "encryption": "psk2", "encryption_type": "WPA2-PSK", "key":"12345678", "macfilter":"allow", "mac_list":["00:83:09:00:15:d4","00:83:09:00:15:d5"]}
  }
}

const auditParam = {
  auditUrl : 'https://139.224.41.89',
  auditUrlFail : 'https://11.224.41.89',
  auditPort : '3080',
  siteMac: '02:00:4c:4f:4f:50',
  siteMac2: '0A:00:4c:4f:4f:70',
  siteSTNanchangMac: '00:E0:67:1A:AB:E6'
}

const testUnionBody = {
  testSeriesUnions:{"unionType":"Hub-spoken","hubSite":"beijing","spokenSites":['shanghai'],
  "office":true, "private":true, "bondSpeed":1024},
  testParallelUnions:{"unionType":"Hub-spoken","hubSite":"nanjing","spokenSites":['wuhan','guangzhou'],
  "office":true, "private":false, "bondSpeed":1024}
}

const saasSearchPatternBody = {
  chinaCode: {"proxyServices":[],"neIds":[],"popIds":[],"_id":"5f3fe5a50910b1bf1ce0544d","areaCode":"0X8040000","__v":0,"area":0,"areaDes":"*","country":1,"countryDes":"China","district":0,"districtDes":"*","isp":1,"ispDes":"ChinaTelecom","region":1,"regionDes":"EastAsia","popDetailLists":[]}
}

const testPopBody = {
   testSTPop1Body:{"hostName": "lt-pop","popId":"lt-pop","cac":7,"eac":10,
   "ipAddress":[{'publicAddress':'10.192.11.2','isp':'default','ispCode':140,'iface':'enp2s0','nat':false},
   {'publicAddress':'10.192.11.2','isp':'中国电信','ispCode':11,'iface':'enp2s0','nat':false}]}
}

const testServiceBody = {
  testSTSaas1Body:{"hostName": "lt-pop","popId":"lt-pop","prefer_pop_id":326,"service":"Saas服务",'popType':8}
  }

const testCPEGlobalConfigBody = {
    ST: {
        "regUrl": "http://controller-ci2.netgrounder.com:6116/api/v1/ne/cpe",
        "authUrl": "http://authserver-ci2.netgrounder.com:7000",
        "collectdAddr": "10.192.20.210",
        "collectdPort": "6789",
        "salt": "salt-ci2.netgrounder.com",
        "prismAddr": "10.192.20.210:9877",
        "controllers": [
          {
            "domain": "controller-ci2.netgrounder.com",
            "port": 6633,
            "mode": "网关"
          },
          {
            "domain": "controller-ci2.netgrounder.com",
            "port": 6633,
            "mode": "旁挂"
          },
          {
            "domain": "controller-ci2.netgrounder.com",
            "port": 6653,
            "mode": "串联"
          }
        ]
    }
}
const unionTemplate = {
  "name": "flow-sesite-flow-sesite1",
  "companyId": "1258202a-192a-4650-a054-14585e709faa",
  "site1": "e96d21a7-a72f-44a1-972e-e9e492e44cbd",
  "site2": "c727e7f0-4675-4d58-a2d4-a8a950ab7426",
  "remark": "",
  "privateNet": false,
  "officeNet": true,
  "transportMode": "",
  "bandwidth": "10",
  "siteMessage1":{},
  "siteMessage2":{},
  "config":{}
}

const companyBodyTemplate = {
"name":"testCompany",
"address":"测试地址",
"contact":"test-phone",
"remark":"remark",
"mail":"test-mail@test.com",
"englishName":"test-Company",
"city":["中国","上海市","市辖区","浦东新区"],
"mobile":"18696198900",
"englishAddress":"test-Address",
"linkman":"test-Contact",
"config":{"algorithms":"AES-128"},
"channel":""
}

const authParam = {
  authOutUrl: 'https://10.192.20.95',
  authInnerUrl : 'https://10.192.20.91',
  authOutPort : '8006',
  authInnerPort : '8006',
  redirectUrl : 'http://www.netskyper.com',
  bindTimeout : 7199,
  noTrafficTimeout : 1799,
  radiusParam : {
    ip: '192.168.0.122',
    port: '1812',
    radiusType: 'PAP',
    radiusKey: 'authportal@2020'
  },
  ldapParam : {
    ip: '192.168.0.8',
    port: '398',
    adminAccount: 'cn=admin,dc=subao,dc=com',
    password: 'Admin123.',
    rootDN: 'dc=subao,dc=com'
  }
}

export {testCPEGlobalConfigBody, testPopBody, testServiceBody, saasSearchPatternBody, testSiteBody, companyBodyTemplate, testUnionBody, unionTemplate, auditParam, authParam, setupSites}
