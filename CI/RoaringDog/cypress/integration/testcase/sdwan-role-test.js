import {deleteCompanyByName, deleteAllUsers, deleteUser, createUser, createCompanyByData, deleteAllRole, createRole, deleteAllUnions, createUnion, createSiteByData, deleteAllSites, deleteAllGlobalUsersExceptAdmin, deleteRolebyName, deleteAllGlobalRole} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo,rowContains,ClickSidebarMenu, changeSiteCompanyView, checkRightAuth, createWebRole, switchTomenu, checkSidebarMenuList, changeToGlobalView, checkLevel1RoleList, checkLevel2RoleList} from '../utils/web-utils'
import { UserBody, RoleBody, menuList, roleList, webRoleBody} from '../utils/variables-utils'

before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
  //删除公司
  cy.get('@company').then(company => {
    cy.get('@info').then(t_info => {
      deleteAllUnions(t_info.token, company.testCompanyForRole.name)
      deleteAllSites(t_info.token, company.testCompanyForRole.name)
      deleteAllUsers(t_info.token, company.testCompanyForRole.name)
      deleteUser(t_info.token,UserBody.qudaoUser.username)
      deleteAllRole(t_info.token, company.testCompanyForRole.name)
      deleteAllGlobalUsersExceptAdmin(t_info.token)
      deleteAllGlobalRole(t_info.token, 'all')
      deleteRolebyName(t_info.token, "all", RoleBody.globalAdminRole.role)
      deleteCompanyByName(t_info.token,company.testCompanyForRole.name)
      //create roleCompany
      createCompanyByData(t_info.token,company.testCompanyForRole)
      createRole(t_info.token, "all", RoleBody.globalAdminRole)
      //create role for modify case
      createRole(t_info.token, company.testCompanyForRole.name, RoleBody.modifyRole)
      //create role for jump forbidden case
      createRole(t_info.token, company.testCompanyForRole.name, RoleBody.jumpRole)
      //create sonRole to check users user can see the two role
      createRole(t_info.token, company.testCompanyForRole.name, RoleBody.son1Role)
      createRole(t_info.token, company.testCompanyForRole.name, RoleBody.son2Role)
      //create twoRole to check allRW role and onlyR role 
      createRole(t_info.token, company.testCompanyForRole.name, RoleBody.allRW)
      createRole(t_info.token, company.testCompanyForRole.name, RoleBody.onlyR)
      //create user belong to modify role to check if modify is active 
      createUser(t_info.token,UserBody.modifyRoleUser)
      //create user belong to jumper role
      createUser(t_info.token,UserBody.jumpUser)
      //create admins user
      createUser(t_info.token,UserBody.adminRoleUser)
      //create users user
      createUser(t_info.token,UserBody.userRoleUser)
      //create two allRW user and onlyR user
      createUser(t_info.token,UserBody.allRWuser)
      createUser(t_info.token,UserBody.onlyRuser)
      //create two sites to help check site authority
      createSiteByData(t_info.token, company.testCompanyForRole.name, this.site.RoleSite1Body)
      createSiteByData(t_info.token, company.testCompanyForRole.name, this.site.RoleSite2Body)
      //create one union to help check site authority
      createUnion(t_info.token, company.testCompanyForRole.name,this.site.RoleSite1Body.name,this.site.RoleSite2Body.name)
    }) 
  })
})

describe('role page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/roleManage',this.info)
   })

   //SDWANDEV-4552
   it('check default role in company', function(){
    changeSiteCompanyView(this.company.testCompanyForRole.name)
    //check there are two default role in company
    rowContains('[data-cy="userTable"]','admins',0 ,1 ,['admins'])
    rowContains('[data-cy="userTable"]','users',0 ,1 ,['users'])
  })
  
  //SDWANDEV-4565
   it('check default admins role auth right', function(){
    cy.logout()
    cy.typeLogin(UserBody.adminRoleUser.username,UserBody.adminRoleUser.password)
    //check admin user have right authority
    Object.keys(menuList.company_default_admin_view).forEach(function($key) {
      ClickSidebarMenu(menuList.company_default_admin_view[$key][0])
      checkSidebarMenuList(menuList.company_default_admin_view[$key][0],menuList.company_default_admin_view[$key])
    })
    checkRightAuth(webRoleBody.adminRole)
  })

  //	SDWANDEV-4566
  it('check default users role auth right', function(){
    cy.logout()
    cy.typeLogin(UserBody.userRoleUser.username,UserBody.userRoleUser.password)
    //check users user have right authority
    Object.keys(menuList.company_default_user_view).forEach(function($key) {
      ClickSidebarMenu(menuList.company_default_user_view[$key][0])
      checkSidebarMenuList(menuList.company_default_user_view[$key][0],menuList.company_default_user_view[$key])
    })
    checkRightAuth(webRoleBody.userRole)
  })

  //SDWANDEV-4563
  it('check admins user can create role and delete not admins role', function(){
    cy.logout()
    //admin user login
    cy.typeLogin(UserBody.adminRoleUser.username,UserBody.adminRoleUser.password)
    //navigate to 角色管理
    ClickSidebarMenu('账户')
    switchTomenu('角色管理')
    //create role
    cy.get('[data-cy="createRole"]').click()
    createWebRole(RoleBody.newRole,webRoleBody.newRole)
    cy.contains('创建成功')
    //can not delete admin role
    cy.get('[data-cy="userTable"]').contains('admins').parents('tr').within(() => {
      cy.contains('button', '删除').should('not.exist')
    })
    //can delete other role
    cy.get('[data-cy="userTable"]').contains(RoleBody.newRole.role).parents('tr').within(() => {
      cy.contains('button', '删除').click()
    })
    cy.get('[class="el-message-box__btns"]').contains("确定").click()
    cy.contains('操作成功')
  })

  //SDWANDEV-4554
  it('check admins user can check role and modify not admins role, role auth right after role modified', function(){
    //check modifyuser have authority to access 行政区划
    cy.logout()
    cy.typeLogin(UserBody.modifyRoleUser.username,UserBody.modifyRoleUser.password)
    ClickSidebarMenu('账户')
    cy.contains('行政区划').should('exist')
    cy.logout()
    //admin user modify role to remove 行政区划
    cy.typeLogin(UserBody.adminRoleUser.username,UserBody.adminRoleUser.password)
    ClickSidebarMenu('账户')
    switchTomenu('角色管理')
    cy.get('[data-cy="userTable"]').contains(RoleBody.modifyRole.role).parents('tr').within(() => {
      cy.contains('button', '编辑').click()
    })
    RoleBody.modifyRole.role = "modify2roleName"
    createWebRole(RoleBody.modifyRole,webRoleBody.modifyRole)
    //check modifyuser have no authority to access 行政区划
    cy.logout()
    cy.typeLogin(UserBody.modifyRoleUser.username,UserBody.modifyRoleUser.password)
    ClickSidebarMenu('账户')
    cy.contains('行政区划').should('not.exist')
  })

  //SDWANDEV-4555
  it('role can not be delete when user belongs to role', function(){
    //check users role can not be delete by super admin user
    changeSiteCompanyView(this.company.testCompanyForRole.name)
    cy.get('[data-cy="userTable"]').contains("users").parents('tr').within(() => {
      cy.contains('button', '删除').click()
    })
    cy.get('[class="el-message-box__btns"]').contains("确定").click()
    cy.contains('该角色被其他账户使用中，禁止删除')
    //check users role can not be deleted by admins user
    cy.logout()
    cy.typeLogin(UserBody.adminRoleUser.username,UserBody.adminRoleUser.password)
    ClickSidebarMenu('账户')
    switchTomenu('角色管理')
    cy.get('[data-cy="userTable"]').contains("users").parents('tr').within(() => {
      cy.contains('button', '删除').click()
    })
    cy.get('[class="el-message-box__btns"]').contains("确定").click()
    cy.contains('该角色被其他账户使用中，禁止删除')
  })

  //	SDWANDEV-4556
  it('check admins user can not give role and user authority when create role', function(){
    cy.logout()
    //admin user login
    cy.typeLogin(UserBody.adminRoleUser.username,UserBody.adminRoleUser.password)
    //navigate to 角色管理
    ClickSidebarMenu('账户')
    switchTomenu('角色管理')
    //create role and check 个人账户 and 角色管理 读写 is not clickable
    cy.get('[data-cy="createRole"]').click()
    cy.get('[role="dialog"]').within(()=>{
      cy.contains('个人账户').parent('div').parent('[role="treeitem"]').within(()=>{
        cy.contains('读写').parents('[class="el-tree-node__content"]').within(()=>{
          cy.get('label').should('have.class','el-checkbox is-disabled')
        })
      })
      cy.contains('角色管理').parent('div').parent('[role="treeitem"]').within(()=>{
        cy.contains('读写').parents('[class="el-tree-node__content"]').within(()=>{
          cy.get('label').should('have.class','el-checkbox is-disabled')
        })
      })
    })
  })

   //	SDWANDEV-4557
   it.skip('user can see role which authority is less or eq selfs authrity, can not see other role', function(){
    cy.logout()
    cy.typeLogin(UserBody.userRoleUser.username,UserBody.userRoleUser.password)
    //navigate to 角色管理
    ClickSidebarMenu('账户')
    switchTomenu('角色管理')
    //check users user can see two sonrole but not see modify role
    rowContains('[data-cy="userTable"]',RoleBody.son2Role.role,0 ,1 ,[RoleBody.son2Role.role])
    rowContains('[data-cy="userTable"]',RoleBody.son2Role.role,0 ,1 ,[RoleBody.son2Role.role])
    cy.contains(RoleBody.modifyRole.role).should('not.exist')
  })

  //	SDWANDEV-4553
  it('user have authority page if forbidden to jump page which not have authority ', function(){
    cy.logout()
    cy.typeLogin(UserBody.jumpUser.username,UserBody.jumpUser.password)
    //navigate to 概览
    cy.contains('离线').click()
    cy.url().should('not.contain',"alarm")
    //navigate to 配置
    ClickSidebarMenu('配置')
    switchTomenu('设备管理')
    cy.contains(this.site.RoleSite1Body.sn[0]).click()
    cy.url().should('not.contain',"site")
  })

  //	SDWANDEV-4561
  it('all page auth right', function(){
    cy.logout()
    cy.typeLogin(UserBody.allRWuser.username,UserBody.allRWuser.password)
    //check all rw auth right 
    checkRightAuth(UserBody.allRWuser.scopes)
    cy.logout()
    cy.typeLogin(UserBody.onlyRuser.username,UserBody.onlyRuser.password)
    //check only r auth right
    checkRightAuth(UserBody.onlyRuser.scopes)
  })

   
  it('创建角色页面全局模式按钮开关测试', function (){
    changeToGlobalView("roleManage",this.info)
    cy.get('[data-cy="createRole"]').click()
    cy.contains('角色名称')
    checkLevel1RoleList(Object.keys(roleList['globalMode']))
    for (const title of Object.keys(roleList['globalMode'])){
      checkLevel2RoleList('company', title, roleList['companyMode'][title])
    }
    cy.checkCheckBoxWithDatacy('[data-cy="globalMode"]')
    checkLevel1RoleList(Object.keys(roleList['globalMode']))
    for (const title of Object.keys(roleList['globalMode'])){
      checkLevel2RoleList('global', title, roleList['companyMode'][title], roleList['globalMode'][title])
    }
    cy.contains('取消').click()

  })

  it('超级管理员可以创建全局模式售前交付运维测试角色', function (){
    var roleList = [RoleBody.globalOPerationRole, RoleBody.globaldeliveryRole,RoleBody.globalPreSaleRole]
    var allRole = [1,0,0]
    var webRoleList = [[], webRoleBody.globaldeliveryRole,webRoleBody.globalPreSaleRole]
    for (var i=0;i<roleList.length;i++){
      cy.get('[data-cy="createRole"]').click()
      cy.checkCheckBoxWithDatacy('[data-cy="globalMode"]')
      createWebRole(roleList[i], webRoleList[i],allRole[i])
      cy.contains('创建成功')
    }
  })

  it('非超级管理员不能创建全局模式角色', function (){
    cy.logout()
    cy.typeLogin(UserBody.adminRoleUser.username,UserBody.adminRoleUser.password)
    //navigate to 角色管理
    ClickSidebarMenu('账户')
    switchTomenu('角色管理')
    //changeToGlobalView("roleManage",this.info)
    cy.get('[data-cy="createRole"]').click()
    cy.contains('角色名称')
    cy.get('[data-cy="globalMode"]').should('not.exist')
  })

})