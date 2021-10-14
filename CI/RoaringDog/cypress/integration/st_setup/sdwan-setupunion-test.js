import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView, createWebUnion, rowContains} from '../utils/web-utils'
import {testUnionBody} from '../utils/variables-utils'
import {deleteAllUnions} from '../utils/basic-utils'


before(function () {
  cy.fixture("companies/companies.json").as('company')
  getToken()
  cy.get('@company').then(company => {
    cy.get('@info').then(t_info => {
      deleteAllUnions(t_info.token,company.testCompanyST.name)
    })
  })
})

describe('site page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/union',this.info)
    changeSiteCompanyView(this.company.testCompanyST.name)
   })

    it('create serise sites unions in ST env', function(){
      createWebUnion(testUnionBody.testSeriesUnions)
      rowContains('[data-cy=unionTable]',testUnionBody.testSeriesUnions.hubSite + "-" + testUnionBody.testSeriesUnions.spokenSites[0],2,3,[testUnionBody.testSeriesUnions.spokenSites[0]])
      if (testUnionBody.testSeriesUnions.spokenSites.length > 1) {rowContains('[data-cy=unionTable]',testUnionBody.testSeriesUnions.hubSite + "-" + testUnionBody.testSeriesUnions.spokenSites[1],2,3,[testUnionBody.testSeriesUnions.spokenSites[1]])}
    })

    it('create parallel sites unions in ST env', function(){
      createWebUnion(testUnionBody.testParallelUnions)
      rowContains('[data-cy=unionTable]',testUnionBody.testParallelUnions.hubSite + "-" + testUnionBody.testParallelUnions.spokenSites[0],2,3,[testUnionBody.testParallelUnions.spokenSites[0]])
      rowContains('[data-cy=unionTable]',testUnionBody.testParallelUnions.hubSite + "-" + testUnionBody.testParallelUnions.spokenSites[1],2,3,[testUnionBody.testParallelUnions.spokenSites[1]])
    })

    if (testUnionBody.hasOwnProperty('testGatewaylUnions')) {
        it('create gateway sites unions in ST env', function () {
            createWebUnion(testUnionBody.testGatewaylUnions)
            cy.get("[data-cy=unionTable]")
        })
    }

    if (testUnionBody.hasOwnProperty('testGatewayHAUnions')) {
        it('create gateway HA sites unions in ST env', function () {
            createWebUnion(testUnionBody.testGatewayHAUnions)
            cy.get("[data-cy=unionTable]")
        })
    }
})