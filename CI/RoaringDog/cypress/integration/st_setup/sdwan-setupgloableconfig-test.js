import {changeToGlobalView, getToken,visitAndSetPageUserInfo} from '../utils/web-utils'
import {testCPEGlobalConfigBody} from '../utils/variables-utils.js'
import {createGlobalConfig, modifyCPEGlobalConfig} from '../utils/basic-utils'

const globalConfigBody = {"regUrl":"","authUrl":"","collectdAddr":"","collectdPort":"","salt":"","controllers":[]}

before(function () {
  getToken() 
  cy.get('@info').then(t_info => {
    createGlobalConfig(t_info.token,globalConfigBody)
  })
 })

describe('service page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/controller',this.info)
    cy.reload()
    changeToGlobalView("controller",this.info)
    cy.wait(2000)
   })

    it('config cpe global config', function(){
      modifyCPEGlobalConfig(testCPEGlobalConfigBody.ST)
    })

})
