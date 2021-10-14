import {createSaasSearchPatternByCode} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, searchArea, searchPop, checkPopList, checksearchPopNum, addPoptoCode, changeToGlobalView} from '../utils/web-utils'
import {testServiceBody,saasSearchPatternBody} from '../utils/variables-utils'


before(function () {
  getToken() 
  cy.get('@info').then(t_info => {
    createSaasSearchPatternByCode(t_info.token,saasSearchPatternBody.chinaCode.areaCode,saasSearchPatternBody.chinaCode)
    if (saasSearchPatternBody.hasOwnProperty('SingaporeCode')) {createSaasSearchPatternByCode(t_info.token,saasSearchPatternBody.SingaporeCode.areaCode,saasSearchPatternBody.SingaporeCode)}
  })
 })

describe('areaCode test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/areaCode',this.info)
    cy.reload()
    changeToGlobalView("areaCode",this.info)
    cy.wait(1000)
   })
    
    it('Add china areaCode to saas and anycast services', function(){
      searchArea(saasSearchPatternBody.chinaCode.areaCode)
      cy.get('[data-cy="popConfigs"]').contains(saasSearchPatternBody.chinaCode.countryDes).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
      })
      cy.url().should('contain', 'serviceDetail')
      cy.contains('button', '添加').click()
      searchPop(testServiceBody.testSTSaas1Body.hostName)
      //checkPopList(testServiceBody.testSTSaas1Body.hostName)
      checksearchPopNum(1)
      if (saasSearchPatternBody.hasOwnProperty('SingaporeCode')) {
          cy.get('li.el-select-dropdown__item').filter(':visible').click({ multiple: true })
          searchPop(testServiceBody.testSTAnycast1Body.hostName)
          checkPopList(testServiceBody.testSTAnycast1Body.hostName)
      }
      addPoptoCode()
    })

    if (saasSearchPatternBody.hasOwnProperty('SingaporeCode')) {
        it('Add singapore areaCode to saas', function () {
            searchArea(saasSearchPatternBody.SingaporeCode.areaCode)
            cy.get('[data-cy="popConfigs"]').contains(saasSearchPatternBody.SingaporeCode.countryDes).parents('tr').within(() => {
                cy.contains('button', '编辑').click()
            })
            cy.url().should('contain', 'serviceDetail')
            cy.contains('button', '添加').click()
            searchPop(testServiceBody.testSTSaas2Body.hostName)
            //checkPopList(testServiceBody.testSTSaas2Body.hostName)
            checksearchPopNum(1)
            addPoptoCode()
        })
    }
})