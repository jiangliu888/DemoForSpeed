import {deleteCompanyByName, deleteAllUnions, deleteAllSites, createCompanyByData} from '../utils/basic-utils'
import {testSiteBody, setupSites} from '../utils/variables-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView, createWebSite} from '../utils/web-utils'


before(function () {
  cy.fixture("companies/companies.json").as('company')
  getToken()
  //删除公司
  cy.get('@company').then(company => {
    cy.get('@info').then(t_info => {
      deleteAllUnions(t_info.token,company.testCompanyST.name)
      deleteAllSites(t_info.token,company.testCompanyST.name)
      deleteCompanyByName(t_info.token,company.testCompanyST.name)
      if (company.hasOwnProperty('testCompanySTAPI')) {deleteCompanyByName(t_info.token,company.testCompanySTAPI.name)}
      if (company.hasOwnProperty('testCompanySTAPI2')) {deleteCompanyByName(t_info.token,company.testCompanySTAPI2.name)}
      createCompanyByData(t_info.token,company.testCompanyST)
      if (company.hasOwnProperty('testCompanySTAPI')) {createCompanyByData(t_info.token,company.testCompanySTAPI)}
      if (company.hasOwnProperty('testCompanySTAPI2')) {createCompanyByData(t_info.token,company.testCompanySTAPI2)}
    }) 
  })
})

describe('site page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/site',this.info)
    changeSiteCompanyView(this.company.testCompanyST.name)
   })

    for (const site of setupSites) {
        it('create ' + site + ' sites in ST env', function () {
            createWebSite(testSiteBody[site])
            cy.contains('创建成功')
            cy.get("[data-cy=siteContainer]")
        })
    }
})
