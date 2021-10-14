companyId=$1
neId1=$2
neId2=$3
neId3=$4
mongo --host mongo prism --eval "db.dropDatabase()"
mongo --host mongo prism --eval "db.alert.insert({ '_id' : ObjectId('5fbcd4f053afe7f9b7cb643a'), 'alertId' : '71b93a3ecb05dbb707f1930234574e788ccbb9edf92e158ca348fd3654e95a13', 'name' : 'OnlyMobile', 'code' : '0304', 'status' : 'firing', 'severity' : 'Warning', 'startsAt' : '2020-11-24T17:39:50.270397731+08:00', 'updatesAt' : '2020-11-24T17:40:30.275103409+08:00', 'endsAt' : '2020-11-24T17:40:22.07127243+08:00', 'labels' : { 'companyId' : '$companyId', 'hostname' : 'site1-cpe', 'instance' : 'Collectd Sever Alert', 'env' : 'test env', 'neId' : '$neId1', 'severity' : 'Warning', 'siteId' : '143809eb-6490-49ae-89ad-2ce296def6db', 'siteName' : 'dashBoard-gw1site', 'alertname' : 'OnlyMobile', 'companyName' : 'CompanyDashBoard', 'deviceId' : '3011' }, 'annotations' : { 'description' : 'site1-cpe : hardware self test fail, error code 1.', 'summary' : 'site1-cpe : hardware error.' }, 'url' : 'site1-cpe_CpeHardwareError', 'companyId' : '$companyId', 'deviceId' : '3011' })"
mongo --host mongo prism --eval "db.alert.insert({ '_id' : ObjectId('5fbcd4f053afe7f9b7cb6431'), 'alertId' : '71b93a3ecb05dbb707f1930234574e788ccbb9edf92e158ca348fd3654e95a14', 'name' : 'WanLinkDown', 'code' : '0305', 'status' : 'firing', 'severity' : 'Critical', 'startsAt' : '2020-11-24T17:39:50.270397731+08:00', 'updatesAt' : '2020-11-24T17:40:30.275103409+08:00', 'endsAt' : '2020-11-24T17:40:22.07127243+08:00', 'labels' : { 'companyId' : '$companyId', 'hostname' : 'site1-cpe', 'instance' : 'Collectd Sever Alert', 'env' : 'test env', 'neId' : '$neId2', 'severity' : 'Critical', 'siteId' : '143809eb-6490-49ae-89ad-2ce296def6db', 'siteName' : 'dashBoard-gw2site', 'alertname' : 'WanLinkDown', 'companyName' : 'CompanyDashBoard', 'deviceId' : '3012' }, 'annotations' : { 'description' : 'site1-cpe : hardware self test fail, error code 1.', 'summary' : 'site1-cpe : hardware error.' }, 'url' : 'site1-cpe_CpeHardwareError', 'companyId' : '$companyId', 'deviceId' : '3012' })"
mongo --host mongo prism --eval "db.alert.insert({ '_id' : ObjectId('5fbf94705c19a4d8f9279139'), 'alertId' : '71b93a3ecb05dbb707f1930234574e788ccbb9edf92e158ca348fd3654e95a15', 'name' : 'NodeOffline', 'code' : '0101', 'status' : 'firing', 'severity' : 'Emergency', 'startsAt' : '2020-11-26T01:27:55.863374922+08:00', 'updatesAt' : '2020-11-26T23:20:36.527599896+08:00', 'endsAt' : '2020-11-26T23:18:55.863374922+08:00', 'labels' : { 'companyId' : '$companyId', 'hostname' : 'site1-cpe', 'instance' : 'Collectd Sever Alert', 'env' : 'test env', 'neId' : '$neId3', 'severity' : 'Emergency', 'siteId' : '143809eb-6490-49ae-89ad-2ce296def6db', 'siteName' : 'dashBoard-gw3site', 'alertname' : 'NodeOffline', 'companyName' : 'CompanyDashBoard', 'deviceId' : '3013' }, 'annotations' : { 'description' : 'site1-cpe : hardware self test fail, error code 1.', 'summary' : 'site1-cpe : hardware error.' }, 'url' : 'site1-cpe_CpeHardwareError', 'companyId' : '$companyId', 'deviceId' : '3013' })"