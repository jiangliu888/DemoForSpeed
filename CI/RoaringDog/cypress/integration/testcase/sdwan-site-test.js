import {deleteCompanyByName, deleteAllUnions,deleteAllSites, createCompanyByData,checkCPENeidbyName, createSiteByData, initCpeGlobalConf, deleteSiteByName,deleteUser,createUser,getSiteNEidBycomNameAndStName,getLogsNumber} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView, editWebSite,createWebSite, rowContains,createWebUnion,changeToGlobalView,ClickSidebarSubMenu,CheckWebSiteReadonly, replaceSiteBySN} from '../utils/web-utils'
import {testSiteBody, testUnionBody, UserBody} from '../utils/variables-utils'
import {checkSite,checkSystemWithConsul,modify_cpe_type,checkDevice,checkSystemNetworkWithConsul, checkDeviceDeleted} from '../utils/consulCheck-utils'
import {exec_cmd_on_local_ignoreErr, checkAiwanJson, checkInfoJson, checkNeJson, checkStartupJson, checkWirelessJson, checkFirewallJson, checkNetworkJson, checkDhcpJson} from '../utils/thrusterCheck-utils'
const thrusterTool = "/tmp/create_config"


export function checkSearchResult(inputStr, expNum){
  cy.get('[data-cy="siteSearch"]').clear().type(inputStr)
  cy.contains('共 '+expNum+' 条')
}

export function search_site(searchBy, value){
  cy.get('[class="filter-container"]').within(()=>{
    cy.get('[data-cy="loginSelect"]').click()
  })
  cy.get('[class="el-scrollbar"]').contains(searchBy).click()
  cy.get('[class="filter-container"]').within(()=>{
    cy.get('[data-cy="loginSearch"]').clear().type(value)
    cy.get('[class="el-icon-search"]').click()
  })
}

before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
  //删除公司
  cy.get('@company').then(company => {
    cy.get('@site').then(site => {
      modify_cpe_type(site.seriesSiteBody.sn[0], "BX3000-4GE-L")
      cy.get('@info').then(t_info => {
        deleteAllUnions(t_info.token, company.testCompanyST.name)
        deleteAllSites(t_info.token, company.testCompanyST.name)
        deleteAllSites(t_info.token, company.testCompanySite.name)
        deleteUser(t_info.token, UserBody.testUserSite.username)
        deleteCompanyByName(t_info.token, company.testCompanySite.name)
        deleteCompanyByName(t_info.token, company.testCompanyST.name)
        createCompanyByData(t_info.token, company.testCompanyST)
        createCompanyByData(t_info.token, company.testCompanySite)
        createUser(t_info.token, UserBody.testUserSite)
        initCpeGlobalConf(t_info.token)
        createSiteByData(t_info.token, company.testCompanyST.name, site.gatewaySiteBody)
        createSiteByData(t_info.token, company.testCompanyST.name, site.seriesSiteBody)
        createSiteByData(t_info.token, company.testCompanyST.name, site.parallerMSiteBody)
        createSiteByData(t_info.token, company.testCompanyST.name, site.seriesMSiteBody)
        createSiteByData(t_info.token, company.testCompanyST.name, site.parallerSiteBody)
        createSiteByData(t_info.token, company.testCompanyST.name, site.paCheckNeidBody)
        createSiteByData(t_info.token, company.testCompanyST.name, site.MipsSiteBody)
        createSiteByData(t_info.token, company.testCompanySite.name, site.gatewaySite2Body)
        createSiteByData(t_info.token, company.testCompanyST.name, site.searchSite1Body)
        createSiteByData(t_info.token, company.testCompanyST.name, site.searchSite2Body)
        cy.reload()
      })
    })
  })
 })

describe('site page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/site',this.info)
    changeSiteCompanyView(this.company.testCompanyST.name)
   })

    it('create and delete gateway site test', function(){
      createWebSite(testSiteBody.testGW)
      cy.contains('创建成功')
      checkSite(this.info.token, this.company.testCompanyST.name, testSiteBody.testGW.name, testSiteBody.testGW.sn)
      checkDevice(this.info.token, this.company.testCompanyST.name, testSiteBody.testGW.name, testSiteBody.testGW.sn)
      checkSystemWithConsul(testSiteBody.testGW.sn)
      rowContains('[data-cy=siteTable]',testSiteBody.testGW.name,1,3,[testSiteBody.testGW.name,testSiteBody.testGW.sn])
      let cmd = thrusterTool + " " + Cypress.env('consulUrl') + " " + Cypress.env('consulToken') + " " +  testSiteBody.testGW.sn
      exec_cmd_on_local_ignoreErr(cmd)
      checkAiwanJson(this.info.token, this.company.testCompanyST.name, testSiteBody.testGW.name, testSiteBody.testGW.sn)
      checkInfoJson(this.info.token, this.company.testCompanyST.name, testSiteBody.testGW.name, testSiteBody.testGW.sn)
      checkNeJson(testSiteBody.testGW.sn)
      checkStartupJson(testSiteBody.testGW, testSiteBody.testGW.sn)
      checkFirewallJson(testSiteBody.testGW, testSiteBody.testGW.sn)
      checkNetworkJson(testSiteBody.testGW, testSiteBody.testGW.sn)
      checkDhcpJson(testSiteBody.testGW, testSiteBody.testGW.sn)
      checkWirelessJson(testSiteBody.testGW, testSiteBody.testGW.sn)
      cy.get('[data-cy="siteTable"]').contains(testSiteBody.testGW.name).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
      cy.contains('操作成功')
      //check the add and del log of site
      getLogsNumber(this.info.token,{resourceType:'site',action:'add',company:this.company.testCompanyST.name,username:'admin'})
      cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(10)})
      getLogsNumber(this.info.token,{resourceType:'site',action:'del',company:this.company.testCompanyST.name,username:'admin'})
      cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(1)})
     })

     it('create and delete gateway MIPS site test 1 Wan', function(){
      createWebSite(testSiteBody.testGW_MIPS_1W)
      cy.contains('创建成功')
      checkDevice(this.info.token, this.company.testCompanyST.name, testSiteBody.testGW_MIPS_1W.name, testSiteBody.testGW_MIPS_1W.sn)
      checkSystemNetworkWithConsul(testSiteBody.testGW_MIPS_1W.sn)
      rowContains('[data-cy=siteTable]',testSiteBody.testGW_MIPS_1W.name,1,3,[testSiteBody.testGW_MIPS_1W.name,testSiteBody.testGW_MIPS_1W.sn])
      cy.get('[data-cy="siteTable"]').contains(testSiteBody.testGW_MIPS_1W.name).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
      cy.contains('操作成功')
   })

    it('create and delete gateway MIPS site test 2 Wan', function () {
      createWebSite(testSiteBody.testGW_MIPS_2W)
      cy.contains('创建成功')
      checkDevice(this.info.token, this.company.testCompanyST.name, testSiteBody.testGW_MIPS_2W.name, testSiteBody.testGW_MIPS_2W.sn)
    checkSystemNetworkWithConsul(testSiteBody.testGW_MIPS_2W.sn)
      rowContains('[data-cy=siteTable]', testSiteBody.testGW_MIPS_2W.name, 1, 3, [testSiteBody.testGW_MIPS_2W.name,testSiteBody.testGW_MIPS_2W.sn])
      cy.get('[data-cy="siteTable"]').contains(testSiteBody.testGW_MIPS_2W.name).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
      cy.contains('操作成功')
    })

    it('create and delete gateway ARMS site test', function(){
      createWebSite(testSiteBody.testGW_ARMS)
      cy.contains('创建成功')
      checkDevice(this.info.token, this.company.testCompanyST.name, testSiteBody.testGW_ARMS.name, testSiteBody.testGW_ARMS.sn)
      checkSystemNetworkWithConsul(testSiteBody.testGW_ARMS.sn)
      rowContains('[data-cy=siteTable]',testSiteBody.testGW_ARMS.name,1,3,[testSiteBody.testGW_ARMS.name,testSiteBody.testGW_ARMS.sn])
      cy.get('[data-cy="siteTable"]').contains(testSiteBody.testGW_ARMS.name).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
      cy.contains('操作成功')
     })

     it('create ARMS site failure', function(){
       createWebSite(testSiteBody.testGW_ARMS_Fail)
       cy.contains('ARM设备第一个LAN占用网口数须超过三个')
     })

     it('modify arm site test', function(){
       rowContains('[data-cy=siteTable]',this.site.MipsSiteBody.name,1,3,[this.site.MipsSiteBody.name,this.site.MipsSiteBody.sn[0]])
       cy.get('[data-cy="siteTable"]').contains(this.site.MipsSiteBody.name).parents('tr').within(() => {
          cy.contains('button', '编辑').click()
       })
       cy.get('[data-cy=siteDeleteLan]').click()
       cy.clickButtonWithLable('确 定')
       if (this.site.MipsSiteBody.sameNet){
        cy.get('.el-message-box').within(()=>{
          cy.contains("确定").click()
        })
      }
       cy.contains('更新成功')
       checkDevice(this.info.token, this.company.testCompanyST.name, this.site.MipsSiteBody.name, this.site.MipsSiteBody.sn[0])
       checkSystemNetworkWithConsul(this.site.MipsSiteBody.sn[0])
       //check the update log of site
       getLogsNumber(this.info.token,{resourceType:'site',action:'update',company:this.company.testCompanyST.name,username:'admin'})
       cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(1)})
      })

     it('modify gateway site test', function(){
       rowContains('[data-cy=siteTable]',this.site.gatewaySiteBody.name,1,3,[this.site.gatewaySiteBody.name,this.site.gatewaySiteBody.sn[0]])
       checkCPENeidbyName(this.info.token,this.company.testCompanyST.name, this.site.gatewaySiteBody.name, 3)
       cy.get('[data-cy="siteTable"]').contains(this.site.gatewaySiteBody.name).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
      })
      var body = testSiteBody.testSTGuangzhou
      body.name = "modify-gwsite", body.tunnelNum = "6869",body.nets = ["172.19.42.0/24"],body.location = "modify-gwlocation1",body.sn = "2001"
      body.wans[0].public_ip = "1.2.3.4",body.wans[0].prefer_pop_eac = "6"
      body.lans[1].IDC = true
      body.wifi.ssid = "testwifiModify", body.wifi.key = "23456789"
      editWebSite(body)
      cy.contains('更新成功')
      cy.reload()
      changeSiteCompanyView(this.company.testCompanyST.name)
      rowContains('[data-cy=siteTable]',body.name,1,3,[body.name,body.sn])
      //check the update log of site with detail
      getLogsNumber(this.info.token,{resourceType:'site',action:'update',company:this.company.testCompanyST.name,username:'admin',detail:'修改带宽值为1024Mbps'})
      cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(1)})
     })

    it('create and delete series site test', function(){
      createWebSite(testSiteBody.testSE)
      cy.contains('创建成功')
      checkDevice(this.info.token, this.company.testCompanyST.name, testSiteBody.testSE.name, testSiteBody.testSE.sn)
      rowContains('[data-cy=siteTable]',testSiteBody.testSE.name,1,3,[testSiteBody.testSE.name,testSiteBody.testSE.sn])
      let cmd = thrusterTool + " " + Cypress.env('consulUrl') + " " + Cypress.env('consulToken') + " " +  testSiteBody.testSE.sn
      exec_cmd_on_local_ignoreErr(cmd)
      checkAiwanJson(this.info.token, this.company.testCompanyST.name, testSiteBody.testSE.name, testSiteBody.testSE.sn)
      checkInfoJson(this.info.token, this.company.testCompanyST.name, testSiteBody.testSE.name, testSiteBody.testSE.sn)
      checkNeJson(testSiteBody.testSE.sn)
      checkStartupJson(testSiteBody.testSE, testSiteBody.testSE.sn)
      getSiteNEidBycomNameAndStName(this.info.token, this.company.testCompanyST.name,testSiteBody.testSE.name)
      cy.get('@neId').then(neId => {
        expect(neId).to.not.equal("")
        cy.wrap(neId).as('tmp_neId')
      })
      cy.get('[data-cy="siteTable"]').contains(testSiteBody.testSE.name).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
      cy.contains('操作成功')
      cy.get('@tmp_neId').then(tmp_neId => {
        expect(tmp_neId).to.not.equal("")
        checkDeviceDeleted(tmp_neId)
      })
    })

    it('modify series site test', function(){
      rowContains('[data-cy=siteTable]',this.site.seriesSiteBody.name,1,3,[this.site.seriesSiteBody.name,this.site.seriesSiteBody.sn[0]])
      checkCPENeidbyName(this.info.token,this.company.testCompanyST.name, this.site.seriesSiteBody.name, 0)
      cy.get('[data-cy="siteTable"]').contains(this.site.seriesSiteBody.name).parents('tr').within(() => {
       cy.contains('button', '编辑').click()
     })
     var body = testSiteBody.testSTBeijing
     body.name = "modify-sename1", body.tunnelNum = "7000",body.private = ["10.194.0.0/26","10.194.0.64/27","10.194.0.96/30","10.194.0.100/32"],body.location = "modify-selocation1",body.sn = "2002"
     body.wans[0].mtu = "1400",body.wans[0].prefer_ip = "1.2.3.4", body.wans[0].staticIp = '10.194.16.2', body.wans[0].gatewayMac = '11:22:33:44:55:66'
     editWebSite(body)
     cy.contains('更新成功')
     cy.reload()
     changeSiteCompanyView(this.company.testCompanyST.name)
     rowContains('[data-cy=siteTable]',body.name,1,3,[body.name,body.sn])
     let cmd = thrusterTool + " " + Cypress.env('consulUrl') + " " + Cypress.env('consulToken') + " " +  body.sn
     exec_cmd_on_local_ignoreErr(cmd)
     checkAiwanJson(this.info.token, this.company.testCompanyST.name, body.name, body.sn)
     checkInfoJson(this.info.token, this.company.testCompanyST.name, body.name, body.sn)
     checkNeJson(body.sn)
     checkStartupJson(body, body.sn)
     cy.get('[data-cy="siteTable"]').contains("modify-sename1").parents('tr').within(() => {
         cy.contains('button', '编辑').click()
     })
    cy.get('[data-cy=siteDialog]').within(() => {
        cy.contains(body.wans[0].name).parents('[data-cy=siteWanList]').within(() => {
            if (Cypress.$('[class="el-collapse-item__header"]').length > 0) {
                cy.log('walking into not active branch, need to expand the wan')
                cy.contains(body.wans[0].name).then(($btn) => {
                    if ($btn.hasClass('is-active')) {
                        cy.log("active")
                    } else {
                        cy.log("not-active")
                        cy.contains(body.wans[0].name).click()
                    }
                })
            }
        })
        cy.contains(body.wans[0].name).parents('[data-cy=siteWanList]').within(() => {
            cy.clearLableValue('静态IP', '')
            body.wans[0].staticIp = ''
        })
        cy.clickButtonWithLable('确 定')
        exec_cmd_on_local_ignoreErr(cmd)
        checkStartupJson(body, body.sn)
    })
    })
    
    it('create and delete paralles site test', function(){
      createWebSite(testSiteBody.testPA)
      cy.contains('创建成功')
      checkSite(this.info.token, this.company.testCompanyST.name, testSiteBody.testPA.name, testSiteBody.testPA.sn)
      // checkSite(this.info.token,this.company.testCompanyST.name, testSiteBody.testPA.name)
      rowContains('[data-cy=siteTable]',testSiteBody.testPA.name,1,3,[testSiteBody.testPA.name,testSiteBody.testPA.sn])
      let cmd = thrusterTool + " " + Cypress.env('consulUrl') + " " + Cypress.env('consulToken') + " " +  testSiteBody.testPA.sn
      exec_cmd_on_local_ignoreErr(cmd)
      checkAiwanJson(this.info.token, this.company.testCompanyST.name, testSiteBody.testPA.name, testSiteBody.testPA.sn)
      checkInfoJson(this.info.token, this.company.testCompanyST.name, testSiteBody.testPA.name, testSiteBody.testPA.sn)
      checkNeJson(testSiteBody.testPA.sn)
      checkStartupJson(testSiteBody.testPA, testSiteBody.testPA.sn)
      cy.get('[data-cy="siteTable"]').contains(testSiteBody.testPA.name).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
      cy.contains('操作成功')
    })

    it('modify parallers site test', function(){
      rowContains('[data-cy=siteTable]',this.site.parallerSiteBody.name,1,3,[this.site.parallerSiteBody.name,this.site.parallerSiteBody.sn[0]])
      cy.get('[data-cy="siteTable"]').contains(this.site.parallerSiteBody.name).parents('tr').within(() => {
       cy.contains('button', '编辑').click()
     })
     var body = testSiteBody.testSTNanjing
     body.name = "modify-paname1", body.tunnelNum = "7001",body.nets = ["172.19.15.0/24"],body.location = "modify-spalocation1",body.sn = "2003",body.HA = false
     body.wans[0].ip = "172.20.14.27"
     body.lans[0].ip_addr = "172.21.14.27"
     editWebSite(body)
     cy.contains('更新成功')
     cy.reload()
     changeSiteCompanyView(this.company.testCompanyST.name)
     rowContains('[data-cy=siteTable]',body.name,1,3,[body.name,body.sn])
    })

    it('parallers change gw check neid', function(){
      rowContains('[data-cy=siteTable]',this.site.paCheckNeidBody.name,1,3,[this.site.paCheckNeidBody.name,this.site.paCheckNeidBody.sn[0]])
      checkCPENeidbyName(this.info.token,this.company.testCompanyST.name, this.site.paCheckNeidBody.name, 0)
      cy.get('[data-cy="siteTable"]').contains(this.site.paCheckNeidBody.name).parents('tr').within(() => {
       cy.contains('button', '删除').click()
     })
     cy.get('[class="el-message-box__btns"]').contains("确定").click()
     createSiteByData(this.info.token, this.company.testCompanyST.name,this.site.gwCheckNeidBody)
     checkCPENeidbyName(this.info.token,this.company.testCompanyST.name, this.site.gwCheckNeidBody.name, 0)
    })

  it('batch import site test ', function(){
    cy.contains('批量建站').click()
    cy.get('[class="el-message-box"]').within(() => {
      cy.contains('确定').click()
    })
    const fileName = 'import_success-ac1.xlsx';
    cy.get('[class="drop"]').attachFile(fileName, { subjectType: 'drag-n-drop' });
    cy.get('[data-cy="confirmEdit"]').click()
    // cy.contains("批量创建成功")
    visitAndSetPageUserInfo('/site',this.info)
    search_site('站点名称', 'site-208')
    cy.contains('共 9 条')
    this.site.bacthImportSiteList.forEach(st => {
      checkSite(this.info.token,this.company.testCompanyST.name, st.name)
      if(!st.hasOwnProperty("type")){
        checkSystemNetworkWithConsul(st.sn)
      }
    })
  })

  it('batch import site check file content ', function(){
    cy.contains('批量建站').click()
    cy.get('[class="el-message-box"]').within(() => {
      cy.contains('确定').click()
    })
    const fileName = 'check_content-ac2.xlsx';
    cy.get('[class="drop"]').attachFile(fileName, { subjectType: 'drag-n-drop' });
    cy.contains('数据校验失败，请仔细确认标红部分数据并修改，校对后重新导入')
    cy.get('table').within(() => {
      cy.get("td:contains('必填项')").should('have.length', 10)
    })
  })

  it('batch import site check file support 400 sites ', function(){
    cy.contains('批量建站').click()
    cy.get('[class="el-message-box"]').within(() => {
      cy.contains('确定').click()
    })
    const fileName = '400sites-ac3.xlsx';
    cy.get('[class="drop"]').attachFile(fileName, { subjectType: 'drag-n-drop' });
    cy.contains('单次导入最多支持200个站点')
  })

  it('batch import site check part success and rollback ', function(){
    cy.contains('批量建站').click()
    cy.get('[class="el-message-box"]').within(() => {
      cy.contains('确定').click()
    })
    const fileName = 'partsuccess_rollback-ac4.xlsx';
    cy.get('[class="drop"]').attachFile(fileName, { subjectType: 'drag-n-drop' });
    cy.get('[data-cy="confirmEdit"]').click()
    cy.get('[class="el-message-box"]').within(() => {
      cy.contains('确定').click()
    })
    visitAndSetPageUserInfo('/site',this.info)
    search_site('站点名称', 'site-2091')
    cy.contains('暂无数据')
  })

  it('check export file template', function(){
    cy.contains('批量建站').click()
    cy.get('[class="el-message-box"]').within(() => {
      cy.contains('确定').click()
    })
    cy.get('[class="el-link el-link--primary is-underline"]').should('have.attr', 'href').and('include', 'createSitesTemplate.xlsx')
  })

  it('batch import site check union ok', function(){
    cy.contains('批量建站').click()
    cy.get('[class="el-message-box"]').within(() => {
      cy.contains('确定').click()
    })
    const fileName = 'make_union-ac5.xlsx';
    cy.get('[class="drop"]').attachFile(fileName, { subjectType: 'drag-n-drop' });
    cy.get('[data-cy="confirmEdit"]').click()
    // cy.contains("批量创建成功")
    visitAndSetPageUserInfo('/union',this.info)
    createWebUnion(testUnionBody.testbatchSiteUnion)
    cy.contains("创建成功")
  })

  it('gw config add 2nd wan and 2nd lans', function(){
    createWebSite(testSiteBody.testConfig_GW_ARMS)
    cy.contains('创建成功')
    search_site('站点名称', testSiteBody.testConfig_GW_ARMS.name)
    rowContains('[data-cy=siteTable]',testSiteBody.testConfig_GW_ARMS.name,1,3,[testSiteBody.testConfig_GW_ARMS.name,testSiteBody.testConfig_GW_ARMS.sn])
    var cmd = thrusterTool + " " + Cypress.env('consulUrl') + " " + Cypress.env('consulToken') + " " +  testSiteBody.testConfig_GW_ARMS.sn
    exec_cmd_on_local_ignoreErr(cmd)
    checkAiwanJson(this.info.token, this.company.testCompanyST.name, testSiteBody.testConfig_GW_ARMS.name, testSiteBody.testConfig_GW_ARMS.sn)
    checkInfoJson(this.info.token, this.company.testCompanyST.name, testSiteBody.testConfig_GW_ARMS.name, testSiteBody.testConfig_GW_ARMS.sn)
    checkNeJson(testSiteBody.testConfig_GW_ARMS.sn)
    checkStartupJson(testSiteBody.testConfig_GW_ARMS, testSiteBody.testConfig_GW_ARMS.sn)
    checkFirewallJson(testSiteBody.testConfig_GW_ARMS, testSiteBody.testConfig_GW_ARMS.sn)
    checkNetworkJson(testSiteBody.testConfig_GW_ARMS, testSiteBody.testConfig_GW_ARMS.sn)
    checkDhcpJson(testSiteBody.testConfig_GW_ARMS, testSiteBody.testConfig_GW_ARMS.sn)
    checkWirelessJson(testSiteBody.testConfig_GW_ARMS, testSiteBody.testConfig_GW_ARMS.sn)
    // add WAN2 and LAN2
    let updatedSite = testSiteBody.testConfig_GW_ARMS
    updatedSite.wans.push({"name":"WAN2","mtu":"1200","public_ip":"","ip_mode":"FIA","ip_type":"PPPOE","account":'ningbo',"password":'ningbo',"bandwidth":"200",
        "prefer_pop_cac":"1", "prefer_pop_eac":"2","prefer_ip":"10.196.20.3", "ifname":'lan3','proxy': true})
    updatedSite.lans.push({"name":"LAN2","lan_port_num":1,"ip_addr":"172.32.18.1","mask":"24","DHCP":true,"ip_start":"172.32.18.78","ip_end":"172.32.18.180","internet":false,"IDC":true,'phy_ifname':'lan1'})
    // update the site on portal
    cy.get('[data-cy="siteTable"]').contains(testSiteBody.testConfig_GW_ARMS.name).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
    })
    editWebSite(updatedSite)
    cy.contains('更新成功')
    search_site('站点名称', updatedSite.name)
    rowContains('[data-cy=siteTable]',updatedSite.name,1,3,[updatedSite.name,updatedSite.sn])
    // call thruster to check the updated configurations
    var cmd = thrusterTool + " " + Cypress.env('consulUrl') + " " + Cypress.env('consulToken') + " " +  testSiteBody.testConfig_GW_ARMS.sn
    exec_cmd_on_local_ignoreErr(cmd)
    checkAiwanJson(this.info.token, this.company.testCompanyST.name, testSiteBody.testConfig_GW_ARMS.name, testSiteBody.testConfig_GW_ARMS.sn)
    checkInfoJson(this.info.token, this.company.testCompanyST.name, testSiteBody.testConfig_GW_ARMS.name, testSiteBody.testConfig_GW_ARMS.sn)
    checkNeJson(testSiteBody.testConfig_GW_ARMS.sn)
    checkStartupJson(testSiteBody.testConfig_GW_ARMS, testSiteBody.testConfig_GW_ARMS.sn)
    checkFirewallJson(testSiteBody.testConfig_GW_ARMS, testSiteBody.testConfig_GW_ARMS.sn)
    checkNetworkJson(testSiteBody.testConfig_GW_ARMS, testSiteBody.testConfig_GW_ARMS.sn)
    checkDhcpJson(testSiteBody.testConfig_GW_ARMS, testSiteBody.testConfig_GW_ARMS.sn)
    checkWirelessJson(testSiteBody.testConfig_GW_ARMS, testSiteBody.testConfig_GW_ARMS.sn)
    cy.get('[data-cy="siteTable"]').contains(testSiteBody.testConfig_GW_ARMS.name).parents('tr').within(() => {
      cy.contains('button', '删除').click()
    })
    cy.get('[class="el-message-box__btns"]').contains("确定").click()
    cy.contains('操作成功')
  })

    it('modify series site config', function(){
        rowContains('[data-cy=siteTable]',this.site.seriesMSiteBody.name,1,3,[this.site.seriesMSiteBody.name,this.site.seriesMSiteBody.sn[0]])
        cy.get('[data-cy="siteTable"]').contains(this.site.seriesMSiteBody.name).parents('tr').within(() => {
            cy.contains('button', '编辑').click()
        })
        var body = testSiteBody.testSTBeijing
        body.name = "seCPEConfigUpdate", body.tunnelNum = "9090",body.private = ["10.194.0.0/26","10.194.0.64/27","10.194.0.96/30","10.194.0.150/32"],body.location = "shanghai",body.sn = "ft3000"
        body.wans[0].mtu = "1200",body.wans[0].prefer_ip = "1.2.3.4",body.wans[0].gatewayMac="e4:f0:04:6f:4c:af",body.wans[0].staticIp='10.190.10.1'
        editWebSite(body)
        cy.contains('更新成功')
        rowContains('[data-cy=siteTable]',body.name,1,3,[body.name,body.sn])
        let cmd = thrusterTool + " " + Cypress.env('consulUrl') + " " + Cypress.env('consulToken') + " " +  body.sn
        exec_cmd_on_local_ignoreErr(cmd)
        checkAiwanJson(this.info.token, this.company.testCompanyST.name, body.name, body.sn)
        checkInfoJson(this.info.token, this.company.testCompanyST.name, body.name, body.sn)
        checkNeJson(body.sn)
        checkStartupJson(body, body.sn)
    })

    it('modify parallers site config', function(){
        rowContains('[data-cy=siteTable]',this.site.parallerMSiteBody.name,1,3,[this.site.parallerMSiteBody.name,this.site.parallerMSiteBody.sn[0]])
        cy.get('[data-cy="siteTable"]').contains(this.site.parallerMSiteBody.name).parents('tr').within(() => {
            cy.contains('button', '编辑').click()
        })
        var body = testSiteBody.testSTNanjing
        body.name = "paCPEConfigUpdate", body.tunnelNum = "7001",body.nets = ["172.49.15.0/24"],body.location = "beijing",body.sn = "ft3001",body.HA = false
        body.wans[0].ip = "172.23.14.27"
        body.lans[0].ip_addr = "172.25.14.27"
        editWebSite(body)
        cy.contains('更新成功')
        rowContains('[data-cy=siteTable]',body.name,1,3,[body.name,body.sn])
        let cmd = thrusterTool + " " + Cypress.env('consulUrl') + " " + Cypress.env('consulToken') + " " +  body.sn
        exec_cmd_on_local_ignoreErr(cmd)
        checkAiwanJson(this.info.token, this.company.testCompanyST.name, body.name, body.sn)
        checkInfoJson(this.info.token, this.company.testCompanyST.name, body.name, body.sn)
        checkNeJson(body.sn)
        checkStartupJson(body, body.sn)
    })

  it('wifi config test', function(){
    deleteSiteByName(this.info.token, this.company.testCompanyST.name, testSiteBody.testConfig_GW_ARMS.name)
    createWebSite(testSiteBody.testConfig_GW_ARMS)
    cy.contains('创建成功')
    // Remove the reload if portal refreshes the page after site creation done.
    cy.reload()
    search_site('站点名称', testSiteBody.testConfig_GW_ARMS.name)
    rowContains('[data-cy=siteTable]',testSiteBody.testConfig_GW_ARMS.name,1,3,[testSiteBody.testConfig_GW_ARMS.name,testSiteBody.testConfig_GW_ARMS.sn])
    // add LAN2 and update wifi
    let updatedSite = JSON.parse(JSON.stringify(testSiteBody.testConfig_GW_ARMS))
    updatedSite.lans.push({"name":"LAN2","lan_port_num":1,"ip_addr":"172.32.18.1","mask":"24","DHCP":true,"ip_start":"172.32.18.78","ip_end":"172.32.18.180","internet":false,"IDC":true,'phy_ifname':'lan1'})
    updatedSite.wifi.network = 'lan2', updatedSite.wifi.macfilter = 'deny', updatedSite.wifi.encryption_type = 'WEP Open System', updatedSite.wifi.encryption = 'wep-open'
    // update the site on portal
    cy.get('[data-cy="siteTable"]').contains(testSiteBody.testConfig_GW_ARMS.name).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
    })
    editWebSite(updatedSite)
    cy.contains('更新成功')
    search_site('站点名称', updatedSite.name)
    rowContains('[data-cy=siteTable]',updatedSite.name,1,3,[updatedSite.name,updatedSite.sn])
    // call thruster to check the updated configurations
    var cmd = thrusterTool + " " + Cypress.env('consulUrl') + " " + Cypress.env('consulToken') + " " +  testSiteBody.testConfig_GW_ARMS.sn
    exec_cmd_on_local_ignoreErr(cmd)
    checkWirelessJson(updatedSite, testSiteBody.testConfig_GW_ARMS.sn)
    // clear wifi config
    let updatedWifi = JSON.parse(JSON.stringify(updatedSite))
    updatedWifi.wifi.encryption_type = 'No Encryption',updatedWifi.wifi.encryption = 'none', updatedWifi.wifi.ssid = ""
    // update the site on portal
    cy.get('[data-cy="siteTable"]').contains(testSiteBody.testConfig_GW_ARMS.name).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
    })
    editWebSite(updatedWifi)
    cy.contains('更新成功')
    search_site('站点名称', updatedSite.name)
    rowContains('[data-cy=siteTable]',updatedSite.name,1,3,[updatedSite.name,updatedSite.sn])
    // call thruster to check the updated configurations
    exec_cmd_on_local_ignoreErr(cmd)
    checkWirelessJson(updatedWifi, testSiteBody.testConfig_GW_ARMS.sn)
    cy.get('[data-cy="siteTable"]').contains(testSiteBody.testConfig_GW_ARMS.name).parents('tr').within(() => {
      cy.contains('button', '删除').click()
    })
    cy.get('[class="el-message-box__btns"]').contains("确定").click()
    cy.contains('操作成功')
    })

  it('site authority test', function(){
      search_site('站点名称', this.site.gatewaySite2Body.name)
      cy.contains('共 0 条')
      changeToGlobalView("site",this.info)
      cy.contains('添加').should('not.exist')
      cy.contains('批量建站').should('not.exist')
      cy.contains('编辑').should('not.exist')
      cy.contains('删除').should('not.exist')
      search_site('站点名称', this.site.gatewaySite2Body.name)
      cy.contains('共 1 条')
      cy.contains('详情').click()
      CheckWebSiteReadonly()
      search_site('站点名称', this.site.gatewaySiteBody.name)
      cy.contains('共 1 条')
      search_site('资产序列号', this.site.gatewaySiteBody.sn.toString())
      cy.contains('共 1 条')
      search_site('站点名称', this.site.gatewaySite2Body.name)
      cy.contains('共 1 条')
      cy.logout()
      cy.typeLogin('testSiteUser@test.com','1wsx@edc')
      ClickSidebarSubMenu('配置','站点注册','siteTable')
      cy.contains('添加').should('not.exist')
      cy.contains('批量建站').should('not.exist')
      cy.contains('编辑').should('not.exist')
      cy.contains('删除').should('not.exist')
      search_site('站点名称', this.site.gatewaySite2Body.name)
      cy.contains('共 1 条')
      search_site('站点名称', this.site.gatewaySiteBody.name)
      cy.contains('共 0 条')
    })

    //SDWANDEV-4360
    it('search site by remark and replace site by other sn', function(){
      rowContains('[data-cy=siteTable]',this.site.searchSite1Body.name,1,3,[this.site.searchSite1Body.name,this.site.searchSite1Body.sn[0]])
      rowContains('[data-cy=siteTable]',this.site.searchSite2Body.name,1,3,[this.site.searchSite2Body.name,this.site.searchSite2Body.sn[0]])
      // checkSearchResult(this.site.searchSite1Body.remark, 1)
      // checkSearchResult(this.site.searchSite2Body.remark, 1)
      // checkSearchResult("beizhu", 2)
      // search_site_by_name(this.site.searchSite2Body.remark)
      replaceSiteBySN(this.site.searchSite2Body.name, "2009")
      checkDevice(this.info.token, this.company.testCompanyST.name, this.site.searchSite2Body.name, "2009")
    })
})
