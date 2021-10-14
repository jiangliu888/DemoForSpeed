import {deleteCompanyByName,deleteAllSites, createCompanyByData, createSiteByData, deleteAllUsers, deleteAllRole,deleteUser,createUser,createRole, deleteAllGlobalUsersExceptAdmin} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView,changeToGlobalView, setSiteBaseInfo, defaultRegionTemplate} from '../utils/web-utils'
import {RoleBody,UserBody,RegionTestBody} from '../utils/variables-utils'

var test_regions = RegionTestBody.test_regions
var test_city = RegionTestBody.test_city
var default_regions = RegionTestBody.default_regions
const cities = test_city[0]+','+test_city[1]+'、'+test_city[2]+'，'+test_city[3]

function regionRowContains(datacy,filter,start,end, values){
    cy.get(datacy).contains(filter).parents('tr').eq(0).within(() => {
      var i = start,j=0
      for (; i < end; i++,j++) {
        if (values[j] == '') {
          cy.get('th').eq(i).get('div').should('be.empty')
        } else {
          cy.get('th').eq(i).contains(values[j])
        }
      }
    })
  }

function default_region_template_check(){
  cy.get('[data-cy=regionTable]').contains('编辑').parents('tbody').within(()=>{
    cy.get('tr').should('have.length',7).each(($item,$index)=>{
      cy.get('tr').eq($index).within(()=>{
        cy.get('td').eq(1).should(($span)=>{
        expect($span.text()).to.equal(RegionTestBody.default_regions[$index])
        })
      })
    })
    cy.get('tr').each(($item,$index)=>{
      var result = RegionTestBody.default_regions[$index].match(/\（(.+)\）/)
      var num = parseInt(result[1])
      cy.get('tr').eq($index).within(()=>{
        cy.get('td').eq(0).click()
      })
      cy.get('tr').eq($index+1).find('>td>div').eq(1).find('span').should('have.length',num)
      cy.get('tr').eq($index).within(()=>{
        cy.get('td').eq(0).click()
      })      
    })         
  })
}

function createRegion(regionName,remark){
  cy.contains('button','新建区域').click()
  cy.get('[data-cy=regionForm]').find('.el-input__inner').eq(0).type(regionName)
  cy.get('[data-cy=regionForm]').find('.el-input__inner').eq(1).type(remark)
  //cy.get('.el-dialog__footer').filter(':visible').find('button').eq(1).click()
  cy.contains('确 定').click()
}

function deleteRegion(regionName){
  cy.get('td').contains(regionName).parents('tr').eq(0).contains('button','删除').click()
  cy.contains('确定').click()
  cy.contains('删除成功')
  cy.reload()  
}

function addCityToRegion(regionName,city){  
  cy.contains('td',regionName).prev().find('i').click({force: true})
  cy.get('.input-new-tag > .el-input__inner').filter(':visible').type(city,{force:true}).type('{enter}')
  cy.contains('td',regionName).prev().find('i').click({force: true})
}

function deleteCityFromRegion(regionName,city){  
  cy.contains('td',regionName).prev().find('i').click({force: true})
    city.forEach((item)=>{
    cy.contains('span',item).click({force: true})      
})  
  cy.contains('span','批量删除').click()
  cy.contains('button','确定').click()
  cy.contains('删除成功')
  cy.contains('td',regionName).prev().find('i').click({force: true})     
}

function moveCitytoRegion(city,srcRegion,dstRegion){
  cy.contains('td',srcRegion).prev().find('i').click({force: true})
  city.forEach((item)=>{
    cy.contains('span',item).click({force: true})     
  })
  cy.contains('span','批量转移').click({force: true})
  cy.contains('label',dstRegion).click({force: true})
  cy.get('.dialog-footer').eq(1).find('button').eq(1).click()
  cy.contains('转移成功') 
  cy.contains('td',srcRegion).prev().find('i').click({force: true})
}

function checkifCityExistInRegion(city,Region,flag){
  cy.contains('td',Region).prev().find('i').click({force: true})
  if (flag=='Exist') {
    city.forEach((item)=>{
      cy.get('tr').contains(item).should('exist')     
    })
  } else {
    city.forEach((item)=>{
      cy.get('tr').contains(item).should('not.exist')
    })
  }  
  cy.contains('td',Region).prev().find('i').click({force: true})
}

function siteRegionCheck(siteInfo){
  siteInfo.forEach((item)=>{
    cy.get('td').contains(item[0]).parents('tr').within(()=>{
      cy.get('td').eq(0).should('have.text',item[1])
      cy.get('td').eq(1).should('have.text',item[2])
    })
  })   
}

function deviceRegionCheck(siteInfo){
  cy.get('[data-cy=deviceTable]').find('.el-checkbox__input').should('be.visible')
  siteInfo.forEach((item)=>{
    cy.get('td').contains(item[0]).parents('tr').within(()=>{
      cy.get('td').eq(1).should('have.text',item[1])
      cy.get('td').eq(2).should('have.text',item[2])
    })
  })   
}

function gotoRegionPageWithAccount(username,password){
    cy.typeLogin(username,password)
    cy.contains('账户').click()
    cy.contains('行政区划').click()
    cy.contains('新建区域')
}

function gotoSitePageWithAccount(username,password){
  cy.typeLogin(username,password)
  cy.contains('配置').click()
  cy.contains('站点注册').filter(':visible').click()
}

function changeSiteCity(site,city){
    cy.get('td').contains(site).parents('tr').find('td').last().find('button').contains('编辑').click({force: true})
    cy.get('input[placeholder=选择城市]').eq(1).parent('div').click({force: true}).within(()=>{
      cy.get('.el-input__icon').click({force: true})
    })    
    if (city != '') {
      cy.get('input[placeholder=选择城市]').eq(1).type(city,{force: true})                
      cy.contains('.el-cascader__suggestion-item',city).click()      
      cy.contains('确 定').click()    
    } else {            
      cy.contains('确 定').click()     
    }
    cy.reload()
}

function createChannelUser(username,pswd,channel,token){
    var body = UserBody.qudaoUser
    body['username'] = username
    body['password'] = pswd
    body['channel'] = channel
    createUser(token,body)
}

function createNormalUser(username,pswd,company,token){
  var body = UserBody.userRoleUser
  body['username'] = username
  body['password'] = pswd
  body['company'] = company
  createUser(token,body)
}

function varInitial(site) {
  window.site1 = JSON.parse(JSON.stringify(site.RegionSite1Body))
  window.site2 = JSON.parse(JSON.stringify(site.RegionSite2Body))
  window.site3 = JSON.parse(JSON.stringify(site.RegionSite3Body))
  window.site4 = JSON.parse(JSON.stringify(site.RegionSite4Body))
}

before(function () {
    cy.fixture("companies/companies.json").as('company')
    cy.fixture("companies/sites/sites.json").as('site')
    getToken()
    //删除公司
    cy.get('@company').then(company => {
      cy.get('@site').then(site => {
        cy.get('@info').then(t_info => {
          varInitial(site)
          deleteAllSites(t_info.token, company.testCompany1Region.name)
          deleteAllSites(t_info.token, company.testCompany2Region.name)
          deleteAllSites(t_info.token, company.testCompany3Region.name)
          deleteAllSites(t_info.token, company.testCompany4Region.name)
          deleteAllUsers(t_info.token,company.testCompany1Region.name)
          deleteAllUsers(t_info.token,company.testCompany3Region.name)
          deleteUser(t_info.token,'33@qq.com')
          deleteAllGlobalUsersExceptAdmin(t_info.token)
          deleteAllRole(t_info.token, 'all')
          deleteCompanyByName(t_info.token, company.testCompany1Region.name)
          deleteCompanyByName(t_info.token, company.testCompany2Region.name)
          deleteCompanyByName(t_info.token, company.testCompany3Region.name)
          deleteCompanyByName(t_info.token, company.testCompany4Region.name)
          deleteCompanyByName(t_info.token, company.testCompany5Region.name)
          createRole(t_info.token, "all", RoleBody.globalAdminRole)
          visitAndSetPageUserInfo('/regionManage',this.info)
          changeToGlobalView("regionManage",this.info)
          defaultRegionTemplate()
          createCompanyByData(t_info.token, company.testCompany1Region)
          createCompanyByData(t_info.token, company.testCompany2Region)
          createCompanyByData(t_info.token, company.testCompany3Region)
          createCompanyByData(t_info.token, company.testCompany4Region)
          createNormalUser('11@qq.com','1111qq!',company.testCompany1Region.name,t_info.token)
          createNormalUser('111@qq.com','1111qq!',company.testCompany1Region.name,t_info.token)
          createNormalUser('333@qq.com','3333qq!',company.testCompany3Region.name,t_info.token)
          createChannelUser('33@qq.com','3333qq!','region',t_info.token)
          createSiteByData(t_info.token, company.testCompany1Region.name, site.RegionSite2Body)
          createSiteByData(t_info.token, company.testCompany1Region.name, site.RegionSite3Body)
          createSiteByData(t_info.token, company.testCompany1Region.name, site.RegionSite1Body)
          createSiteByData(t_info.token, company.testCompany1Region.name, site.RegionSite4Body)
          cy.reload()
        })
      })
    })
   })

describe('Regionalism page test', function() {
    beforeEach(function () {
     visitAndSetPageUserInfo('/regionManage',this.info)
     changeToGlobalView("regionManage",this.info)    
     defaultRegionTemplate()
     changeSiteCompanyView(this.company.testCompany1Region.name)
     defaultRegionTemplate()
     changeToGlobalView("regionManage",this.info)
    })
    //SDWANDEV-4587
    it('Default region template check', function(){
      // global view
      regionRowContains('[data-cy=regionTable]','区域',0,4, ['','区域','备注','操作'])
      default_region_template_check()
      // normal company view 
      changeSiteCompanyView(this.company.testCompany1Region.name)
      default_region_template_check()
      // create new company and check the region template
      createCompanyByData(this.info.token, this.company.testCompany5Region)
      cy.reload()
      changeSiteCompanyView(this.company.testCompany5Region.name)
      default_region_template_check()
      deleteCompanyByName(this.info.token, this.company.testCompany5Region.name)
    })
    //SDWANDEV-4588
    it('Modify the region template under global mode',function(){
      // add new region 
      createRegion(test_regions[0],'remark')
      cy.contains('创建成功')
      cy.contains(test_regions[0] + '（0）').should('exist')
      // add new city
      addCityToRegion(test_regions[0],cities)
      cy.contains('创建成功')
      checkifCityExistInRegion(test_city.slice(0,4),test_regions[0],'Exist')
      cy.get('tr').contains(test_regions[0]+'（4）').should('exist')
      // move city
      moveCitytoRegion(test_city.slice(0,2),test_regions[0],test_regions[2])
      checkifCityExistInRegion(test_city.slice(0,2),test_regions[2],'Exist')
      checkifCityExistInRegion(test_city.slice(0,2),test_regions[0],'notExist')
      // delete city
      deleteCityFromRegion(test_regions[0],test_city.slice(2,3))
      checkifCityExistInRegion(test_city.slice(2,3),test_regions[0],'notExist')
      // delete region
      deleteRegion(test_regions[1])
      cy.contains(test_regions[1]).should('not.exist')
      // add duplicate region
      createRegion(test_regions[0],'remark')
      cy.contains('创建失败，区域名称已经存在')
      cy.get('[data-cy=regionDialog]').find('.el-button--default').filter(':visible').click()
      cy.get('tr').contains(test_regions[0]).should('have.length',1)
      // add duplicate city
      addCityToRegion(test_regions[0],test_city[4]+','+test_city[5])
      cy.contains('创建失败，城市名称已经存在')
      checkifCityExistInRegion(test_city.slice(4,6),test_regions[0],'notExist')
      changeSiteCompanyView(this.company.testCompany1Region.name)
      cy.contains(test_regions[0]).should('not.exist')
      cy.contains(test_regions[1]).should('exist')
      checkifCityExistInRegion(test_city.slice(0,2),test_regions[2],'notExist')
      defaultRegionTemplate()
      cy.contains(test_regions[0]+'（1）').should('exist')
      cy.contains(test_regions[1]).should('not.exist')
      checkifCityExistInRegion(test_city.slice(0,2),test_regions[2],'Exist')
      checkifCityExistInRegion(['test city4'],test_regions[0],'Exist')
      changeToGlobalView("regionManage",this.info)
      defaultRegionTemplate()
      cy.contains(test_regions[0]).should('not.exist')
      cy.contains(test_regions[1]).should('exist')
      changeSiteCompanyView(this.company.testCompany1Region.name)
      defaultRegionTemplate()
      cy.contains(test_regions[0]).should('not.exist')
      cy.contains(test_regions[1]).should('exist')
      checkifCityExistInRegion(test_city.slice(0,2),test_regions[2],'notExist')
    })
    //SDWANDEV-4589
    it('Modify the region template under common mode',function(){
      changeSiteCompanyView(this.company.testCompany1Region.name)
      // add new region 
      createRegion(test_regions[0],'remark')
      cy.contains('创建成功')
      cy.contains(test_regions[0]+'（0）').should('exist')
      // add new city
      addCityToRegion(test_regions[0],cities)
      cy.contains('创建成功')
      checkifCityExistInRegion(test_city.slice(0,4),test_regions[0],'Exist')
      cy.get('tr').contains(test_regions[0]+'（4）').should('exist')
      // move city
      moveCitytoRegion(test_city.slice(0,2),test_regions[0],test_regions[2])
      checkifCityExistInRegion(test_city.slice(0,2),test_regions[2],'Exist')
      checkifCityExistInRegion(test_city.slice(0,2),test_regions[0],'notExist')
      // delete city
      deleteCityFromRegion(test_regions[0],test_city.slice(2,3))
      checkifCityExistInRegion(test_city.slice(2,3),test_regions[0],'notExist')
      // delete region
      deleteRegion(test_regions[1])
      cy.contains(test_regions[1]).should('not.exist')
      // add duplicate region
      createRegion(test_regions[0],'remark')
      cy.contains('创建失败，区域名称已经存在')
      cy.get('[data-cy=regionDialog]').find('.el-button--default').filter(':visible').click()
      cy.get('tr').contains(test_regions[0]).should('have.length',1)
      // add duplicate city
      addCityToRegion(test_regions[0],test_city[4]+','+test_city[5])
      cy.contains('创建失败，城市名称已经存在')
      checkifCityExistInRegion(test_city.slice(4,6),test_regions[0],'notExist')
      changeToGlobalView("regionManage",this.info)
      cy.contains(test_regions[0]).should('not.exist')
      cy.contains(test_regions[1]).should('exist')
      checkifCityExistInRegion(test_city.slice(0,2),test_regions[2],'notExist')
      changeSiteCompanyView(this.company.testCompany3Region.name)
      cy.contains(test_regions[0]).should('not.exist')
      cy.contains(test_regions[1]).should('exist')
      checkifCityExistInRegion(test_city.slice(0,2),test_regions[2],'notExist')      
  })
  //SDWANDEV-4592
  it('Region modification no impact between companies',function(){
    changeSiteCompanyView(this.company.testCompany3Region.name)
    defaultRegionTemplate()
    changeSiteCompanyView(this.company.testCompany4Region.name)
    defaultRegionTemplate()
    cy.logout()
    // company1 account1 login
    gotoRegionPageWithAccount('11@qq.com','1111qq!')
    // add new region 
    createRegion(test_regions[0],'remark')
    cy.contains('创建成功')
    cy.contains(test_regions[0]+'（0）').should('exist') 
    // add new city
    addCityToRegion(test_regions[0],cities)
    cy.contains('创建成功')
    checkifCityExistInRegion(test_city.slice(0,4),test_regions[0],'Exist')
    cy.contains(test_regions[0]+'（4）').should('exist') 
    cy.logout()
    // company1 account2 login
    gotoRegionPageWithAccount('111@qq.com','1111qq!')
    checkifCityExistInRegion(test_city.slice(0,4),test_regions[0],'Exist')
    cy.contains(test_regions[0]+'（4）').should('exist')
    deleteCityFromRegion(test_regions[0],[test_city[0]])
    checkifCityExistInRegion([test_city[0]],test_regions[0],'notExist')
    cy.logout()
    // company2 account1 login
    gotoRegionPageWithAccount('333@qq.com','3333qq!')
    cy.contains(test_regions[0]).should('not.exist')
    createRegion(test_regions[0],'remark')
    cy.contains('创建成功')
    cy.contains(test_regions[0]+'（0）').should('exist')
    cy.logout()
    // channel account login 
    gotoRegionPageWithAccount('33@qq.com','3333qq!')
    changeSiteCompanyView(this.company.testCompany3Region.name)
    addCityToRegion(test_regions[0],cities)
    cy.contains('创建成功')
    cy.contains(test_regions[0]+'（4）').should('exist')
    changeSiteCompanyView(this.company.testCompany4Region.name)
    cy.contains(test_regions[0]+'（4）').should('not.exist')
    cy.logout()
    // channel company account login
    gotoRegionPageWithAccount('333@qq.com','3333qq!')
    cy.contains(test_regions[0]+'（4）').should('exist')
  })
  describe('Region modification linkage check', function() {
    beforeEach(function () {      
      changeSiteCompanyView(this.company.testCompany1Region.name)
      createRegion(test_regions[0],'remark')
      addCityToRegion(test_regions[0],cities)
      moveCitytoRegion(test_city.slice(2,3),test_regions[0],test_regions[1])
      var bodytmp=[].concat(default_regions)
      bodytmp.forEach((item,index)=>{
        item=item.replace('（','(')
        item=item.replace('）',')')
        bodytmp[index]=item
      })
      bodytmp.push(test_regions[0]+'(3)')
      bodytmp[0] = test_regions[1]+'(18)'
      cy.wrap(bodytmp).as('body')   
      visitAndSetPageUserInfo('/site',this.info)
      changeSiteCity(site1.name,test_city[2])
      changeSiteCity(site4.name,test_city[0])
      changeSiteCity(site2.name,test_city[5])      
      changeSiteCity(site3.name,test_city[5])               
     })
     //SDWANDEV-4594
     it('Region check for site edit page',function(){
      cy.get('td').contains(site1.name).parents('tr').find('td').last().find('button').contains('编辑').click()
      cy.get('input[placeholder=选择城市]').eq(1).click()
      var body1 = this.body
      body1.forEach((item,index)=>{  
        var result = body1[index].match(/\((.+)\)/)
        var num = parseInt(result[1])    
        cy.contains(item).should('exist').click()
        cy.contains(item).parents('div').eq(1).next().find('li').should('have.length',num)
      })
      var result = body1[1].match(/\((.+)\)/)
      var num = parseInt(result[1])
      cy.get('input[placeholder=选择城市]').eq(1).clear().type('东北')
      cy.get('.el-cascader__suggestion-panel > .el-scrollbar__wrap').find('li').should('have.length',num)
      .each(($li)=>{
        cy.get($li).should('contain',body1[1])
      })
      cy.get('input[placeholder=选择城市]').eq(1).type('{esc}')
      var result = body1[body1.length - 1].match(/\((.+)\)/)
      var num = parseInt(result[1])
      cy.get('td').contains(site4.name).parents('tr').find('td').last().find('button').contains('编辑').click()
      cy.get('input[placeholder=选择城市]').eq(1).clear().type(test_regions[0])
      cy.get('.el-cascader__suggestion-panel > .el-scrollbar__wrap').find('li').should('have.length',num)
      .each(($li)=>{
        cy.get($li).should('contain',body1.slice(-1))
      })
      cy.get('input[placeholder=选择城市]').eq(1).clear().type(test_city[0])
      cy.get('.el-cascader__suggestion-panel > .el-scrollbar__wrap').find('li').should('have.length',1).and('have.text',test_regions[0]+'(3) / '+test_city[0])      
    })
    //SDWANDEV-4595
    it('Region check for site&device page',function(){          
      siteRegionCheck([[site2.name,test_regions[3],test_city[5]],[site3.name,test_regions[3],test_city[5]],   
                      [site1.name,test_regions[1],test_city[2]],[site4.name,test_regions[0],test_city[0]]])                      
      changeToGlobalView("site",this.info)
      cy.get('.el-table__header').find('th').should('not.contain','区域') 
      cy.get('.el-table__header').find('th').should('not.contain','城市')            
      visitAndSetPageUserInfo('/device',this.info)
      cy.get('.el-table__header').find('th').should('not.contain','区域') 
      cy.get('.el-table__header').find('th').should('not.contain','城市') 
      changeSiteCompanyView(this.company.testCompany1Region.name)
      deviceRegionCheck([[site4.name,test_regions[0],test_city[0]],[site1.name,test_regions[1],test_city[2]],   
                      [site2.name,test_regions[3],test_city[5]],[site3.name,test_regions[3],test_city[5]]])   
      visitAndSetPageUserInfo('/regionManage',this.info)
      moveCitytoRegion(test_city.slice(2,3),test_regions[1],test_regions[7])
      deleteCityFromRegion(test_regions[3],[test_city[5]])
      deleteRegion(test_regions[0])
      visitAndSetPageUserInfo('/device',this.info)
      deviceRegionCheck([[site4.name,'',test_city[0]],[site1.name,test_regions[7],test_city[2]],   
                        [site2.name,'',test_city[5]],[site3.name,'',test_city[5]]])
      visitAndSetPageUserInfo('/site',this.info)
      siteRegionCheck([[site4.name,'',test_city[0]],[site1.name,test_regions[7],test_city[2]],   
                      [site2.name,'',test_city[5]],[site3.name,'',test_city[5]]]) 
      visitAndSetPageUserInfo('/regionManage',this.info)
      addCityToRegion(test_regions[3],test_city[5])
      addCityToRegion(test_regions[6],test_city[0])
      visitAndSetPageUserInfo('/site',this.info)
      siteRegionCheck([[site4.name,test_regions[6],test_city[0]],[site2.name,test_regions[3],test_city[5]],   
                      [site3.name,test_regions[3],test_city[5]]]) 
      visitAndSetPageUserInfo('/device',this.info)
      deviceRegionCheck([[site4.name,test_regions[6],test_city[0]],[site2.name,test_regions[3],test_city[5]],   
                        [site3.name,test_regions[3],test_city[5]]])
    })
    //SDWANDEV-4596
    it('Region filter check for site&device page',function(){
      var tmp = [].concat(default_regions)
      tmp.forEach((item,index)=>{
        item=item.replace(/（\d+）/g,'(0)')
        tmp[index]=item
      })
      tmp[0] = test_regions[1]+'(1)' 
      tmp[2] = test_regions[3]+'(1)'
      tmp.push(test_regions[0]+'(1)')           
      cy.get('input[placeholder=选择城市]').eq(0).click()
      tmp.forEach((item,index)=>{  
        var result = tmp[index].match(/\((.+)\)/)
        var num = parseInt(result[1])    
        cy.contains(item).click()
        if (item==test_regions[1]+'(1)') {
          cy.contains(item).parents('div').eq(1).next().find('li').should('have.length',num).and('have.text',test_city[2]+'(1)')
        } else if (item==test_regions[3]+'(1)') {
          cy.contains(item).parents('div').eq(1).next().find('li').should('have.length',num).and('have.text',test_city[5]+'(2)')
        } else if (item==test_regions[0]+'(1)') {
          cy.contains(item).parents('div').eq(1).next().find('li').should('have.length',num).and('have.text',test_city[0]+'(1)')
        } else {
          cy.contains('暂无数据')
        }
      })
      cy.contains(test_regions[3]+'(1)').click().parents('div').eq(1).next().contains('li',test_city[5]).find('.el-checkbox__inner').click()
      cy.contains('共 2 条')
      siteRegionCheck([[site2.name,test_regions[3],test_city[5]],[site3.name,test_regions[3],test_city[5]]])
      cy.contains(test_regions[0]+'(1)').click().parents('div').eq(1).next().contains('li',test_city[0]).find('.el-checkbox__inner').click()
      cy.contains('共 3 条')
      siteRegionCheck([[site4.name,test_regions[0],test_city[0]]])
      visitAndSetPageUserInfo('/device',this.info)
      cy.get('input[placeholder=选择城市]').eq(0).click()
      cy.contains(test_regions[3]+'(1)').click().parents('div').eq(1).next().contains('li',test_city[5]).find('.el-checkbox__inner').click()
      cy.contains('共 2 条')
      deviceRegionCheck([[site2.name,test_regions[3],test_city[5]],[site3.name,test_regions[3],test_city[5]]])
      cy.contains(test_regions[0]+'(1)').click().parents('div').eq(1).next().contains('li',test_city[0]).find('.el-checkbox__inner').click()
      cy.contains('共 3 条')
      deviceRegionCheck([[site4.name,test_regions[0],test_city[0]]])
    })
    //SDWANDEV-4599
    it('User region limition check',function(){    
      changeSiteCity(site3.name,'')
      cy.logout()
      gotoSitePageWithAccount('111@qq.com','1111qq!')
      cy.contains('共 4 条')
      siteRegionCheck([[site2.name,test_regions[3],test_city[5]],[site3.name,'',''],   
              [site1.name,test_regions[1],test_city[2]],[site4.name,test_regions[0],test_city[0]]])
      //修改权限
      visitAndSetPageUserInfo('/accountManage',this.info)
      cy.get('td').contains('111@qq.com').parents('tr').find('td').last().find('button').contains('编辑').click()
      cy.get('[data-cy=regions]').find('.el-tag__close').click()
      cy.get('input[placeholder=选择区域]').click()
      cy.get('.el-select-group__wrap').eq(1).contains('span',test_regions[1]).click()
      cy.get('.el-select-group__wrap').eq(1).contains('span',test_regions[0]).click()
      cy.contains('确认').click()
      cy.contains('更新成功')
      cy.logout()
      gotoSitePageWithAccount('111@qq.com','1111qq!')
      cy.contains('共 2 条')
      siteRegionCheck([[site1.name,test_regions[1],test_city[2]],[site4.name,test_regions[0],test_city[0]]])
      cy.get('input[placeholder=选择城市]').eq(0).click()
      cy.get('.el-cascader-panel > div').eq(0).find('li').should('have.length',2).within(()=>{
        cy.contains(test_regions[1]+'(1)')
        cy.contains(test_regions[0]+'(1)')
      })
      cy.contains('设备管理').click()
      deviceRegionCheck([[site1.name,test_regions[1],test_city[2]],[site4.name,test_regions[0],test_city[0]]])
      cy.get('input[placeholder=选择城市]').eq(0).click()
      cy.get('.el-cascader-panel > div').eq(0).find('li').should('have.length',2).within(()=>{
        cy.contains(test_regions[1]+'(1)')
        cy.contains(test_regions[0]+'(1)')
      })  
    })        
  })
})