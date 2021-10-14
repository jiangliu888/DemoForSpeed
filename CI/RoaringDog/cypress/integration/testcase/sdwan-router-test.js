import {deleteCompanyByName, deleteAllSites, createCompanyByData, createSiteByData} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView, rowContains,createrouter,updaterouter,modifyRouter} from '../utils/web-utils'
import {testRouterBody,testRouterModifyBody} from '../utils/variables-utils'
import {checkroutersWithConsul} from '../utils/consulCheck-utils'



before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
  //删除公司
  cy.get('@company').then(company => {
    cy.get('@site').then(site => {
      cy.get('@info').then(t_info => {
        deleteAllSites(t_info.token,company.testCompany1Router.name)
        deleteAllSites(t_info.token,company.testCompany2Router.name)
        deleteCompanyByName(t_info.token,company.testCompany1Router.name)
        deleteCompanyByName(t_info.token,company.testCompany2Router.name)
      })
      //创建公司
      cy.get('@info').then(t_info => {
        createCompanyByData(t_info.token,company.testCompany1Router)
        createCompanyByData(t_info.token,company.testCompany2Router)
        createSiteByData(t_info.token, company.testCompany1Router.name,site.RouterGwSite1Body)
        createSiteByData(t_info.token, company.testCompany1Router.name,site.RouterGwSite2Body)
        createSiteByData(t_info.token, company.testCompany2Router.name,site.RouterGwSite3Body)
        createSiteByData(t_info.token, company.testCompany2Router.name,site.RouterGwSite4Body)
        cy.reload()
      }) 
    })
  }) 
})

describe('Router page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/routerConfig',this.info)
    changeSiteCompanyView(this.company.testCompany1Router.name)
    cy.contains("前往")
   })

    it('create modify and delete Router test', function(){
      createrouter(testRouterBody.routerFailBody)
      cy.get('[data-cy="cancelEdit"]').click()
      //createrouter(testRouterBody.routerOnlyPortBody)
      createrouter(testRouterBody.routerFullBody)
      let checkList = [testRouterBody.routerFullBody.name,testRouterBody.routerFullBody.site_name,testRouterBody.routerFullBody.srcCIDR,testRouterBody.routerFullBody.srcPort,testRouterBody.routerFullBody.dstCIDR,testRouterBody.routerFullBody.protocol.join(' '),testRouterBody.routerFullBody.dstPort,testRouterBody.routerFullBody.nextHop,testRouterBody.priority]
      rowContains('[data-cy="rules"]',testRouterBody.routerFullBody.name,1, 9 ,checkList)
      updaterouter()
      checkroutersWithConsul(this.info.token,this.company.testCompany1Router.name, testRouterBody.routerFullBody.site_name, testRouterBody.routerFullBody.name, testRouterBody.routerFullBody.nextHop)
      //modifyRouter(testRouterModifyBody.modifyNextHop)
      //rowContains('[data-cy="rules"]',testRouterBody.routerFullBody.name,1, 9 ,checkList)
      modifyRouter(testRouterModifyBody.modifyDstPort)
      let checkList_m = [testRouterBody.routerFullBody.name,testRouterBody.routerFullBody.site_name,testRouterBody.routerFullBody.srcCIDR,testRouterBody.routerFullBody.srcPort,testRouterBody.routerFullBody.dstCIDR,testRouterBody.routerFullBody.protocol.join(' '),testRouterModifyBody.modifyDstPort.dstPort,testRouterBody.routerFullBody.nextHop,testRouterBody.priority]
      rowContains('[data-cy="rules"]',testRouterBody.routerFullBody.name,1, 9 ,checkList_m)
      cy.get('[data-cy="rules"]').contains(testRouterBody.routerFullBody.name).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
      cy.contains('删除成功')
    })

    it('Router belong to own company test', function(){
      createrouter(testRouterBody.routerFullBody)
      cy.contains("共 1 条")
      updaterouter()
      changeSiteCompanyView(this.company.testCompany2Router.name)
      cy.contains("共 0 条")
      createrouter(testRouterBody.routerOnlyPortCompany2)
      cy.contains("共 1 条")
      updaterouter()
      checkroutersWithConsul(this.info.token,this.company.testCompany2Router.name, testRouterBody.routerOnlyPortCompany2.site_name, testRouterBody.routerOnlyPortCompany2.name, testRouterBody.routerOnlyPortCompany2.nextHop)
    })
})
