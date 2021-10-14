import {createManager, createOpenflow,createNetAlg, modifyCPEGlobalConfig,createGlobalConfig} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeToGlobalView} from '../utils/web-utils'
import {testManagerBody, testOpenflowBody,testNetAlgBody,testCPEGlobalConfigBody, testGlobalConfigBody} from '../utils/variables-utils'
import {checkGaeaServiceWithConsul, checkGlobalConfigNeWithConsul} from '../utils/consulCheck-utils'


export function addManager(managers){
  cy.get('[data-cy="managersForm"]').within(() => {  
    managers.global.forEach(global => {
      cy.get('[data-cy="addManagerGlobal"]').click()
      cy.get('[data-cy="managersIp"]').last().clear().type(global.ip)
      cy.get('[data-cy="managersPort"]').last().clear().type(global.port)
    })
  })
  for(var spKey in managers.specific){
    cy.get('[data-cy="addManagerNe"]').click()
    cy.get('[data-cy="inputManagerNeid"]').clear().type(spKey)
    cy.get('[data-cy="confirmInputManagerNeid"]').click()
    cy.contains('Neid('+spKey).click()
    cy.contains('Neid('+spKey).parent('div').parent('div').within(()=>{
      cy.get('[data-cy="deleteManagerSpecificIp"]').click()
    })
    managers.specific[spKey].forEach(sp => {
      cy.contains('Neid('+spKey).within(()=>{
        cy.get('[data-cy="handelManager"]').click()
      })
      cy.get('[data-cy="managerDropdown"]:visible').contains('添加地址').click({force: true})
      cy.contains('Neid('+spKey).parent('div').parent('div').within(()=>{
        cy.get('[data-cy="managerSpecificIp"]').last().clear().type(sp.ip)
        cy.get('[data-cy="managerSpecificPort"]').last().clear().type(sp.port)
      })
    })
  }
  cy.get('[data-cy="managerUpdate"]').click()
} 

export function addOpenflow(openflows){
  cy.get('[data-cy="openFlowForm"]').within(() => {  
    openflows.global.forEach(global => {
      cy.get('[data-cy="addOpenflowG"]').click()
      cy.get('[data-cy="openFlowIp"]').last().clear().type(global.ip)
      cy.get('[data-cy="openFlowPort"]').last().clear().type(global.port)
    })
  })
  for(var spKey in openflows.specific){
    cy.get('[data-cy="addOpenflowNe"]').click()
    cy.get('[data-cy="inputOpenflowNeid"]').clear().type(spKey)
    cy.get('[data-cy="cancelInputOpenflowNeid"]').contains('确 定').click()
    cy.contains('Neid('+spKey).click()
    cy.contains('Neid('+spKey).parent('div').parent('div').within(()=>{
      cy.get('[data-cy="deleteOpenflowSIp"]').click()
    })
    openflows.specific[spKey].forEach(sp => {
      cy.contains('Neid('+spKey).within(()=>{
        cy.get('[data-cy="handelOpenflow"]').click()
      })
      cy.get('[data-cy="openFlowDrop"]:visible').contains('添加地址').click({force: true})
      cy.contains('Neid('+spKey).parent('div').parent('div').within(()=>{
        cy.get('[data-cy="openFlowSip"]').last().clear().type(sp.ip)
        cy.get('[data-cy="openFlowSport"]').last().clear().type(sp.port)
      })
    })
  }
  cy.get('[data-cy="updateOpenflow"]').click()
} 

export function addSaasSearchPattern(saasSearchPattern){
  saasSearchPattern.forEach(ssp => { 
    cy.get('[data-cy="saasPatternAddArea"]').click()
    cy.contains("请输入区域码").parent('div').parent('div').parent('div').parent('div').within(() => {
      cy.get('input').clear().type(ssp.code)
      cy.get('button').contains("确定").click()
    })
    ssp.services.forEach(srvs =>{
      cy.contains('区域码('+ssp.code).click()
      cy.contains('区域码('+ssp.code).within(()=>{
        cy.get('[data-cy="saasPatternDrop"]').click()
      })
      cy.get('[data-cy="saasPatternDropdown"]:visible').contains('添加Pop').click({force: true})
      cy.get('[data-cy="saasPatternSelectPop"]').click()
      cy.get('[class="el-scrollbar"]').contains('dpdk').click()
      cy.get('[data-cy="saasPatternInputNeid"]').click()
      cy.get('[class="el-scrollbar"]').contains(srvs.neId).click()
      cy.get('[data-cy="saasPatternServiceId"]').click()
      cy.get('[class="el-scrollbar"]:visible').contains(srvs.serviceId).click()
      cy.get('[data-cy="saasPatternConfirm"]').click()  
    })
    ssp.proxyServices.forEach(prs=>{
      cy.contains('区域码('+ssp.code).click()
      cy.contains('区域码('+ssp.code).within(()=>{
        cy.get('[data-cy="saasPatternDrop"]').click()
      })
      cy.get('[data-cy="saasPatternDropdown"]:visible').contains('添加Pop').click({force: true})
      cy.get('[data-cy="saasPatternSelectPop"]').click()
      cy.get('[class="el-scrollbar"]').contains('world').click()
      cy.get('[data-cy="saasPatternInputNeid"]').click()
      cy.get('[class="el-scrollbar"]:visible').contains(prs).click()
      cy.get('[data-cy="saasPatternConfirm"]').click()  
    })
  })
  cy.get('[data-cy="saasPatternUpdate"]').click()
}

export function inputValueByDatacy(datacy,value){
  cy.get(datacy).within(() => {
    cy.get('input').clear().type(value)
  })
}

export function modifyNetAlg(netconfig){
  inputValueByDatacy('[data-cy="netAlgConfigUpperBandwidth"]',netconfig.upperBandwidth.toString())
  inputValueByDatacy('[data-cy="netAlgConfigLowerBandwidth"]',netconfig.lowerBandwidth.toString())
  inputValueByDatacy('[data-cy="netAlgConfigUpperBwPercent"]',netconfig.upperBwPercent.toString())
  inputValueByDatacy('[data-cy="netAlgConfigLowerBwPercent"]',netconfig.lowerBwPercent.toString())
  inputValueByDatacy('[data-cy="netAlgConfigMaxLossIn15Min"]',netconfig.maxLossIn15Min.toString())
  inputValueByDatacy('[data-cy="netAlgConfigAvgLossIn60Min"]',netconfig.avgLossIn60Min.toString())
  inputValueByDatacy('[data-cy="netAlgConfigMaxLossRatio"]',netconfig.maxLossRatio.toString())
  inputValueByDatacy('[data-cy="netAlgConfigForwardingCost"]',netconfig.forwardingCost.toString())
  inputValueByDatacy('[data-cy="netAlgConfigWeightCoefficient"]',netconfig.weightCoefficient.toString())
  cy.get('[data-cy="netAlgConfigUpdate"]').click()
}

export function checkValueByDatacy(datacy,value){
  cy.get(datacy).within(() => {
    cy.get('input').should('have.value',value)
  })
}

export function checkNetConfig(netconfig){
  checkValueByDatacy('[data-cy="netAlgConfigUpperBandwidth"]',netconfig.upperBandwidth.toString())
  checkValueByDatacy('[data-cy="netAlgConfigLowerBandwidth"]',netconfig.lowerBandwidth.toString())
  checkValueByDatacy('[data-cy="netAlgConfigUpperBwPercent"]',netconfig.upperBwPercent.toString())
  checkValueByDatacy('[data-cy="netAlgConfigLowerBwPercent"]',netconfig.lowerBwPercent.toString())
  checkValueByDatacy('[data-cy="netAlgConfigMaxLossIn15Min"]',netconfig.maxLossIn15Min.toString())
  checkValueByDatacy('[data-cy="netAlgConfigAvgLossIn60Min"]',netconfig.avgLossIn60Min.toString())
  checkValueByDatacy('[data-cy="netAlgConfigMaxLossRatio"]',netconfig.maxLossRatio.toString())
  checkValueByDatacy('[data-cy="netAlgConfigForwardingCost"]',netconfig.forwardingCost.toString())
  checkValueByDatacy('[data-cy="netAlgConfigWeightCoefficient"]',netconfig.weightCoefficient.toString())
}

export function checkSaasSearchPattern(searchPattern){
  searchPattern.forEach(sp => {
    cy.contains('区域码(' + sp.code + ')').click()
    cy.contains('区域码(' + sp.code + ')').parent('div').parent('div').within(()=>{
      cy.get('[class="el-row"]').should('have.length',sp.services.length + sp.proxyServices.length)
    })
  })
}

export function checkManagerAndOpenflow(managers,openflows){
  cy.get('[data-cy="managersIp"]').should('have.length', managers.global.length)
  cy.get('[data-cy="openFlowIp"]').should('have.length', openflows.global.length)
}

export function deleteManager(managers){
  cy.get('[data-cy="managersForm"]').within(() => {  
    managers.global.forEach(() => {
      cy.get('[data-cy="deleteManagerGlobal"]').last().click()
    })
  })
  for(var spKey in managers.specific){
    managers.specific[spKey].forEach(sp => {
      cy.contains('Neid('+spKey).within(()=>{
        cy.get('[data-cy="handelManager"]').click()
      })
      cy.get('[data-cy="managerDropdown"]:visible').contains('删除网元').click()
    })
  }
  cy.get('[data-cy="managerUpdate"]').click()
}

export function deleteOpenflow(openflows){
  cy.get('[data-cy="openFlowForm"]').within(() => {  
    openflows.global.forEach(() => {
      cy.get('[data-cy="deleteOpenflowG"]').last().click()
    })
  })
  for(var spKey in openflows.specific){
    openflows.specific[spKey].forEach(sp => {
      cy.contains('Neid('+spKey).within(()=>{
        cy.get('[data-cy="handelOpenflow"]').click()
      })
      cy.get('[data-cy="openFlowDrop"]:visible').contains('删除网元').click()
    })
  }
  cy.get('[data-cy="updateOpenflow"]').click()
}

export function deleteSaasSearchPattern(saasSearchPattern){
  saasSearchPattern.forEach(ssp => { 
    cy.contains('区域码('+ssp.code).within(()=>{
      cy.get('[data-cy="saasPatternDrop"]').click()
    })
    cy.get('[data-cy="saasPatternDropdown"]:visible').contains('删除').click()
  })
  cy.get('[data-cy="saasPatternUpdate"]').click()
}

before(function () {
  getToken() 
  cy.get('@info').then(t_info => {
    createManager(t_info.token,testManagerBody.basic)
    createOpenflow(t_info.token,testOpenflowBody.basic)
    createNetAlg(t_info.token,testNetAlgBody.default)
    createGlobalConfig(t_info.token,testGlobalConfigBody.default)
  })
 })

describe('controller test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/controller',this.info)
    cy.reload()
    changeToGlobalView("controller",this.info)
   })
    
    it('correct show controller test', function(){
      //check page show the correct manager and openflow info
      checkManagerAndOpenflow(testManagerBody.basic,testOpenflowBody.basic)
      checkNetConfig(testNetAlgBody.default)
    })

    it('config controller test', function(){
      addManager(testManagerBody.add)
      addOpenflow(testOpenflowBody.add)
      modifyNetAlg(testNetAlgBody.edit)
      checkGaeaServiceWithConsul()
    })

    it('delete controller test', function(){
      deleteManager(testManagerBody.basic)
      deleteOpenflow(testOpenflowBody.basic)
    })

    it('config globalconfigNe test', function(){
      modifyCPEGlobalConfig(testCPEGlobalConfigBody.ST)
      checkGlobalConfigNeWithConsul()
    })
})