import {getToken,visitAndSetPageUserInfo,rowContains,checkTableLineNumber,ClickRow,searchTable,changeToGlobalView} from '../utils/web-utils'
import {exec_cmd_on_local,checkPopInfoWithConsul,checkPopStatusWithConsul,add_server_port, del_server_port, checkDeviceDeleted} from '../utils/consulCheck-utils'
import {testPopBody, putTestPopBody, putTestPop2Body,PopTypeForward,testServiceBody, PopTypeSaas, PopTypeAnycast} from '../utils/variables-utils.js'
import {deletePopByPopId, createPOP, getPopNEidByPopId,getLogsNumber} from '../utils/basic-utils'

export function checkPopIpAdresses(popInfo) {
  ClickRow('[data-cy=popConfigs]',popInfo.hostName,0)
  popInfo.ipAddress.forEach(checkPopIpAdress)
}

function checkPopIpAdress(ipAddress){
  rowContains('[data-cy=popIpList]',ipAddress.publicAddress,1,4,[ipAddress.isp,ipAddress.ispCode,ipAddress.iface,ipAddress.nat])
}

function checkPopCpesInfo(cpeNum,cpeInfo){
  cy.get('.el-popover').filter('[aria-hidden="false"]').within(() => {
    cy.get('table').eq(1).within(() => {
     for (var i=0; i < cpeNum; i++) {
         for (var j=0; j < 4; j++) {
           cy.get('tr').eq(i).children('td').eq(j).contains(cpeInfo[i][j])
         }
     }
    })
  })
}


function filterTag(tag){
  cy.get('[data-cy=popConfigs]').contains('标签').parents('th').click()
  cy.get('[role=group]').within(() => {
  cy.checkGroupCheckBoxWithLable(tag)
  })
  cy.contains('筛选').click({force: true})
}

before(function () {
  getToken()
  exec_cmd_on_local("bash /e2e/RoaringDog/test/prepPoptest.sh")
    cy.reload()
 })

describe('Pop page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/pop',this.info)
    changeToGlobalView("pop",this.info)
   })

    it('check pop list num and info', function(){
      // checkTableLineNumber(2)
      rowContains('[data-cy=popConfigs]',testPopBody.testPop1Body.hostName,5,6,[testPopBody.testPop1Body.cpeNum])
      ClickRow('[data-cy=popConfigs]',testPopBody.testPop1Body.hostName,5)
      checkPopCpesInfo(testPopBody.testPop1Body.cpeNum,testPopBody.testPop1Body.cpes)
      ClickRow('[data-cy=popConfigs]',testPopBody.testPop1Body.hostName,1)
      rowContains('[data-cy=popConfigs]',testPopBody.testPop2Body.hostName,5,6,[testPopBody.testPop2Body.cpeNum])
      ClickRow('[data-cy=popConfigs]',testPopBody.testPop2Body.hostName,5)
      checkPopCpesInfo(testPopBody.testPop2Body.cpeNum,testPopBody.testPop2Body.cpes)
      checkPopIpAdresses(testPopBody.testPop1Body)
      checkPopIpAdresses(testPopBody.testPop2Body)
    })
  

    it('pop list support search,filter', function(){
      checkTableLineNumber(2)
      filterTag('node.dpdk')
      checkTableLineNumber(1)
      searchTable('popSearch',testPopBody.testPop1Body.hostName)
      checkTableLineNumber(1)
      searchTable('popSearch',testPopBody.testPop1Body.ipAddress[0].publicAddress)
      checkTableLineNumber(1)
      rowContains('[data-cy=popConfigs]',testPopBody.testPop1Body.hostName,2,3,[testPopBody.testPop1Body.hostName])
    })

    it('config pop neid and cac eac', function(){
       cy.get('[data-cy=addPop]').click()
       cy.contains('共 3 条')
       cy.ClickSelectValue('[data-cy=popId]',testPopBody.testPopBody.hostName)
       cy.get('[data-cy=cac]').type(testPopBody.testPopBody.cac)
       cy.get('[data-cy=eac]').type(testPopBody.testPopBody.eac)
       cy.ClickSelectValue('[data-cy=routeCodeTypeSelect]','ER')
       cy.contains('button', '确认').click()
       cy.contains('更新成功') 
       checkPopInfoWithConsul(this.info.token,testPopBody.testPopBody.popId,PopTypeForward)
       searchTable('popSearch','11.1.1.2')
       cy.get('td').eq(1).click()
       cy.ClickDropDownValue('[data-cy=popDropdown]','[data-cy=popDropdown4]','维护态')   
       checkPopStatusWithConsul(this.info.token,testPopBody.testPopBody.popId,PopTypeForward, 'MAINTENANCE')
       getPopNEidByPopId(this.info.token,testPopBody.testPopBody.popId,PopTypeForward)
       cy.get('@neId').then(neId => {
         expect(neId).to.not.equal("")
         cy.wrap(neId).as('tmp_neId')
       })
      cy.get('[data-cy=popConfigs]').contains(testPopBody.testPopBody.hostName).parents('tr').within(() => {
        cy.contains('button', '编辑').should('not.exist')
        cy.contains('button', '删除').click()
      })
      cy.contains('button', '确定').click()
      cy.get('@tmp_neId').then(tmp_neId => {
        expect(tmp_neId).to.not.equal("")
        checkDeviceDeleted(tmp_neId)
      })
      //check the operation log of pop
      getLogsNumber(this.info.token,{resourceType:'pop',action:'add',company:'all',username:'admin'})
      cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(1)})
      getLogsNumber(this.info.token,{resourceType:'pop',action:'del',company:'all',username:'admin'})
      cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(1)})
      getLogsNumber(this.info.token,{resourceType:'pop',action:'update',company:'all',username:'admin'})
      cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(1)})
    })

    it('resource center change info reload web', function(){
      add_server_port()
      cy.reload()
      searchTable('popSearch','13.1.1.3')
      checkTableLineNumber(1)
      del_server_port()
      cy.reload()
      searchTable('popSearch','13.1.1.3')
      checkTableLineNumber(0)
    }) 
})

