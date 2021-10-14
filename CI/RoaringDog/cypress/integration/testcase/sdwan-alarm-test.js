import {createAlertGroup, createAlertRule, createCompanyByData, deleteAllAlertGroup, deleteAllAlertRule, deleteCompanyByName} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView, changeToGlobalView, changeAlarmPanelView,setAlertRule,setAlertGroup,modifyAlertGroup} from '../utils/web-utils'
import {exec_cmd_on_local} from '../utils/consulCheck-utils'
import {alert, alertBody} from '../utils/variables-utils'


before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
  //删除公司
  cy.get('@company').then(company => {
    cy.get('@site').then(site => {
      cy.get('@info').then(t_info => {
        deleteAllAlertRule(t_info.token,'all')
        deleteAllAlertGroup(t_info.token,'all')
        exec_cmd_on_local("bash /e2e/RoaringDog/test/prepAlarmtest.sh")
        createAlertGroup(t_info.token,'all',alertBody.alertGroup)
        cy.get('@AlertGroupId').then(AlertGroupId => {
          createAlertRule(t_info.token,'all',alertBody.alertRule,AlertGroupId)
        })
        deleteCompanyByName(t_info.token,company.testCompanyAlarm.name)
        createCompanyByData(t_info.token,company.testCompanyAlarm)
        cy.reload()
      }) 
    })
    }) 
})

describe('alarm page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/alarm',this.info)
    changeToGlobalView("alarm",this.info)
   })

    it('create and delete alertGroup', function(){
      changeAlarmPanelView("告警组设置")
      cy.get('[data-cy=addReceiver]').filter(':visible').click()
      setAlertGroup(alert.alertGroup)
      cy.contains("创建成功")
      cy.get('[data-cy="alarmConfig"]').contains(alert.alertGroup.name).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("确定").click()
      cy.contains("操作成功")
    })

    it('create and delete alertRule', function(){
      changeAlarmPanelView("告警规则设置")
      cy.get('[data-cy=addReceiver]').filter(':visible').click()
      setAlertRule(alert.alertRule)
      cy.contains("创建成功")
      cy.get('[data-cy="alertRules"]').contains(alert.alertRule.alertGroup[0]).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("确定").click()
      cy.contains("操作成功")
    })

    it('modify alert group test', function(){
      changeAlarmPanelView("告警组设置")
      cy.get('[data-cy="alarmConfig"]').contains(alertBody.alertGroup.name).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      let user = {"userName":"modifyalertUser1","email":"modifyalert1@alert.com","mobile":"13344444446"}
      modifyAlertGroup(user)
      cy.contains("更新成功")
    })

    it('modify alert rule test', function(){
      changeAlarmPanelView("告警规则设置")
      cy.get('[data-cy="alertRules"]').contains(alert.alertRule.alertGroup[0]).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      alert.alertRule.alertGroup = [], alert.alertRule.alertType = ["CPE设备故障","CPE业务异常","CPE网络异常","CPE配置错误"],alert.alertRule.severity = ["紧急"]
      setAlertRule(alert.alertRule)
      cy.contains("更新成功")
    })

    it('correct show alert', function(){
      cy.contains('共 2 条')
      cy.contains('NodeOffline')
      cy.contains('CpeHardwareError')
      changeAlarmPanelView("告警日志")
      cy.contains('共 1 条')
      changeSiteCompanyView(this.company.testCompanyAlarm.name)
      cy.contains('共 0 条')
    })

})
