import {deleteCompanyByName, deleteAllUnions,deleteAllSites, createCompanyByData,createPOP, deletePopByPopId,getLogsNumber,createSiteByData,deleteSiteByName,deleteAllUsers,deleteUser,deleteAllGlobalUsersExceptAdmin,deleteAllRole,createUser,createRole,modifySiteBWByData} from '../utils/basic-utils'
import {UserBody,RoleBody,popBody} from '../utils/variables-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView,changeToGlobalView} from '../utils/web-utils'
import {exec_cmd_on_local} from '../utils/consulCheck-utils'

function createAdminsUser(username,pswd,company,token){
    var body = UserBody.adminRoleUser
    body['username'] = username
    body['password'] = pswd
    body['company'] = company
    createUser(token,body)
}

function createChannelUser(username,pswd,channel,token){
    var body = UserBody.allRWuser
    body['username'] = username
    body['password'] = pswd
    body['channel'] = channel 
    body['company'] = 'all'
    createUser(token,body)
}

function createNormalUser(username,pswd,company,token){
    var body = UserBody.userRoleUser
    body['username'] = username
    body['password'] = pswd
    body['company'] = company
    createUser(token,body)
  }
  

function LoginPost(account,pswd) {
    cy.request('POST', '/api/v1/tokens', {"username":account,"password":pswd}).its('body').as('tokenbody')    
}

export function checkLogsNumber(logtype,num){
    cy.get('[slot=title]').contains('日志').click()
    if (logtype == '操作日志') {
        cy.contains('[role=menuitem]','操作日志').click({force:true})
        cy.contains('共 ' + num +' 条')
    } else if (logtype=='登录日志') {
        cy.contains('[role=menuitem]','登录日志').click({force:true})
        cy.contains('共 ' + num +' 条')
    }
}

export function getLogsNumberViaWeb(logtype){
    cy.contains('[slot=title]','日志').click()
    if (logtype == '操作日志') {
        cy.contains('[role=menuitem]','操作日志').click({force:true})
        var res = cy.$$('.el-pagination__total').text()
        var r = res.match(/(\d+)/)        
        return parseInt(r[0])
    } else if (logtype=='登录日志') {
        cy.contains('[role=menuitem]','登录日志').click({force:true})
        let res = Cypress.$('.el-pagination__total').text()
        let r = res.match(/(\d+)/)
        return parseInt(r[0])
    }
}

export function filterLog(filterlist){
    filterlist.forEach((item,index) => {
        if (item.length && index==0) {
            cy.get('.el-table__header').find('th').contains('公司').click()
            item.forEach((i)=>{
                cy.get('.el-checkbox').contains(i).click()
            })           
            cy.get('button:visible').contains('筛选').should('not.have.class','.is-disabled').click({force:true})
        } else if (item.length && index==1) {
            cy.get('.el-table__header').find('th').contains('操作').click()
            item.forEach((i)=>{
                cy.get('.el-checkbox').contains(i).click()
            })
            cy.get('button:visible').contains('筛选').should('not.have.class','.is-disabled').click({force:true})
        } else if (item.length && index==2) {
            cy.get('.el-table__header').find('th').contains('类型').click()
            item.forEach((i)=>{
                cy.get('.el-checkbox').contains(i).click()
            })         
            cy.get('button:visible').contains('筛选').should('not.have.class','.is-disabled').click({force:true})
        }
    })   
}

export function logTimeFilter(starttime,endtime){
    cy.get('[placeholder=开始日期]').type(starttime)
    cy.get('[placeholder=结束日期]').type(endtime).type('{enter}')
}

export function accountOrDetailFilter(type,value){
    cy.get('[data-cy=operationSelect]').click()
    cy.get('[x-placement=bottom-start]').within(()=>{
        cy.get('li').contains(type).click()
    })
    cy.get('[data-cy=operationSearch]').type(value)
    cy.get('[data-cy=triggerQuery]').click()
}

function gotoSitePageWithAccount(username,password){
    cy.typeLogin(username,password)
    cy.contains('配置').click()
    cy.contains('站点注册').filter(':visible').click()
  }


  const visitAndSetPage = (url, info,user) => {
    let expires
    cy.visit(url, {
        onBeforeLoad (win) {
          // and before the page finishes loading
          // set the user object in local storage
          Cypress.log(info)
          expires = new Date().getTime() + info.expiresIn * 1000
          win.localStorage.setItem('user', user.toString())
          win.localStorage.setItem('token', info.token)
          win.localStorage.setItem('expires-at', expires.toString(10))
          win.localStorage.setItem('remember', true.toString())
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
          deletePopByPopId(t_info.token,popBody.testpop.popId)
          deleteAllUnions(t_info.token,company.testCompany1Log.name)
          deleteAllSites(t_info.token,company.testCompany1Log.name)        
          deleteAllUsers(t_info.token,company.testCompany1Log.name)
          deleteCompanyByName(t_info.token,company.testCompany1Log.name)
          createCompanyByData(t_info.token,company.testCompany1Log)
          deleteAllUnions(t_info.token,company.testCompany2Log.name)
          deleteAllSites(t_info.token,company.testCompany2Log.name)        
          deleteAllUsers(t_info.token,company.testCompany2Log.name)
          deleteAllGlobalUsersExceptAdmin(t_info.token)
          deleteAllRole(t_info.token, 'all')
          deleteCompanyByName(t_info.token,company.testCompany2Log.name)
          createCompanyByData(t_info.token,company.testCompany2Log)
          createRole(t_info.token, "all", RoleBody.allRW)
          // admins user
          createAdminsUser('log@subao.com','test11!',company.testCompany1Log.name,t_info.token)
          // channel user
          createChannelUser('logc@subao.com','test22!',company.testCompany1Log.channel,t_info.token) 
          // normal user
          createNormalUser('logn@subao.com','test33!',company.testCompany1Log.name,t_info.token)             

        }) 
      })
    }) 
  })

  describe('log page test', function() {    
    before(function (){       
        exec_cmd_on_local("bash /e2e/RoaringDog/test/haddleLog.sh" + " " + "emptyLog"+ " " + "操作日志" + " " + "ALL")
        exec_cmd_on_local("bash /e2e/RoaringDog/test/haddleLog.sh" + " " + "emptyLog"+ " " + "登录日志" + " " + "ALL")
        LoginPost('log@subao.com','test11!')
        LoginPost('logc@subao.com','test22!')
        createSiteByData(this.info.token, this.company.testCompany1Log.name, this.site.LogSite1Body)
        createSiteByData(this.info.token, this.company.testCompany2Log.name, this.site.LogSite2Body)
        createAdminsUser('logtest@subao.com','test11!',this.company.testCompany1Log.name,this.info.token)
        deleteUser(this.info.token,'logtest@subao.com')
        deleteSiteByName(this.info.token, this.company.testCompany1Log.name, this.site.LogSite1Body.name)
        deleteSiteByName(this.info.token, this.company.testCompany2Log.name, this.site.LogSite2Body.name)
        exec_cmd_on_local("bash /e2e/RoaringDog/test/haddleLog.sh" + " " + "modifyLogTime" + " " + "操作日志" + " " + this.company.testCompany1Log.name)
        exec_cmd_on_local("bash /e2e/RoaringDog/test/haddleLog.sh" + " " + "modifyLogTime" + " " + "登录日志" + " " + this.company.testCompany1Log.name) 
        createSiteByData(this.info.token, this.company.testCompany1Log.name, this.site.LogSite3Body)
        //deleteSiteByName(this.info.token, this.company.testCompany1Log.name, this.site.LogSite3Body.name)
        cy.get('@tokenbody').then(tokenbody=>{
            modifySiteBWByData(tokenbody.token,this.company.testCompany1Log.name,this.site.LogSite3Body, '8888' )
        })
        LoginPost('logn@subao.com','test33!')
        visitAndSetPageUserInfo('/operationLog',this.info)       
    })
    // SDWANDEV-4696
    it('check logs under global mode', function(){
        // 全局模式下操作日志总数检查
        checkLogsNumber('操作日志',8)
        // 按账户过滤
        accountOrDetailFilter('账户','admin')
        checkLogsNumber('操作日志',7)
        cy.reload()
        // 按详情过滤
        accountOrDetailFilter('详情','修改带宽')
        checkLogsNumber('操作日志',1)
        cy.reload()
        // 按时间过滤
        logTimeFilter('2021-08-01','2021-08-02')
        checkLogsNumber('操作日志',4)
        cy.reload()
        // 按 <公司 + 操作(增加) + 类型> 过滤      
        filterLog([[this.company.testCompany1Log.name],['增加'],['站点']])
        checkLogsNumber('操作日志',2)
        cy.reload()
        // 按 <公司 + 操作(删除) + 类型> 过滤  
        filterLog([[this.company.testCompany1Log.name],['删除'],['账号']])
        checkLogsNumber('操作日志',1)
        cy.reload()
        // 按 <公司 + 操作(修改) + 类型> 过滤  
        filterLog([[this.company.testCompany1Log.name],['修改'],[]])
        checkLogsNumber('操作日志',1)                  
        cy.reload()
        // 全局模式下登录日志总数检查
        checkLogsNumber('登录日志',3)
        filterLog([[this.company.testCompany1Log.name]]) 
        checkLogsNumber('登录日志',2)
        cy.reload()  
        // 登录日志按时间过滤      
        logTimeFilter('2021-08-01','2021-08-02')
        checkLogsNumber('登录日志',1)
 
    })
    //	SDWANDEV-4697
    it('check logs under common mode', function(){
        visitAndSetPageUserInfo('/operationLog',this.info) 
        changeSiteCompanyView(this.company.testCompany1Log.name)
        // 普通模式下操作日志总数检查
        checkLogsNumber('操作日志',6)
        // 按账户过滤
        accountOrDetailFilter('账户','admin')
        checkLogsNumber('操作日志',5)
        cy.reload()
        // 按详情过滤
        accountOrDetailFilter('详情','修改带宽')
        checkLogsNumber('操作日志',1)
        cy.reload()
        // 按时间过滤
        logTimeFilter('2021-08-01','2021-08-02')
        checkLogsNumber('操作日志',4)
        cy.reload()
        // 按 <操作(增加) + 类型> 过滤       
        filterLog([[],['增加'],['站点']])
        checkLogsNumber('操作日志',2)
        cy.reload()
        // 按 <操作(删除) + 类型> 过滤 
        filterLog([[],['删除'],['账号']])
        checkLogsNumber('操作日志',1)
        cy.reload()
        // 按 <操作(修改) + 类型> 过滤 
        filterLog([[],['修改'],[]])
        checkLogsNumber('操作日志',1)            
        cy.reload()
        // 登录日志总数检查
        checkLogsNumber('登录日志',2)
        // 按时间过滤
        logTimeFilter('2021-08-01','2021-08-02')
        checkLogsNumber('登录日志',1)
    })
    // 	SDWANDEV-4699
    it('login log view permission check',function(){
        // 渠道用户登录前，确认全局模式和普通模式下的登录日志初始数量
        visitAndSetPageUserInfo('/loginLog',this.info)
        checkLogsNumber('登录日志',3)
        changeSiteCompanyView(this.company.testCompany1Log.name)
        checkLogsNumber('登录日志',2) 
        // 渠道用户登录1次
        LoginPost('logc@subao.com','test22!')
        cy.reload()
        // 普通模式下检查登录日志数，无变化
        checkLogsNumber('登录日志',2)
        // 切换到全局模式下检查登录日志数，增加了1条
        changeToGlobalView('loginLog',this.info)
        checkLogsNumber('登录日志',4)
        // 渠道用户登录查看登录日志数，无变化
        cy.get('@tokenbody').then(tokeninfo => {
            visitAndSetPage('/loginLog',tokeninfo,'logc@subao.com')
        })
        changeSiteCompanyView(this.company.testCompany1Log.name)
        checkLogsNumber('登录日志',2)
    })
    // SDWANDEV-4698
    it('operation log view permission check',function(){
        // 新建pop点前，确认全局模式和普通模式下的操作日志初始数量
        visitAndSetPageUserInfo('/operationLog',this.info)
        checkLogsNumber('操作日志',8)        
        changeSiteCompanyView(this.company.testCompany1Log.name)
        checkLogsNumber('操作日志',6) 
        // 全局模式下，新建pop点
        createPOP(this.info.token,popBody.testpop)
        cy.reload()
        // 普通模式下检查操作日志数量，无变化
        checkLogsNumber('操作日志',6)
        // 切换到全局模式下检查日志数，增加了1条
        changeToGlobalView('operationLog',this.info)
        checkLogsNumber('操作日志',9)
        // 渠道用户登录查看，日志数无变化
        LoginPost('logc@subao.com','test22!')
        cy.get('@tokenbody').then(tokeninfo => {
            visitAndSetPage('/operationLog',tokeninfo,'logc@subao.com')
        })
        changeSiteCompanyView(this.company.testCompany1Log.name)
        checkLogsNumber('操作日志',6)
    })


})