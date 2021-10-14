import {deleteCompanyByName, deleteAllUsers, deleteUser, createUser, createCompanyByData, deleteAllRole, createRole, deleteAllUnions, deleteAllSites, createSiteByData, createUnion, deleteAllGlobalUsersExceptAdmin,deleteAllGlobalRole,deletePopByPopId,putPop,createSpiTags, createSpiTemplate,deleteAllSpiTags,deleteAllSpiTemp, deleteAllSpiScenario, createSpiScenario,deleteAllSpiStrategy} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo,rowContains,changeToGlobalView,ClickSidebarMenu,checkSidebarMenuList, changeSiteCompanyView, switchTomenu, checkRightAuth, setUser, setDistributorUser,setGlobalUser,clickGlobalView,user,password,createWebRole,setCompany} from '../utils/web-utils'
import {menuList, UserBody, RoleBody,webRoleBody,testServiceBody,PopTypeSaas,popBody,testSpiTagBody,testSpiTemplateBody,testScenarioBody,testCompanyBody} from '../utils/variables-utils'


function checkAccountType(typeName, datacy,shouldCheck){
  cy.get(datacy).click()
  cy.wait(400)
  cy.get('.el-scrollbar').filter(':visible').within(() =>{
      cy.get('li[class^=el-select-dropdown__item]').contains(typeName).should(shouldCheck)
  })
}

function deleteWebUser(userName){
  cy.get('[data-cy="userTable"]').contains(userName).parents('tr').within(() => {
    cy.contains('button', '删除').click()
  })
  cy.get('[class="el-message-box__btns"]').contains("确定").click()
  cy.contains('操作成功')
}

function haveNoCompanyRight(companyName,switchWaitTime=1){
  cy.get('span > .el-icon-arrow-up').eq(0).click({force: true})
  cy.wait(switchWaitTime)
  cy.get('ul > li').contains(companyName).should('not.exist')
}

function searchUser(searchBy, value){
  cy.get('[class="button-container"]').within(()=>{
    cy.get('[class="el-select"]').click()
  })
  cy.get('[class="el-scrollbar"]').contains(searchBy).click()
  cy.get('[class="button-container"]').within(()=>{
    cy.get('input[class="el-input__inner"]').eq(1).clear().type(value)
    cy.get('[class="el-icon-search"]').click()
  })
}

before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
  //删除公司
  cy.get('@company').then(company => {
    cy.get('@info').then(t_info => {
      deleteAllSpiStrategy(t_info.token)
      deleteAllSpiScenario(t_info.token)
      deleteAllSpiTemp(t_info.token)
      deleteAllSpiTags(t_info.token)
      deleteAllUnions(t_info.token, company.testCompanyForUser.name)
      deleteAllSites(t_info.token, company.testCompanyForUser.name)
      deleteAllUsers(t_info.token, company.testCompanyForUser.name)
      deleteUser(t_info.token,UserBody.testUserDistributor.username)
      deleteAllRole(t_info.token, company.testCompanyForUser.name)
      deleteAllGlobalUsersExceptAdmin(t_info.token)
      deleteCompanyByName(t_info.token,company.testCompanyForUser.name)
      deleteCompanyByName(t_info.token,company.testCompany2ForUser.name)
      deletePopByPopId(t_info.token,testServiceBody.putSaasBody.popId,PopTypeSaas)
      deletePopByPopId(t_info.token,popBody.testpop2.popId)
      deletePopByPopId(t_info.token,popBody.testpop3.popId)
      deletePopByPopId(t_info.token,popBody.testpop.popId)
      deleteAllGlobalRole(t_info.token, 'all')
      createRole(t_info.token, "all", RoleBody.globalAdminRole)
      createRole(t_info.token, "all", RoleBody.globalOPerationRole)
      createRole(t_info.token, "all", RoleBody.globaldeliveryRole)
      createRole(t_info.token, "all", RoleBody.globalPreSaleRole)
      //create pop service
      putPop(t_info.token,popBody.testpop2)
      putPop(t_info.token,popBody.testpop3)
      putPop(t_info.token,popBody.testpop)
      putPop(t_info.token,testServiceBody.putSaasBody)
      //create userCompany
      createCompanyByData(t_info.token,company.testCompanyForUser)
      createCompanyByData(t_info.token,company.testCompany2ForUser)
      //create global user
      createUser(t_info.token,UserBody.globalOperateUserForTest)
      createUser(t_info.token,UserBody.globalPreSaleUserForTest)
      //create user for modify case
      createUser(t_info.token,UserBody.modifyUser)
      //create sonRole to check user which have two role have right authority 
      createRole(t_info.token, company.testCompanyForUser.name, RoleBody.userSon1Role)
      createRole(t_info.token, company.testCompanyForUser.name, RoleBody.userSon2Role)
      //create two role user
      createUser(t_info.token,UserBody.multiRoleUser)
      //create admins user
      createUser(t_info.token,UserBody.userAdminUser)
      //create users user
      createUser(t_info.token,UserBody.userOdUser)
      createUser(t_info.token,UserBody.userOd2User)
      //create two sites to help check site authority
      createSiteByData(t_info.token, company.testCompanyForUser.name, this.site.UserSite1Body)
      createSiteByData(t_info.token, company.testCompanyForUser.name, this.site.UserSite2Body)
      //create one union to help check site authority
      createUnion(t_info.token, company.testCompanyForUser.name,this.site.UserSite1Body.name,this.site.UserSite2Body.name)
      createSpiTags(t_info.token, company.testCompanyForUser.name,testSpiTagBody.SpiTagSaas)
      createSpiTags(t_info.token, 'all',testSpiTagBody.SpiGTagSaas)
      createSpiTemplate(t_info.token, company.testCompanyForUser.name,testSpiTemplateBody.SpiTemplateSaas)
      createSpiTemplate(t_info.token, 'all',testSpiTemplateBody.SpiTemplateGlobalSaas)
      createSpiScenario(t_info.token, company.testCompanyForUser.name,testSpiTemplateBody.SpiTemplateGlobalSaas,testScenarioBody.SpiScenarioG)
    }) 
  })
})

describe('user page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/accountManage',this.info)
   })

    //SDWANDEV-4564
    it('admin user create and delete user test', function(){
      //admin user login
      cy.logout()
      cy.typeLogin(UserBody.userAdminUser.username,UserBody.userAdminUser.password)
      ClickSidebarMenu('账户')
      switchTomenu('个人账户')
      // admin user create user
      setUser(UserBody.webctUser)
      cy.contains('创建成功')
      for (var i=0;i<  UserBody.webctUser.roles.length;i++){
        rowContains('[data-cy="userTable"]',UserBody.webctUser.username,0, 4 ,[UserBody.webctUser.username, UserBody.webctUser.roles[i],UserBody.webctUser.company, "all"])
      }
      //create user login
      cy.logout()
      cy.typeLogin(UserBody.webctUser.username,UserBody.webctUser.password)
      //admin user delete created user
      cy.logout()
      cy.typeLogin(UserBody.userAdminUser.username,UserBody.userAdminUser.password)
      changeSiteCompanyView(this.company.testCompanyForUser.name)
      ClickSidebarMenu('账户')
      switchTomenu('个人账户')
      deleteWebUser(UserBody.webctUser.username)
    })

    //SDWANDEV-4559
    it('admin user can see and modify user whose authority less than itself', function(){
      //admin user login
      cy.logout()
      cy.typeLogin(UserBody.userAdminUser.username,UserBody.userAdminUser.password)
      ClickSidebarMenu('账户')
      switchTomenu('个人账户')
      //admin user can not modify itself
      cy.get('[data-cy="userTable"]').contains(UserBody.userAdminUser.username).parents('tr').within(() => {
        cy.contains('button', '编辑').should('not.exist')
      })
      //admin user can see 4 user
      cy.contains('共 4 条')
      //modify user
      cy.get('[data-cy="userTable"]').contains(UserBody.modifyUser.username).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
      })
      cy.get('[data-cy=userForm]').within(() => {
        cy.checkCheckBoxWithLable("修改密码")
        cy.typeInputWithLable('密码','1wsx@edc1')
        cy.typeElinputWithLable('角色',"userSon1Role")
        cy.typeElinputWithLable('角色',"users")
        cy.typeInputWithLable('联系方式','12345678901')       
      })
      cy.contains('确认').click()
      cy.contains('更新成功')
      //check modify success
      rowContains('[data-cy="userTable"]',UserBody.modifyUser.username, 0, 4 ,[UserBody.modifyUser.username,"userSon1Role", UserBody.modifyUser.company, "all"])
      cy.logout()
      cy.typeLogin(UserBody.modifyUser.username,'1wsx@edc1')
    }) 

    it('admin user authority check', function(){
      cy.contains('当前模式为全局模式')
      Object.keys(menuList.admin_g_view).forEach(function($key) {
          ClickSidebarMenu(menuList.admin_g_view[$key][0])
          checkSidebarMenuList(menuList.admin_g_view[$key][0],menuList.admin_g_view[$key])
    })
      changeSiteCompanyView(this.company.testCompanyForUser.name)
      Object.keys(menuList.admin_c_view).forEach(function($key) {
        ClickSidebarMenu(menuList.admin_c_view[$key][0])
        checkSidebarMenuList(menuList.admin_c_view[$key][0],menuList.admin_c_view[$key])
    })
  })

    //SDWANDEV-4560
    it('users user can not edit user and can see user whose authority is less than itself', function(){
      cy.logout()
      cy.typeLogin(UserBody.userOdUser.username,UserBody.userOdUser.password)
      ClickSidebarMenu('账户')
      switchTomenu('个人账户')
      //check user can see other user whose authority is less or eq itself
      rowContains('[data-cy="userTable"]',UserBody.userOd2User.username, 0, 4 ,[UserBody.userOd2User.username,"users", UserBody.userOd2User.company, "all"])
      cy.contains('button', '编辑').should('not.exist')
  })

  //	SDWANDEV-4558
  it('check user authority who has multi role', function(){
    cy.logout()
    cy.typeLogin(UserBody.multiRoleUser.username,UserBody.multiRoleUser.password)
    //check users user have right authority
    Object.keys(menuList.multiRole_user_view).forEach(function($key) {
      ClickSidebarMenu(menuList.multiRole_user_view[$key][0])
      checkSidebarMenuList(menuList.multiRole_user_view[$key][0],menuList.multiRole_user_view[$key])
    })
    checkRightAuth(webRoleBody.multiRole)
  })

    it('Create Distributor User', function () {
        // SDWANDEV-4327
        setDistributorUser(UserBody.testUserDistributor)
        cy.contains('创建成功')
        rowContains('[data-cy="userTable"]',UserBody.testUserDistributor.username,0, 1 ,[UserBody.testUserDistributor.username],"admins")
        cy.logout()
        cy.typeLogin(UserBody.testUserDistributor.username,UserBody.testUserDistributor.password)
    })

  it('创建账户页面内全局模式开关测试', function (){
    cy.contains('新建').click()
    checkAccountType('全局', '[data-cy="accountType"]','be.visible')
  })

  it('超级管理员创建管全部或者部分公司的全局模式售前交付运维测试账号', function (){
    var userList = [UserBody.globalOperateUser, UserBody.globalPreSaleUser, UserBody.globalDliveryUser]
    for (var i=0;i<userList.length;i++){
        setGlobalUser(userList[i],['所有公司'],'全局')
        cy.contains('创建成功')
        rowContains('[data-cy="userTable"]',userList[i].username,1, 4 ,[userList[i].username,"全局",userList[i].roles[0]])
        cy.logout()
        cy.typeLogin(userList[i].username,userList[i].password)
        changeSiteCompanyView(this.company.testCompanyForUser.name)
        changeSiteCompanyView(this.company.testCompany2ForUser.name)
        cy.logout()
        cy.typeLogin(user, password)
        clickGlobalView()
        ClickSidebarMenu('账户')
        switchTomenu('个人账户')
        deleteWebUser(userList[i].username)
    }
  })
  before(function () {
    deleteCompanyByName(this.info.token,testCompanyBody.testCompanyForUser.name)
  })
  it('全局运维账号可以创建查看删除公司和站点配置全局参数等', function (){
    setGlobalUser(UserBody.globalOperateUser,[this.company.testCompanyForUser.name],'全局')
    cy.contains('创建成功')
    cy.logout()
    cy.typeLogin(UserBody.globalOperateUser.username,UserBody.globalOperateUser.password)
    changeSiteCompanyView(this.company.testCompanyForUser.name)
    checkRightAuth(webRoleBody.globalOPerationRole)
    haveNoCompanyRight(this.company.testCompany2ForUser.name)
    clickGlobalView()
    checkRightAuth(webRoleBody.globalOPerationRole,true,this.company.testCompanyForUser.name)
  })

  before(function () {
    deleteCompanyByName(this.info.token,testCompanyBody.testCompanyForUser.name)
  })
  it('全局交付账号可以创建查看删除公司和站点不能配置全局参数等', function (){
    setGlobalUser(UserBody.globalDliveryUser,[this.company.testCompanyForUser.name],'全局')
    cy.contains('创建成功')
    cy.logout()
    cy.typeLogin(UserBody.globalDliveryUser.username,UserBody.globalDliveryUser.password)
    changeSiteCompanyView(this.company.testCompanyForUser.name)
    checkRightAuth(webRoleBody.globaldeliveryRole)
    haveNoCompanyRight(this.company.testCompany2ForUser.name)
    clickGlobalView()
    checkRightAuth(webRoleBody.globaldeliveryRole,true,this.company.testCompanyForUser.name)
  })

  it('全局售前账号可以查看公司和站点查看监控信息和站点告警导出报表', function (){
    setGlobalUser(UserBody.globalPreSaleUser,[this.company.testCompanyForUser.name],'全局')
    cy.contains('创建成功')
    cy.logout()
    cy.typeLogin(UserBody.globalPreSaleUser.username,UserBody.globalPreSaleUser.password)
    changeSiteCompanyView(this.company.testCompanyForUser.name)
    checkRightAuth(webRoleBody.globalPreSaleRole)
    haveNoCompanyRight(this.company.testCompany2ForUser.name)
    clickGlobalView()
    checkRightAuth(webRoleBody.globalPreSaleRole,true,this.company.testCompanyForUser.name)
  })

  before(function () {
    deleteAllRole(this.info.token, testCompanyBody.testCompanyForUser.name)
  })
  it('运维全局模式账户可以创建和删除公司角色', function (){
    cy.logout()
    cy.typeLogin(UserBody.globalOperateUserForTest.username,UserBody.globalOperateUserForTest.password)
    clickGlobalView()
    ClickSidebarMenu('账户')
    switchTomenu('角色管理')
    cy.contains('角色描述')
    cy.get('[data-cy="createRole"]').click()
    createWebRole(RoleBody.webAuthRole,[], 1,this.company.testCompanyForUser.name)
    cy.contains('创建成功')
    cy.setNumInTablePage('50条')
    cy.get('[data-cy="userTable"]').contains(RoleBody.webAuthRole.role).parents('tr').within(() => {
      cy.contains('button', '删除').click()
    })
    cy.get('[class="el-message-box__btns"]').contains("确定").click()
    cy.contains('操作成功',{timeout:10000})
  })

  it('运维全局账户不可以查看所有的全局模式账户', function(){
    cy.logout()
    cy.typeLogin(UserBody.globalOperateUserForTest.username,UserBody.globalOperateUserForTest.password)
    clickGlobalView()
    ClickSidebarMenu('账户')
    switchTomenu('角色管理')
    cy.contains('角色描述')
    cy.setNumInTablePage('50条')
    cy.get('[data-cy="userTable"]').contains(RoleBody.globalPreSaleRole.role).should('not.be.visible')
    cy.get('[data-cy="userTable"]').contains(RoleBody.globaldeliveryRole.role).should('not.be.visible')
    cy.get('[data-cy="userTable"]').contains(RoleBody.globalPreSaleRole.role).should('not.be.visible')
  })

  before(function () {
    deleteCompanyByName(this.info.token,testCompanyBody.testCompanyForUser.name)
  })
  it('运维全局账户创建和删除公司账户，对于该公司的admin账户或者其他具有账户读写权限的公司账户可见', function(){
    cy.logout()
    cy.typeLogin(UserBody.globalOperateUserForTest.username,UserBody.globalOperateUserForTest.password)
    clickGlobalView()
    ClickSidebarMenu('账户')
    switchTomenu('公司管理')
    setCompany(testCompanyBody.testCompanyForUser)
    cy.contains('创建成功')
    cy.logout()
    cy.typeLogin(UserBody.globalPreSaleUserForTest.username,UserBody.globalPreSaleUserForTest.password)
    clickGlobalView()
    ClickSidebarMenu('账户')
    switchTomenu('公司管理')
    cy.contains('电话')
    cy.setNumInTablePage('50条')
    cy.get('[data-cy="companyTable"]').contains(testCompanyBody.testCompanyForUser.name)
  })

  it.skip('根据用户名公司角色搜索账户，支持账户批量删除', function(){
    clickGlobalView()
    ClickSidebarMenu('账户')
    switchTomenu('个人账户')
    searchUser('角色','运维')
    cy.contains('共 1 条')
    searchUser('公司',testCompanyBody.testCompanyForUser)
    cy.contains('共 2 条')
    searchUser('用户名',UserBody.userAdminUser.name)
    cy.contains('共 1 条')
  })

  it('同时有全局售前和全局交付角色的账号可以创建查看删除公司和站点', function(){
    setGlobalUser(UserBody.globalMultiRoleUser,[this.company.testCompanyForUser.name],'全局')
    cy.contains('创建成功')
    cy.logout()
    cy.typeLogin(UserBody.globalMultiRoleUser.username,UserBody.globalMultiRoleUser.password)
    changeSiteCompanyView(this.company.testCompanyForUser.name)
    //checkRightAuth(webRoleBody.globalMultiRoleUser)
    haveNoCompanyRight(this.company.testCompany2ForUser.name)
    clickGlobalView()
    checkRightAuth(webRoleBody.globalMultiRoleUser,true,this.company.testCompanyForUser.name)

  })

  it('选择部分公司的全局账号显示跟所管辖公司相关的信息', function(){
    setGlobalUser(UserBody.globalOperateUser,[this.company.testCompanyForUser.name],'全局')
    cy.contains('创建成功')
    cy.logout()
    cy.typeLogin(UserBody.globalOperateUser.username,UserBody.globalOperateUser.password)
    clickGlobalView()
    ClickSidebarMenu('账户')
    switchTomenu('角色管理')
    cy.contains('默认公司管理员').should('have.length', 1)
  })
})
