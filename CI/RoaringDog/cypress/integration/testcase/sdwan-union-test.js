import {deleteCompanyByName, deleteAllUnions,deleteAllSites, createSiteByData, createCompanyByData,deleteUser, createUser, createUnion,getLogsNumber} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView, createWebUnion, rowContains, changeToGlobalView,ClickSidebarSubMenu} from '../utils/web-utils'
import {testUnionBody,UserBody,} from '../utils/variables-utils'
import {checkUnionInfoWithConsul} from '../utils/consulCheck-utils'

before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
})

beforeEach(function () {
  visitAndSetPageUserInfo('/union',this.info)
  changeSiteCompanyView(this.company.testCompanyUN.name)
 })

describe('union page test', function() {
  before(function(){
    deleteAllUnions(this.info.token,this.company.testCompanyUN.name)
    deleteAllSites(this.info.token,this.company.testCompanyUN.name)
    deleteAllUnions(this.info.token,this.company.testCompanyUN3.name)
    deleteAllSites(this.info.token,this.company.testCompanyUN3.name)
    deleteUser(this.info.token, UserBody.testUserUnion.username)
    deleteUser(this.info.token, UserBody.testUserUnion2.username)
    deleteCompanyByName(this.info.token,this.company.testCompanyUN.name)
    deleteCompanyByName(this.info.token,this.company.testCompanyUN2.name)
    deleteCompanyByName(this.info.token,this.company.testCompanyUN3.name)
    createCompanyByData(this.info.token,this.company.testCompanyUN)
    createCompanyByData(this.info.token,this.company.testCompanyUN2)
    createCompanyByData(this.info.token,this.company.testCompanyUN3)
    createUser(this.info.token, UserBody.testUserUnion)
    createUser(this.info.token, UserBody.testUserUnion2)
    createSiteByData(this.info.token, this.company.testCompanyUN.name,this.site.UnGwSiteBody)
    createSiteByData(this.info.token, this.company.testCompanyUN.name,this.site.UnSeSiteBody)
    createSiteByData(this.info.token, this.company.testCompanyUN.name,this.site.UnPaSiteBody)
    createSiteByData(this.info.token, this.company.testCompanyUN3.name,this.site.UnGwSite2Body)
    createSiteByData(this.info.token, this.company.testCompanyUN3.name,this.site.UnPaSite2Body)
    cy.reload()
  })

    it('create modify and delete hubUnions union test', function(){
      createWebUnion(testUnionBody.testParallel_hubUnions)
      testUnionBody.testParallel_hubUnions.spokenSites.forEach(spoken => {
        checkUnionInfoWithConsul(this.info.token,this.company.testCompanyUN.name,testUnionBody.testParallel_hubUnions.hubSite + "-" + spoken)
      })
      testUnionBody.testParallel_hubUnions.spokenSites.forEach(spoken => {
        rowContains('[data-cy=unionTable]',testUnionBody.testParallel_hubUnions.hubSite + "-" + spoken,1,3,[testUnionBody.testParallel_hubUnions.hubSite,spoken])
        cy.get('[data-cy="unionTable"]').contains(testUnionBody.testParallel_hubUnions.hubSite + "-" +  spoken).parents('tr').within(() => {
          cy.contains('button', '编辑').click()
        })
        cy.get('[data-cy="unionDialog"]').within(() => {
          cy.typeInputWithLable('限速',100)
          cy.clickButtonWithLable('确 定')
        })
        cy.contains('更新成功')
        cy.reload()
        changeSiteCompanyView(this.company.testCompanyUN.name)
        cy.get('[data-cy="unionTable"]').contains(testUnionBody.testParallel_hubUnions.hubSite + "-" +  spoken).parents('tr').within(() => {
          cy.contains('button', '删除').click()
        })
        cy.get('[class="el-message-box__btns"]').contains("确定").click()
        cy.contains('操作成功')
      })
      //check the operation log of union
      getLogsNumber(this.info.token,{resourceType:'union',action:'add',company:this.company.testCompanyUN.name,username:'admin'})
      cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(2)})
      getLogsNumber(this.info.token,{resourceType:'union',action:'del',company:this.company.testCompanyUN.name,username:'admin'})
      cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(2)})
      getLogsNumber(this.info.token,{resourceType:'union',action:'update',company:this.company.testCompanyUN.name,username:'admin',detail:'修改带宽值为100Mbps'})
      cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(2)})
    })

    it('create modify and delete NormalUnions union test', function(){
      createWebUnion(testUnionBody.testse_gwUnions)
      checkUnionInfoWithConsul(this.info.token,this.company.testCompanyUN.name,testUnionBody.testse_gwUnions.site1 + "-" + testUnionBody.testse_gwUnions.site2)
      rowContains('[data-cy=unionTable]',testUnionBody.testse_gwUnions.site1 + "-" + testUnionBody.testse_gwUnions.site2,1,3,[testUnionBody.testse_gwUnions.site1,testUnionBody.testse_gwUnions.site2])
      cy.get('[data-cy="unionTable"]').contains(testUnionBody.testse_gwUnions.site1 + "-" + testUnionBody.testse_gwUnions.site2).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
      })
      cy.get('[data-cy="unionDialog"]').within(() => {
        cy.typeInputWithLable('限速',100)
        cy.clickButtonWithLable('确 定')
      })
      cy.contains('更新成功')
      cy.reload()
      changeSiteCompanyView(this.company.testCompanyUN.name)
      cy.get('[data-cy="unionTable"]').contains(testUnionBody.testse_gwUnions.site1 + "-" + testUnionBody.testse_gwUnions.site2).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
      cy.contains('操作成功')
    })
})
describe('union page test', function() {
    before(function () {
      deleteAllUnions(this.info.token,this.company.testCompanyUN.name)
      deleteAllUnions(this.info.token,this.company.testCompanyUN3.name)
      createUnion(this.info.token, this.company.testCompanyUN.name,this.site.UnPaSiteBody.name,this.site.UnGwSiteBody.name)
      createUnion(this.info.token, this.company.testCompanyUN3.name,this.site.UnGwSite2Body.name,this.site.UnPaSite2Body.name)
     })
    
     it('union use authority test', function(){
      changeToGlobalView("union",this.info)
      cy.contains('拓扑网络图')
      cy.contains('添加').should('not.exist')
      rowContains('[data-cy=unionTable]',this.site.UnPaSiteBody.name + "-" +this.site.UnGwSiteBody.name,0,4,[this.company.testCompanyUN.name,this.site.UnPaSiteBody.name + "-" +this.site.UnGwSiteBody.name,this.site.UnPaSiteBody.name,this.site.UnGwSiteBody.name])
      rowContains('[data-cy=unionTable]',this.site.UnGwSite2Body.name + "-" +this.site.UnPaSite2Body.name,0,4,[this.company.testCompanyUN3.name,this.site.UnGwSite2Body.name + "-" +this.site.UnPaSite2Body.name,this.site.UnGwSite2Body.name,this.site.UnPaSite2Body.name])
      cy.contains('编辑').should('not.exist')
      cy.contains('删除').should('not.exist')
      cy.logout()
      cy.typeLogin('testUnionUser@test.com','1wsx@edc')
      ClickSidebarSubMenu('配置','拓扑管理','unionTable')
      cy.contains('共 1 条')
      cy.contains('拓扑网络图')
      cy.contains('添加').should('not.exist')
      cy.contains('编辑').should('not.exist')
      cy.contains('删除').should('not.exist')
      cy.logout()
      cy.typeLogin('testUnionUser2@test.com','1wsx@edc')
      ClickSidebarSubMenu('配置','拓扑管理','unionTable')
      cy.contains('共 0 条')
    })

})