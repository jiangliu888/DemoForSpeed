const testCompanyBody = 
{
  testCompany:{"name":"testCompany","address":"测试地址","contact":"test-phone","remark":"remark","mail":"test-mail@test.com","englishName":"test-Company","city":["中国","上海市","市辖区","浦东新区"],"mobile":"18696198900","englishAddress":"test-Address","linkman":"test-Contact","config":{"algorithms":"AES-128"},"channel":"qudao"},
  testCompanyModify:{"name":"测试修改","address":"测试地址","contact":"test-phone","remark":"remark","mail":"test-mail@test.com","englishName":"test-Company","city":["中国","上海市","市辖区","浦东新区"],"mobile":"18696198900","englishAddress":"test-Address","linkman":"test-Contact","config":{"algorithms":"AES-128"},"channel":"qudao"},
  testCompanyForUser:{"name":"testCompanyUserRole","address":"测试地址","contact":"test-phone","remark":"remark","mail":"test-mail@test.com","englishName":"test-Company","city":["中国","上海市","市辖区","浦东新区"],"mobile":"18696198900","englishAddress":"test-Address","linkman":"test-Contact","config":{"algorithms":"AES-128"},"channel":"qudao"}
  }

const UserBody = {
  adminRoleUser: {"username":"roleAdminUser@wanda.com","password":"1wsx@EDC","company":"roleCompany","companyId":"","regions":["all"],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2-0","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","4","4-0","5","5-0","5-1","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["a0823124-f6f1-474f-b0cc-148689a81db3"],"roles":["admins"],"extra":{"accountType":"公司"}},
  globalPartCompanyOperateUser: {"username":"zhaoqi@subao.com","password":"1wsx@EDC","company":"roleCompany","companyId":"","regions":["all"],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2-0","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","4","4-0","5","5-0","5-1","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["a0823124-f6f1-474f-b0cc-148689a81db3"],"roles":["运维"],"extra":{"accountType":"全局","companyList":["userCompany"]}},
  globalOperateUserForTest: {"username":"zhaoqi@subao.com","password":"1wsx@EDC","company":"all","companyId":"","regions":["all"],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2-0","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","4","4-0","5","5-0","5-1","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["a0823124-f6f1-474f-b0cc-148689a81db3"],"roles":["运维"],"extra":{"accountType":"全局","companyList":["allCompany"]}},
  globalPreSaleUserForTest: {"username":"nizhefeng@subao.com","password":"1wsx@EDC","company":"all","companyId":"","regions":["all"],"scopes":["0-0-0","0-1-0","0-2-0","0-3-0","0-4-0","0-5-0","0-6-0","0-6-2","0-11-0","0-7-0","0-8-0","0-9-0","0-10-0","1-0-0","1-1-0","4","4-0","5","5-0","5-1","2","2-0","2-1","2-2","3-0-0","3-1-0","3-2-0"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["a0823124-f6f1-474f-b0cc-148689a81db3"],"roles":["售前"],"extra":{"accountType":"全局","companyList":["allCompany"]}},
  globalOperateUser: {"username":"baodian@subao.com","password":"1wsx@EDC","company":"roleCompany","companyId":"","regions":["all"],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2-0","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","4","4-0","5","5-0","5-1","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["a0823124-f6f1-474f-b0cc-148689a81db3"],"roles":["运维"],"extra":{"accountType":"全局","companyList":["allCompany"]}},
  globalDliveryUser: {"username":"qianling@subao.com","password":"1wsx@EDC","company":"roleCompany","companyId":"","regions":["all"],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2-0","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","4","4-0","5","5-0","5-1","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["a0823124-f6f1-474f-b0cc-148689a81db3"],"roles":["交付"],"extra":{"accountType":"全局","companyList":["allCompany"]}},
  globalPreSaleUser: {"username":"xuchuang@subao.com","password":"1wsx@EDC","company":"roleCompany","companyId":"","regions":["all"],"scopes":["0-0-0","0-1-0","0-2-0","0-3-0","0-4-0","0-5-0","0-6-0","0-6-2","0-11-0","0-7-0","0-8-0","0-9-0","0-10-0","1-0-0","1-1-0","4","4-0","5","5-0","5-1","2","2-0","2-1","2-2","3-0-0","3-1-0","3-2-0"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["a0823124-f6f1-474f-b0cc-148689a81db3"],"roles":["售前"],"extra":{"accountType":"全局","companyList":["allCompany"]}},
  globalMultiRoleUser:{"username":"globalMultiRoleUser@subao.com","password":"1wsx@EDC","company":"roleCompany","companyId":"","regions":["all"],"scopes":["0-0-0","0-1-0","0-2-0","0-3-0","0-4-0","0-5-0","0-6-0","0-6-2","0-11-0","0-7-0","0-8-0","0-9-0","0-10-0","1-0-0","1-1-0","4","4-0","5","5-0","5-1","2","2-0","2-1","2-2","3-2-0","3-2-0"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["a0823124-f6f1-474f-b0cc-148689a81db3"],"roles":["售前","交付"],"extra":{"accountType":"全局","companyList":["allCompany"]}},
  userRoleUser: {"username":"roleOdUser@wanda.com","password":"1wsx@EDC","company":"roleCompany","companyId":"","regions":["all"],"scopes":["0-0-0","0-1-0","0-2-0","0-4-0","0-5-0","0-6-0","1-0-0","1-1-0","3-0-0","3-1-0","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"user","channel":"","rolesId":["96d10ee8-832d-4bef-9453-4b43e5949a3f"],"roles":["users"],"extra":{"accountType":"公司"}},
  modifyRoleUser: {"username":"roleModifyUser@wanda.com","password":"1wsx@EDC","company":"roleCompany","companyId":"","regions":["all"],"scopes":["0-0-2","0-1-1","0-4-1","0-5-1","0-6-0","1-0-1","1-1-1","3-0-0","3-1-0","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"user","channel":"","rolesId":["96d10ee8-832d-4bef-9453-4b43e5949a3f"],"roles":["ModifyRole"],"extra":{"accountType":"公司"}},
  qudaoUser: {"username":"qudao@wanda.com","password":"1wsx@EDC","company":"all","companyId":"","regions":["all"],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2-0","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"test","rolesId":["5f122d78-9566-4328-a11a-04421e82d57c"],"roles":["admins"],"extra":{"accountType":"公司"}},
  modifyUser: {"username":"modifyUser@wanda.com","password":"1wsx@EDC","company":"userCompany","companyId":"","regions":["all"],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2-0","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["a0823124-f6f1-474f-b0cc-148689a81db3",""],"roles":["admins","users"],"extra":{"accountType":"公司"}},
  userAdminUser: {"username":"userAdminUser@wanda.com","password":"1wsx@EDC","company":"userCompany","companyId":"","regions":["all"],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2-0","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["a0823124-f6f1-474f-b0cc-148689a81db3"],"roles":["admins"],"extra":{"accountType":"公司"}},
  userOdUser: {"username":"userOdUser@wanda.com","password":"1wsx@EDC","company":"userCompany","companyId":"","regions":["all"],"scopes":["0-0-0","0-1-0","0-2-0","0-4-0","0-5-0","0-6-0","1-0-0","1-1-0","3-0-0","3-1-0","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"user","channel":"","rolesId":["96d10ee8-832d-4bef-9453-4b43e5949a3f"],"roles":["users"],"extra":{"accountType":"公司"}},
  userOd2User: {"username":"userOd2User@wanda.com","password":"1wsx@EDC","company":"userCompany","companyId":"","regions":["all"],"scopes":["0-0-0","0-1-0","0-2-0","0-4-0","0-5-0","0-6-0","1-0-0","1-1-0","3-0-0","3-1-0","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"user","channel":"","rolesId":["96d10ee8-832d-4bef-9453-4b43e5949a3f"],"roles":["users"],"extra":{"accountType":"公司"}},
  multiRoleUser: {"username":"multiRoleUser@wanda.com","password":"1wsx@EDC","company":"userCompany","companyId":"","regions":["all"],"scopes":["0-0-0","0-1-0","0-2-0","0-0-2","0-1-1","0-2-1"],"contact":"","admin":true,"enabled":true,"version":0,"role":"user","channel":"","rolesId":["96d10ee8-832d-4bef-9453-4b43e5949a3f",""],"roles":["userSon1Role","userSon2Role"],"extra":{"accountType":"公司"}},
  webctUser: {"username":"testUser@wanda.com","password":"1wsx@EDC","company":"userCompany","companyId":"","regions":["all"],"scopes":["0-0-0","0-1-0","0-2-0","0-0-2","0-1-1","0-2-1"],"contact":"","admin":true,"enabled":true,"version":0,"role":"user","channel":"","rolesId":["96d10ee8-832d-4bef-9453-4b43e5949a3f",""],"roles":["userSon1Role","users"],"extra":{"accountType":"公司"}},
  checkAuthUser: {"username":"authCheckUser@wanda.com","password":"1wsx@EDC","company":"userCompany","companyId":"","regions":["all"],"scopes":["0-0-0","0-1-0","0-2-0","0-0-2","0-1-1","0-2-1"],"contact":"","admin":true,"enabled":true,"version":0,"role":"user","channel":"","rolesId":["96d10ee8-832d-4bef-9453-4b43e5949a3f"],"roles":["users"],"extra":{"accountType":"公司"}},
  jumpUser:{"username":"jumpUser@wanda.com","password":"1wsx@EDC","company":"roleCompany","companyId":"cce7ae2d-5f8d-475b-9959-c59850eac904","regions":["all"],"scopes":["0-1","0-1-0","0-1-1"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["2cf7fdc9-c173-404b-9623-4b534e457731"],"roles":['jumpRole'],"extra":{"accountType":"公司"}},
  testUserUnion:{"username":"testUnionUser@test.com","password":"1wsx@edc","company":"UN-company","companyId":"","scopes":[],"contact":"12345678910","admin":false,"enabled":true,"version":0,"role":"admin","rolesId":["5f122d78-9566-4328-a11a-04421e82d57c"],"roles":["admins"],"extra":{"accountType":"公司"}},
  testUserUnion2:{"username":"testUnionUser2@test.com","password":"1wsx@edc","company":"UN2-company","companyId":"","scopes":[],"contact":"12345678910","admin":false,"enabled":true,"version":0,"role":"admin","rolesId":["5f122d78-9566-4328-a11a-04421e82d57c"],"roles":["admins"],"extra":{"accountType":"公司"}},
  testUserSite:{"username":"testSiteUser@test.com","password":"1wsx@edc","company":"Site-company","companyId":"","scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2-0","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"contact":"12345678910","admin":false,"enabled":true,"version":0,"role":"admin","rolesId":["5f122d78-9566-4328-a11a-04421e82d57c"],"roles":["admins"],"extra":{"accountType":"公司"}},
  testUserDistributor:{"username":"Distributor@test.com","password":"1wsx@edc","company":"渠道商","companyId":"","scopes":[],"contact":"12345678910","admin":false,"enabled":true,"version":0,"role":"ordinaryUser","rolesId":["5f122d78-9566-4328-a11a-04421e82d57c"],"roles":["users"],"extra":{"accountType":"公司"}},
  testUserDistributor2:{"username":"Distributor2@test.com","password":"1wsx@edc","company":"渠道商","companyId":"","scopes":[],"contact":"12345678910","admin":false,"enabled":true,"version":0,"role":"ordinaryUser","rolesId":["5f122d78-9566-4328-a11a-04421e82d57c"],"roles":["users"],"extra":{"accountType":"公司"}},
  allRWuser:{"username":"allRWuser@wanda.com","password":"1wsx@EDC","company":"roleCompany","companyId":"a4c60bef-112c-456c-a02d-2ab5ae13933f","regions":["all"],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2","0-2-0","0-2-1","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6","0-6-0","0-6-1","0-11","0-11-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","4","4-0","5","5-0","5-1","2","2-0","2-1","2-2","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["970f4979-9661-480f-b817-cbe0e0e9cae3"],"roles":["allWR"],"extra":{"accountType":"公司"}},
  onlyRuser:{"username":"onlyRuser@wanda.com","password":"1wsx@EDC","company":"roleCompany","companyId":"a4c60bef-112c-456c-a02d-2ab5ae13933f","regions":["all"],"scopes":["0-0-0","0-1-0","0-2-0","0-4-0","0-5-0","0-6-0","1-0-0","1-1-0","3-0-0","3-1-0"],"contact":"","admin":true,"enabled":true,"version":0,"role":"admin","channel":"","rolesId":["70300531-408a-4258-9b12-eeedeca4720c"],"roles":["onlyR"],"extra":{"accountType":"公司"}},
  devideTestUser:{"username":"test_forDevice@netskyper.com","password":"1wsx@EDC","company":"","companyId":"913b1971-1856-4066-90a5-21ce00822752","regions":["all"],"scopes":["0-1-0"],"contact":"","admin":true,"enabled":true,"version":1,"role":"admin","channel":"","rolesId":[ "108d9ad3-4ba1-41fd-8df0-870aff75c89a"],"roles":["device_test"],"extra":{"accountType":"全局"}}
}

const RoleBody = {
  globalAdminRole : {"roleId":"","companyId":"e0409708-d573-45de-8c4a-6ca6c0381cc1","regions":[],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2-0","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"desc":"for test","extra":{"globalMode":true},"role":"admins","createdAt":"2021-07-13T05:47:42.076Z","company":""},
  globalOPerationRole : {"roleId":"","companyId":"e0409708-d573-45de-8c4a-6ca6c0381cc1","regions":[],"scopes":["0","0-0","0-0-0","0-0-1","0-0-2","0-1","0-1-0","0-1-1","0-2","0-2-0","0-2-1","0-3","0-3-0","0-3-1","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6","0-6-0","0-6-2","0-6-1","0-6-3","0-11","0-11-0","0-11-1","0-7","0-7-0","0-7-1","0-8","0-8-0","0-8-1","0-9","0-9-0","0-9-1","0-10","0-10-0","0-10-1","1","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","1-2","4","4-0","5","5-0","5-1","2","2-0","2-1","2-2","3","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-2","3-2-0","3-2-1","3-3","3-2-0","3-2-1"],"desc":"运维角色","extra":{"globalMode":true},"role":"运维","createdAt":"2021-07-13T05:47:42.076Z","company":""},
  globaldeliveryRole :  {"roleId":"","companyId":"e0409708-d573-45de-8c4a-6ca6c0381cc1","regions":[],"scopes":["0-0","0-0-0","0-0-1","0-0-2","0-1","0-1-0","0-1-1","0-2","0-2-0","0-2-1","0-3","0-3-0","0-3-1","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6-0","0-6-2","0-6-1","0-11","0-11-0","0-11-1","0-7-0","0-8-0","0-9-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","4","4-0","5","5-0","5-1","2","2-0","2-1","2-2","3-2","3-2-0","3-2-1","3-3","3-2-0","3-2-1"],"desc":"交付角色","extra":{"globalMode":true},"role":"交付","createdAt":"2021-07-13T05:47:42.076Z","company":""},
  globalPreSaleRole :   {"roleId":"","companyId":"e0409708-d573-45de-8c4a-6ca6c0381cc1","regions":[],"scopes":["0-0-0","0-1-0","0-2-0","0-3-0","0-4-0","0-5-0","0-6-0","0-6-2","0-11-0","0-7-0","0-8-0","0-9-0","0-10-0","1-0-0","1-1-0","4","4-0","5","5-0","5-1","2","2-0","2-1","2-2","3-0-0","3-1-0","3-2-0","3-3-0"],"desc":"售前角色","extra":{"globalMode":true},"role":"售前","createdAt":"2021-07-13T05:47:42.076Z","company":""},
  newRole: {"roleId":"","companyId":"7a9cc716-bcbd-4ca3-9b42-f73ebef93afd","regions":[],"scopes":["0-0-2","0-1-1","0-4-1","0-5-1","0-6-0","1-0-1","1-1-1","3-0-0","3-1-0","3-3"],"desc":"测试角色1","extra":{"globalMode":false},"role":"Role1","createdAt":"2021-07-14T13:49:01.091Z","company":""},
  webAuthRole: {"roleId":"","companyId":"7a9cc716-bcbd-4ca3-9b42-f73ebef93afd","regions":[],"scopes":["0-0-2","0-1-1","0-4-1","0-5-1","0-6-0","1-0-1","1-1-1","3-0-0","3-1-0","3-3"],"desc":"验证权限","extra":{"globalMode":false},"role":"checkAuthRole","createdAt":"2021-07-14T13:49:01.091Z","company":""},
  modifyRole: {"roleId":"","companyId":"7a9cc716-bcbd-4ca3-9b42-f73ebef93afd","regions":[],"scopes":["0-0-2","0-1-1","0-4-1","0-5-1","0-6-0","1-0-1","1-1-1","3-0-0","3-1-0","3-3"],"desc":"修改角色","extra":{"globalMode":false},"role":"ModifyRole","createdAt":"2021-07-14T13:49:01.091Z","company":""},
  son1Role: {"roleId":"","companyId":"af4af36b-66bb-4eb0-b105-a7b2e9dec3d3","regions":[],"scopes":["0-0-0","0-1-0","0-2-0"],"desc":"小普通用户1","extra":{"globalMode":false},"role":"son1Role","createdAt":"2021-07-15T05:53:39.997Z","company":""},
  son2Role: {"roleId":"","companyId":"af4af36b-66bb-4eb0-b105-a7b2e9dec3d3","regions":[],"scopes":["0-4-0","0-5-0","0-6-0"],"desc":"小普通用户2","extra":{"globalMode":false},"role":"son2Role","createdAt":"2021-07-15T05:53:39.997Z","company":""},
  userSon1Role: {"roleId":"","companyId":"af4af36b-66bb-4eb0-b105-a7b2e9dec3d3","regions":[],"scopes":["0-0-0","0-1-0","0-2-0"],"desc":"普通读用户","extra":{"globalMode":false},"role":"userSon1Role","createdAt":"2021-07-15T05:53:39.997Z","company":""},
  userSon2Role: {"roleId":"","companyId":"af4af36b-66bb-4eb0-b105-a7b2e9dec3d3","regions":[],"scopes":["0-0-2","0-1-1","0-2-1"],"desc":"普通读写用户","extra":{"globalMode":false},"role":"userSon2Role","createdAt":"2021-07-15T05:53:39.997Z","company":""},
  jumpRole: {"roleId":"","companyId":"cce7ae2d-5f8d-475b-9959-c59850eac904","regions":[],"scopes":["0-1","0-1-0","0-1-1"],"desc":"for jump forbidden test","extra":{"globalMode":false},"role":"jumpRole","createdAt":"2021-07-15T08:46:23.741Z","company":""},
  allRW: {"roleId":"","companyId":"a4c60bef-112c-456c-a02d-2ab5ae13933f","regions":[],"scopes":["0-0","0-0-0","0-0-2","0-1","0-1-0","0-1-1","0-2","0-2-0","0-2-1","0-4","0-4-0","0-4-1","0-5","0-5-0","0-5-1","0-6","0-6-0","0-6-1","0-11","0-11-0","1-0","1-0-0","1-0-1","1-1","1-1-0","1-1-1","4","4-0","5","5-0","5-1","2","2-0","2-1","2-2","3-0","3-0-0","3-0-1","3-1","3-1-0","3-1-1","3-3"],"desc":"所有权限","extra":{"globalMode":false},"role":"allWR","createdAt":"2021-08-10T01:51:09.962Z","company":""},
  onlyR: {"roleId":"","companyId":"a4c60bef-112c-456c-a02d-2ab5ae13933f","regions":[],"scopes":["0-0-0","0-1-0","0-2-0","0-4-0","0-5-0","0-6-0","1-0-0","1-1-0","3-0-0","3-1-0"],"desc":"只读","extra":{"globalMode":false},"role":"onlyR","createdAt":"2021-08-10T01:51:09.962Z","company":""},
  deviceRole: {"roleId":"","companyId":"a4c60bef-112c-456c-a02d-2ab5ae13933f","regions":[],"scopes":["0-1-0"],"desc":"only for device test","extra":{"globalMode":true},"role":"device_test","createdAt":"2021-08-10T01:51:09.962Z","company":""}
}

const webRoleBody = {
  globalOPerationRole:[{level:1,roleList:['配置'],checkRole:['w']},
                       {level:1,roleList:['监控'],checkRole:['w']},
                       {level:1,roleList:['报表'],checkRole:['w']},
                       {level:1,roleList:['日志'],checkRole:['w']},
                       {level:1,roleList:['审计'],checkRole:['w']},
                       {level:1,roleList:['账户'],checkRole:['w']}
                      ],
  globaldeliveryRole : [{level:2,roleList:['配置','站点注册'],checkRole:['w']},
                        {level:2,roleList:['配置','设备管理'],checkRole:['w']},
                        {level:2,roleList:['配置','拓扑管理'],checkRole:['w']},
                        {level:2,roleList:['配置','区域码管理'],checkRole:['w']},
                        {level:2,roleList:['配置','防火墙'],checkRole:['w']},
                        {level:2,roleList:['配置','路由管理'],checkRole:['w']},
                        {level:3,roleList:['配置','策略管理','只读(策略应用)'],checkRole:[]},
                        {level:3,roleList:['配置','策略管理','只读(规则,模板,场景)'],checkRole:[]},
                        {level:3,roleList:['配置','策略管理','读写'],checkRole:['w_companyView']},
                        {level:2,roleList:['配置','审计配置'],checkRole:['w']},
                        {level:3,roleList:['配置','Pop点管理','只读'],checkRole:['r']},
                        {level:3,roleList:['配置','服务管理','只读'],checkRole:['r']},
                        {level:3,roleList:['配置','区域码管理(全局)','只读'],checkRole:['r']},
                        {level:2,roleList:['监控','站点概览'],checkRole:['w']},
                        {level:2,roleList:['监控','设备告警'],checkRole:['w']},
                        {level:1,roleList:['报表'],checkRole:['w']},
                        {level:1,roleList:['日志'],checkRole:['w']},
                        {level:1,roleList:['审计'],checkRole:['w']},
                        {level:2,roleList:['账户','公司管理'],checkRole:['w']},
                        {level:2,roleList:['账户','行政区划'],checkRole:['w']}
                      ],
globalPreSaleRole : [{level:3,roleList:['配置','站点注册','只读'],checkRole:['r']},
                      {level:3,roleList:['配置','设备管理','只读'],checkRole:['r']},
                      {level:3,roleList:['配置','拓扑管理','只读'],checkRole:['r']},
                      {level:3,roleList:['配置','区域码管理','只读'],checkRole:['r']},
                      {level:3,roleList:['配置','防火墙','只读'],checkRole:['r']},
                      {level:3,roleList:['配置','路由管理','只读'],checkRole:['r']},
                      {level:3,roleList:['配置','策略管理','只读(策略应用)'],checkRole:[]},
                      {level:3,roleList:['配置','策略管理','只读(规则,模板,场景)'],checkRole:['r_all']},
                      {level:3,roleList:['配置','审计配置','只读'],checkRole:['r']},
                      {level:3,roleList:['配置','Pop点管理','只读'],checkRole:['r']},
                      {level:3,roleList:['配置','服务管理','只读'],checkRole:['r']},
                      {level:3,roleList:['配置','区域码管理(全局)','只读'],checkRole:['r']},
                      {level:3,roleList:['监控','站点概览','只读'],checkRole:['r']},
                      {level:3,roleList:['监控','设备告警','只读'],checkRole:['r']},
                      {level:1,roleList:['报表'],checkRole:['w']},
                      {level:1,roleList:['日志'],checkRole:['w']},
                      {level:1,roleList:['审计'],checkRole:['w']},
                      {level:3,roleList:['账户','公司管理','只读'],checkRole:['r']},
                      {level:3,roleList:['账户','行政区划','只读'],checkRole:['r']}
                    ],
         newRole : [{level:3,roleList:['配置','站点注册','内网网段读写'],checkRole:['w_innerNet']},
                    {level:3,roleList:['配置','设备管理', '读写'],checkRole:['w']},
                    {level:3,roleList:['配置','防火墙', '读写'],checkRole:['w']},
                    {level:3,roleList:['配置','路由管理', '读写'],checkRole:['w']},
                    {level:3,roleList:['配置','策略管理','只读(策略应用)'],checkRole:['r_apply']},
                    {level:3,roleList:['监控','站点概览', '读写'],checkRole:['w']},
                    {level:3,roleList:['监控','设备告警', '读写'],checkRole:['w']},
                    {level:3,roleList:['账户','个人账户','只读'],checkRole:['r']},
                    {level:3,roleList:['账户','角色管理','只读'],checkRole:['r']},
                    {level:2,roleList:['账户','行政区划'],checkRole:['w']}
                  ],
        modifyRole : [{level:3,roleList:['配置','站点注册','内网网段读写'],checkRole:['w_innerNet']},
                  {level:3,roleList:['配置','设备管理', '读写'],checkRole:['w']},
                  {level:3,roleList:['配置','防火墙', '读写'],checkRole:['w']},
                  {level:3,roleList:['配置','路由管理', '读写'],checkRole:['w']},
                  {level:3,roleList:['监控','站点概览', '读写'],checkRole:['w']},
                  {level:3,roleList:['监控','设备告警', '读写'],checkRole:['w']},
                  {level:3,roleList:['账户','个人账户','只读'],checkRole:['r']},
                  {level:3,roleList:['账户','角色管理','只读'],checkRole:['r']}
                ],
       multiRole : [{level:3,roleList:['配置','站点注册','只读'],checkRole:['r']},
                    {level:3,roleList:['配置','设备管理','只读'],checkRole:['r']},
                    {level:3,roleList:['配置','拓扑管理','只读'],checkRole:['r']},
                    {level:3,roleList:['配置','防火墙','只读'],checkRole:['r']},
                    {level:3,roleList:['配置','路由管理','只读'],checkRole:['r']},
                    {level:3,roleList:['配置','策略管理','只读(策略应用)'],checkRole:['r_apply']}],
       adminRole : [{level:3,roleList:['配置','站点注册','只读'],checkRole:[]},
                    {level:3,roleList:['配置','站点注册','内网网段读写'],checkRole:['w_innerNet']},
                    {level:2,roleList:['配置','设备管理'],checkRole:['w']},
                    {level:3,roleList:['配置','拓扑管理','只读'],checkRole:['r']},
                    {level:2,roleList:['配置','防火墙'],checkRole:['w']},
                    {level:2,roleList:['配置','路由管理'],checkRole:['w']},
                    {level:3,roleList:['配置','策略管理','只读(策略应用)'],checkRole:['r_apply']},
                    {level:2,roleList:['监控','站点概览'],checkRole:['w']},
                    {level:2,roleList:['监控','设备告警'],checkRole:['w']},
                    {level:1,roleList:['报表'],checkRole:['w']},
                    {level:1,roleList:['日志'],checkRole:['w']},
                    {level:2,roleList:['账户','个人账户'],checkRole:['w']},
                    {level:2,roleList:['账户','角色管理'],checkRole:['w']},
                    {level:2,roleList:['账户','行政区划'],checkRole:['w']}
                  ],
        userRole : [{level:3,roleList:['配置','站点注册','只读'],checkRole:['r']},
                  {level:3,roleList:['配置','设备管理','只读'],checkRole:['r']},
                  {level:3,roleList:['配置','拓扑管理','只读'],checkRole:['r']},
                  {level:3,roleList:['配置','防火墙','只读'],checkRole:['r']},
                  {level:3,roleList:['配置','路由管理','只读'],checkRole:['r']},
                  {level:3,roleList:['配置','策略管理','只读(策略应用)'],checkRole:['r_apply']},
                  {level:3,roleList:['监控','站点概览','只读'],checkRole:['r']},
                  {level:3,roleList:['监控','设备告警','只读'],checkRole:['r']},
                  {level:3,roleList:['账户','个人账户','只读'],checkRole:['r']},
                  {level:3,roleList:['账户','角色管理','只读'],checkRole:['r']},
                  {level:2,roleList:['账户','行政区划'],checkRole:['w']}
                ],
        globalMultiRoleUser:[{level:2,roleList:['配置','站点注册'],checkRole:['w']},
                {level:2,roleList:['配置','设备管理'],checkRole:['w']},
                {level:2,roleList:['配置','拓扑管理'],checkRole:['w']},
                {level:2,roleList:['配置','区域码管理'],checkRole:['w']},
                {level:2,roleList:['配置','防火墙'],checkRole:['w']},
                {level:2,roleList:['配置','路由管理'],checkRole:['w']}]
}
const PopTypeForward = 6
const PopTypeAnycast = 7
const PopTypeSaas = 8

const default_bandwidth = 1000
const pop1_cac = "4"
const pop1_eac = "4"
const pop2_cac = "4"
const pop2_eac = "5"
const pop1_ip = "10.196.20.4"
const pop2_ip = "10.194.20.3"
const setupSites = ['testSTBeijing', 'testSTShanghai', 'testSTGuangzhou', 'testSTNanjing', 'testSTWuhan', 'testSTChongqing', 'testSTZhengjiang', 'testSTChangsha', 'testSTNanchang']
const testSiteBody = {
  testSTBeijing:{"name":"beijing","sn":"1002","tunnelNum":"4000","nets": "","location":"beijing","reportInterval":"10","scoreInterval":"10","enablePrivate":true,
  "private":["10.193.0.0/26","10.193.0.64/27","10.193.0.96/30","10.193.0.100/32"],"longitude":"116.352963","latitude":"40.409079",
  "type":"串联","HA":false,
  "wans":[{"name":"WAN1","mtu":"1380","bandwidth":default_bandwidth, "prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip,"staticIp":'10.194.16.2',"proxy":false, "ifname": "enp1s0f0",'ip_mode':'FIA'}],
  "lans":[{"IDC":true, 'pair': 'enp1s0f0', 'ifname': 'enp1s0f1', 'ip_mode': 'FIA'}]},
  testSTShanghai:{"name":"shanghai","sn":"1003","tunnelNum":"6868","nets": "","location":"shanghai","reportInterval":"10","scoreInterval":"10","enablePrivate":true,
  "type":"串联","HA":false,"natNet":"100.64.0.0/16","longitude":"121.48789949","latitude":"31.24916171",
  "private":["10.193.0.101/32", "10.193.0.102/32", "10.193.0.103/32", "10.193.0.104/30", "10.193.0.108/30", "10.193.0.112/28", "10.193.0.128/26", "10.193.0.192/29"],
  "wans":[{"name":"WAN1","mtu":"1380","bandwidth":default_bandwidth,"prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip,"proxy":false}],
  "lans":[],
  "4G":[{"name_4g": "enp1s0f3", "usage":"internal"}]},
  testSTChongqing:{"name":"chongqing","sn":"1007","tunnelNum":"0","nets": "","location":"chongqing","reportInterval":"10","scoreInterval":"10","enablePrivate":true,
  "type":"串联","HA":false,
  "private": ["10.193.0.200/29", "10.193.0.208/28", "10.193.0.224/27"],"longitude":"106.558434","latitude":"29.568996",
  "wans":[{"name":"WAN1","mtu":"1380","bandwidth":default_bandwidth,"prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip,"gatewayMac":"b8:69:f4:cb:ff:44"}],
  "lans":[]},
  testSTZhengjiang:{"name":"zhenjiang","sn":"1009","tunnelNum":"6000","nets": "","location":"zhengjiang","reportInterval":"10","scoreInterval":"10",
  "type":"串联","HA":false,"longitude":"119.451206","latitude":"32.189886",
  "wans":[{"name":"WAN1","mtu":"1380","bandwidth":default_bandwidth,"prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip}],
  "lans":[]},
  testSTNanjing:{"name":"nanjing","sn":"1005","tunnelNum":"6868","nets": "","location":"nanjing","reportInterval":"10","scoreInterval":"10","longitude":"118.802422","latitude":"32.064653",
  "type":"旁挂","HA":true,"haDevice":"1005S","HAaddress":{"master_wanip":"172.20.14.32","master_wanmask":"24","master_wangw":"172.20.14.1","standby_wanip":"172.20.14.22","standby_wanmask":"24","standby_wangw":"172.20.14.1",
        "master_lanip":"172.21.14.32","master_lanmask":"24","master_langw":"172.21.14.1","standby_lanip":"172.21.14.22","standby_lanmask":"24","standby_langw":"172.21.14.1"},
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"10.194.14.2","ip_mode":"FIA","ip_type":"静态ip地址","ip":'172.20.14.25',"mask":'24',"gateway":"172.20.14.1","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip,'ifname':'enp1s0f0'},
          {"name":"WAN2","mtu":"1380","public_ip":"10.196.14.2","ip_mode":"FIA","ip_type":"静态ip地址","ip":'172.20.14.26',"mask":'24',"gateway":"172.20.14.1","bandwidth":default_bandwidth,
          "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip}],
  "lans":[{"name":"LAN1","ip_addr":"172.21.14.25","mask":"24","gateway":"172.21.14.1","IDC":true, 'ifname': 'enp1s0f1', 'pair': 'enp1s0f0', 'ip_mode': 'FIA'}],
  "dyn_routing":{"bgp":true,"ospf":false,"metric":100,"routing_report":[{"prefix_nets":"1.1.1.1/32","action":"忽略","metric":100},{"prefix_nets":"10.0.200.0/24","action":"忽略","metric":100}]}
  },
  testSTWuhan:{"name":"wuhan","sn":"1006","tunnelNum":"0","nets": "","location":"wuhan","reportInterval":"10","scoreInterval":"10",
  "type":"旁挂","HA":false,"longitude":"114.311582","latitude":"30.598467",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"静态ip地址","ip":'172.20.15.27',"mask":'24',"gateway":"172.20.15.1","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip},
        {"name":"WAN2","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"静态ip地址","ip":'172.20.15.28',"mask":'24',"gateway":"172.20.15.1","bandwidth":default_bandwidth,
        "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip}],
  "lans":[{"name":"LAN1","ip_addr":"172.21.15.27","mask":"24","gateway":"172.21.15.1"}],
  "dyn_routing":{"bgp":true,"ospf":false,"metric":200}
  },
  testSTGuangzhou:{"name":"guangzhou","sn":"1004","tunnelNum":"6868","nets": ["172.19.43.0/24"],"location":"guangzhou","reportInterval":"10","scoreInterval":"10",
  "type":"网关","HA":false,"longitude":"113.374375","latitude":"23.368923",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"DHCP","bandwidth":default_bandwidth,"proxy":true,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip}],
  "lans":[{"name":"LAN1","ip_addr":"172.19.43.0","mask":"24","DHCP":false,"internet":false,"IDC":true},
          {"name":"LAN2","ip_addr":"192.168.1.1","mask":"24","DHCP":true,"internet":true,"IDC":false,"ip_start":"192.168.1.99", "ip_end":"192.168.1.150"}],
  "4G":[{"name_4g": "eth1", "usage":"backup","prefer_cac":pop1_cac,"prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip}],
  "wifi":{"ssid":"testwifi", "network":"lan1", "encryption": "psk2", "encryption_type": "WPA2-PSK", "key":"12345678", "macfilter":"allow", "mac_list":["00:83:09:00:15:d4","00:83:09:00:15:d5"]}
  },
  testPA:{"name":"nanjing","sn":"1005","tunnelNum":"6868","nets": ["172.19.14.0/24"],"location":"nanjing",
  "type":"旁挂","HA":false,"sameNet":true,"reportInterval":"10","scoreInterval":"10","longitude":"121.48789949","latitude":"31.24916171",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"10.194.14.2","ip_mode":"FIA","ip_type":"静态ip地址","ip":'172.20.14.25',"mask":'24',"gateway":"172.20.14.1","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip,"group":"103",'ifname':'enp1s0f0'},
          {"name":"WAN2","mtu":"1380","public_ip":"10.196.14.2","ip_mode":"FIA","ip_type":"静态ip地址","ip":'172.20.14.26',"mask":'24',"gateway":"172.20.14.1","bandwidth":default_bandwidth,
          "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip}],
  "lans":[{"name":"LAN1","ip_addr":"172.21.14.25","mask":"24","gateway":"172.21.14.1","IDC":true,'ip_mode':'FIA','ifname':'enp1s0f1','pair':'enp1s0f0'}]
  },
  testSE:{"name":"beijing","sn":"1002","tunnelNum":"4000","nets": "","location":"beijing",
  "private":["10.193.0.0/26","10.193.0.64/27","10.193.0.96/30","10.193.0.100/32"],
  "type":"串联","HA":false,"reportInterval":"10","scoreInterval":"10","longitude":"121.48789949","latitude":"31.24916171",
  "wans":[{"name":"WAN1","mtu":"1380","bandwidth":default_bandwidth, 'ip_mode':"FIA","prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip,"group":"101", 'proxy': true, "ifname": 'enp1s0f0'}],
  "lans":[{"IDC":true, 'ifname':'enp1s0f1','pair':'enp1s0f0','ip_mode':'FIA'}]},
  testGW:{"name":"guangzhou","sn":"1004","tunnelNum":"6868","nets": ["172.19.43.0/24"],"location":"guangzhou","sameNet":true,"reportInterval":"10","scoreInterval":"10",
  "type":"网关","HA":false,"longitude":"121.48789949","latitude":"31.24916171",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"DHCP","bandwidth":default_bandwidth,"ifname":"eth0","proxy":true,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip,"group":"101 102","prefer_cac":pop2_cac},
          {"name":"WAN2","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"静态ip地址","ip":'10.194.12.2',"mask":'24',"gateway":"10.194.12.1","bandwidth":default_bandwidth,
          "ifname":"eth1","proxy":true,"prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip}],
  "lans":[{"name":"LAN1","ip_addr":"172.19.43.0","mask":"24","DHCP":false,"internet":false,"ifname":"tun1","phy_ifname": "eth2","IDC":true,"ip_mode":"FIA","pair": "eth0"},
          {"name":"LAN2","ip_addr":"192.168.1.1","mask":"24","DHCP":true,"internet":true,"IDC":false,"phy_ifname": "eth3","ip_start":"192.168.1.99", "ip_end":"192.168.1.150"}],
  "wifi":{"ssid":"testwifi", "network":"lan1", "encryption": "psk2", "encryption_type": "WPA2-PSK", "key":"12345678", "macfilter":"allow", "mac_list":["00:83:09:00:15:d4","00:83:09:00:15:d5"]}
  },
  testGW_MIPS_1W:{"name":"mips1","sn":"1020","tunnelNum":"6868","nets": ["172.19.45.0/24"],"location":"changsha",
  "type":"网关","HA":false,"reportInterval":"10","scoreInterval":"10","longitude":"121.48789949","latitude":"31.24916171",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"DHCP","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip,"group":"101 102","prefer_cac":pop2_cac}],
  "lans":[{"name":"LAN1","lan_port_num":4,"ip_addr":"172.19.45.0","mask":"24","DHCP":false,"internet":false,"IDC":true}]
  },
  testGW_MIPS_2W:{"name":"mips1","sn":"1021","tunnelNum":"6868","nets": ["172.19.45.0/24"],"location":"changsha",
  "type":"网关","HA":false,"reportInterval":"10","scoreInterval":"10","longitude":"121.48789949","latitude":"31.24916171",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"DHCP","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip,"group":"101 102","prefer_cac":pop2_cac},
          {"name":"WAN2","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"DHCP","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip,"group":"101 102","prefer_cac":pop2_cac}],
  "lans":[{"name":"LAN1","lan_port_num":2,"ip_addr":"172.19.45.0","mask":"24","DHCP":false,"internet":false,"IDC":true},
          {"name":"LAN2","lan_port_num":1,"ip_addr":"172.19.46.0","mask":"24","DHCP":false,"internet":true,"IDC":false}]
  },
  testGW_ARMS:{"name":"mips1","sn":"1030","tunnelNum":"6868","nets": ["172.19.45.0/24"],"location":"changsha",
  "type":"网关","HA":false,"reportInterval":"10","scoreInterval":"10","longitude":"121.48789949","latitude":"31.24916171",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"DHCP","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip,"group":"101 102","prefer_cac":pop2_cac}],
  "lans":[{"name":"LAN1","lan_port_num":6,"ip_addr":"172.19.45.0","mask":"24","DHCP":false,"internet":false,"IDC":true}]
  },
  testGW_ARMS_Fail:{"name":"mips1","sn":"1030","tunnelNum":"6868","nets": ["172.19.45.0/24"],"location":"changsha",
  "type":"网关","HA":false,"reportInterval":"10","scoreInterval":"10","longitude":"121.48789949","latitude":"31.24916171",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"DHCP","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip,"group":"101 102","prefer_cac":pop2_cac}],
  "lans":[{"name":"LAN1","lan_port_num":3,"ip_addr":"172.19.45.0","mask":"24","DHCP":false,"internet":false,"IDC":true}]
  },
  testSTChangsha:{"name":"changsha","sn":"1020","tunnelNum":"0","nets": ["172.19.45.0/24"],"location":"changsha","reportInterval":"10","scoreInterval":"10",
  "type":"网关","HA":false,"natNet":"100.64.0.0/16", "natPort": true,"longitude":"113.087559","latitude":"28.251818",
  "wans":[{"name":"WAN1","mtu":"1380","ip_mode":"FIA","ip_type":"静态ip地址","ip":'10.194.18.2',"mask":'24',"gateway":"10.194.18.1","bandwidth":default_bandwidth,"proxy":true,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip},
          {"name":"WAN2","mtu":"1380","public_ip":"","logic_if_name":"pppoe-wan2","ip_mode":"FIA","ip_type":"PPPOE","account":'changsha',"password":'changsha',"bandwidth":default_bandwidth,"proxy":true,
          "prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip}],
  "lans":[{"name":"LAN1","ip_addr":"172.19.45.1","mask":"24","DHCP":true,"ip_start":"172.19.45.99","ip_end":"172.19.45.151","internet":false,"IDC":true,"lan_port_num":4, "gateway":"172.19.45.173"},
          {"name":"LAN2","ip_addr":"172.19.43.1","mask":"24","DHCP":true,"ip_start":"172.19.43.101","ip_end":"172.19.43.149","internet":true,"IDC":true,"lan_port_num":1}],
  "wifi":{"ssid":"testwifi", "network":"lan1", "encryption": "psk2", "encryption_type": "WPA2-PSK", "key":"12345678", "macfilter":"allow", "mac_list":["00:83:09:00:15:d4","00:83:09:00:15:d5"]}
  },
  testSTNanchang:{"name":"nanChang","sn":"1021A","tunnelNum":"0","nets": "","location":"nanchang","reportInterval":"10","scoreInterval":"10",
  "type":"网关","HA":true,"haDevice":"1021S","HAaddress":{"master_wanip":"10.194.17.2","master_wanmask":"24","master_wangw":"10.194.17.1","standby_wanip":"10.194.17.3","standby_wanmask":"24","standby_wangw":"10.194.17.1",
  "master_wan2ip":"10.0.13.130","master_wan2mask":"24","master_wan2gw":"10.0.13.1","standby_wan2ip":"10.0.13.129","standby_wan2mask":"24","standby_wan2gw":"10.0.13.1",
  "master_lanip":"172.19.17.2","master_lanmask":"24","standby_lanip":"172.19.17.3","standby_lanmask":"24"},
  "natNet":"100.64.0.0/16", "natPort": true,"longitude":"115.95046","latitude":"28.551604",
  "wans":[{"name":"WAN1","mtu":"1380","ip_mode":"FIA","ip_type":"静态ip地址","ip":'10.194.17.155',"mask":'24',"gateway":"10.194.17.1","bandwidth":default_bandwidth,"proxy":true,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip},
          {"name":"WAN2","mtu":"1380","ip_mode":"FIA","ip_type":"静态ip地址","ip":'10.0.13.155',"mask":'24',"gateway":"10.0.13.1","bandwidth":default_bandwidth,"proxy":true,
          "prefer_pop_cac":pop1_cac, "prefer_pop_eac":pop1_eac,"prefer_ip":pop1_ip}],
  "lans":[{"name":"LAN1","ip_addr":"172.19.17.1","mask":"24","DHCP":true,"ip_start":"172.19.17.99","ip_end":"172.19.17.151","internet":false,"IDC":true,"lan_port_num":1}],
  "wifi":{"ssid":"testwifi", "network":"lan1", "encryption": "psk2", "encryption_type": "WPA2-PSK", "key":"12345678", "macfilter":"allow", "mac_list":["00:83:09:00:15:d4","00:83:09:00:15:d5"]},
  "dyn_routing":{"bgp":false,"ospf":true,"metric":80,"routing_report":[{"prefix_nets":"172.19.17.0/24","action":"通告","metric":80}],"routing_filter":["10.194.15.0/24","10.196.12.0/24"]}
  },
  testConfig_GW_ARMS:{"name":"arm1","sn":"GH8C1889","tunnelNum":"6868","nets": ["172.32.16.0/24"],"location":"ningbo",
  "type":"网关","HA":false,"reportInterval":"10","scoreInterval":"10","longitude":"113.087559","latitude":"28.251818",
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"DHCP","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip, "ifname":'wan','proxy': true}],
  "lans":[{"name":"LAN1","lan_port_num":4,"ip_addr":"172.32.16.1","mask":"24","DHCP":false,"internet":false,"IDC":true,'ifname':'tun1',"ip_mode":"FIA",'pair':'wan','phy_ifname':'lan0'}],
  "wifi":{"ssid":"debugWifi", "network":"lan1", "encryption": "psk2", "encryption_type": "WPA2-PSK", "key":"12345678", "macfilter":"allow", "mac_list":["00:83:09:00:15:d4","00:83:09:00:15:d5"]}
  },
  testConfig_audit_GW_ARMS:{"name":"arm1","sn":"3107","tunnelNum":"6868","nets": ["172.38.17.0/24"],"location":"audit_ningbo",
  "type":"网关","HA":false,"reportInterval":"10","scoreInterval":"10","longitude":"113.087559","latitude":"28.251818",
  "auditAuth":{"audit": true, "auditMac": '02:00:4c:4f:4d:50', "auth": false},
  "wans":[{"name":"WAN1","mtu":"1380","public_ip":"","ip_mode":"FIA","ip_type":"DHCP","bandwidth":default_bandwidth,
  "prefer_pop_cac":pop2_cac, "prefer_pop_eac":pop2_eac,"prefer_ip":pop2_ip, "ifname":'wan','proxy': true}],
  "lans":[{"name":"LAN1","lan_port_num":4,"ip_addr":"172.38.17.1","mask":"24","DHCP":false,"internet":false,"IDC":true,'ifname':'tun1',"ip_mode":"FIA",'pair':'wan','phy_ifname':'lan0'}]}
}

const testSpiRuleBody = {
  spiModifyRule :{"srcCIDR":"192.168.100.0/24","dstCIDR":"192.168.200.0/24","l4proto":["1"],"srcPort":"25,55,99","dstPort":"55-40","dstDomain":""},
  spiRuleAdd :{"srcCIDR":"10.192.0.0/24","dstCIDR":"10.192.1.0/24","l4proto":["1","6","17"],"srcPort":"22","dstPort":"99","dstDomain":""}
}

const testSpiTagBody = {
  SpiAddTFail:{"spiTagId":"","name":"SpiaddTFail","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"id":"71","l4proto":["6"]},
                                                                                                                  {"id":"73","srcCIDR":"10.0.0.0/8","l4proto":["1","6","17"]}],
                                                                                                      "fail_rules":[{"id":"72","srcCIDR":"10.0.0.0/8","l4proto":["1","6","17"]},
                                                                                                      {"id":"76","dstCIDR":"128.0.0.0/1","l4proto":["17"],"dstDomain":""}],            
                                                                                                                  "tag":5,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiAddTag:{"spiTagId":"","name":"SpiaddTagAllType","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"id":"81","l4proto":["1","6"]},
                                                                                                                 {"id":"82","l4proto":["17"]},
                                                                                                                 {"id":"83","srcCIDR":"20.0.0.0/8","l4proto":["1","6","17"]},
                                                                                                                 {"id":"84","srcCIDR":"192.168.0.0/24","dstCIDR":"192.168.1.0/24","l4proto":["1","6"],"srcPort":"25,55","dstPort":"55-40,88","dstDomain":""},
                                                                                                                 {"id":"85","srcCIDR":"192.168.0.0/24","dstCIDR":"www.baidu.com","l4proto":["1","6","17"],"srcPort":"22","dstPort":"99","dstDomain":""},
                                                                                                                 {"id":"86","srcCIDR":"192.168.2.0/24","dstCIDR":"netdna\.bootstrapcdn\.com","l4proto":["6"],"srcPort":"22","dstPort":"99","dstDomain":""}],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiTagAllIP :{"spiTagId":"","name":"allIp","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"id":"31","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":"128.0.0.0/1","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false},
                                                                                                         {"id":"32","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":"0.0.0.0/1","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false}],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiTagAllIPUdp :{"spiTagId":"","name":"allIpUdp","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"id":"91","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":"128.0.0.0/1","l4proto":["17"],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false},
                                                                                                               {"id":"92","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":"0.0.0.0/1","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false}],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiTagSaas :{"spiTagId":"","name":"SPISaas","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"id":"71","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":".*\\.onenote\\.com","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false},{"id":"72","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":"8.8.8.8","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false}],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiTagModifySaas :{"spiTagId":"","name":"SPIModifySaas","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"id":"71","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":".*\\.onenote\\.com","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false},{"id":"72","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":"8.8.8.8","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false}],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiSTTagSaas :{"spiTagId":"","name":"STSaas","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"id":"71","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":".*\\.onenote\\.com","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false},{"id":"72","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":"8.8.8.8","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false}],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiGTagSaas :{"spiTagId":"","name":"GlobalSaas","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"id":"71","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":".*\\.google\\.com","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false},{"id":"72","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":"8.8.8.8","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false}],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiGTagModifySaas :{"spiTagId":"","name":"GlobalModifySaas","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"id":"71","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":".*\\.google\\.com","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false},{"id":"72","vport":{"iface":"","index":0},"srcCIDR":"","dstCIDR":"8.8.8.8","l4proto":[],"srcPort":"","dstPort":"","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false}],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiModifyTag :{"spiTagId":"","name":"allIpUdp","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"search":"128.0.0.0/1","id":"91","vport":{"iface":"","index":0},"srcCIDR":"172.19.14.125/32","dstCIDR":"0.0.0.0/1","l4proto":["6"],"dstPort":"5021","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false},
                {"search":"0.0.0.0/1","id":"92","vport":{"iface":"","index":0},"dstCIDR":"www.baidu.com","l4proto":[],"srcPort":"5021","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false}],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiGModifyTag :{"spiTagId":"","name":"GlobalSaas","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc","rules":[{"search":"google","id":"91","vport":{"iface":"","index":0},"srcCIDR":"187.19.14.125/32","dstCIDR":"0.0.0.0/1","l4proto":["6"],"dstPort":"5021","dstDomain":"","edit":false,"icmpType":"8","icmpCode":"0","first":false},
                ],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
  SpiChangeTagRules: {"spiTagId":"","name":"SPISaas","companyId":"068b9065-5fbd-4473-b9eb-ed49212866fc",
                     "add_rules":[{"id":"71","vport":{"iface":"","index":0},"dstCIDR":".*\\.biying\\.com","l4proto":["1","6"]}],
                     "delete_rules":[{"id":"71","search":"onenote"}],"tag":0,"priority":600,"role":"","enabled":false,"remark":"","siteList":[]},
}

const testSpiTemplateBody = {
  SpiTemplateSaas :{"actionTemplateId":"","name":"saasTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"SPISaas","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e","actions":{"inited":false,"saas":{"enable":true,"param":[{"id":"71","agent":"8.8.8.8","index":0,"ttl":"600","code":"1","dstCIDR":".*\\.onenote\\.com"},{"agent":"135004189","index":1,"ttl":"600","code":"1","dstCIDR":"","id":"72"}]},"fec":{"enable":false,"param":{"policy":"","dynamicParam":{"period": '1200',"trigger": '10',"recovery": '1'}}},"transportPolicy":{"enable":false,"param":{"policy":"","waitParam": {"maxTime": '12000',"maxPktNum": '20'}}},"priority":{"enable":false,"param":{"level":""}},"wan":{"enable":false,"param":{"policy":"assign","ports":[]}},"analyze":{"enable":false,"param":""},"office":{"enable":false,"param":{"nextHop":"","dnsParam":[]}}}},
  SpiModifyTemplateSaas :{"actionTemplateId":"","name":"saasModifyTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"SPIModifySaas","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e","actions":{"inited":false,"saas":{"enable":true,"param":[{"id":"71","agent":"8.8.8.8","index":0,"ttl":"600","code":"1","dstCIDR":".*\\.onenote\\.com"},{"agent":"135004189","index":1,"ttl":"600","code":"1","dstCIDR":"","id":"72"}]},"fec":{"enable":false,"param":{"policy":"","dynamicParam":{"period": '1200',"trigger": '10',"recovery": '1'}}},"transportPolicy":{"enable":false,"param":{"policy":"","waitParam": {"maxTime": '12000',"maxPktNum": '20'}}},"priority":{"enable":false,"param":{"level":""}},"wan":{"enable":false,"param":{"policy":"assign","ports":[]}},"analyze":{"enable":false,"param":""},"office":{"enable":false,"param":{"nextHop":"","dnsParam":[]}}}},
  SpiTemplateSTSaas :{"actionTemplateId":"","name":"saasSTTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"STSaas","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e","actions":{"inited":false,"saas":{"enable":true,"param":[{"id":"71","agent":"11.10.10.10","index":0,"ttl":"600","code":"1","dstCIDR":".*\\.onenote\\.com"},{"agent":"135004189","index":1,"ttl":"600","code":"1","dstCIDR":"","id":"72"}]},"fec":{"enable":false,"param":{"policy":"","dynamicParam":{"period": '1200',"trigger": '10',"recovery": '1'}}},"transportPolicy":{"enable":false,"param":{"policy":"","waitParam": {"maxTime": '12000',"maxPktNum": '20'}}},"priority":{"enable":false,"param":{"level":""}},"wan":{"enable":false,"param":{"policy":"assign","ports":[]}},"analyze":{"enable":false,"param":""},"office":{"enable":false,"param":{"nextHop":"","dnsParam":[]}}}},
  SpiTemplateGlobalSaas :{"actionTemplateId":"","name":"saasGlobalTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"GlobalSaas","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e","actions":{"inited":false,"saas":{"enable":true,"param":[{"id":"71","agent":"10.10.10.10","index":0,"ttl":"600","code":"1","dstCIDR":""},{"agent":"135004189","index":1,"ttl":"600","code":"1","dstCIDR":"","id":"72"}]},"fec":{"enable":false,"param":{"policy":"","dynamicParam":{"period": '1200',"trigger": '10',"recovery": '1'}}},"transportPolicy":{"enable":false,"param":{"policy":"","waitParam": {"maxTime": '12000',"maxPktNum": '20'}}},"priority":{"enable":false,"param":{"level":""}},"wan":{"enable":false,"param":{"policy":"assign","ports":[]}},"analyze":{"enable":false,"param":""},"office":{"enable":false,"param":{"nextHop":"","dnsParam":[]}}}},
  SpiTemplatePro :{"actionTemplateId":"","name":"saasProTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"allIpUdp","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e","actions":{"inited":false,"saas":{"enable":true,"param":[{"id":"91","agent":"135004189","index":0,"ttl":"600","code":"1","dstCIDR":""},{"agent":"135004189","index":1,"ttl":"600","code":"1","dstCIDR":"","id":"92"}]},"fec":{"enable":false,"param":{"policy":"","dynamicParam":{"period": '1200',"trigger": '10',"recovery": '1'}}},"transportPolicy":{"enable":false,"param":{"policy":"","waitParam": {"maxTime": '12000',"maxPktNum": '20'}}},"priority":{"enable":false,"param":{"level":""}},"wan":{"enable":false,"param":{"policy":"assign","ports":[]}},"analyze":{"enable":false,"param":""},"office":{"enable":false,"param":{"nextHop":"","dnsParam":[]}}}},
  SpiTemplateDelete :{"actionTemplateId":"","name":"saasTemDelete","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"SPISaas","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e","actions":{"inited":false,"saas":{"enable":true,"param":[{"id":"71","agent":"114.114.114.114","index":0,"ttl":"600","code":"1","dstCIDR":""},{"agent":"135004189","index":1,"ttl":"600","code":"1","dstCIDR":"","id":"72"}]},"fec":{"enable":false,"param":{"policy":"","dynamicParam":{"period": '99',"trigger": '10',"recovery": '1'}}},"transportPolicy":{"enable":false,"param":{"policy":"","waitParam": {"maxTime": '99',"maxPktNum": '20'}}},"priority":{"enable":false,"param":{"level":""}},"wan":{"enable":false,"param":{"policy":"assign","ports":[]}},"analyze":{"enable":false,"param":""},"office":{"enable":false,"param":{"nextHop":"","dnsParam":[]}}}},
  SpiTemplateAdd :{"actionTemplateId":"","name":"allIpTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"allIpUdp","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e",
                   "actions":{"inited":false,"saas":{"enable":true,"saasType":"自动出口","saasConfig":{},"param":[{"agent":"0","index":0,"ttl":"600","code":"1","dstCIDR":"","spiRuleId":""},{"agent":"0","index":0,"ttl":"600","code":"1","dstCIDR":"","spiRuleId":""}]},
                                             "transportPolicy":{"enable":true,"param":{"policy":"可靠","waitParam": {"maxTime": '12000',"maxPktNum": '20'}}},
                                             "fec":{"enable":true,"param":{"policy":"","dynamicParam": {"period": '1200',"trigger": '10',"recovery": '1'}}},
                                             "priority":{"enable":true,"param":{"level":"中"}},
                                             "wan":{"enable":true,"param":{"policy":"优选","ports":["WAN1","WAN2"]}},
                                             "analyze":{"enable":true,"param":""},
                                             "office":{"enable":true,"param":{"nextHop":""}}}},
  SpiSAASDesignatedTemplateAdd :{"actionTemplateId":"","name":"SAASDesignatedTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"allIpUdp","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e",
                                             "actions":{"inited":false,"saas":{"enable":true,"saasType":"指定出口","saasConfig":{'agent':'114.114.114.114', 'ttl': 599,'saasList':[{'saasName':'web-ci-saas','saasPort':'44.44.44.44-default-0'},{'saasName':'web-ci-saas2','saasPort':'55.55.55.55-中国移动-13'}]},
                                                                               "param":[{"agent":"0","index":0,"ttl":"600","code":"1","dstCIDR":"","spiRuleId":""},{"agent":"0","index":0,"ttl":"600","code":"1","dstCIDR":"","spiRuleId":""}]}}},
  SpiSAASDedicateTemplateModify :{"actionTemplateId":"","name":"saasDedicateTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"allIpUdp","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e",
                                                                               "actions":{"inited":false,"saas":{"enable":true,"saasType":"指定出口","saasConfig":{'agent':'8.8.8.9', 'ttl': 200,'saasList':[{'saasName':'web-ci-saas','saasPort':'44.44.44.44-default-0'}]},
                                                                                                                 "param":[{"agent":"0","index":0,"ttl":"600","code":"1","dstCIDR":"","spiRuleId":""},{"agent":"0","index":0,"ttl":"600","code":"1","dstCIDR":"","spiRuleId":""}]}}},
  SpiTemplateGAdd :{"actionTemplateId":"","name":"allGIpTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"GlobalModifySaas","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e",
                                             "actions":{"inited":false,"transportPolicy":{"enable":true,"param":{"policy":"可靠","waitParam": {"maxTime": '12000',"maxPktNum": '20'}}},
                                                                       "fec":{"enable":true,"param":{"policy":"","dynamicParam": {"period": '1200',"trigger": '10',"recovery": '1'}}},
                                                                       "priority":{"enable":true,"param":{"level":"中"}},
                                                                       "wan":{"enable":true,"param":{"policy":"优选","ports":["WAN1","WAN2"]}},
                                                                       "analyze":{"enable":true,"param":""},
                                                                       "office":{"enable":true,"param":{"nextHop":""}}}},
  SpiTemplateModify :{"actionTemplateId":"","name":"saasModifyTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"SPIModifySaas","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e",
                      "actions":{"inited":false,"fec":{"enable":true,"param":{"policy":"持续","dynamicParam":{"period": '9999',"trigger": '10',"recovery": '1'}}},
                                                "transportPolicy":{"enable":true,"param":{"policy":"可靠","waitParam": {"maxTime": '10',"maxPktNum": '1'}}}}},
  SpiTemplateGModify :{"actionTemplateId":"","name":"saasGlobalTemplate","tag":1,"companyId":"c06fe01e-9e09-4ec5-a4eb-9f87f27c5b06","tagName":"GlobalSaas","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e",
                                                "actions":{"inited":false,"fec":{"enable":true,"param":{"policy":"持续","dynamicParam":{"period": '9999',"trigger": '10',"recovery": '1'}}},
                                                                          "transportPolicy":{"enable":true,"param":{"policy":"可靠","waitParam": {"maxTime": '10',"maxPktNum": '1'}}}}},
  SPITemplateDedicate :{"actionTemplateId":"","name":"saasDedicateTemplate","tag":1,"companyId":"5fed3d13-b999-4d4d-8bbd-0c799ebfb02e","tagName":"GlobalSaas","tagId":"d2858457-88d2-48f1-b2e4-4d775074df4e",
                        "actions":{"inited":false,"saas":{"enable":true,"param":[{"agent":"8.8.8.8","ttl":"600","srcCIDR":"","dstCIDR":".*\\.google\\.com","l4proto":"","srcPort":"","dstPort":"","id":"71"},
                        {"agent":"0","ttl":"600","srcCIDR":"","dstCIDR":"8.8.8.8","l4proto":"","srcPort":"","dstPort":"","id":"72"}],"type":"assignExit","appointment":[{"serviceId":344,"carrierId":0,"carrierList":[{"public_ip":"44.44.44.44","lan_ip":"192.168.20.1","netmask":24,"gateway":"10.192.12.1","is_nat":false,"iface_name":"enp2s0","isp":{"isp_name":"default","isp_code":0}}]},
                        {"serviceId":328,"carrierId":13,"carrierList":[{"public_ip":"55.55.55.55","lan_ip":null,"netmask":24,"gateway":"10.192.12.1","is_nat":false,"iface_name":"enp1s0f0","isp":{"isp_name":"中国移动","isp_code":13}}]}],"ttl":"600","dns":"8.8.8.8"},"fec":{"enable":false,"param":{"policy":"","dynamicParam":{"period":"1200","trigger":"10","recovery":"1"}}},
                        "transportPolicy":{"enable":false,"param":{"policy":"","waitParam":{"maxTime":"12000","maxPktNum":"20"}}},"priority":{"enable":false,"param":{"level":""}},"wan":{"enable":false,"param":{"policy":"assign","ports":[]}},"analyze":{"enable":false,"param":""},"office":{"enable":false,"param":{"nextHop":"","dnsParam":[]}}}}                                                               
}

const testScenarioBody = {
  SpiScenarioSaas : {"spiScenarioId":"","name":"saasScenario","companyId":"a4309a85-1b2e-4a4c-af07-b3a28f7204a3","siteId":[],"remark":"","spiStrategys":[],"templateList":[],"siteList":[]},
  SpiScenarioPro : {"spiScenarioId":"","name":"ProScenario","companyId":"a4309a85-1b2e-4a4c-af07-b3a28f7204a3","siteId":[],"remark":"","spiStrategys":[],"templateList":[],"siteList":[]},
  SpiScenarioST : {"spiScenarioId":"","name":"STScenario","companyId":"a4309a85-1b2e-4a4c-af07-b3a28f7204a3","siteId":[],"remark":"","spiStrategys":[],"templateList":[],"siteList":[]},
  SpiScenarioG : {"spiScenarioId":"","name":"GScenario","companyId":"a4309a85-1b2e-4a4c-af07-b3a28f7204a3","siteId":[],"remark":"","spiStrategys":[],"templateList":[],"siteList":[]},
  SpiScenarioDedicate : {"spiScenarioId":"","name":"DedicateScenario","companyId":"a4309a85-1b2e-4a4c-af07-b3a28f7204a3","siteId":[],"remark":"","spiStrategys":[],"templateList":[],"siteList":[]},
  SpiScenarioAdd : {"name": "ScenarioAdd"},
  SpiDedicateScenario : {"name": "DedicateScenario","spiStrategys":['SAASDesignatedTemplate']}
}

const testStrategyBody={
  SpiStrategyAdd : {"name": "gwsesiteSaasAdd", "siteList":["spi-gwsite","spi-sesite"]},
  SpiStrategyDedicate : {"name": "gwsesiteSaasAdd", "siteList":["spi-dedicate-gwsite"]},
  SpiStrategyModify : {"name": "pasiteSaasAdd", "siteList":["spi-pasite"]}
}

const testQosBody = {
  gwQos1 : {"first":true,"qosId":"","name":"","companyId":"3714f895-aa85-4a60-96fc-24f5885475eb","siteId":"b99f549e-95d0-4db4-9613-f60718f76858","ipIn":"192.168.1.0/24","ipOut":"192.168.4.1/32","protocolNo":"*","portIn":"342","portOut":"5201","neworkFlowType":"5","priority":"2","edit":true},
  gwQos2 : {"first":true,"qosId":"","name":"","companyId":"3714f895-aa85-4a60-96fc-24f5885475eb","siteId":"b99f549e-95d0-4db4-9613-f60718f76858","ipIn":"192.168.2.0/28","ipOut":"192.168.5.0/28","protocolNo":"1","portIn":"343","portOut":"5202","neworkFlowType":"2","priority":"1","edit":true},
  gwQos3 : {"first":true,"qosId":"","name":"","companyId":"3714f895-aa85-4a60-96fc-24f5885475eb","siteId":"b99f549e-95d0-4db4-9613-f60718f76858","ipIn":"192.168.3.1/32","ipOut":"192.168.6.0/24","protocolNo":"17","portIn":"344","portOut":"5203","neworkFlowType":"3","priority":"0","edit":true},
  paQos1 : {"first":true,"qosId":"","name":"","companyId":"3714f895-aa85-4a60-96fc-24f5885475eb","siteId":"b99f549e-95d0-4db4-9613-f60718f76858","ipIn":"10.192.1.1/32","ipOut":"10.192.3.0/24","protocolNo":"1","portIn":"222","portOut":"443","neworkFlowType":"2","priority":"1","edit":true},
  paQos2 : {"first":true,"qosId":"","name":"","companyId":"3714f895-aa85-4a60-96fc-24f5885475eb","siteId":"b99f549e-95d0-4db4-9613-f60718f76858","ipIn":"10.192.2.0/28","ipOut":"10.192.4.0/24","protocolNo":"6","portIn":"223","portOut":"444","neworkFlowType":"1","priority":"0","edit":true},
  seQos1 : {"first":true,"qosId":"","name":"","companyId":"3714f895-aa85-4a60-96fc-24f5885475eb","siteId":"b99f549e-95d0-4db4-9613-f60718f76858","ipIn":"172.10.1.0/24","ipOut":"172.10.2.0/28","protocolNo":"17","portIn":"32","portOut":"80","neworkFlowType":"3","priority":"2","edit":true}
}

const testUnionBody = {
  testSeriesUnions:{"unionType":"Hub-spoken","hubSite":"beijing","spokenSites":['shanghai','chongqing'],
  "office":true, "private":false, "bondSpeed":1024},
  testParallelUnions:{"unionType":"Hub-spoken","hubSite":"nanjing","spokenSites":['wuhan','guangzhou','changsha','nanChang'],
  "office":true, "private":false, "bondSpeed":1024},
  testGatewaylUnions:{"unionType":"普通","site1":"guangzhou","site2":'changsha',
  "office":true, "private":false, "bondSpeed":1024},
  testGatewayHAUnions:{"unionType":"普通","site1":"wuhan","site2":'nanChang',
  "office":true, "private":false, "bondSpeed":1024},
  testParallel_hubUnions:{"unionType":"Hub-spoken","hubSite":"un-pasite","spokenSites":['un-gwsite','un-sesite'],
  "office":true, "private":false, "bondSpeed":10},
  testbatchSiteUnion:{"unionType":"普通","site1":"site-2091","site2":'site-2092',
  "office":true, "private":false, "bondSpeed":1024},
  testse_gwUnions:{"unionType":"普通","site1":"un-sesite","site2":'un-gwsite',
  "office":true, "private":false, "bondSpeed":1024}
}

const testManagerBody = {
  basic: {global:[{"ip":"127.0.0.1","port":65535},{"ip":"127.0.0.2","port":80}],specific:{}},
  add: {global:[{"ip":"127.0.0.1","port":33333},{"ip":"127.0.0.2","port":81}],specific:{}}
}
const testOpenflowBody = {
  basic:{global:[{"ip":"127.0.0.1","port":6633},{"ip":"127.0.0.1","port":6653}],specific:{}},
  add:{global:[{"ip":"127.0.0.1","port":6634},{"ip":"127.0.0.1","port":6654}],specific:{}}
}
const testNetAlgBody = {
  default : {"upperBandwidth":200,"lowerBandwidth":5,"upperBwPercent":300,"lowerBwPercent":20,"maxLossIn15Min":0.8,"avgLossIn60Min":0.4,"maxLossRatio":100,"forwardingCost":2,"weightCoefficient":2},
  edit : {"upperBandwidth":100,"lowerBandwidth":20,"upperBwPercent":200,"lowerBwPercent":30,"maxLossIn15Min":1.8,"avgLossIn60Min":0.8,"maxLossRatio":10,"forwardingCost":5,"weightCoefficient":5}
}
const testGlobalConfigBody = {
  default : {"regUrl":"https://controller-st.netgrounder.com:9001/api/v1/ne/cpe","authUrl":"https://authserver-st.netgrounder.com","collectdAddr":"10.194.20.105","collectdPort":"6789","salt":"salt-cpe.test.netgrounder.com","controllers":[]}
}

const saasSearchPatternBody = {
  hubeiCode : {"proxyServices":[],"neIds":[327,328,343],"popIds":["web-ci-anycast","web-ci-saas","web-ci-anycast2"],"_id":"5f3c7fdaba11d102ee1e3a07","areaCode":"0X8058580","__v":0,"area":6,"areaDes":"CenterChina","country":1,"countryDes":"China","district":22,"districtDes":"Hubei","isp":1,"ispDes":"ChinaTelecom","region":1,"regionDes":"EastAsia","popDetailLists":[]},
  shanghaiCode : {"proxyServices":[],"neIds":[328],"popIds":["web-ci-saas"],"_id":"5f3c7fdaba11d102ee1e39f6","areaCode":"0X8054400","__v":0,"area":5,"areaDes":"EastChina","country":1,"countryDes":"China","district":16,"districtDes":"Shanghai","isp":1,"ispDes":"ChinaTelecom","region":1,"regionDes":"EastAsia","popDetailLists":[]},
  chinaCode: {"proxyServices":[],"neIds":[],"popIds":[],"_id":"5f3fe5a50910b1bf1ce0544d","areaCode":"0X8040000","__v":0,"area":0,"areaDes":"*","country":1,"countryDes":"China","district":0,"districtDes":"*","isp":1,"ispDes":"ChinaTelecom","region":1,"regionDes":"EastAsia","popDetailLists":[]},
  SingaporeCode: {"proxyServices":[],"neIds":[],"popIds":[],"_id":"5f3fe5a50910b1bf1ce055d3","areaCode":"0X180c0000","__v":0,"area":0,"areaDes":"*","country":3,"countryDes":"Singapore","district":0,"districtDes":"*","isp":36,"ispDes":"Singapore","region":3,"regionDes":"SoutheastAsia","popDetailLists":[]}
  // hubeiDelete : {"proxyServices":[],"neIds":[],"popIds":[],"_id":"5f3c7fdaba11d102ee1e3a07","areaCode":"0X8058580","__v":0,"area":6,"areaDes":"CenterChina","country":1,"countryDes":"China","district":22,"districtDes":"Hubei","isp":1,"ispDes":"ChinaTelecom","region":1,"regionDes":"EastAsia","popDetailLists":[]},
  // shanghaiDelete : {"proxyServices":[],"neIds":[],"popIds":[],"_id":"5efdc502ba11d102eea4be10","areaCode":"0X8054400","__v":0,"area":5,"areaDes":"EastChina","country":1,"countryDes":"China","district":16,"districtDes":"Shanghai","isp":0,"ispDes":"ALIYUN","region":1,"regionDes":"EastAsia","popDetailLists":[]},
}

const popBody ={
  testpop: {"routeCode":{"type":"CR","cac":4,"eac":1},"popType":6,"neId":"","status":"NORMAL","edit":true,"selected":false,"first":true,"popId":"X223328",
  "url":"http://10.194.20.105:8000/api/v1/configs/servers/47","hostname":"test-pop","os_version":"Ubuntu","tags":["node.cr","node.dpdk"],
  "ips":[{"public_ip":"11.1.1.2","lan_ip":"10.1.1.2","netmask":24,"gateway":"10.1.1.1","is_nat":true,"iface_name":"enp1s0f0","isp":{"isp_name":"中国电信","isp_code":11}}],
  "geo":{"country":{"en":"","zh":"","longitude":"","latitude":""},"province":{"en":"","zh":"","longitude":"","latitude":""},"city":{"en":"","zh":"","longitude":"","latitude":""}},
  "saasServices":[{"serviceId":11,"iface":"enp1s0f0"}]},
  testpop2: {"routeCode":{"type":"CR","cac":4,"eac":2},"popType":6,"neId":"","status":"NORMAL","edit":true,"selected":false,"first":true,"popId":"X223315",
  "url":"http://10.194.20.105:8000/api/v1/configs/servers/48","hostname":"test-pop2","os_version":"Ubuntu 1804","tags":["env.test","node.kernal"],
  "ips":[{"public_ip":"22.22.22.22","lan_ip":"192.168.20.1","netmask":24,"gateway":"","is_nat":false,"iface_name":"enp1s0f0","isp":{"isp_name":"中国联通","isp_code":12}}],
  "geo":{"country":{"en":"China","zh":"中国","longitude":null,"latitude":null},"province":{"en":"Shanghai","zh":"上海市","longitude":null,"latitude":null},"city":{"en":"Shanghai","zh":"上海市","longitude":null,"latitude":null}},
  "saasServices":[]},
  testpop3: {"routeCode":{"type":"ER","cac":4,"eac":11},"popType":6,"neId":"","status":"NORMAL","edit":true,"selected":false,"first":true,"popId":"X223313",
  "url":"http://10.194.20.105:8000/api/v1/configs/servers/49","hostname":"test-pop3","os_version":"Ubuntu 1804","tags":["env.test","node.dpdk"],
  "ips":[{"public_ip":"11.11.11.11","lan_ip":"192.168.10.1","netmask":24,"gateway":"","is_nat":false,"iface_name":"enp1s0f0","isp":{"isp_name":"中国联通","isp_code":12}}],
  "geo":{"country":{"en":"China","zh":"中国","longitude":null,"latitude":null},"province":{"en":"Shanghai","zh":"上海市","longitude":null,"latitude":null},"city":{"en":"Shanghai","zh":"上海市","longitude":null,"latitude":null}},
  "saasServices":[{"serviceId":12,"iface":"enp1s0f0"}]},
  testpop4 :{"routeCode":{"type":"CR","cac":4,"eac":22},"popType":6,"neId":"","status":"NORMAL","edit":true,"selected":false,"first":true,"popId":"X223316",
  "url":"http://10.194.20.105:8000/api/v1/configs/servers/50","hostname":"test-pop4","os_version":"Ubuntu 1804","tags":["env.test","node.cr","node.kernal"],
  "ips":[{"public_ip":"11.11.1.1","lan_ip":null,"netmask":24,"gateway":"","is_nat":false,"iface_name":"enp8s0f0","isp":{"isp_name":"中国联通","isp_code":12}}],
  "geo":{"country":{"en":"","zh":"","longitude":"","latitude":""},"province":{"en":"","zh":"","longitude":"","latitude":""},"city":{"en":"","zh":"","longitude":"","latitude":""}},"saasServices":[]}
}

const testPopBody = {
   testSTPop1Body:{"hostName": "cn-sh-pop-1","popId":"S2K781","cac":4,"eac":4,
   "ipAddress":[{'publicAddress':'10.194.20.4','isp':'default','ispCode':140,'iface':'enp8s0f0','nat':false},
   {'publicAddress':'10.196.20.4','isp':'中国电信','ispCode':11,'iface':'enp8s0f1','nat':false},
   {'publicAddress':'10.196.20.5','isp':'中国移动','ispCode':13,'iface':'enp8s0f2','nat':false}]},
   testSTPop2Body:{"hostName": "cn-sh-pop-2","popId":"X223311","cac":4,"eac":5,
   "ipAddress":[{'publicAddress':'10.194.20.3','isp':'default','ispCode':140,'iface':'enp1s0f0','nat':false},
   {'publicAddress':'10.196.20.3','isp':'中国电信','ispCode':11,'iface':'enp1s0f1','nat':false}]},
   testPopBody:{"hostName": "test-pop","popId":"X223328","cac":4,"eac":1,
   "ipAddress":[{'publicAddress':'11.1.1.2','isp':'中国电信','ispCode':11,'iface':'enp1s0f0','nat':true},
   {'publicAddress':'13.1.1.3','isp':'中国联通','ispCode':12,'iface':'enp1s0f3','nat':false}]},
   testPop1Body:{"hostName": "test-pop3","popId":"X223313","cac":4,"eac":11,"cpeNum":2,"cpes":[['pop-company',65521,2061,'modify-selocation'],['pop-company',65523,2063,'modify-selocation']],
   "ipAddress":[{'publicAddress':'11.11.11.11','isp':'中国联通','ispCode':12,'iface':'enp1s0f0','nat':false}]},
   testPop2Body:{"hostName": "test-pop2","popId":"X223315","cac":4,"eac":2,"cpeNum":2,"cpes":[['pop-company',65522,2062,'modify-selocation'],['pop-company',65521,2061,'modify-selocation']],
   "ipAddress":[{'publicAddress':'22.22.22.22','isp':'中国联通','ispCode':12,'iface':'enp1s0f0','nat':false}]},
   testDevicePopBody:{"hostName": "device-pop","popId":"X30000","cac":12,"eac":11,
   "ipAddress":[{'publicAddress':'10.30.1.2','isp':'中国电信','ispCode':11,'iface':'enp1s0f0','nat':true},
   {'publicAddress':'10.40.1.3','isp':'中国联通','ispCode':12,'iface':'enp1s0f3','nat':false}]},
   testDevicePop2Body:{"hostName": "device-pop2","popId":"X30001","cac":10,"eac":3,
   "ipAddress":[{'publicAddress':'12.12.11.5','isp':'中国电信','ispCode':11,'iface':'enp1s0f1','nat':true},
   {'publicAddress':'12.12.11.10','isp':'中国移动','ispCode':10,'iface':'enp1s0f0','nat':false}]}
} 

const testServiceBody = {
  testSTSaas1Body:{"hostName": "cn-sh-pop-2","popId":"X223311","prefer_pop_id":342,"service":"Saas服务",'popType':8},
  testSTAnycast1Body:{"hostName": "anycast-st-vm-01","popId":"anycast-st-vm-01","prefer_pop_id":342,"service":"Anycast服务",'popType':7},
  testSTSaas2Body:{"hostName": "saas-st-vm-01","popId":"saas-st-vm-01","prefer_pop_id":326,"service":"Saas服务",'popType':8},
  putAnycastBody:{"popId":"web-ci-anycast","neId":"","preferPop":326,"edit":true,"selected":false,"first":true,"sn": "web-ci-anycast","url":"http://10.194.20.105:8000/api/v1/configs/servers/61","hostname":"web-ci-anycast","os_version":"1804",
  "tags":["env.test","node.kernal"],"ips":[{"public_ip":"4.4.4.4","lan_ip":"192.168.3.2","netmask":24,"gateway":"10.192.12.1","is_nat":false,"iface_name":"enp1s0f0","isp":{"isp_name":"default","isp_code":140}}],
  "geo":{"country":{"en":"","zh":"","longitude":"","latitude":""},"province":{"en":"","zh":"","longitude":"","latitude":""},"city":{"en":"","zh":"","longitude":"","latitude":""}},"popType":7,
  "routeCode":{"type":"CR","cac":4,"eac":1},"saasServices":[]},
  putSaasBody:{"popId":"web-ci-saas","neId":"","preferPop":342,"edit":true,"selected":false,"first":true,"sn": "web-ci-saas","url":"http://10.194.20.105:8000/api/v1/configs/servers/62","hostname":"web-ci-saas","os_version":"1804",
  "tags":["env.test","node.kernal"],"ips":[{"public_ip":"44.44.44.44","lan_ip":"192.168.20.1","netmask":24,"gateway":"10.192.12.1","is_nat":false,"iface_name":"enp2s0","isp":{"isp_name":"default","isp_code":140}}],
  "geo":{"country":{"en":"","zh":"","longitude":"","latitude":""},"province":{"en":"","zh":"","longitude":"","latitude":""},"city":{"en":"","zh":"","longitude":"","latitude":""}},"popType":8,
  "routeCode":{"type":"CR","cac":4,"eac":2},"saasServices":[]},
  putAnycastBody2:{"popId":"web-ci-anycast2","neId":"","preferPop":358,"edit":true,"selected":false,"first":true,"sn": "web-ci-anycast2","url":"http://10.194.20.105:8000/api/v1/configs/servers/63","hostname":"web-ci-anycast2","os_version":"1804",
  "tags":["env.test","node.kernal"],"ips":[{"public_ip":"5.5.5.5","lan_ip":"192.168.10.1","netmask":24,"gateway":"10.192.12.1","is_nat":false,"iface_name":"enp1s0f0","isp":{"isp_name":"default","isp_code":140}}],
  "geo":{"country":{"en":"","zh":"","longitude":"","latitude":""},"province":{"en":"","zh":"","longitude":"","latitude":""},"city":{"en":"","zh":"","longitude":"","latitude":""}},"popType":7,
  "routeCode":{"type":"ER","cac":4,"eac":11},"saasServices":[]},
  putCompanySaasBody:{"popId":"web-ci-saas2","neId":"","preferPop":374,"edit":true,"selected":false,"first":true,"sn": "web-ci-saas2","url":"http://10.194.20.105:8000/api/v1/configs/servers/64","hostname":"web-ci-saas2","os_version":"1804",
  "tags":["env.test","node.cr","node.dpdk","node.kernal"],"ips":[{"public_ip":"55.55.55.55","lan_ip":null,"netmask":24,"gateway":"10.192.12.1","is_nat":false,"iface_name":"enp1s0f0","isp":{"isp_name":"中国移动","isp_code":13}}],
  "geo":{"country":{"en":"China","zh":"中国","longitude":null,"latitude":null},"province":{"en":"Shanghai","zh":"上海市","longitude":null,"latitude":null},"city":{"en":"Shanghai","zh":"上海市","longitude":null,"latitude":null}},"popType":8,
  "routeCode":{"type":"CR","cac":4,"eac":22},"saasServices":[{"serviceId":13,"iface":"enp1s0f0"}]}
  }

const putTestPopBody = {
  "routeCode":{"type":"ER","cac":4,"eac":11},
  "popType":6,"neId":"",
  "status":"NORMAL","edit":true,"selected":false,"first":true,"sn": "X223313",
  "popId":"X223313","url":"http://10.194.20.105:8000/api/v1/configs/servers/49",
  "hostname":"test-pop3","os_version":"Ubuntu",
  "tags":[],
  "ips":[],"geo":{},"saasServices":[]}

const putTestPop2Body = {
    "routeCode":{"type":"ER","cac":4,"eac":2},
    "popType":6,"neId":"",
    "status":"NORMAL","edit":true,"selected":false,"first":true,"sn": "X223315",
    "popId":"X223315","url":"http://10.194.20.105:8000/api/v1/configs/servers/48",
    "hostname":"test-pop2","os_version":"Ubuntu",
    "tags":[],
    "ips":[],"geo":{},"saasServices":[]}

const putDevicePopBody = {
  "routeCode":{"type":"ER","cac":12,"eac":11},
  "popType":6,"neId":"",
  "status":"NORMAL","edit":true,"selected":false,"first":true,"sn": "X30000",
  "popId":"X30000","url":"http://10.194.20.105:8000/api/v1/configs/servers/68",
  "hostname":"device-pop","os_version":"Ubuntu",
  "tags":[],
  "ips":[],"geo":{},"saasServices":[]}

const putDevicePop2Body = {
  "routeCode":{"type":"ER","cac":10,"eac":3},
  "popType":6,"neId":"",
  "status":"NORMAL","edit":true,"selected":false,"first":true,"sn": "X30001",
  "popId":"X30001","url":"http://10.194.20.105:8000/api/v1/configs/servers/70",
  "hostname":"device-pop2","os_version":"Ubuntu",
  "tags":[],
  "ips":[],"geo":{},"saasServices":[]}

const testFirewallBody = {
  aclFailBody:{"name":"FailAcl","strategy":"permit",'hint':'五元组不可全部为空'},
  aclFullBody:{"name":"FullAcl","site_name":'gwsite1-firewall',"priority":499,"protocol":["TCP","UDP","ICMP"],"srcCIDR":"192.168.0.0/1","dstCIDR":"192.168.255.254","dstPort":"22,5000-6000","strategy":"permit",'hint':'创建成功'},
  aclOnlyPortBody:{"name":"OnlyPort","dstPort":"22,5000-5500,65535","strategy":"permit",'hint':'创建成功'},
  aclAuthBody:{"name":"authAcl","priority":499,"protocol":["TCP","UDP","ICMP"],"srcCIDR":"192.168.0.0/1","dstCIDR":"192.168.255.254","dstPort":"22,5000-6000","strategy":"permit",'hint':'创建成功'},
  aclOnlyPortCompany2:{"name":"OnlyPort","site_name":'gwsite3-firewall',"dstPort":"22,5000-5500,65535","strategy":"permit",'hint':'创建成功'}
}

const testRouterBody = {
  routerFailBody:{"name":"FailRouter","site_name":'gwsite2-router',"nextHop":"gwsite1-router",'hint':'五元组不可全部为空'},
  routerFullBody:{"name":"FullRouter","site_name":'gwsite2-router',"priority":499,"protocol":["TCP","UDP","ICMP"],"srcCIDR":"192.168.0.0/1","dstCIDR":"192.168.255.254","srcPort":"65535","dstPort":"22,5000-6000","nextHop":"gwsite2-router",'hint':'创建成功'},
  routerOnlyPortBody:{"name":"OnlyPort","srcPort":"0","dstPort":"22,5000-5500,65535","nextHop":"gwsite1-router",'hint':'创建成功'},
  routerAuthBody:{"name":"authRouter","priority":499,"protocol":["TCP","UDP","ICMP"],"srcCIDR":"192.168.0.0/1",'hint':'必填项'},
  routerOnlyPortCompany2:{"name":"OnlyPort","site_name":'gwsite3-router',"srcPort":"0","dstPort":"22,5000-5500,65535","nextHop":"gwsite4-router",'hint':'创建成功'}
}

const testRouterModifyBody = {
  modifyNextHop:{"name":"FullRouter","nextHop":"gwsite1-router",'action':'cancel'},
  modifyDstPort:{"name":"FullRouter","dstPort":"65535",'action':'confirm'}
}

const testCPEGlobalConfigBody = {
    ST: {
        "regUrl": "https://controller-st.netgrounder.com:9001/api/v1/ne/cpe",
        "authUrl": "https://authserver-st.netgrounder.com",
        "collectdAddr": "10.194.20.105",
        "collectdPort": "6789",
        "salt": "salt-cpe.test.netgrounder.com",
        "prismAddr": "10.194.20.105:9877",
        "controllers": [
          {
            "domain": "controller-st.netgrounder.com",
            "port": 6633,
            "mode": "网关"
          },
          {
            "domain": "controller-st.netgrounder.com",
            "port": 6633,
            "mode": "旁挂"
          },
          {
            "domain": "controller-st.netgrounder.com",
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

const siteTemp = {
"parallel" : {"name":"paTemp","engName":"","remark":"pa remark","companyId":"0c35c96a-baf9-4f2c-86cb-ba2fb10431a1","city":"","engLocation":"","location":"pa location","ha":false,
"config":{"privateAddrs":"172.19.14.0/24","seriesAddrs":"","nets":[],"cpeType":"parallel","mtu":1400,"localPort":8989,"enabled":true,"sn":["1005"],
  "wan":[{"publicIp":"10.194.14.2","ipType":"static","ipAddress":"172.20.14.25","mask":"24","ipmode":"FIA","gateway":"172.20.14.1","bandwidth":"1000","logicName":"","proxy":true,"preferHomeCodeCac":"4","preferGroup":"103","preferHomeCodeEac":"4","preferIP":"10.194.20.4"},
    {"ipmode":"FIA","proxy":true,"publicIp":"10.196.14.2","ipType":"static","ipAddress":"172.20.14.26","mask":"24","gateway":"172.20.14.1","bandwidth":"1000","preferGroup":"","preferCac":"4","preferHomeCodeCac":"4","preferHomeCodeEac":"5","preferIP":"10.194.20.3"}],
  "lan":[{"lanIp":"172.21.14.25","mask":"24","ethNum":1,"internet":true,"idc":true,"dhcp":false,"gateway":"172.21.14.1","dhcpSever":false,"dhcpPool":""}],
  "wifi":{"ssid":"","encryption":["none"],"network":"","password":"","macCheck":"","macArr":""},"fwGroups":[],"natGroups":[],"bandwidth":10},
"haConfig":{"wanipAddress1":"","wanipAddress2":"","wanmask1":"","wanmask2":"","wangateway1":"","wangateway2":"","lanIp1":"","lanIp2":"","lanIpMask1":"","lanIpMask2":"","reportInterval":60,"scoreInterval":60,"enableLte":false,"lteName":"wwan0","isHub": false,"longitude":"115.95046","latitude":"28.551604"},
"sideHanging":false,"sideHangingSn":""
},
"series" : {"name":"seTemp","engName":"","remark":"remart","companyId":"0c35c96a-baf9-4f2c-86cb-ba2fb10431a1","city":"","engLocation":"","location":"se-location","ha":false,
"config":{"privateAddrs":"","seriesAddrs":"10.193.0.0/26\n10.193.0.64/27\n10.193.0.96/30\n10.193.0.100/32","nets":[],"cpeType":"series","mtu":1400,"localPort":8989,"enabled":true,"sn":["2011"],
  "wan":[{"publicIp":"","ipType":"","ipAddress":"","mask":"","ipmode":"FIA","gateway":"","bandwidth":10,"logicName":"","proxy":true,"preferGroup":"101","preferCac":"4","preferHomeCodeCac":"4","preferHomeCodeEac":"5","preferIP":"10.192.20.4","gatewayMac":"11:22:33:44:55:66","staticIp":"10.192.20.1"}],
  "lan":[{"lanIp":"","mask":"","ethNum":1,"internet":true,"idc":true,"dhcp":false,"gateway":"","dhcpSever":false,"dhcpPool":""}],
  "wifi":{"ssid":"","encryption":["none"],"network":"","password":"","macCheck":"","macArr":""},"fwGroups":[],"natGroups":[],"bandwidth":10},
"haConfig":{"wanipAddress1":"","wanipAddress2":"","wanmask1":"","wanmask2":"","wangateway1":"","wangateway2":"","lanIp1":"","lanIp2":"","lanIpMask1":"","lanIpMask2":"","reportInterval":60,"scoreInterval":60,"enableLte":false,"lteName":"wwan0","enableInterflow":true,"isHub": false,"longitude":"115.95046","latitude":"28.551604"},
"sideHanging":false,"sideHangingSn":""
},
"gateway" : {"name":"gwTemp","engName":"","remark":"gw remark","companyId":"0c35c96a-baf9-4f2c-86cb-ba2fb10431a1","city":"","engLocation":"","location":"guanghzou","ha":false,
"config":{"privateAddrs":"172.19.43.0/24","seriesAddrs":"","nets":[],"cpeType":"gateway","mtu":1400,"localPort":8989,"enabled":true,"sn":["1004"],
  "wan":[{"publicIp":"","ipType":"dhcp","ipAddress":"","mask":"","ipmode":"FIA","gateway":"","bandwidth":10,"logicName":"","proxy":true,"preferGroup":"101 102","preferCac":"4","preferHomeCodeCac":"4","preferHomeCodeEac":"5","preferIP":"10.192.20.3"},
    {"ipmode":"FIA","proxy":true,"ipType":"static","ipAddress":"10.194.12.2","mask":"24","gateway":"10.194.12.1","bandwidth":"1000","preferGroup":"102","preferCac":"4","preferHomeCodeCac":"4","preferHomeCodeEac":"4","preferIP":"10.194.20.3"}],
  "lan":[{"lanIp":"172.19.43.1","mask":"24","ethNum":"4","internet":true,"idc":true,"dhcp":false,"gateway":"172.19.43.1","dhcpSever":false,"dhcpPool":""},
    {"lanIp":"192.168.1.1","mask":"24","gateway":"192.168.1.1","dhcpSever":true,"dhcpPool":"192.168.1.2\n192.168.1.9","ethNum":"1"}],
  "wifi":{"ssid":"testwifi","encryption":["22","psk2"],"network":"lan1","password":"12345678","macCheck":"allow","macArr":"00:83:09:00:15:d4\n00:83:09:00:15:d5"},"fwGroups":[],"natGroups":[],"bandwidth":10},
"haConfig":{"wanipAddress1":"","wanipAddress2":"","wanmask1":"","wanmask2":"","wangateway1":"","wangateway2":"","lanIp1":"","lanIp2":"","lanIpMask1":"","lanIpMask2":"","reportInterval":60,"scoreInterval":60,"enableLte":true,"lteName":"wwan0","natNet":"100.64.0.0/16","isHub": false,"longitude":"115.95046","latitude":"28.551604"},
"sideHanging":false,"sideHangingSn":""
}
}

const menuList = {
  admin_g_view: {'配置':['配置','站点注册','设备管理','拓扑管理','Pop点管理','服务管理','区域码管理','控制器管理','策略管理'],
                 '监控':['监控','设备告警','服务状态'],
                 '账户':['账户','个人账户','角色管理','公司管理', "行政区划"],
                 '日志':['操作日志','登录日志']},
  admin_c_view: {'配置':['配置','站点注册','设备管理','拓扑管理','区域码管理','防火墙','路由管理','策略管理','审计配置'],
                 '监控':['监控','站点概览','设备告警'],
                 '账户':['账户','个人账户',"角色管理", "行政区划"],
                 '报表':['统计报表'],
                 '日志':['操作日志','登录日志'],
                 '审计':['数据分析','实时监控','上网日志']},
  company_default_admin_view: {'配置':['配置','站点注册','设备管理','拓扑管理','防火墙','路由管理','策略管理'],
                               '监控':['监控','站点概览','设备告警'],
                               '账户':['账户','个人账户',"角色管理", "行政区划"]},
  company_default_user_view: {'配置':['配置','站点注册','设备管理','拓扑管理','防火墙','路由管理','策略管理'],
                              '监控':['监控','站点概览','设备告警'],
                              '账户':['账户','个人账户',"角色管理", "行政区划"]},
  multiRole_user_view: {'配置':['配置','站点注册','设备管理','拓扑管理','区域码管理']}
}

const roleList = {companyMode: {'配置':['站点注册','设备管理','拓扑管理','区域码管理','防火墙','路由管理','策略管理','审计配置'],'监控':['站点概览','设备告警'],'报表':['统计报表'],'日志':['操作日志','登录日志'],'审计':['数据分析','实时监控','上网日志'],'账户':['个人账户','角色管理','行政区划']},
                  globalMode: {'配置':['Pop点管理','服务管理','区域码管理(全局)','控制器管理'],'监控':['服务状态'],'报表':[],'日志':[],'审计':[],'账户':['公司管理']}}

const alert = {
  alertGroup : {"groupId":"","name":"testAlertGroup","companyId":"2fc5d5bb-a3d0-4dd3-b6cc-96f821f9f27d","contacts":[{"userName":"alertUser1","email":"alert1@alert.com","mobile":"13344444444"},{"userName":"alertUser2","email":"alert2@alert.com","mobile":"13344444445"}]},
  alertRule : {"alertGroup":["testModifyAlertGroup"],"alertType":["CPE设备故障","CPE业务异常","CPE网络异常","CPE HA故障","CPE配置错误"],"limit":100,"severity":["紧急","重要","一般"]}
}

const alertBody = {
  alertGroup : {"groupId":"","name":"testModifyAlertGroup","companyId":"2fc5d5bb-a3d0-4dd3-b6cc-96f821f9f27d","contacts":[{"userName":"alertUser1","email":"alert1@alert.com","mobile":"+8613344444444"},{"userName":"alertUser2","email":"alert2@alert.com","mobile":"+8613344444445"}]},
  alertRule : {"ruleId":"","companyId":"2fc5d5bb-a3d0-4dd3-b6cc-96f821f9f27d","limit":100,"filters":{"severity":["Emergency","Critical","Warning"],"name":["CpeConfigError","CPEDupMaster","CPENoMaster","NetworkPortDown","CpeE2ETrafficDropOff","CpeMobileTrafficTooHigh","ServiceQualityDecline","CpeStatusError","LinkScoreDecline","NodeNetworkError","NodeOffline","NodeMemoryLow","NodeCpuHigh","CpeStatusError","NodeStorageLow","NodeLoadHigh","CpeHardwareError"]},"groups":["60121bb114e97dcb390f6e9c"]}
}

const auditParam = {
  auditUrl : 'https://139.224.41.89',
  auditUrlFail : 'https://11.224.41.89',
  auditPort : '3080',
  siteMac: '02:00:4c:4f:4f:50',
  siteMac2: '0A:00:4c:4f:4f:70',
  siteSTNanchangMac: '00:E0:67:1A:AB:E6'
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

const RegionTestBody = {
  "default_regions": ['华北地区（17）','东北地区（16）','华东地区（52）','华中地区（18）','华南地区（18）','西南地区（7）','西北地区（6）'],
  "test_regions": ['测试地区','华北地区','东北地区','华东地区','华中地区','华南地区','西南地区','西北地区'],
  "test_city": ['测试城市1','测试城市2','测试城市3','test city4','测试城市5','上海市']
}

const ReportTestBody = {
  service_overview: {'关键项': '基本信息', '部署设备数': '0', '解决/报障工单数': '0/0', '新增设备数': '0', '加速类型': 'SAAS加速'},
  device_status: {'站点名称':['区域城市', '序列号', '设备型号', '是否新增', '签约带宽(Mbps)', '峰值带宽(Mbps)'],
                  'report-gwsite1': ['/','3014','BX3000-4GE-L', '是','10'],
                  'report-gwsite2': ['/','3015','BX3000-4GE-L', '是','10'],
                  'report-gwsite3': ['/','3016','BX3000-4GE-L', '是','10'],
                  'report-gwsite4': ['/','3017','BX3000-4GE-L', '是','10']                
                },
  service_quality: {'互联站点':['优化前丢包','优化后丢包','带宽(Mbps)','合同带宽(Mbps)','时延(ms)'],
                  'report-gwsite1-report-gwsite2':['0','0','0.00','10','0'],
                  'report-gwsite3-report-gwsite4':['0','0','0.00','10','0']
                  },
  ticket_detail: {'工单编号': ['起止时间','内容简述','用时统计','状态'],
                  'NSKY-GZ-20210725-0033':['Office.com 无法访问','处理中'],
                  'NSKY-GZ-20210801-0085':['2021/08/01 08:05:46~2021/08/02 09:03:03','未知故障','1 天 0 小时 57 分钟 16.93 秒 ','已关闭']
  }
}

// Used cpe neids in db: 65523 65522 65521 65520 65504 65488 65472 65456 65440 65424
// Used pop neids in db: 1014 998

export {testCompanyBody, testSiteBody, testUnionBody, testQosBody,testSpiRuleBody,testSpiTagBody,testSpiTemplateBody,
  testManagerBody,testOpenflowBody,testNetAlgBody,popBody,testPopBody,testServiceBody,saasSearchPatternBody, putTestPopBody, putTestPop2Body, putDevicePopBody, putDevicePop2Body, testGlobalConfigBody,
  PopTypeForward,PopTypeAnycast,PopTypeSaas, testFirewallBody, testRouterBody, testRouterModifyBody, testCPEGlobalConfigBody, companyBodyTemplate, siteTemp, unionTemplate, menuList,
  alert,alertBody,testScenarioBody,testStrategyBody,auditParam,authParam,UserBody,RoleBody,RegionTestBody,ReportTestBody, setupSites, roleList,webRoleBody}
