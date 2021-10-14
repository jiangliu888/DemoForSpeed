import {deletePopByPopId,putPop,createSaasSearchPatternByCode,getPopNEidByPopId} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, searchArea, searchPop, checkPopList, checksearchPopNum, addPoptoCode, changeToGlobalView} from '../utils/web-utils'
import {testServiceBody,popBody,saasSearchPatternBody, PopTypeSaas, PopTypeAnycast} from '../utils/variables-utils'
import {checkSearchPatternWithConsul} from '../utils/consulCheck-utils'


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
  getToken() 
  cy.get('@info').then(t_info => {
    deletePopByPopId(t_info.token,testServiceBody.putAnycastBody.popId,PopTypeAnycast)
    deletePopByPopId(t_info.token,testServiceBody.putAnycastBody2.popId,PopTypeAnycast)
    deletePopByPopId(t_info.token,testServiceBody.putSaasBody.popId,PopTypeSaas)
    deletePopByPopId(t_info.token,popBody.testpop2.popId)
    deletePopByPopId(t_info.token,popBody.testpop3.popId)
    deletePopByPopId(t_info.token,popBody.testpop.popId)
    putPop(t_info.token,popBody.testpop2)
    putPop(t_info.token,popBody.testpop3)
    putPop(t_info.token,popBody.testpop)
    putPop(t_info.token,testServiceBody.putAnycastBody)
    putPop(t_info.token,testServiceBody.putAnycastBody2)
    putPop(t_info.token,testServiceBody.putSaasBody)
    createSaasSearchPatternByCode(t_info.token,saasSearchPatternBody.hubeiCode.areaCode,saasSearchPatternBody.hubeiCode)
    createSaasSearchPatternByCode(t_info.token,saasSearchPatternBody.shanghaiCode.areaCode,saasSearchPatternBody.shanghaiCode)
  })
 })

describe('areaCode test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/areaCode',this.info)
    changeToGlobalView("areaCode",this.info)
   })
    
    it('correct search about areaCode', function(){
      //check consul
      checkSearchPatternWithConsul(saasSearchPatternBody.hubeiCode.areaCode)
      //by areaCode and district
      searchArea(saasSearchPatternBody.hubeiCode.areaCode)
      checkSearchResult(saasSearchPatternBody.hubeiCode.areaCode)
      checkSearchResultLength(1)
      searchArea(saasSearchPatternBody.hubeiCode.districtDes)
      checkSearchResult(saasSearchPatternBody.hubeiCode.districtDes)
      checkSearchResultLength(1)
      //by pop info
      searchArea(testServiceBody.putSaasBody.ips[0].public_ip)
      checkSearchResult(saasSearchPatternBody.hubeiCode.areaCode)
      checkSearchResult(saasSearchPatternBody.shanghaiCode.areaCode)
      checkSearchResultLength(2)
      getPopNEidByPopId(this.info.token,testServiceBody.putAnycastBody.popId)
      cy.get('@neId').then(neId => {
        if(neId != ""){
          searchArea(neId)
          checkSearchResult(saasSearchPatternBody.hubeiCode.areaCode)
          checkSearchResult(saasSearchPatternBody.shanghaiCode.areaCode)
          checkSearchResultLength(2)
        }
      })
    })

    it('batch delete service when modify areaCode', function(){
      //batch delete pop
      searchArea(saasSearchPatternBody.hubeiCode.areaCode)
      cy.get('[data-cy="popConfigs"]').contains(saasSearchPatternBody.hubeiCode.areaCode).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
      })
      cy.url().should('contain', 'serviceDetail')
      cy.contains(testServiceBody.putAnycastBody2.hostname).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.contains("更新成功")
      //consulCheck
      cy.contains("主机名").parents('tr').within(() => {
        cy.get('.el-checkbox').click()
      })
      cy.contains('button', '批量删除').click()
      cy.contains('button', '确定').click()
      cy.contains("删除成功")
      //consulCheck
    })

    it('route to service page when modify areaCode and show service', function(){
      //add pop
      searchArea(saasSearchPatternBody.shanghaiCode.areaCode)
      cy.get('[data-cy="popConfigs"]').contains(saasSearchPatternBody.shanghaiCode.areaCode).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
      })
      cy.url().should('contain', 'serviceDetail')
      cy.contains(testServiceBody.putSaasBody.hostname).parents('tr').within(() => {
        cy.get('i.el-icon-info').click()
      })
      cy.url().should('contain', 'service')
      cy.contains("服务管理")
    })

    it('add pop when modify areaCode support search', function(){
      //add pop
      searchArea(saasSearchPatternBody.shanghaiCode.areaCode)
      cy.get('[data-cy="popConfigs"]').contains(saasSearchPatternBody.shanghaiCode.areaCode).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
      })
      cy.url().should('contain', 'serviceDetail')
      cy.contains('button', '添加').click()
      searchPop(testServiceBody.putAnycastBody2.ips[0].public_ip)
      checkPopList(testServiceBody.putAnycastBody2.hostname)
      checksearchPopNum(1)
      searchPop(testServiceBody.putAnycastBody.hostname)
      checkPopList(testServiceBody.putAnycastBody2.hostname)
      checkPopList(testServiceBody.putAnycastBody.hostname)
      checksearchPopNum(2)
      addPoptoCode()
      checkSearchPatternWithConsul(saasSearchPatternBody.shanghaiCode.areaCode)
    })
})