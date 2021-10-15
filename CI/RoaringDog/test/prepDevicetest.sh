echo "--------Remove sites for device companies."
mongo --host mongo insight --eval 'db.sites.remove({"companyId":"d0dbee8c-1bb8-432b-8c05-a1b48be094b5"})'
mongo --host mongo insight --eval 'db.sites.remove({"companyId":"9e7a0cef-7b8c-41eb-af35-d0f80e6a4c1a"})'
echo "--------Remove sites' assets for device companies."
mongo --host mongo insight --eval 'db.assets.remove({"sn" : "3001"})'
mongo --host mongo insight --eval 'db.assets.remove({"sn" : "3002"})'
mongo --host mongo insight --eval 'db.assets.remove({"sn" : "3003"})'
mongo --host mongo insight --eval 'db.assets.remove({"sn" : "3004"})'
mongo --host mongo insight --eval 'db.assets.remove({"sn" : "3005"})'
mongo --host mongo insight --eval 'db.assets.remove({"sn" : "3006"})'
mongo --host mongo insight --eval 'db.assets.remove({"sn" : "pany12-"})'
echo "--------Remove sites'globalneids for device companies."
mongo --host mongo insight --eval 'db.globalneids.remove({"sn" : "3001"})'
mongo --host mongo insight --eval 'db.globalneids.remove({"sn" : "3002"})'
mongo --host mongo insight --eval 'db.globalneids.remove({"sn" : "3003"})'
mongo --host mongo insight --eval 'db.globalneids.remove({"sn" : "3004"})'
mongo --host mongo insight --eval 'db.globalneids.remove({"sn" : "3005"})'
mongo --host mongo insight --eval 'db.globalneids.remove({"sn" : "3006"})'
mongo --host mongo insight --eval 'db.globalneids.remove({"sn" : "pany12-"})'
echo "--------Remove pops for device test."
mongo --host mongo insight --eval 'db.popconfigs.remove({"neId" : 998})'
mongo --host mongo insight --eval 'db.popconfigs.remove({"neId" : 1014})'
mongo --host mongo insight --eval 'db.companies.remove({"companyId":"d0dbee8c-1bb8-432b-8c05-a1b48be094b5"})'
mongo --host mongo insight --eval 'db.companies.remove({"companyId":"9e7a0cef-7b8c-41eb-af35-d0f80e6a4c1a"})'
echo "--------Remove pops' globalneids for device test."
mongo --host mongo insight --eval 'db.globalneids.remove({"sn" : "X30000"})'
mongo --host mongo insight --eval 'db.globalneids.remove({"sn" : "X30001"})'
# create companies
echo "--------Create device companies."
mongo --host mongo insight --eval 'db.companies.insert({ "_id" : ObjectId("6124a17e8775c0622bb1b277"), "city" : [ "中国", "上海市", "市辖区", "浦东新区" ], "companyId" : "d0dbee8c-1bb8-432b-8c05-a1b48be094b5", "name" : "Distributor-company", "address" : "测试地址", "contact" : "test-phone", "remark" : "remark", "mail" : "test-mail@test.com", "createdAt" : ISODate("2021-08-24T07:36:30.549Z"), "englishName" : "test-Company", "mobile" : "18696198900", "englishAddress" : "test-Address", "linkman" : "test-Contact", "config" : { "algorithms" : "AES-128" }, "channel" : "Distributor", "version" : 1, "__v" : 0 })'
mongo --host mongo insight --eval 'db.companies.insert({ "_id" : ObjectId("6124a17e8775c0622bb1b27b"), "city" : [ "中国", "上海市", "市辖区", "浦东新区" ], "companyId" : "9e7a0cef-7b8c-41eb-af35-d0f80e6a4c1a", "name" : "Distributor-company12", "address" : "测试地址", "contact" : "test-phone", "remark" : "remark", "mail" : "test-mail@test.com", "createdAt" : ISODate("2021-08-24T07:36:30.796Z"), "englishName" : "test-Company", "mobile" : "18696198900", "englishAddress" : "test-Address", "linkman" : "test-Contact", "config" : { "algorithms" : "AES-128" }, "channel" : "Distributor", "version" : 1, "__v" : 0 })'
# create pops
echo "--------Create pops for device test."
mongo --host mongo insight --eval 'db.popconfigs.insert({ "_id" : ObjectId("6124a17d8775c0622bb1b272"), "saasServices" : [ ], "neId" : 998, "popId" : "X30000", "status" : "NORMAL", "routeCode" : { "type" : "ER", "cac" : 12, "eac" : 11 }, "popType" : 6, "message" : { "hostname" : "device-pop" }, "__v" : 0 })'
mongo --host mongo insight --eval 'db.globalneids.insert({ "_id" : ObjectId("6124a17d8775c0622bb1b271"), "type" : 6, "sn" : "X30000", "neid" : 998, "__v" : 0 })'
mongo --host mongo insight --eval 'db.popconfigs.insert({ "_id" : ObjectId("6124a17e8775c0622bb1b275"), "saasServices" : [ ], "neId" : 1014, "popId" : "X30001", "status" : "NORMAL", "routeCode" : { "type" : "ER", "cac" : 10, "eac" : 3 }, "popType" : 6, "message" : { "hostname" : "device-pop2" }, "__v" : 0 })'
mongo --host mongo insight --eval 'db.globalneids.insert({ "_id" : ObjectId("6124a17e8775c0622bb1b274"), "type" : 6, "sn" : "X30001", "neid" : 1014, "__v" : 0 })'
# create sites
echo "--------Create site distributor-sesite 3001 for device companies."
mongo --host mongo insight --eval 'db.sites.insert({ "_id" : ObjectId("6124a17f8775c0622bb1b282"), "name" : "distributor-sesite", "remark" : "remart", "companyId" : "d0dbee8c-1bb8-432b-8c05-a1b48be094b5", "city" : "", "location" : "se-location", "ha" : false, "config" : { "privateAddrs" : "", "seriesAddrs" : "10.193.0.0/26\n10.193.0.64/27\n10.193.0.96/30\n10.193.0.100/32", "nets" : [ ], "cpeType" : "series", "mtu" : 1400, "localPort" : 8989, "enabled" : true, "sn" : [ "3001" ], "wan" : [ { "publicIp" : "", "ipType" : "", "ipAddress" : "", "mask" : "", "ipmode" : "FIA", "gateway" : "", "bandwidth" : 10, "logicName" : "", "proxy" : true, "preferGroup" : "101", "preferCac" : "4", "preferHomeCodeCac" : "4", "preferHomeCodeEac" : "5", "preferIP" : "10.192.20.4", "gatewayMac" : "11:22:33:44:55:66", "staticIp" : "10.192.20.1" } ], "lan" : [ { "lanIp" : "", "mask" : "", "ethNum" : 1, "internet" : true, "idc" : true, "dhcp" : false, "gateway" : "", "dhcpSever" : false, "dhcpPool" : "" } ], "wifi" : { "ssid" : "", "encryption" : [ "none" ], "network" : "", "password" : "", "macCheck" : "", "macArr" : "" }, "fwGroups" : [ ], "natGroups" : [ ], "bandwidth" : 10, "neid" : 65424 }, "haConfig" : { "wanipAddress1" : "", "wanipAddress2" : "", "wanmask1" : "", "wanmask2" : "", "wangateway1" : "", "wangateway2" : "", "lanIp1" : "", "lanIp2" : "", "lanIpMask1" : "", "lanIpMask2" : "", "reportInterval" : 60, "scoreInterval" : 60, "enableLte" : true, "lteName" : "wwan0", "enableInterflow" : true, "isHub" : false, "longitude" : "115.95046", "latitude" : "28.551604", "exportRule" : [ { "cidr" : "", "action" : "permit", "metric" : 200 } ], "metric" : 100, "preferHomeCodeCac" : "10", "preferHomeCodeEac" : "3" }, "sideHanging" : false, "sideHangingSn" : "", "siteId" : "215823d6-ea71-4b87-98ff-eb51eac85447", "createdAt" : ISODate("2021-08-24T07:36:31.624Z"), "__v" : 0 })'
# assets
mongo --host mongo insight --eval 'db.assets.insert({ "_id" : ObjectId("6124a17f8775c0622bb1b280"), "id" : "3001", "sn" : "3001", "siteId" : "215823d6-ea71-4b87-98ff-eb51eac85447", "companyId" : "d0dbee8c-1bb8-432b-8c05-a1b48be094b5", "city" : "", "enabled" : true, "message" : { "url" : "http://10.194.20.105:8000/api/v1/assets/devices/3001", "model" : "BX3000-4GE-L", "hardware" : "", "ifnames" : [ "enp1s0f0", "enp1s0f1", "enp1s0f2", "enp1s0f3" ], "sn" : "3001", "os" : "Ubuntu", "state" : "MANUFACTURED", "manufacturer" : "SUBAO", "location" : null, "iccid" : null, "seid" : null, "mac" : null, "manufacturerAt" : null }, "createdAt" : ISODate("2021-08-24T07:36:31.582Z"), "__v" : 0, "disableAlert" : false })'
# globalneids
mongo --host mongo insight --eval 'db.globalneids.insert({ "_id" : ObjectId("6124a17f8775c0622bb1b281"), "type" : 0, "sn" : "3001", "neid" : 65424, "__v" : 0 })'

echo "--------Create site distributor-pasite 3002 for device companies."
mongo --host mongo insight --eval 'db.sites.insert({ "_id" : ObjectId("6124a1808775c0622bb1b287"), "name" : "distributor-pasite", "remark" : "pa remark", "companyId" : "d0dbee8c-1bb8-432b-8c05-a1b48be094b5", "city" : "", "location" : "pa location", "ha" : false, "config" : { "privateAddrs" : "172.19.14.0/24", "seriesAddrs" : "", "nets" : [ ], "cpeType" : "parallel", "mtu" : 1400, "localPort" : 8989, "enabled" : true, "sn" : [ "3002" ], "wan" : [ { "publicIp" : "10.194.14.2", "ipType" : "static", "ipAddress" : "172.20.14.25", "mask" : "24", "ipmode" : "FIA", "gateway" : "172.20.14.1", "bandwidth" : "1000", "logicName" : "", "proxy" : true, "preferHomeCodeCac" : "4", "preferGroup" : "103", "preferHomeCodeEac" : "4", "preferIP" : "10.194.20.4" }, { "ipmode" : "FIA", "proxy" : true, "publicIp" : "10.196.14.2", "ipType" : "static", "ipAddress" : "172.20.14.26", "mask" : "24", "gateway" : "172.20.14.1", "bandwidth" : "1000", "preferGroup" : "", "preferCac" : "4", "preferHomeCodeCac" : "4", "preferHomeCodeEac" : "5", "preferIP" : "10.194.20.3" } ], "lan" : [ { "lanIp" : "172.21.14.25", "mask" : "24", "ethNum" : 1, "internet" : true, "idc" : true, "dhcp" : false, "gateway" : "172.21.14.1", "dhcpSever" : false, "dhcpPool" : "" } ], "wifi" : { "ssid" : "", "encryption" : [ "none" ], "network" : "", "password" : "", "macCheck" : "", "macArr" : "" }, "fwGroups" : [ ], "natGroups" : [ ], "bandwidth" : 10, "neid" : 65440 }, "haConfig" : { "wanipAddress1" : "", "wanipAddress2" : "", "wanmask1" : "", "wanmask2" : "", "wangateway1" : "", "wangateway2" : "", "lanIp1" : "", "lanIp2" : "", "lanIpMask1" : "", "lanIpMask2" : "", "reportInterval" : 60, "scoreInterval" : 60, "enableLte" : false, "lteName" : "wwan0", "isHub" : false, "longitude" : "115.95046", "latitude" : "28.551604" }, "sideHanging" : false, "sideHangingSn" : "", "siteId" : "df6975cf-f412-4fd6-8f84-fd307d956b41", "createdAt" : ISODate("2021-08-24T07:36:32.680Z"), "__v" : 0 })'
mongo --host mongo insight --eval 'db.assets.insert({ "_id" : ObjectId("6124a1808775c0622bb1b285"), "id" : "3002", "sn" : "3002", "siteId" : "df6975cf-f412-4fd6-8f84-fd307d956b41", "companyId" : "d0dbee8c-1bb8-432b-8c05-a1b48be094b5", "city" : "", "enabled" : true, "message" : { "url" : "http://10.194.20.105:8000/api/v1/assets/devices/3002", "model" : "BX3000-4GE-L", "hardware" : "", "ifnames" : [ "enp1s0f0", "enp1s0f1", "enp1s0f2", "enp1s0f3" ], "sn" : "3002", "os" : "Ubuntu", "state" : "MANUFACTURED", "manufacturer" : "SUBAO", "location" : null, "iccid" : null, "seid" : null, "mac" : null, "manufacturerAt" : null }, "createdAt" : ISODate("2021-08-24T07:36:32.644Z"), "__v" : 0, "disableAlert" : false })'
mongo --host mongo insight --eval 'db.globalneids.insert({ "_id" : ObjectId("6124a1808775c0622bb1b286"), "type" : 0, "sn" : "3002", "neid" : 65440, "__v" : 0 })'
echo "--------Create site distributor-gwsite 3003 for device companies."
mongo --host mongo insight --eval 'db.sites.insert({ "_id" : ObjectId("6124a1818775c0622bb1b28c"), "name" : "distributor-gwsite", "remark" : "gw remark", "companyId" : "d0dbee8c-1bb8-432b-8c05-a1b48be094b5", "city" : "", "location" : "guanghzou", "ha" : false, "config" : { "privateAddrs" : "172.19.43.0/24", "seriesAddrs" : "", "nets" : [ ], "cpeType" : "gateway", "mtu" : 1400, "localPort" : 8989, "enabled" : true, "sn" : [ "3003" ], "wan" : [ { "publicIp" : "", "ipType" : "dhcp", "ipAddress" : "", "mask" : "", "ipmode" : "FIA", "gateway" : "", "bandwidth" : 10, "logicName" : "", "proxy" : true, "preferGroup" : "101 102", "preferCac" : "4", "preferHomeCodeCac" : "4", "preferHomeCodeEac" : "5", "preferIP" : "10.192.20.3" }, { "ipmode" : "FIA", "proxy" : true, "ipType" : "static", "ipAddress" : "10.194.12.2", "mask" : "24", "gateway" : "10.194.12.1", "bandwidth" : "1000", "preferGroup" : "102", "preferCac" : "4", "preferHomeCodeCac" : "4", "preferHomeCodeEac" : "4", "preferIP" : "10.194.20.3" } ], "lan" : [ { "lanIp" : "172.19.43.1", "mask" : "24", "ethNum" : "4", "internet" : true, "idc" : true, "dhcp" : false, "gateway" : "172.19.43.1", "dhcpSever" : false, "dhcpPool" : "" }, { "lanIp" : "192.168.1.1", "mask" : "24", "gateway" : "192.168.1.1", "dhcpSever" : true, "dhcpPool" : "192.168.1.2\n192.168.1.9", "ethNum" : "1" } ], "wifi" : { "ssid" : "testwifi", "encryption" : [ "22", "psk2" ], "network" : "lan1", "password" : "12345678", "macCheck" : "allow", "macArr" : "00:83:09:00:15:d4\n00:83:09:00:15:d5" }, "fwGroups" : [ ], "natGroups" : [ ], "bandwidth" : 10, "neid" : 65457 }, "haConfig" : { "wanipAddress1" : "", "wanipAddress2" : "", "wanmask1" : "", "wanmask2" : "", "wangateway1" : "", "wangateway2" : "", "lanIp1" : "", "lanIp2" : "", "lanIpMask1" : "", "lanIpMask2" : "", "reportInterval" : 60, "scoreInterval" : 60, "enableLte" : false, "lteName" : "wwan0", "natNet" : "100.64.0.0/16", "isHub" : false, "longitude" : "115.95046", "latitude" : "28.551604", "exportRule" : [ { "cidr" : "", "action" : "permit", "metric" : 200 } ], "metric" : 100 }, "sideHanging" : false, "sideHangingSn" : "", "siteId" : "cacb7677-17d2-459b-bb17-dcd86a1c9d73", "createdAt" : ISODate("2021-08-24T07:36:33.431Z"), "__v" : 0 })'
mongo --host mongo insight --eval 'db.assets.insert({ "_id" : ObjectId("6124a1818775c0622bb1b28a"), "id" : "3003", "sn" : "3003", "siteId" : "cacb7677-17d2-459b-bb17-dcd86a1c9d73", "companyId" : "d0dbee8c-1bb8-432b-8c05-a1b48be094b5", "city" : "", "enabled" : true, "message" : { "url" : "http://10.194.20.105:8000/api/v1/assets/devices/3003", "model" : "BX1000-X4GE", "hardware" : "", "ifnames" : [ ], "sn" : "3003", "os" : "OpenWrt", "state" : "MANUFACTURED", "manufacturer" : "intel", "location" : null, "iccid" : null, "seid" : null, "mac" : null, "manufacturerAt" : null }, "createdAt" : ISODate("2021-08-24T07:36:33.400Z"), "__v" : 0, "disableAlert" : false })'
mongo --host mongo insight --eval 'db.globalneids.insert({ "_id" : ObjectId("6124a1818775c0622bb1b28b"), "type" : 1, "sn" : "3003", "neid" : 65457, "__v" : 0 })'
echo "--------Create site distributor-gwsite2 pany12- for device companies."
mongo --host mongo insight --eval 'db.sites.insert({ "_id" : ObjectId("6124a1828775c0622bb1b291"), "name" : "distributor-gwsite2", "remark" : "gw remark", "companyId" : "d0dbee8c-1bb8-432b-8c05-a1b48be094b5", "city" : "", "location" : "guanghzou", "ha" : false, "config" : { "privateAddrs" : "172.19.44.0/24", "seriesAddrs" : "", "nets" : [ ], "cpeType" : "gateway", "mtu" : 1400, "localPort" : 8989, "enabled" : true, "sn" : [ "pany12-" ], "wan" : [ { "publicIp" : "", "ipType" : "dhcp", "ipAddress" : "", "mask" : "", "ipmode" : "FIA", "gateway" : "", "bandwidth" : 10, "logicName" : "", "proxy" : true, "preferGroup" : "101 102", "preferCac" : "4", "preferHomeCodeCac" : "4", "preferHomeCodeEac" : "5", "preferIP" : "10.192.20.3" }, { "ipmode" : "FIA", "proxy" : true, "ipType" : "static", "ipAddress" : "10.194.12.2", "mask" : "24", "gateway" : "10.194.12.1", "bandwidth" : "1000", "preferGroup" : "102", "preferCac" : "4", "preferHomeCodeCac" : "4", "preferHomeCodeEac" : "4", "preferIP" : "10.194.20.3" } ], "lan" : [ { "lanIp" : "172.19.44.1", "mask" : "24", "ethNum" : "4", "internet" : true, "idc" : true, "dhcp" : false, "gateway" : "172.19.44.1", "dhcpSever" : false, "dhcpPool" : "" }, { "lanIp" : "192.168.1.1", "mask" : "24", "gateway" : "192.168.1.1", "dhcpSever" : true, "dhcpPool" : "192.168.1.2\n192.168.1.9", "ethNum" : "1" } ], "wifi" : { "ssid" : "testwifi", "encryption" : [ "22", "psk2" ], "network" : "lan1", "password" : "12345678", "macCheck" : "allow", "macArr" : "00:83:09:00:15:d4\n00:83:09:00:15:d5" }, "fwGroups" : [ ], "natGroups" : [ ], "bandwidth" : 10, "neid" : 65472 }, "haConfig" : { "wanipAddress1" : "", "wanipAddress2" : "", "wanmask1" : "", "wanmask2" : "", "wangateway1" : "", "wangateway2" : "", "lanIp1" : "", "lanIp2" : "", "lanIpMask1" : "", "lanIpMask2" : "", "reportInterval" : 60, "scoreInterval" : 60, "enableLte" : true, "lteName" : "wwan0", "natNet" : "100.64.0.0/16", "isHub" : false, "longitude" : "115.95046", "latitude" : "28.551604", "exportRule" : [ { "cidr" : "", "action" : "permit", "metric" : 200 } ], "metric" : 100 }, "sideHanging" : false, "sideHangingSn" : "", "siteId" : "ef9d921e-586b-42a2-af2b-ef3e14536979", "createdAt" : ISODate("2021-08-24T07:36:34.206Z"), "__v" : 0 })'
mongo --host mongo insight --eval 'db.assets.insert({ "_id" : ObjectId("6124a1828775c0622bb1b28f"), "id" : "pany12-", "sn" : "pany12-", "siteId" : "ef9d921e-586b-42a2-af2b-ef3e14536979", "companyId" : "d0dbee8c-1bb8-432b-8c05-a1b48be094b5", "city" : "", "enabled" : true, "message" : { "url" : "http://10.194.20.105:8000/api/v1/assets/devices/pany12-", "model" : "BX3000-4GE-L", "hardware" : "", "ifnames" : [ "enp1s0f0", "enp1s0f1", "enp1s0f2", "enp1s0f3" ], "sn" : "pany12-", "os" : "Ubuntu", "state" : "MANUFACTURED", "manufacturer" : "SUBAO", "location" : null, "iccid" : null, "seid" : null, "mac" : null, "manufacturerAt" : null }, "createdAt" : ISODate("2021-08-24T07:36:34.146Z"), "__v" : 0, "disableAlert" : false })'
mongo --host mongo insight --eval 'db.globalneids.insert({ "_id" : ObjectId("6124a1828775c0622bb1b290"), "type" : 0, "sn" : "pany12-", "neid" : 65472, "__v" : 0 })'
echo "--------Create site distributor2-sesite 3004 for device companies."
mongo --host mongo insight --eval 'db.sites.insert({ "_id" : ObjectId("6124a1828775c0622bb1b296"), "name" : "distributor2-sesite", "remark" : "remart", "companyId" : "9e7a0cef-7b8c-41eb-af35-d0f80e6a4c1a", "city" : "", "location" : "se-location", "ha" : false, "config" : { "privateAddrs" : "", "seriesAddrs" : "10.193.0.0/26\n10.193.0.64/27\n10.193.0.96/30\n10.193.0.100/32", "nets" : [ ], "cpeType" : "series", "mtu" : 1400, "localPort" : 8989, "enabled" : true, "sn" : [ "3004" ], "wan" : [ { "publicIp" : "", "ipType" : "", "ipAddress" : "", "mask" : "", "ipmode" : "FIA", "gateway" : "", "bandwidth" : 10, "logicName" : "", "proxy" : true, "preferGroup" : "101", "preferCac" : "4", "preferHomeCodeCac" : "4", "preferHomeCodeEac" : "5", "preferIP" : "10.192.20.4", "gatewayMac" : "11:22:33:44:55:66", "staticIp" : "10.192.20.1" } ], "lan" : [ { "lanIp" : "", "mask" : "", "ethNum" : 1, "internet" : true, "idc" : true, "dhcp" : false, "gateway" : "", "dhcpSever" : false, "dhcpPool" : "" } ], "wifi" : { "ssid" : "", "encryption" : [ "none" ], "network" : "", "password" : "", "macCheck" : "", "macArr" : "" }, "fwGroups" : [ ], "natGroups" : [ ], "bandwidth" : 10, "neid" : 65488 }, "haConfig" : { "wanipAddress1" : "", "wanipAddress2" : "", "wanmask1" : "", "wanmask2" : "", "wangateway1" : "", "wangateway2" : "", "lanIp1" : "", "lanIp2" : "", "lanIpMask1" : "", "lanIpMask2" : "", "reportInterval" : 60, "scoreInterval" : 60, "enableLte" : false, "lteName" : "wwan0", "enableInterflow" : true, "isHub" : false, "longitude" : "115.95046", "latitude" : "28.551604" }, "sideHanging" : false, "sideHangingSn" : "", "siteId" : "058b0cb5-c4e3-48f8-9b15-5f17465b743b", "createdAt" : ISODate("2021-08-24T07:36:34.964Z"), "__v" : 0 })'
mongo --host mongo insight --eval 'db.assets.insert({ "_id" : ObjectId("6124a1828775c0622bb1b294"), "id" : "3004", "sn" : "3004", "siteId" : "058b0cb5-c4e3-48f8-9b15-5f17465b743b", "companyId" : "9e7a0cef-7b8c-41eb-af35-d0f80e6a4c1a", "city" : "", "enabled" : true, "message" : { "url" : "http://10.194.20.105:8000/api/v1/assets/devices/3004", "model" : "BX3000-4GE-L", "hardware" : "", "ifnames" : [ "enp1s0f0", "enp1s0f1", "enp1s0f2", "enp1s0f3" ], "sn" : "3004", "os" : "Ubuntu", "state" : "MANUFACTURED", "manufacturer" : "SUBAO", "location" : null, "iccid" : null, "seid" : null, "mac" : null, "manufacturerAt" : null }, "createdAt" : ISODate("2021-08-24T07:36:34.925Z"), "__v" : 0 })'
mongo --host mongo insight --eval 'db.globalneids.insert({ "_id" : ObjectId("6124a1828775c0622bb1b295"), "type" : 0, "sn" : "3004", "neid" : 65488, "__v" : 0 })'
echo "--------Create site distributor2-pasite 3005 for device companies."
mongo --host mongo insight --eval 'db.sites.insert({ "_id" : ObjectId("6124a1838775c0622bb1b29b"), "name" : "distributor2-pasite", "remark" : "pa remark", "companyId" : "9e7a0cef-7b8c-41eb-af35-d0f80e6a4c1a", "city" : "", "location" : "pa location", "ha" : false, "config" : { "privateAddrs" : "172.19.14.0/24", "seriesAddrs" : "", "nets" : [ ], "cpeType" : "parallel", "mtu" : 1400, "localPort" : 8989, "enabled" : true, "sn" : [ "3005" ], "wan" : [ { "publicIp" : "10.194.14.2", "ipType" : "static", "ipAddress" : "172.20.14.25", "mask" : "24", "ipmode" : "FIA", "gateway" : "172.20.14.1", "bandwidth" : "1000", "logicName" : "", "proxy" : true, "preferHomeCodeCac" : "4", "preferGroup" : "103", "preferHomeCodeEac" : "4", "preferIP" : "10.194.20.4" }, { "ipmode" : "FIA", "proxy" : true, "publicIp" : "10.196.14.2", "ipType" : "static", "ipAddress" : "172.20.14.26", "mask" : "24", "gateway" : "172.20.14.1", "bandwidth" : "1000", "preferGroup" : "", "preferCac" : "4", "preferHomeCodeCac" : "4", "preferHomeCodeEac" : "5", "preferIP" : "10.194.20.3" } ], "lan" : [ { "lanIp" : "172.21.14.25", "mask" : "24", "ethNum" : 1, "internet" : true, "idc" : true, "dhcp" : false, "gateway" : "172.21.14.1", "dhcpSever" : false, "dhcpPool" : "" } ], "wifi" : { "ssid" : "", "encryption" : [ "none" ], "network" : "", "password" : "", "macCheck" : "", "macArr" : "" }, "fwGroups" : [ ], "natGroups" : [ ], "bandwidth" : 10, "neid" : 65504 }, "haConfig" : { "wanipAddress1" : "", "wanipAddress2" : "", "wanmask1" : "", "wanmask2" : "", "wangateway1" : "", "wangateway2" : "", "lanIp1" : "", "lanIp2" : "", "lanIpMask1" : "", "lanIpMask2" : "", "reportInterval" : 60, "scoreInterval" : 60, "enableLte" : false, "lteName" : "wwan0", "isHub" : false, "longitude" : "115.95046", "latitude" : "28.551604" }, "sideHanging" : false, "sideHangingSn" : "", "siteId" : "c6ea3cdf-63bc-4169-b690-58d3e3b76207", "createdAt" : ISODate("2021-08-24T07:36:35.564Z"), "__v" : 0 })'
mongo --host mongo insight --eval 'db.assets.insert({ "_id" : ObjectId("6124a1838775c0622bb1b299"), "id" : "3005", "sn" : "3005", "siteId" : "c6ea3cdf-63bc-4169-b690-58d3e3b76207", "companyId" : "9e7a0cef-7b8c-41eb-af35-d0f80e6a4c1a", "city" : "", "enabled" : true, "message" : { "url" : "http://10.194.20.105:8000/api/v1/assets/devices/3005", "model" : "BX3000-4GE-L", "hardware" : "", "ifnames" : [ "enp1s0f0", "enp1s0f1", "enp1s0f2", "enp1s0f3" ], "sn" : "3005", "os" : "Ubuntu", "state" : "MANUFACTURED", "manufacturer" : "SUBAO", "location" : null, "iccid" : null, "seid" : null, "mac" : null, "manufacturerAt" : null }, "createdAt" : ISODate("2021-08-24T07:36:35.532Z"), "__v" : 0 })'
mongo --host mongo insight --eval 'db.globalneids.insert({ "_id" : ObjectId("6124a1838775c0622bb1b29a"), "type" : 0, "sn" : "3005", "neid" : 65504, "__v" : 0 })'
echo "--------Create site distributor2-gwsite 3006 for device companies."
mongo --host mongo insight --eval 'db.sites.insert({ "_id" : ObjectId("6124a1848775c0622bb1b2a0"), "name" : "distributor2-gwsite", "remark" : "gw remark", "companyId" : "9e7a0cef-7b8c-41eb-af35-d0f80e6a4c1a", "city" : "", "location" : "guanghzou", "ha" : false, "config" : { "privateAddrs" : "172.19.45.0/24", "seriesAddrs" : "", "nets" : [ ], "cpeType" : "gateway", "mtu" : 1400, "localPort" : 8989, "enabled" : true, "sn" : [ "3006" ], "wan" : [ { "publicIp" : "", "ipType" : "dhcp", "ipAddress" : "", "mask" : "", "ipmode" : "FIA", "gateway" : "", "bandwidth" : 10, "logicName" : "", "proxy" : true, "preferGroup" : "101 102", "preferCac" : "4", "preferHomeCodeCac" : "4", "preferHomeCodeEac" : "5", "preferIP" : "10.192.20.3" }, { "ipmode" : "FIA", "proxy" : true, "ipType" : "static", "ipAddress" : "10.194.12.2", "mask" : "24", "gateway" : "10.194.12.1", "bandwidth" : "1000", "preferGroup" : "102", "preferCac" : "4", "preferHomeCodeCac" : "4", "preferHomeCodeEac" : "4", "preferIP" : "10.194.20.3" } ], "lan" : [ { "lanIp" : "172.19.45.1", "mask" : "24", "ethNum" : "4", "internet" : true, "idc" : true, "dhcp" : false, "gateway" : "172.19.45.1", "dhcpSever" : false, "dhcpPool" : "" }, { "lanIp" : "192.168.1.1", "mask" : "24", "gateway" : "192.168.1.1", "dhcpSever" : true, "dhcpPool" : "192.168.1.2\n192.168.1.9", "ethNum" : "1" } ], "wifi" : { "ssid" : "testwifi", "encryption" : [ "22", "psk2" ], "network" : "lan1", "password" : "12345678", "macCheck" : "allow", "macArr" : "00:83:09:00:15:d4\n00:83:09:00:15:d5" }, "fwGroups" : [ ], "natGroups" : [ ], "bandwidth" : 10, "neid" : 65521 }, "haConfig" : { "wanipAddress1" : "", "wanipAddress2" : "", "wanmask1" : "", "wanmask2" : "", "wangateway1" : "", "wangateway2" : "", "lanIp1" : "", "lanIp2" : "", "lanIpMask1" : "", "lanIpMask2" : "", "reportInterval" : 60, "scoreInterval" : 60, "enableLte" : true, "lteName" : "wwan0", "natNet" : "100.64.0.0/16", "isHub" : false, "longitude" : "115.95046", "latitude" : "28.551604" }, "sideHanging" : false, "sideHangingSn" : "", "siteId" : "65b7f185-4332-4e99-9594-b32a060607d4", "createdAt" : ISODate("2021-08-24T07:36:36.289Z"), "__v" : 0 })'
mongo --host mongo insight --eval 'db.assets.insert({ "_id" : ObjectId("6124a1848775c0622bb1b29e"), "id" : "3006", "sn" : "3006", "siteId" : "65b7f185-4332-4e99-9594-b32a060607d4", "companyId" : "9e7a0cef-7b8c-41eb-af35-d0f80e6a4c1a", "city" : "", "enabled" : true, "message" : { "url" : "http://10.194.20.105:8000/api/v1/assets/devices/3006", "model" : "BX1000-X4GE", "hardware" : "", "ifnames" : [ ], "sn" : "3006", "os" : "OpenWrt", "state" : "MANUFACTURED", "manufacturer" : "intel", "location" : null, "iccid" : null, "seid" : null, "mac" : null, "manufacturerAt" : null }, "createdAt" : ISODate("2021-08-24T07:36:36.242Z"), "__v" : 0 })'
mongo --host mongo insight --eval 'db.globalneids.insert({ "_id" : ObjectId("6124a1848775c0622bb1b29f"), "type" : 1, "sn" : "3006", "neid" : 65521, "__v" : 0 })'

echo "--------Remove logs for all companies."
mongo --host mongo insight --eval 'db.logs.remove({"companyId":"d0dbee8c-1bb8-432b-8c05-a1b48be094b5"})'
mongo --host mongo insight --eval 'db.logs.remove({"companyId":"9e7a0cef-7b8c-41eb-af35-d0f80e6a4c1a"})'



