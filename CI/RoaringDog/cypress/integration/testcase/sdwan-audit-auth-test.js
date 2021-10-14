import {deleteCompanyByName, deleteAllSites, createSiteByData, createCompanyByData} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView, createWebSite, enableSiteAuthAudit, configAudit,enableAuth,enableAudit,changeAuditPanelView,configAuth,checkTableLineNumber,rowContains} from '../utils/web-utils'
import {checkAuditCorpInfo, checkAuthLdapTimeoutNavUrlInfo, checkAuthRaduisInfo, checkAuditCorpApInfo} from '../utils/authAuditCheck-utils'
import {exec_cmd_on_local,checkAuthAuditConsul} from '../utils/consulCheck-utils'
import {auditParam, authParam, testSiteBody} from '../utils/variables-utils'


function enableAuditFailure(url, port){
  configAudit(url, port)
  cy.contains('连接服务器失败',{ timeout: 10000 })
}

function disableAudit(){
  changeAuditPanelView('全局配置')
  cy.get('[data-cy="auditGlobalConfig"]').within(() => {
      cy.unCheckCheckBoxWithLable('启用审计')
      cy.typeInputWithLable('云审计服务', '')
      cy.clearValueBydatacy('[data-cy="auditGlobalConfig.serverPort"]')
      cy.contains('保存').click()
  })
  cy.contains('保存成功') 
}

function checkAuditDefault(){
  changeAuditPanelView('全局配置')
  cy.get('[data-cy="auditGlobalConfig"]').within(() => {
      cy.CheckBoxWithLableDefault('启用审计', 'el-switch')
      cy.CheckDefaultInputValueBydatacy('[data-cy="auditGlobalConfig.serverPort"]', '3080')
  })
}

function checkAuthDefault(){
  changeAuditPanelView('认证参数')
  cy.get('[data-cy="second-pane"]').within(() => {
      cy.CheckBoxWithLableDefault('启用认证', 'el-switch')
      cy.CheckDefaultInputValueBydatacy('[data-cy="authConfig.portalPort"]', '8006')
  })
}

function enableAuthFail(){
  changeAuditPanelView('认证参数')
  cy.get('[data-cy="second-pane"]').within(() => {
      cy.checkCheckBoxWithLable('启用认证')
      cy.CheckBoxWithLableDefault('启用认证', 'el-switch')
      cy.CheckDefaultInputValueBydatacy('[data-cy="authConfig.portalPort"]', '8006')
  })
}

function enableAuthParamFail(innerUrl, outUrl, redirectUrl, outPort, innerPort, bondTimeout, noTrafficTimeout, authType, authTypeParam){
  configAuth(innerUrl, outUrl, redirectUrl, outPort, innerPort, bondTimeout, noTrafficTimeout, authType, authTypeParam)
  cy.contains('Request failed') 
}

function disableAuth(){
    changeAuditPanelView('认证参数')
    cy.get('[data-cy="second-pane"]').within(() => {
        cy.typeInputWithLable('内网用认证URL', '')
        cy.typeInputWithLable('外网用认证URL', '')
        cy.clearValueBydatacy('[data-cy="authConfig.intranetPort"]')
        cy.clearValueBydatacy('[data-cy="authConfig.portalPort"]')
        cy.typeInputWithLable('重定向URL', '')
        cy.unCheckCheckBoxWithLable('启用认证')
        cy.contains('服务器').should('not.exist')
    })
    cy.get('[data-cy="second-pane"]').within(() => {
        cy.contains('保存').click()
    })
    cy.contains('保存成功') 
}

function createWhiteBlackList(listType, filterType, content){
  changeAuditPanelView('认证黑白名单')
  cy.get('[data-cy="whiteBlackListPane"]').within(() => {
      cy.contains('新增').click()
  })
  cy.contains('名单类型')
  cy.SelectInputValue('[data-cy="blockForm.addType"]', listType)
  cy.SelectInputValue('[data-cy="blockForm.addNameType"]', filterType)
  cy.typeTextareaWithDataCy('[data-cy="blockForm.content"]', content)
  cy.get('[data-cy="blockForm.dialogVisible.confirm"]').click()
  cy.contains('保存成功',{timeout:5000}) 
}

function search_white_black_list(listType, nameType, content, lineNum){
  cy.SelectInputValue('[data-cy="whiteBlackList.type"]', listType)
  cy.SelectInputValue('[data-cy="whiteBlackList.nametype"]', nameType)
  if (nameType == '全部'){ 
    cy.get('[data-cy="whiteBlackList.queryWhiteblank"]').click()
    checkTableLineNumber(lineNum)   
  }else{
    cy.get('[data-cy="whiteBlackList.keywords"]').clear().type(content)
    cy.get('[data-cy="whiteBlackList.queryWhiteblank"]').click()
    checkTableLineNumber(lineNum)
    if (lineNum == 1){ 
    rowContains('[data-cy="whiteBlackList.WBList"]',content,1,4,[listType, nameType, content])}
  }
}

function clear_white_black_list(){
  cy.get('.el-pagination__total').then(($body) => {
    if ($body.text().includes('共 0 条')){

    }else {
      cy.get('[data-cy="whiteBlackList.WBList"]').contains('名单类型').parents('tr').within(() => {
          cy.get('input[type="checkbox"]').click({force: true})
      })
      cy.get('[data-cy="whiteBlackList.deleteWBList"]').click({force: true})
      cy.contains('成功',{timeout:6000})}
    })
  }

function ensure_audit_auth_enable(){
  changeAuditPanelView('全局配置')
  cy.get('[data-cy="auditGlobalConfig.switchAudit"]').within(() => {
    cy.get('div[role="switch"]').as('value1')
  })
  cy.get('@value1').then(($btn) =>{
  if ($btn.hasClass('is-checked')){}
    else {enableAudit(auditParam.auditUrl, auditParam.auditPort)}
  })
  changeAuditPanelView('认证参数')
  cy.get('[data-cy="authConfig.switchAuth"]').within(() => {
    cy.get('div[role="switch"]').as('value2')
  })
  cy.get('@value2').then(($btn) =>{
    if ($btn.hasClass('is-checked')){}
    else {
          enableAuth(authParam.authInnerUrl, authParam.authOutUrl, authParam.redirectUrl, authParam.authOutPort, authParam.authInnerPort, authParam.bindTimeout, authParam.noTrafficTimeout, 'Radius认证', authParam.radiusParam)
          cy.wait(2000)}
  })
  }

before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
})

beforeEach(function () {
  visitAndSetPageUserInfo('/auditConfig',this.info)
  changeSiteCompanyView(this.company.testCompanyAudit.name)
 })

describe('audit page test', function() {
  before(function(){
    deleteAllSites(this.info.token,this.company.testCompanyAudit.name)
    deleteCompanyByName(this.info.token,this.company.testCompanyAudit.name)
    deleteCompanyByName(this.info.token,this.company.testCompanyAudit2.name)
    createCompanyByData(this.info.token,this.company.testCompanyAudit)
    createCompanyByData(this.info.token,this.company.testCompanyAudit2)
    createSiteByData(this.info.token, this.company.testCompanyAudit.name,this.site.AuditC1Site1Body)
    createSiteByData(this.info.token, this.company.testCompanyAudit.name,this.site.AuditC1Site2Body)
    cy.reload()
    exec_cmd_on_local("bash /e2e/RoaringDog/test/prepAuthtest.sh")
  })
   
    //SDWANDEV-4531
    it('enable company audit', function(){
      enableAudit(auditParam.auditUrl, auditParam.auditPort)
      checkAuditCorpInfo(this.info.token, this.company.testCompanyAudit.name)
      disableAudit()
      checkAuditCorpInfo(this.info.token, this.company.testCompanyAudit.name)
    })

    //SDWANDEV-4533
    it('check default company audit and auth', function(){
      changeSiteCompanyView(this.company.testCompanyAudit2.name)
      checkAuditDefault()
      checkAuthDefault()
    })

    //SDWANDEV-4534
    it('enable company audit with site', function(){
      enableAudit(auditParam.auditUrl, auditParam.auditPort)
      visitAndSetPageUserInfo('/site',this.info)
      enableSiteAuthAudit(this.site.AuditC1Site1Body.name, this.site.AuditC1Site1Body.sn[0],false, true, auditParam.siteMac)
      checkAuditCorpApInfo(this.info.token, this.company.testCompanyAudit.name,this.site.AuditC1Site1Body.name, auditParam.siteMac, 'True')
      checkAuthAuditConsul(this.site.AuditC1Site1Body['sn'], 'default', 'configEnable')
    })

    //SDWANDEV-4570
    it('change site audit mac', function(){
      enableAudit(auditParam.auditUrl, auditParam.auditPort)
      visitAndSetPageUserInfo('/site',this.info)
      enableSiteAuthAudit(this.site.AuditC1Site1Body.name, this.site.AuditC1Site1Body.sn[0],false, true, auditParam.siteMac)
      enableSiteAuthAudit(this.site.AuditC1Site1Body.name, this.site.AuditC1Site1Body.sn[0],false, true, auditParam.siteMac2)
      cy.wait(2000)
      checkAuditCorpApInfo(this.info.token, this.company.testCompanyAudit.name,this.site.AuditC1Site1Body.name, auditParam.siteMac2, 'True')
    })

    //SDWANDEV-4568
    it('add and delete site when audit enable', function(){
      enableAudit(auditParam.auditUrl, auditParam.auditPort)
      visitAndSetPageUserInfo('/site',this.info)
      createWebSite(testSiteBody.testConfig_audit_GW_ARMS)
      cy.contains("创建成功",{timeout:10000})
      cy.wait(2000)
      checkAuditCorpApInfo(this.info.token, this.company.testCompanyAudit.name,testSiteBody.testConfig_audit_GW_ARMS.name, testSiteBody.testConfig_audit_GW_ARMS.auditAuth.auditMac, 'True')
      cy.get('[data-cy="siteTable"]').contains(testSiteBody.testConfig_audit_GW_ARMS.name).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
      cy.contains('操作成功',{timeout:10000})
      cy.wait(2000)
      checkAuditCorpApInfo(this.info.token, this.company.testCompanyAudit.name,testSiteBody.testConfig_audit_GW_ARMS.name, testSiteBody.testConfig_audit_GW_ARMS.auditAuth.auditMac, 'False')
    })

    //SDWANDEV-4569
    it('enable company auth only not allow', function(){
       disableAudit()
       enableAuthFail()
    })

    //SDWANDEV-4571
    it('enable company audit and auth without site fail', function(){
      enableAuditFailure(auditParam.auditUrlFail, auditParam.auditPort)
      enableAudit(auditParam.auditUrl, auditParam.auditPort)
      enableAuthParamFail(authParam.authInnerUrl, authParam.authOutUrl, authParam.redirectUrl, '1234', authParam.authInnerPort, authParam.bindTimeout, authParam.noTrafficTimeout,  'LDAP认证', authParam.ldapParam)
    })
    
    //SDWANDEV-4532
    it('enable company audit and auth without site', function(){
      enableAudit(auditParam.auditUrl, auditParam.auditPort)
      enableAuth(authParam.authInnerUrl, authParam.authOutUrl, authParam.redirectUrl, authParam.authOutPort, authParam.authInnerPort, authParam.bindTimeout, authParam.noTrafficTimeout,  'LDAP认证', authParam.ldapParam)
      cy.wait(2000)
      checkAuthLdapTimeoutNavUrlInfo()
      checkAuthAuditConsul(this.site.AuditC1Site1Body['sn'], 'configDisable', 'configDisable')
      disableAuth()
    })
   
    //SDWANDEV-4567
    it('enable company audit and auth with site', function(){
      enableAudit(auditParam.auditUrl, auditParam.auditPort)
      enableAuth(authParam.authInnerUrl, authParam.authOutUrl, authParam.redirectUrl, authParam.authOutPort, authParam.authInnerPort, authParam.bindTimeout, authParam.noTrafficTimeout, 'Radius认证', authParam.radiusParam)
      cy.wait(2000)
      checkAuthRaduisInfo()
      visitAndSetPageUserInfo('/site',this.info)
      enableSiteAuthAudit(this.site.AuditC1Site1Body.name, this.site.AuditC1Site1Body.sn[0],true, true, auditParam.siteMac)
      checkAuthAuditConsul(this.site.AuditC1Site1Body.sn[0], 'configEnable', 'configEnable')
      enableSiteAuthAudit(this.site.AuditC1Site1Body.name, this.site.AuditC1Site1Body.sn[0],false, false, auditParam.siteMac)
      checkAuthAuditConsul(this.site.AuditC1Site1Body.sn[0], 'configDisable', 'configDisable')
    })

    //SDWANDEV-4608
    it('create and delete white list', function(){
      ensure_audit_auth_enable()
      createWhiteBlackList('白名单', '目的IP', ['192.254.12.3','192.254.12.4'])
      createWhiteBlackList('白名单', '源MAC', ['0c:54:15:8e:f6:b9','0c:54:15:8e:f6:b8','0c:54:15:8e:f6:dc'])
      search_white_black_list('白名单', '目的IP', '192.254.12', 2)
      clear_white_black_list()
      search_white_black_list('白名单', '目的IP', '192.254.12', 0)
      search_white_black_list('白名单', '源MAC', '0c:54:15:8e:f6', 3)
      clear_white_black_list()
      search_white_black_list('白名单', '源MAC', '0c:54:15:8e:f6', 0)
    })

    //SDWANDEV-4609
    it('create and delete black list', function(){
      ensure_audit_auth_enable()
      createWhiteBlackList('黑名单', '目的IP', ['192.253.12.3','192.253.12.4'])
      createWhiteBlackList('黑名单', '源MAC', ['0c:55:15:8e:f6:b9'])
      search_white_black_list('黑名单', '目的IP', '192.253.12', 2)
      clear_white_black_list()
      search_white_black_list('黑名单', '目的IP', '192.253.12', 0)
      search_white_black_list('黑名单', '源MAC', '0c:55:15:8e:f6:b9', 1)
      clear_white_black_list()
      search_white_black_list('黑名单', '源MAC', '0c:55:15:8e:f6:b9', 0)
    })

    //SDWANDEV-4610
    it('search black and white list', function(){
      ensure_audit_auth_enable()
      changeAuditPanelView('认证黑白名单')
      clear_white_black_list()
      createWhiteBlackList('黑名单', '目的IP', ['192.253.12.3','192.253.12.4'])
      createWhiteBlackList('白名单', '源MAC', ['0c:54:15:8e:f6:b9','0c:54:15:8e:f6:b8','0c:54:15:8e:f6:dc'])
      search_white_black_list('全部', '全部', '', 5)
      search_white_black_list('黑名单', '全部', '', 2)
      search_white_black_list('白名单', '源MAC', '0c:54:15:8e:f6:b9', 1)
      search_white_black_list('白名单', '全部', '', 3)
    })

    //SDWANDEV-4611
    it('switch company and list white black list', function(){
      ensure_audit_auth_enable()
      changeAuditPanelView('认证黑白名单')
      clear_white_black_list()
      createWhiteBlackList('黑名单', '目的IP', ['192.253.12.3','192.253.12.4'])
      search_white_black_list('全部', '全部', '', 2)
      changeSiteCompanyView(this.company.testCompanyAudit2.name)
      search_white_black_list('全部', '全部', '', 0)
    })
})

