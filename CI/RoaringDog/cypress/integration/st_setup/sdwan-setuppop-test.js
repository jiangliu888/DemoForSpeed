import {changeToGlobalView, getToken,visitAndSetPageUserInfo} from '../utils/web-utils'
import {testPopBody} from '../utils/variables-utils.js'
import {deletePopByPopId} from '../utils/basic-utils'


before(function () {
  getToken() 
  cy.get('@info').then(t_info => {
    deletePopByPopId(t_info.token,testPopBody.testSTPop1Body.popId)
    if (testPopBody.hasOwnProperty('testSTPop2Body')) {deletePopByPopId(t_info.token,testPopBody.testSTPop2Body.popId)}
  })
 })

describe('Pop page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/pop',this.info)
    changeToGlobalView("pop",this.info)
    cy.wait(1000)
   })

    it('config pop1 neid and cac eac', function(){
      cy.get('[data-cy=addPop]').click()
      cy.contains('共 1 条')
      cy.FilterSelectValue('[data-cy=popId]',testPopBody.testSTPop1Body.hostName)
      cy.get('[data-cy=cac]').type(testPopBody.testSTPop1Body.cac)
      cy.get('[data-cy=eac]').type(testPopBody.testSTPop1Body.eac)
      cy.ClickSelectValue('[data-cy=routeCodeTypeSelect]','ER')
      cy.contains('button', '确认').click()
      cy.contains('更新成功') 
    })

    if (testPopBody.hasOwnProperty('testSTPop2Body')) {
        it('config pop2 neid and cac eac', function () {
            cy.get('[data-cy=addPop]').click()
            cy.contains('共 2 条')
            cy.FilterSelectValue('[data-cy=popId]', testPopBody.testSTPop2Body.hostName)
            cy.get('[data-cy=cac]').type(testPopBody.testSTPop2Body.cac)
            cy.get('[data-cy=eac]').type(testPopBody.testSTPop2Body.eac)
            cy.ClickSelectValue('[data-cy=routeCodeTypeSelect]', 'ER')
            cy.contains('button', '确认').click()
            cy.contains('更新成功')
        })
    }

})
