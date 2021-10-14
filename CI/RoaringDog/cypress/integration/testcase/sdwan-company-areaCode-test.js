import {createCompanyByData,deleteCompanyByName,deletePopByPopId,putPop} from '../utils/basic-utils'
import {getToken, changeSiteCompanyView, visitAndSetPageUserInfo, searchArea, searchPop, addPoptoCode} from '../utils/web-utils'
import {testServiceBody,saasSearchPatternBody, PopTypeSaas,popBody} from '../utils/variables-utils'
import {checkCompanySearchPatternWithConsul} from '../utils/consulCheck-utils'


function checkSearchResult(content){
  cy.get('[data-cy="popConfigs"]').contains(content)
}

function checkSearchResultLength(num){
  cy.get('[data-cy="popConfigs"]').within(() => {
    cy.get("tr.el-table__row").should(($tb)=>{
     expect($tb).to.have.length(num)
    })
  })
}

before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken() 
  cy.get('@company').then(company => {
    cy.get('@info').then(t_info => {
      deleteCompanyByName(t_info.token,company.testCompany1AreaCode.name)
      deleteCompanyByName(t_info.token,company.testCompany2AreaCode.name)
      deletePopByPopId(t_info.token,testServiceBody.putCompanySaasBody.popId,PopTypeSaas)
      deletePopByPopId(t_info.token,popBody.testpop4.popId)
      putPop(t_info.token,popBody.testpop4)
      putPop(t_info.token,testServiceBody.putCompanySaasBody)
      createCompanyByData(t_info.token,company.testCompany1AreaCode)
      createCompanyByData(t_info.token,company.testCompany2AreaCode)
    })
  })
})

describe('areaCode test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/companyAreaCode',this.info)
    changeSiteCompanyView(this.company.testCompany1AreaCode.name)
   })
    

   it('Add china areaCode to saas and anycast services in company', function(){
    searchArea(saasSearchPatternBody.chinaCode.areaCode)
    cy.get('[data-cy="popConfigs"]').contains(saasSearchPatternBody.chinaCode.countryDes).parents('tr').within(() => {
      cy.contains('button', '编辑').click()
    })
    cy.url().should('contain', 'companyServiceDetail')
    cy.contains('button', '添加').click()
    searchPop(testServiceBody.putCompanySaasBody.hostname)
    addPoptoCode()
    cy.contains('button', '返回').click()
    // check consul
    checkCompanySearchPatternWithConsul(this.info.token,this.company.testCompany1AreaCode.name,saasSearchPatternBody.chinaCode.areaCode)
    // by pop info
    searchArea(testServiceBody.putCompanySaasBody.ips[0].public_ip)
    checkSearchResult(saasSearchPatternBody.chinaCode.areaCode)
    checkSearchResultLength(1)
   //change company
    changeSiteCompanyView(this.company.testCompany2AreaCode.name)
    searchArea(testServiceBody.putCompanySaasBody.ips[0].public_ip)
    checkSearchResultLength(0)
  })
})