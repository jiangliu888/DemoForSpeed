import {deleteCompanyByName, deleteAllSites, createCompanyByData, createSiteByData, getLogsNumberByCompanyName} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView, rowContains,createAcl,updateacl} from '../utils/web-utils'
import {testFirewallBody} from '../utils/variables-utils'
import {checkAclsWithConsul} from '../utils/consulCheck-utils'




before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
  //删除公司
  cy.get('@company').then(company => {
    cy.get('@site').then(site => {
      cy.get('@info').then(t_info => {
        deleteAllSites(t_info.token,company.testCompany1Firewall.name)
        deleteAllSites(t_info.token,company.testCompany2Firewall.name)
        deleteCompanyByName(t_info.token,company.testCompany1Firewall.name)
        deleteCompanyByName(t_info.token,company.testCompany2Firewall.name)
        createCompanyByData(t_info.token,company.testCompany1Firewall)
        createCompanyByData(t_info.token,company.testCompany2Firewall)
        createSiteByData(t_info.token, company.testCompany1Firewall.name,site.FirewallGwSite1Body)
        createSiteByData(t_info.token, company.testCompany1Firewall.name,site.FirewallGwSite2Body)
        createSiteByData(t_info.token, company.testCompany2Firewall.name,site.FirewallGwSite3Body)
        cy.reload()
      }) 
    })
  }) 
})

describe('firewall page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/firewall',this.info)
    changeSiteCompanyView(this.company.testCompany1Firewall.name)
    cy.contains("前往")
   })

    it('create modify and delete firewall test', function(){
      createAcl(testFirewallBody.aclFailBody)
      cy.get('[data-cy="cancelEdit"]').click()
      //createAcl(testFirewallBody.aclOnlyPortBody)
      createAcl(testFirewallBody.aclFullBody)
      let checkList = [testFirewallBody.aclFullBody.name,testFirewallBody.aclFullBody.site_name,testFirewallBody.aclFullBody.srcCIDR,testFirewallBody.aclFullBody.dstCIDR,testFirewallBody.aclFullBody.protocol.join(' '),testFirewallBody.aclFullBody.dstPort,testFirewallBody.aclFullBody.strategy]
      rowContains('[data-cy="rules"]',testFirewallBody.aclFullBody.name,1, 8 ,checkList)
      updateacl()
      checkAclsWithConsul(this.info.token,this.company.testCompany1Firewall.name, this.site.FirewallGwSite1Body.name, testFirewallBody.aclFullBody.name)
      cy.get('[data-cy="rules"]').contains(testFirewallBody.aclFullBody.name).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
        cy.get('[data-cy="dest_port"]').clear().type(65535)
        cy.get('[data-cy="confirmEdit"]').click()
      })
      cy.contains('更新成功')
      cy.get('[data-cy="rules"]').contains(testFirewallBody.aclFullBody.name).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
      cy.contains('删除成功')
      //check the operation log of company
      getLogsNumberByCompanyName(this.info.token,this.company.testCompany1Firewall.name)
      cy.get('@logsNumber').then(logsNumber =>{
        expect(logsNumber).to.equal(6)
      })
      getLogsNumberByCompanyName(this.info.token,this.company.testCompany2Firewall.name)
      cy.get('@logsNumber').then(logsNumber =>{
        expect(logsNumber).to.equal(1)
      })
    })

    it('firewall belong to own company test', function(){
      createAcl(testFirewallBody.aclFullBody)
      cy.contains("共 1 条")
      updateacl()
      changeSiteCompanyView(this.company.testCompany2Firewall.name)
      cy.contains("共 0 条")
      createAcl(testFirewallBody.aclOnlyPortCompany2)
      cy.contains("共 1 条")
      updateacl()
      checkAclsWithConsul(this.info.token,this.company.testCompany2Firewall.name, testFirewallBody.aclOnlyPortCompany2.site_name, testFirewallBody.aclOnlyPortCompany2.name)
      //check the operation log of company
      getLogsNumberByCompanyName(this.info.token,this.company.testCompany1Firewall.name)
      cy.get('@logsNumber').then(logsNumber =>{
        expect(logsNumber).to.equal(8)
      })
      getLogsNumberByCompanyName(this.info.token,this.company.testCompany2Firewall.name)
      cy.get('@logsNumber').then(logsNumber =>{
        expect(logsNumber).to.equal(3)
      })
    })
})

