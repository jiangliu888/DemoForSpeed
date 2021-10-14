import { createCompanyByData, createSiteByData, createUnion, deleteAllSites, deleteAllUnions, deleteCompanyByName, getIdByCompanyName , getSiteNEidsByNameList} from '../utils/basic-utils'
import { exec_cmd_on_local } from '../utils/consulCheck-utils'
import {visitAndSetPageUserInfo,getToken, changeSiteCompanyView, rowHeaderCheck, rowBodyCheck, checkTableLineNumber} from '../utils/web-utils'

export function checkDeviceContent(type,filter,value){
  if(type == "CPE"){
    cy.get('[class="device-status"]').parent('div').within(()=>{
      cy.get(filter).eq(0).contains(value)
    })
  }else{
    cy.get('[class="device-status"]').parent('div').within(()=>{
      cy.get(filter).eq(1).contains(value)
    })
  }
}

export function checkAlarm(info,company,site){
  cy.get('[class="alarm-content"]').within(() =>{
    rowHeaderCheck(0,7,["站点名称","Deviceld","Neid","告警名称","告警类型","级别","时间"])
    getIdByCompanyName(info.token, company.testCompanyDashBoard.name)
    cy.get('@companyId').then(companyId => {
      var nameList = [site.DashBoardSite1Body.name,site.DashBoardSite2Body.name,site.DashBoardSite3Body.name]
      getSiteNEidsByNameList(info.token,companyId,nameList)
      cy.get('@neIds').then(neIds => {
        rowBodyCheck(nameList[0],0,7,[nameList[0],"3011",neIds[0],"OnlyMobile","CPE网络异常","一般","2020-11-24 09:39"])
        rowBodyCheck(nameList[1],0,7,[nameList[1],"3012",neIds[1],"WanLinkDown","CPE网络异常","重要","2020-11-24 09:39"])
        rowBodyCheck(nameList[2],0,7,[nameList[2],"3013",neIds[2],"NodeOffline","CPE设备故障","紧急","2020-11-25 17:27"])
      })
    })
  })
}

export function checkAlarmJump(name, alarm){
  cy.get('[class="device-status"]').within(() =>{
    cy.contains(name).click()
    cy.url().should('contain',alarm)
  })
  checkTableLineNumber(1)
  cy.contains(alarm)
}

export function checkSite(site){
  cy.get('[class="site-content"]').within(() =>{
    rowHeaderCheck(0,5,["站点","带宽","4G流量","状态","告警"])
    var nameList = [site.DashBoardSite1Body.name,site.DashBoardSite2Body.name,site.DashBoardSite3Body.name]
    rowBodyCheck(nameList[0],0,4,[nameList[0],"KB","KB","离线"])
    rowBodyCheck(nameList[1],0,4,[nameList[1],"KB","KB","离线"])
    rowBodyCheck(nameList[2],0,4,[nameList[2],"KB","KB","离线"])
  })
}

export function checkFlow(){
  cy.get('[class="flow-content"]').within(() =>{
    rowHeaderCheck(0,3,["","今日","本月"])
    rowBodyCheck("隧道流量",0,3,["隧道流量","KB","KB"])
    rowBodyCheck("4G流量",0,3,["4G流量","KB","KB"])
  })
}

export function checkTopo(){
  cy.get('[class="topo-content"]').toMatchImageSnapshot()
}

before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
  //删除公司
  cy.get('@company').then(company => {
    cy.get('@site').then(site => {
      cy.get('@info').then(t_info => {
        deleteAllUnions(t_info.token, company.testCompanyDashBoard.name)
        deleteAllSites(t_info.token, company.testCompanyDashBoard.name)
        deleteCompanyByName(t_info.token,company.testCompanyDashBoard.name)
        createCompanyByData(t_info.token,company.testCompanyDashBoard)
        createSiteByData(t_info.token, company.testCompanyDashBoard.name, site.DashBoardSite1Body)
        createSiteByData(t_info.token, company.testCompanyDashBoard.name, site.DashBoardSite2Body)
        createSiteByData(t_info.token, company.testCompanyDashBoard.name, site.DashBoardSite3Body)
        getIdByCompanyName(t_info.token, company.testCompanyDashBoard.name)
        cy.get('@companyId').then(companyId => {
          var nameList = [site.DashBoardSite1Body.name,site.DashBoardSite2Body.name,site.DashBoardSite3Body.name]
          getSiteNEidsByNameList(t_info.token,companyId,nameList)
          cy.get('@neIds').then(neIds => {
            exec_cmd_on_local("bash /e2e/RoaringDog/test/prepDashBoardtest.sh " + companyId + " " + neIds[0] + " " + neIds[1] + " " + neIds[2])
          })
        })
        createUnion(t_info.token, company.testCompanyDashBoard.name,site.DashBoardSite1Body.name,site.DashBoardSite2Body.name)
        createUnion(t_info.token, company.testCompanyDashBoard.name,site.DashBoardSite1Body.name,site.DashBoardSite3Body.name)
        cy.reload()
      }) 
    })
    }) 
})

describe('company dashboard test', function() {

  beforeEach(function () {
    visitAndSetPageUserInfo('/dashboard',this.info)
    changeSiteCompanyView(this.company.testCompanyDashBoard.name,4000)
   })
  //SDWANDEV-4475 SDWANDEV-4476
    it('device info check', function() {
      //check CPE 在线数/总数
      checkDeviceContent("CPE",'[class="device-online"]',"0/3")
      //check CPE 服务等级下降
      checkDeviceContent("CPE",'[class="device-server-level"]',"1")
      //check CPE 仅4G服务
      checkDeviceContent("CPE",'[class="device-only-4g"]',"1")
      //check CPE 离线
      checkDeviceContent("CPE",'[class="device-offline"]',"3")
      //check HUB 在线数/总数
      checkDeviceContent("HUB",'[class="device-online"]',"0/1")
      //check HUB 服务等级下降
      checkDeviceContent("HUB",'[class="device-server-level"]',"0")
      //check HUB 仅4G服务
      checkDeviceContent("HUB",'[class="device-only-4g"]',"1")
      //check HUB 离线
      checkDeviceContent("HUB",'[class="device-offline"]',"1")
    })

    //SDWANDEV-4479
    it.skip('topo check',function(){
      //checkTopo()
    })

    //SDWANDEV-4478
    it('alarm info check',function(){
      checkAlarm(this.info,this.company,this.site)
    })

    //SDWANDEV-4480
    it('sites info check',function(){
      checkSite(this.site)
    })

    //SDWANDEV-4477
    it('flow info check',function(){
      checkFlow()
    })

    //SDWANDEV-4585
    it('jump to alarm page and filter the result',function(){
      checkAlarmJump("服务等级下降","WanLinkDown")
      cy.go('back')
      checkAlarmJump("仅4G服务","OnlyMobile")
      cy.go('back')
      checkAlarmJump("离线","NodeOffline")
    })
})