import {deleteCompanyByName, deleteAllUnions,deleteAllSites, createCompanyByData, createSiteByData,deleteAllUsers,createUser,createUnion} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView} from '../utils/web-utils'
import {UserBody,ReportTestBody} from '../utils/variables-utils'
import {emptyDownloadsDir,customerNameCheck,serviceItemCheck,exportSuccessCheck,serviceOverviewCheck,deviceStatusCheck,serviceQualityCheck,ticketDetailCheck} from '../utils/reportCheck-utils'
import {exec_cmd_on_host, exec_cmd_on_local} from '../utils/consulCheck-utils'


function createNormalUser(username,pswd,company,token){
  var body = UserBody.userRoleUser
  body['username'] = username
  body['password'] = pswd
  body['company'] = company
  createUser(token,body)
}

function createAdminsUser(username,pswd,company,token){
  var body = UserBody.adminRoleUser
  body['username'] = username
  body['password'] = pswd
  body['company'] = company
  createUser(token,body)
}

function exportCurMonthReport(){
  cy.reload()
  cy.get('[data-cy=time]').click()
  cy.get('li').contains('月').click()
  cy.get('input[placeholder=选择月]').click()
  cy.get('.el-month-table').find('.today').click()
  cy.contains('button','导出报表').click()
  cy.wait(3000)
}

function exportPreMonthReport(){
  cy.reload()
  cy.get('[data-cy=time]').click()
  cy.get('li').contains('月').click()
  cy.get('input[placeholder=选择月]').click()
  cy.get('.el-month-table').find('.today').prev().click()
  cy.get('.el-month-table').should('not.be.visible')
  cy.contains('button','导出报表').click()
  cy.wait(3000)
  
}

function exportCurWeekReport(){
  cy.reload()
  cy.get('[data-cy=time]').click() 
  cy.get('li').contains('周').click()
  cy.get('.el-date-editor').click()
  cy.get('.is-week-mode > tbody').find('.current').next().click()
  cy.contains('button','导出报表').click()
  cy.wait(3000)
}

function exportPreWeekReport(){
  cy.reload()
  cy.get('[data-cy=time]').click()
  cy.get('li').contains('周').click()
  cy.get('.el-date-editor').click()
  cy.get('.is-week-mode > tbody').find('.current').click()
  cy.get('.is-week-mode').should('not.be.visible')
  cy.contains('button','导出报表').click()
  cy.wait(5000)
}

function changeSiteProperty(site,city,bandwidth){
  cy.get('td').contains(site).parents('tr').find('td').last().find('button').contains('编辑').click()
  cy.get('input[placeholder=选择城市]').eq(1).parent('div').click({force: true}).within(()=>{
    cy.get('.el-input__icon').click({force: true})
  })    
  cy.get('input[placeholder=选择城市]').eq(1).type(city)
  cy.get('.el-cascader__suggestion-item').contains(city).click()
  cy.get('[data-cy=speedLimit]').find('input').clear().type(bandwidth)
  cy.contains('确 定').click()
  cy.contains('确定').click()
}

export function changeToGlobalMode(){
    cy.get('div[class=right-menu]',{ timeout: 15000 }).then((div) => {
      if (div.find('span > .el-icon-arrow-up').length > 0) {
        cy.get('div > .el-dropdown').eq(0).click({force: true})
        cy.contains('全局模式').click({ force: true })
      }
    })
  }

before(function () {
    cy.fixture("companies/companies.json").as('company')
    cy.fixture("companies/sites/sites.json").as('site')
    getToken()
    //删除公司
    cy.get('@company').then(company => {
      cy.get('@site').then(site => {
        cy.get('@info').then(t_info => { 
          deleteAllUnions(t_info.token,company.testCompanyReportForm.name)
          deleteAllSites(t_info.token,company.testCompanyReportForm.name)        
          deleteAllUsers(t_info.token,company.testCompanyReportForm.name)
          deleteCompanyByName(t_info.token,company.testCompanyReportForm.name)
          createCompanyByData(t_info.token,company.testCompanyReportForm)
          // admins user
          createAdminsUser('test1@subao.com','test11!',company.testCompanyReportForm.name,this.info.token)
          // normal user
          createNormalUser('test2@subao.com','test22!',company.testCompanyReportForm.name,this.info.token)                      
          cy.reload()
        }) 
      })
    }) 
  })


describe('reportForm page test', function() {
    beforeEach(function () {
     deleteAllUnions(this.info.token,this.company.testCompanyReportForm.name)
     deleteAllSites(this.info.token,this.company.testCompanyReportForm.name)
     createSiteByData(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite1Body)
     createSiteByData(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite2Body)
     createSiteByData(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite3Body)
     createSiteByData(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite4Body)
     visitAndSetPageUserInfo('/reportFormPage',this.info)
     changeSiteCompanyView(this.company.testCompanyReportForm.name)
     emptyDownloadsDir()
    })
     //SDWANDEV-4614
     it('reportForm authority check', function(){
        changeToGlobalMode()
        cy.contains('报表').should('not.exist')
        changeSiteCompanyView(this.company.testCompanyReportForm.name)
        cy.contains('报表')
        visitAndSetPageUserInfo('/roleManage',this.info)
        cy.get('td').contains('admins').parents('tr').find('td').last().contains('button','编辑').click()
        cy.contains('.el-tree-node__label','统计报表').prev().should('have.class','is-checked')
        cy.contains('button','确认').click({force:true})
        cy.get('td').contains('users').parents('tr').find('td').last().contains('button','编辑').click()
        cy.contains('.el-tree-node__label','统计报表').prev().should('not.have.class','is-checked')
        cy.contains('button','确认').click({force:true})       
        cy.logout()
        // admins account login
        cy.typeLogin('test1@subao.com','test11!')
        cy.contains('报表').should('exist')
        cy.logout()
        // users account login
        cy.typeLogin('test2@subao.com','test22!')
        cy.contains('报表').should('not.exist')
     })
     //	SDWANDEV-4615
     it('export reportform per month&week', function(){
         // export current month report
         exportCurMonthReport()
         exportSuccessCheck()
         // export last month report
         emptyDownloadsDir()
         exportPreMonthReport()
         exportSuccessCheck()
         // next month can't be choosen
         cy.get('input[placeholder=选择月]').click()
         cy.get('.el-month-table').find('.today').parent().next().find('td').eq(0).click()
         cy.get('.el-month-table').should('be.visible')
         // export current week report
         emptyDownloadsDir()
         exportCurWeekReport()
         exportSuccessCheck()
         // export last week report
         emptyDownloadsDir()
         exportPreWeekReport()
         exportSuccessCheck()    
         // next week can't be choosen
         cy.get('.el-date-editor').click()
         cy.get('.is-week-mode').find('.current').next().click()
         cy.get('.is-week-mode').should('be.visible')      
     })
     //	SDWANDEV-4632
     it('customer name check',function(){
      // current month report
      exportCurMonthReport()
      customerNameCheck(this.company.testCompanyReportForm.name)
      })
    //	SDWANDEV-4616
     it('Acceleration type check',function(){
      // export current month report
      exportCurMonthReport()
      serviceItemCheck('加速类型','SAAS加速')
      // create union
      createUnion(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite1Body.name,this.site.ReportSite2Body.name)
      emptyDownloadsDir()
      // export current month report
      exportCurMonthReport()
      serviceItemCheck('加速类型','分支组网')
     })
     //SDWANDEV-4626
     it('saas mode month report data check',function(){
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastmonth" + " " + this.site.ReportSite1Body.name + " " + this.site.ReportSite1Body.sn[0])
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastmonth" + " " + this.site.ReportSite2Body.name + " " + this.site.ReportSite2Body.sn[0])      
      // export current month report    
      exportCurMonthReport()
      let tmp = ReportTestBody.service_overview
      tmp['部署设备数'] = '4'
      tmp['新增设备数'] = '2' 
      let data = JSON.stringify(tmp)
      let ds = escape(data) 
      // service and device check    
      serviceOverviewCheck(ds)
      let tmp_2 =  JSON.parse(JSON.stringify(ReportTestBody.device_status))
      tmp_2[this.site.ReportSite1Body.name][3] = '否'
      tmp_2[this.site.ReportSite2Body.name][3] = '否'
      let data_2 = JSON.stringify(tmp_2)
      let ds_2 = escape(data_2)   
      deviceStatusCheck(ds_2)
      // export last month report
      emptyDownloadsDir()
      exportPreMonthReport()
      let tmp_1 = ReportTestBody.service_overview
      tmp_1['部署设备数'] = '2'
      tmp_1['新增设备数'] = '2' 
      let data_1 = JSON.stringify(tmp_1)
      let ds_1 = escape(data_1) 
      // service and device check    
      serviceOverviewCheck(ds_1)
      let tmp_3 =  JSON.parse(JSON.stringify(ReportTestBody.device_status))
      tmp_3[this.site.ReportSite1Body.name][3] = '是'
      tmp_3[this.site.ReportSite2Body.name][3] = '是'
      delete tmp_3[this.site.ReportSite3Body.name]
      delete tmp_3[this.site.ReportSite4Body.name]
      let data_3 = JSON.stringify(tmp_3)
      let ds_3 = escape(data_3)   
      deviceStatusCheck(ds_3)    
     })
     //	SDWANDEV-4648
     it('saas mode week report data check',function(){
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastweek" + " " + this.site.ReportSite1Body.name + " " + this.site.ReportSite1Body.sn[0])
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastweek" + " " + this.site.ReportSite2Body.name + " " + this.site.ReportSite2Body.sn[0])
      // export current week report  
      exportCurWeekReport()
      let tmp = ReportTestBody.service_overview
      tmp['部署设备数'] = '4'
      tmp['新增设备数'] = '2' 
      let data = JSON.stringify(tmp)
      let ds = escape(data) 
      // service and device check    
      serviceOverviewCheck(ds)
      let tmp_2 =  JSON.parse(JSON.stringify(ReportTestBody.device_status))
      tmp_2[this.site.ReportSite1Body.name][3] = '否'
      tmp_2[this.site.ReportSite2Body.name][3] = '否'
      let data_2 = JSON.stringify(tmp_2)
      let ds_2 = escape(data_2)   
      deviceStatusCheck(ds_2)
      // export last week report
      emptyDownloadsDir()
      exportPreWeekReport()
      let tmp_1 = ReportTestBody.service_overview
      tmp_1['部署设备数'] = '2'
      tmp_1['新增设备数'] = '2' 
      let data_1 = JSON.stringify(tmp_1)
      let ds_1 = escape(data_1) 
      // service and device check    
      serviceOverviewCheck(ds_1)
      let tmp_3 =  JSON.parse(JSON.stringify(ReportTestBody.device_status))
      tmp_3[this.site.ReportSite1Body.name][3] = '是'
      tmp_3[this.site.ReportSite2Body.name][3] = '是'
      delete tmp_3[this.site.ReportSite3Body.name]
      delete tmp_3[this.site.ReportSite4Body.name]
      let data_3 = JSON.stringify(tmp_3)
      let ds_3 = escape(data_3)   
      deviceStatusCheck(ds_3)    
     })
     //	SDWANDEV-4627
     it('office mode month report data check',function(){
      // export current month report 
      createUnion(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite1Body.name,this.site.ReportSite2Body.name)
      createUnion(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite3Body.name,this.site.ReportSite4Body.name) 
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastmonth" + " " + this.site.ReportSite1Body.name + " " + this.site.ReportSite1Body.sn[0]+" " +this.site.ReportSite1Body.name+'-'+this.site.ReportSite2Body.name)     
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastmonth" + " " + this.site.ReportSite2Body.name + " " + this.site.ReportSite2Body.sn[0])  
      exportCurMonthReport()
      let tmp = ReportTestBody.service_overview
      tmp['部署设备数'] = '4'
      tmp['新增设备数'] = '2'
      tmp['加速类型'] = '分支组网'
      let data = JSON.stringify(tmp)
      let ds = escape(data) 
      // service and device check    
      serviceOverviewCheck(ds)
      let tmp_2 =  JSON.parse(JSON.stringify(ReportTestBody.device_status))
      tmp_2[this.site.ReportSite1Body.name][3] = '否'
      tmp_2[this.site.ReportSite2Body.name][3] = '否'
      let data_2 = JSON.stringify(tmp_2)
      let ds_2 = escape(data_2)   
      deviceStatusCheck(ds_2)
      // export last month report
      emptyDownloadsDir()
      exportPreMonthReport()
      let tmp_1 = ReportTestBody.service_overview
      tmp_1['部署设备数'] = '2'
      tmp_1['新增设备数'] = '2'
      tmp['加速类型'] = '分支组网' 
      let data_1 = JSON.stringify(tmp_1)
      let ds_1 = escape(data_1) 
      // service and device check    
      serviceOverviewCheck(ds_1)
      let tmp_3 =  JSON.parse(JSON.stringify(ReportTestBody.device_status))
      tmp_3[this.site.ReportSite1Body.name][3] = '是'
      tmp_3[this.site.ReportSite2Body.name][3] = '是'
      delete tmp_3[this.site.ReportSite3Body.name]
      delete tmp_3[this.site.ReportSite4Body.name]
      let data_3 = JSON.stringify(tmp_3)
      let ds_3 = escape(data_3)   
      deviceStatusCheck(ds_3)    
     })
     //	SDWANDEV-4649
     it('office mode week report data check',function(){
      // export current week report 
      createUnion(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite1Body.name,this.site.ReportSite2Body.name)
      createUnion(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite3Body.name,this.site.ReportSite4Body.name)
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastweek" + " " + this.site.ReportSite1Body.name + " " + this.site.ReportSite1Body.sn[0]+" " +this.site.ReportSite1Body.name+'-'+this.site.ReportSite2Body.name)     
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastweek" + " " + this.site.ReportSite2Body.name + " " + this.site.ReportSite2Body.sn[0]) 
      exportCurWeekReport()
      let tmp = ReportTestBody.service_overview
      tmp['部署设备数'] = '4'
      tmp['新增设备数'] = '2'
      tmp['加速类型'] = '分支组网'
      let data = JSON.stringify(tmp)
      let ds = escape(data) 
      // service and device check    
      serviceOverviewCheck(ds)
      let tmp_2 =  JSON.parse(JSON.stringify(ReportTestBody.device_status))
      tmp_2[this.site.ReportSite1Body.name][3] = '否'
      tmp_2[this.site.ReportSite2Body.name][3] = '否'
      let data_2 = JSON.stringify(tmp_2)
      let ds_2 = escape(data_2)   
      deviceStatusCheck(ds_2)
      // export last week report
      emptyDownloadsDir()
      exportPreWeekReport()
      let tmp_1 = ReportTestBody.service_overview
      tmp_1['部署设备数'] = '2'
      tmp_1['新增设备数'] = '2'
      tmp['加速类型'] = '分支组网' 
      let data_1 = JSON.stringify(tmp_1)
      let ds_1 = escape(data_1) 
      // service and device check    
      serviceOverviewCheck(ds_1)
      let tmp_3 =  JSON.parse(JSON.stringify(ReportTestBody.device_status))
      tmp_3[this.site.ReportSite1Body.name][3] = '是'
      tmp_3[this.site.ReportSite2Body.name][3] = '是'
      delete tmp_3[this.site.ReportSite3Body.name]
      delete tmp_3[this.site.ReportSite4Body.name]
      let data_3 = JSON.stringify(tmp_3)
      let ds_3 = escape(data_3)   
      deviceStatusCheck(ds_3)    
     })
     //	SDWANDEV-4628
     it('office mode service quality check',function(){
      // export current week report
      createUnion(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite1Body.name,this.site.ReportSite2Body.name)
      createUnion(this.info.token, this.company.testCompanyReportForm.name,this.site.ReportSite3Body.name,this.site.ReportSite4Body.name)
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastweek" + " " + this.site.ReportSite1Body.name + " " + this.site.ReportSite1Body.sn[0]+" " +this.site.ReportSite1Body.name+'-'+this.site.ReportSite2Body.name)     
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastweek" + " " + this.site.ReportSite2Body.name + " " + this.site.ReportSite2Body.sn[0])
      cy.reload()     
      exportCurWeekReport()
      let tmp =  JSON.parse(JSON.stringify(ReportTestBody.service_quality))
      let data = JSON.stringify(tmp)
      let ds = escape(data) 
      // service quality check    
      serviceQualityCheck(ds)
      // export last week report
      emptyDownloadsDir()
      exportPreWeekReport()
      let tmp_1 =  JSON.parse(JSON.stringify(ReportTestBody.service_quality))
      delete tmp_1[this.site.ReportSite3Body.name + '-' + this.site.ReportSite4Body.name]     
      let data_1 = JSON.stringify(tmp_1)
      let ds_1 = escape(data_1) 
      // service quality check  
      serviceQualityCheck(ds_1) 
     })
     //	SDWANDEV-4631
     it('report check after modify site',function(){
      // export current month report
      exec_cmd_on_local("bash /e2e/RoaringDog/test/reportTest.sh" + " " + "lastmonth" + " " + this.site.ReportSite4Body.name + " " + this.site.ReportSite4Body.sn[0])
      cy.reload()
      visitAndSetPageUserInfo('/site',this.info)
      changeSiteCompanyView(this.company.testCompanyReportForm.name)
      changeSiteProperty(this.site.ReportSite4Body.name,'上海市',1024) 
      visitAndSetPageUserInfo('/reportFormPage',this.info)
      changeSiteCompanyView(this.company.testCompanyReportForm.name)    
      exportCurMonthReport()
      let tmp =  JSON.parse(JSON.stringify(ReportTestBody.device_status))
      tmp[this.site.ReportSite4Body.name][0] = '华东地区/上海市'
      tmp[this.site.ReportSite4Body.name][3] = '否'
      tmp[this.site.ReportSite4Body.name][4] = '1024'
      let data = JSON.stringify(tmp)
      let ds = escape(data) 
      // service quality check    
      deviceStatusCheck(ds)
      // export last month report
      emptyDownloadsDir()
      exportPreMonthReport()
      tmp[this.site.ReportSite4Body.name][3] = '是'
      delete tmp[this.site.ReportSite1Body.name]
      delete tmp[this.site.ReportSite2Body.name]
      delete tmp[this.site.ReportSite3Body.name]
      let data_ = JSON.stringify(tmp)
      let ds_ = escape(data_) 
      deviceStatusCheck(ds_)     
     })
     // SDWANDEV-4629
     it('ticket check',function(){
      let cmd = 'sudo sh -c "echo 127.0.0.1 "api.jiandaoyun.com" >> /etc/hosts"'
      exec_cmd_on_host('172.17.0.1',cmd)
      exportCurMonthReport()
      let tmp =  JSON.parse(JSON.stringify(ReportTestBody.ticket_detail))
      let data = JSON.stringify(tmp)
      let ds = escape(data)
      ticketDetailCheck(ds)
      serviceItemCheck('解决/报障工单数','1/2')
     })
 })
