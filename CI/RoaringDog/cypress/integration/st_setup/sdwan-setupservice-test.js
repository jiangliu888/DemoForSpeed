import {changeToGlobalView, getToken,visitAndSetPageUserInfo} from '../utils/web-utils'
import {testServiceBody} from '../utils/variables-utils.js'
import {deletePopByPopId} from '../utils/basic-utils'


before(function () {
  getToken() 
  cy.get('@info').then(t_info => {
    deletePopByPopId(t_info.token,testServiceBody.testSTSaas1Body.popId, testServiceBody.testSTSaas1Body.popType)
    if (testServiceBody.hasOwnProperty('testSTAnycast1Body')) {deletePopByPopId(t_info.token,testServiceBody.testSTAnycast1Body.popId, testServiceBody.testSTAnycast1Body.popType)}
    if (testServiceBody.hasOwnProperty('testSTSaas2Body')) {deletePopByPopId(t_info.token,testServiceBody.testSTSaas2Body.popId, testServiceBody.testSTSaas2Body.popType)}
  })
 })

describe('service page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/service',this.info)
    changeToGlobalView("service",this.info)
    cy.wait(1000)
   })

    it('config saas1 neid', function(){
      cy.contains('共 0 条')
      cy.contains('button', '新增').click()
      cy.contains('共 1 条')
      cy.FilterSelectValue('[data-cy=popId]',testServiceBody.testSTSaas1Body.hostName)
      cy.ClickSelectValue('[data-cy=popType]',testServiceBody.testSTSaas1Body.service)
      cy.ClickSelectValue('div.el-select.el-select--small[data-cy="preferPop"]',testServiceBody.testSTSaas1Body.prefer_pop_id)
      cy.contains('button', '确认').click()
      cy.contains('更新成功') 

    })


    if (testServiceBody.hasOwnProperty('testSTAnycast1Body')) {
        it('config anycast1 neid', function () {
            cy.contains('共 1 条')
            cy.contains('button', '新增').click()
            cy.contains('共 2 条')
            cy.FilterSelectValue('[data-cy=popId]', testServiceBody.testSTAnycast1Body.hostName)
            cy.ClickSelectValue('[data-cy=popType]', testServiceBody.testSTAnycast1Body.service)
            cy.ClickSelectValue('div.el-select.el-select--small[data-cy="preferPop"]', testServiceBody.testSTAnycast1Body.prefer_pop_id)
            cy.contains('button', '确认').click()
            cy.contains('更新成功')

        })
    }

    if (testServiceBody.hasOwnProperty('testSTSaas2Body')) {
        it('config saas2 neid', function () {
            cy.contains('共 2 条')
            cy.contains('button', '新增').click()
            cy.contains('共 3 条')
            cy.FilterSelectValue('[data-cy=popId]', testServiceBody.testSTSaas2Body.hostName)
            cy.ClickSelectValue('[data-cy=popType]', testServiceBody.testSTSaas2Body.service)
            cy.ClickSelectValue('div.el-select.el-select--small[data-cy="preferPop"]', testServiceBody.testSTSaas2Body.prefer_pop_id)
            cy.contains('button', '确认').click()
            cy.contains('更新成功')

        })
    }

})
