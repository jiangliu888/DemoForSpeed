import { alert, RoleBody, testFirewallBody, testRouterBody, UserBody, saasSearchPatternBody, testServiceBody, testCompanyBody,menuList} from "./variables-utils"

const userKey = 'user'
const tokenKey = 'token'
const expiresAtKey = 'expires-at'
const remember = 'remember'
const rememberStatus = true
const user = 'admin'
const password = 'AIRwalk2013!)'
const tokenUrl = '/api/v1/tokens'
const default_bandwidth = 1000
const default_sitebandwith = 1024


export function getToken () {
  cy.request('POST', tokenUrl, {"username":user,"password":password})
  .its('body')
  .as('info')
}

export const visitAndSetPageUserInfo = (url, info) => {
    let expires
    cy.visit(url, {
        onBeforeLoad (win) {
          // and before the page finishes loading
          // set the user object in local storage
          Cypress.log(info)
          expires = new Date().getTime() + info.expiresIn * 1000
          win.localStorage.setItem(userKey, 'admin'.toString())
          win.localStorage.setItem(tokenKey, info.token)
          win.localStorage.setItem(expiresAtKey, expires.toString(10))
          win.localStorage.setItem(remember, rememberStatus.toString())
        }
      })
  }

export function searchTable(data_cy, keyword){
  cy.get('.filter-container').within(() => {
    cy.get('[data-cy='+data_cy+']').clear().type(keyword)
    //cy.contains('搜索').click()
 })
}

export function checkTableLineNumber(number){
  cy.get('.el-pagination__total').contains('共 '+number+' 条')
}

export function rowContains(datacy,filter,start,end, values){
  cy.get(datacy).contains(filter).parents('tr').eq(0).within(() => {
    var i = start,j=0
    for (; i < end; i++,j++) {
      if (values[j] == '') {
        cy.get('td').eq(i).get('span').should('be.empty')
      } else {
        cy.get('td').eq(i).contains(values[j])
      }
    }
  })
}

export function checkHomeCodeRow(sn, expected) {
    const idList = []
    cy.get('[data-cy="deviceTable"]').contains(sn).parents('tr').eq(0).within(() => {
        cy.get('td').eq(7).within(() => {
            cy.get('span').should('have.length', expected.length)
            cy.get('span').each(($value, index, $collection) => {
                expect($value.text()).to.eq(expected[index])
                // cy.wrap($value).click()
                // cy.wrap($value).getAttributes('aria-describedby').then(ids => {
                //     cy.get('span').parents("div#app").find("div#" + ids[0] + "~div")
                // })
            })
        })
    })
}

export function rowContainsVisible(datacy,filter,start,end, values){
  cy.get(datacy).contains(filter).parents('tr').eq(0).within(() => {
    var i = start,j=0
    for (; i < end; i++,j++) {
      if (values[j] == '') {
        cy.get('td').filter(':visible').eq(i).get('span').should('be.empty')
      } else {
        cy.get('td').filter(':visible').eq(i).contains(values[j])
      }
    }
  })
}

export function rowHeaderCheck(start, end, values){
  cy.get('[class="header"]').within(() => {
    var i = start,j=0
    for (; i < end; i++,j++) {
      if (values[j] == '') {
        cy.get('div').eq(i).should('be.empty')
      } else {
        cy.get('div').eq(i).should('contain',values[j])
      }
    }
  })
}

export function rowBodyCheck(filter, start, end, values){
  cy.get('[class="rows"]').within(() => {
    cy.contains(filter).parents('[class="row-item"]').within(()=>{
      var i = start,j=0
      for (; i < end; i++,j++) {
        if (values[j] == '') {
          cy.get('div[class="ceil"]').eq(i).should('be.empty')
        } else {
          cy.get('div[class="ceil"]').eq(i).should('contain',values[j])
        }
      }
    }) 
  })
}

export function rowUnflod(datacy,filter){
  cy.get(datacy).contains(filter).parents('tr').eq(0).within(() => {
    cy.get('[class="el-icon el-icon-arrow-right"]').click()
  })
}

export function ClickRow(datacy,filter,ColNum){
  cy.get(datacy).contains(filter).parents('tr').within(() => {
     cy.get('td').eq(ColNum).click()
  })
}

export function changeSiteCompanyView(company_name,switchWaitTime=0) {
  cy.get('div[class=right-menu]',{ timeout: 15000 }).then((div) => {
    if (div.find('span > .el-icon-arrow-up').length > 0) {

    } else {
      cy.get('div > .el-dropdown').eq(0).click({force: true})
      cy.contains('普通模式').click({ force: true })
    }
  })
  cy.get('span > .el-icon-arrow-up').eq(0).click({force: true})
  cy.wait(switchWaitTime)
  cy.get('ul > li').contains(company_name).click({force: true})
}

export function changeToGlobalView(url, info){
  clickGlobalView()
  visitAndSetPageUserInfo('/' + url, info)
}

export function clickGlobalView(){
  cy.get('div[class=right-menu]',{ timeout: 15000 }).then((div) => {
    if (div.find('span > .el-icon-arrow-up').length > 0) {
      cy.get('div > .el-dropdown').eq(0).click({force: true})
      cy.contains('全局模式').click({ force: true })
    }
  })
}


export function NoGlobalView(){
  cy.get('div[class=right-menu]').then((div) => {
      cy.get('div > .el-dropdown').eq(0).click()
      cy.contains('全局模式').should('not.exist')
    })
}

export function CanNotSwitchSiteCompanyView(company_name) {
  cy.contains(company_name)
  cy.get('input[id=companyName]').should('have.attr','disabled','disabled')
}

export function replaceSiteBySN(siteName,newSn){
  cy.get('[data-cy="siteTable"]').contains(siteName).parents('tr').within(() => {
    cy.contains('button', '编辑').click()
  })
  cy.get('[data-cy=siteDialog]').within(() => {
    cy.get('[src="img/replace.71419860.svg"]').click()
  })
  cy.contains("设备替换").parents('[role="dialog"]').within(()=>{
    cy.get("input").clear().type(newSn)
  })
  cy.get('[role="listbox"]').contains(newSn).click()
  cy.contains("设备替换").parents('[role="dialog"]').within(()=>{
    cy.contains("确 定").click()
  })
  cy.contains("设备替换成功")
  cy.get('[data-cy=siteDialog]').within(() => {
    cy.contains("确 定").click()
  })
}

export function setSiteBaseInfo(site){
    cy.get('[data-cy=siteDialog]').within(() => { 
    cy.typeInputWithLable('站点名称',site.name)
    cy.ClickInputWithLable('资产序列号',site.sn)
    cy.typeInputWithLable('数据面端口',site.tunnelNum)
    cy.typeInputWithLable('位置',site.location)
    cy.typeInputWithLable('限速',default_sitebandwith)
    cy.typeInputWithLable('经度',site.longitude)
    cy.typeInputWithLable('纬度',site.latitude)
    if(site.nets!=""){cy.typeTextareaWithLable('内网网段', site.nets)}
    if(site.reportInterval!=""){cy.typeInputWithLable('上报间隔', site.reportInterval)}
    if(site.scoreInterval!=""){cy.typeInputWithLable('评分间隔', site.scoreInterval)}
    if(site.hasOwnProperty("enablePrivate")){
      if(site.enablePrivate){cy.checkCheckBoxWithLable('启用二层端口')}
    }

    if(site.hasOwnProperty("natPort")){
      cy.checkCheckBoxWithLable('启用NatPort')
    }
    
    if(site.hasOwnProperty("natNet")){
      {cy.typeInputWithLable('natNet', site.natNet)}
    }
    
    if(site.HA){
      cy.checkCheckBoxWithLable('HA')
      cy.typeInputWithLable('备用设备',site.haDevice)
      cy.contains("HA配置").click()
      cy.typeValueBydatacy('[data-cy="wanipAddress1"]',site.HAaddress.master_wanip)
      cy.typeValueBydatacy('[data-cy="wanmask1"]',site.HAaddress.master_wanmask)
      cy.typeValueBydatacy('[data-cy="wangateway1"]',site.HAaddress.master_wangw)
      cy.typeValueBydatacy('[data-cy="wanipAddress2"]',site.HAaddress.standby_wanip)
      cy.typeValueBydatacy('[data-cy="wanmask2"]',site.HAaddress.standby_wanmask)
      cy.typeValueBydatacy('[data-cy="wangateway2"]',site.HAaddress.standby_wangw)
      cy.typeValueBydatacy('[data-cy="lanIp1"]',site.HAaddress.master_lanip)
      cy.typeValueBydatacy('[data-cy="lanIpMask1"]',site.HAaddress.master_lanmask)
      if(site.HAaddress.hasOwnProperty("master_langw")){
          cy.typeValueBydatacy('[data-cy="lanGateway1"]',site.HAaddress.master_langw)}
      cy.typeValueBydatacy('[data-cy="lanIp2"]',site.HAaddress.standby_lanip)
      cy.typeValueBydatacy('[data-cy="lanIpMask2"]',site.HAaddress.standby_lanmask)
      if(site.HAaddress.hasOwnProperty("standby_langw")){
         cy.typeValueBydatacy('[data-cy="lanGateway2"]',site.HAaddress.standby_langw)}
    }
    if(site.private){cy.typeTextareaWithLable('私网地址', site.private)}
})
}

export function setSiteWan(siteType,wanName,wan){
      cy.contains(wanName).parents('[data-cy=siteWanList]').within(() => {
          if (Cypress.$('[class="el-collapse-item__header"]').length > 0) {
              cy.log('walking into not active branch, need to expand the wan')
              cy.contains(wanName).then(($btn) => {
                if ($btn.hasClass('is-active')) {
                    cy.log("active")
                } else {
                    cy.log("not-active")
                    cy.contains(wanName).click()
                }
            })
          }
      })
    cy.contains(wanName).parents('[data-cy=siteWanList]').within(() => {
      cy.typeInputWithLable('限速',wan.bandwidth)
      if(wan.hasOwnProperty("group")){
        cy.typeInputWithLable('运营商',wan.group)
      }
      if(wan.hasOwnProperty("prefer_cac")){
        cy.typeInputWithLable('优选大区',wan.prefer_cac)
      }
      if(wan.hasOwnProperty("logic_if_name")){
        cy.typeInputWithLable('逻辑网口名',wan.logic_if_name)
      }
      if(wan.hasOwnProperty("staticIp")){
        cy.typeInputWithLable('静态IP',wan.staticIp)
      }
      if(wan.hasOwnProperty("gatewayMac")){
        cy.typeInputWithLable('网关MAC地址',wan.gatewayMac)
      }
      if(wan.hasOwnProperty("proxy")){
        if(wan.proxy){
          cy.checkCheckBoxWithLable('启用代理')
        }else{cy.unCheckCheckBoxWithLable('启用代理')}
      }
      cy.typeInputWithLable('优选Pop CAC',wan.prefer_pop_cac)
      cy.typeInputWithLable('优选Pop EAC',wan.prefer_pop_eac)
      cy.typeInputWithLable('优选IP',wan.prefer_ip)
      if (siteType!="串联"){
          if (wan.public_ip){cy.typeInputWithLable('Public IP',wan.public_ip)}
          cy.typeElinputWithLable('IP类型',wan.ip_type)
          if (wan.ip_type=="静态ip地址"){
              cy.typeInputWithLable('IP地址',wan.ip)
              cy.get('[data-cy=ipAddressMask]').within(() => {
                cy.get('input').clear().type(wan.mask)
             })
              cy.typeInputWithLable('网关',wan.gateway)}
          if (wan.ip_type=='PPPOE'){
              cy.typeInputWithLable('账号',wan.account)
              cy.typeInputWithLable('密码',wan.password)
          }
          cy.typeElinputWithLable('ip-mode',wan.ip_mode)
      }
    })
  }

export function setSiteLan(siteType,lanName,lan){
      cy.contains(lanName).then(($btn) => {
          if ($btn.hasClass('is-active')) {
              cy.log("active")
          } else {
              cy.log("not-active")
              cy.contains(lanName).click()
          }
      })
    cy.contains(lanName).parents('[class="el-collapse-item is-active"]').within(() => {
      cy.typeInputWithLable('Lan口IP',lan.ip_addr)
      cy.get('[data-cy=lanIpMask]').within(() => {
        cy.get('input').clear().type(lan.mask)
     })
      if (siteType=="旁挂"){
         cy.typeInputWithLable('网关',lan.gateway)
      }
      else {
        if (lan.DHCP){
            cy.checkCheckBoxWithLable('DHCP')
            cy.typeInputWithLable('起始地址',lan.ip_start)
            cy.typeInputWithLable('结束地址',lan.ip_end)
        }
        if(lan.gateway){cy.typeInputWithLable('网关',lan.gateway)}
        if(lan.internet){cy.checkCheckBoxWithLable('互联网直出')}
        else{cy.unCheckCheckBoxWithLable('互联网直出')}
        if(lan.IDC){cy.checkCheckBoxWithLable('内网隧道')}
        else{cy.unCheckCheckBoxWithLable('内网隧道')}
        if (lan.hasOwnProperty("lan_port_num")){cy.typeInputWithLable('占用网口数',lan.lan_port_num)}
      }
    })
  }

export function setSiteWifi(wifi){
    cy.checkCheckBoxWithLable('WIFI')
    cy.contains('WIFI').parent('div').parent('div').then(($btn) => {
      if ($btn.hasClass('is-active')) {
          cy.log("active")
      } else {
          cy.log("not-active")
          cy.contains('WIFI').click()
      }
    })
    cy.contains("WIFI").parents('div').within(() => {
    if (Cypress.$('[class="el-collapse-item__header is-active"]').length <= 0){
      cy.contains("WIFI").parents('[class="el-collapse-item__header"]').click()
    }
  })

    cy.contains("WIFI").parents('[class="el-collapse-item is-active"]').within(() => { 
      cy.typeInputWithLable('SSID',wifi.ssid)
      cy.typeElinputWithLable('network',wifi.network)
      cy.contains('network').click()
      cy.typeElinputWithLable('MAC过滤',wifi.macfilter)
      if (wifi.macfilter != "none"){
        cy.typeTextareaWithLable('MAC列表',wifi.mac_list)
      }
      cy.contains("加密方式").parent('div').within(() => {
        cy.get('input').click()
     })
    })
    cy.get('[class=el-cascader-panel]').within(() => {
      if (wifi.hasOwnProperty('encryption_type')) {
          cy.get('li').contains(wifi.encryption_type).click()
          if (wifi.encryption_type != "WEP Open System" && wifi.encryption_type != "No Encryption" && wifi.hasOwnProperty('encryption')) {
              cy.log(wifi.encryption)
              cy.get('li').contains(wifi.encryption).click()
          }
      } else {
          cy.get('li').contains('No Encryption').click()
      }
    })
  if (wifi.hasOwnProperty('encryption_type') && (wifi.encryption_type != "WEP Open System" && wifi.encryption_type != "No Encryption") && wifi.hasOwnProperty('key')) {
      cy.typeInputWithLable('Key', wifi.key)
  }
}

export function setSite4G(info_4g){
  cy.checkCheckBoxWithLable('4G')
  cy.contains("4G").parents('[class="el-collapse-item is-active"]').within(() => { 
    cy.typeInputWithLable('4G名称',info_4g[0].name_4g)
    cy.typeElinputWithLable('Usage',info_4g[0].usage)
    if (info_4g[0].hasOwnProperty("prefer_pop_cac")){
      cy.typeInputWithLable('优选大区',info_4g[0].prefer_cac)
      cy.typeInputWithLable('优选Pop CAC',info_4g[0].prefer_pop_cac)
      cy.typeInputWithLable('优选Pop EAC',info_4g[0].prefer_pop_eac)
      cy.typeInputWithLable('优选IP',info_4g[0].prefer_ip)
    }
  })
}

export function setSiteAuthAudit(authAuditInfo){
  setSiteAudit(authAuditInfo['audit'], authAuditInfo['auditMac'])
  setSiteAuth(authAuditInfo['auth'])
}

export function addRoutingReport(routing, index){
  cy.get('[data-cy=exportRuleCidr]').eq(index).clear().type(routing.prefix_nets)
  if( routing.action != "通告"){
      cy.get('[id=action]').eq(index).parent('div').within(() => {
          cy.get('[class="el-input__inner"]').click({force: true})
      })
      cy.get('.el-scrollbar').filter(':visible').get('li[class=el-select-dropdown__item]').contains(routing.action).should('be.visible').click({force: true})
    }
  cy.get('[data-cy=metric]').eq(index).clear().type(routing.metric)
}

export function setDynRouting(dyn_routing){
    if(dyn_routing.bgp){
        cy.checkCheckBoxWithLable('启用BGP')
        cy.typeInputWithLable('默认Metric',dyn_routing.metric)
   }
   else {cy.unCheckCheckBoxWithLable('启用BGP')}

   if(dyn_routing.ospf){
        cy.checkCheckBoxWithLable('启用ospf')
        cy.typeInputWithLable('默认Metric',dyn_routing.metric)
   }
   else {cy.unCheckCheckBoxWithLable('启用ospf')}

   if(dyn_routing.routing_report){
    if(cy.get('[data-cy=exportRuleCidr]').not(':visible')){
        cy.contains('路由上报过滤').click()}

    dyn_routing.routing_report.forEach((routing,index) => {
          if(index >0){cy.get('[data-cy=addRouterFilter]').click()}
          addRoutingReport(routing, index)})

    if(dyn_routing.routing_filter){
      if(cy.get('[data-cy=dispatchRuleCidr]').not(':visible')){
          cy.contains('路由分发过滤').click()
      }
      cy.typeTextareaWithDataCy('[data-cy=dispatchRuleCidr]', dyn_routing.routing_filter)
    }
  }
  
}

export function createWebSite(siteBody){
    cy.contains('添加').click()
    cy.get('[data-cy=siteDropdown]').within(()=>{
        cy.contains(siteBody.type).click({force: true})
    })
    setSiteBaseInfo(siteBody)
    if (siteBody.hasOwnProperty("wifi")){
      setSiteWifi(siteBody.wifi)
    }
    if (siteBody.hasOwnProperty("auditAuth")){
      setSiteAuthAudit(siteBody.auditAuth)
    }
    siteBody.wans.forEach(wan => {
      if (wan.name=='WAN1') {setSiteWan(siteBody.type,wan.name,wan)}
      else {
         cy.get('.el-icon-circle-plus').eq(0).click()
         setSiteWan(siteBody.type,wan.name,wan)}
    })
    if(siteBody.HA){
        if(siteBody.HAaddress.hasOwnProperty("master_wan2ip")){
           cy.typeValueBydatacy('[data-cy="wanipAddress3"]',siteBody.HAaddress.master_wan2ip)
           cy.typeValueBydatacy('[data-cy="wanmask3"]',siteBody.HAaddress.master_wan2mask)
           cy.typeValueBydatacy('[data-cy="wangateway3"]',siteBody.HAaddress.master_wan2gw)
           cy.typeValueBydatacy('[data-cy="wanipAddress4"]',siteBody.HAaddress.standby_wan2ip)
           cy.typeValueBydatacy('[data-cy="wanmask4"]',siteBody.HAaddress.standby_wan2mask)
           cy.typeValueBydatacy('[data-cy="wangateway4"]',siteBody.HAaddress.standby_wan2gw)
    }}
    siteBody.lans.forEach(lan => {
      if (lan.hasOwnProperty('name')) {
          if (lan.name=='LAN1') {
              setSiteLan(siteBody.type,lan.name,lan)}
          else {
              cy.get('.el-icon-circle-plus').eq(1).click()
              setSiteLan(siteBody.type,lan.name,lan)
          }
      }
    })
    if (siteBody.hasOwnProperty("4G")){
      setSite4G(siteBody["4G"])
    }
    if (siteBody.dyn_routing){
      setDynRouting(siteBody.dyn_routing)
    }
    cy.clickButtonWithLable('确 定')
    if (siteBody.sameNet){
      cy.get('.el-message-box').within(()=>{
        cy.contains("确定").click()
      })
    }

}

export function CheckWebSiteReadonly(){
  cy.get('[data-cy=siteDialog]').within(() =>{
    cy.get('input').should('have.attr','disabled','disabled')
})
    cy.contains('取 消').click()
}

export function editWebSite(siteBody){
  setSiteBaseInfo(siteBody)
  siteBody.wans.forEach(wan => {
      if (wan.name!='WAN1') {
          cy.get('[data-cy=siteWanList]').then(() =>{
              if (Cypress.$('[data-cy=siteWanList]').length < parseInt(wan.name.charAt(wan.name.length-1))){
                  cy.log('siteWanList.length < wan ' + wan.name.charAt(wan.name.length-1))
                  cy.get('.el-icon-circle-plus').eq(0).click()
              }
          })
      }
      setSiteWan(siteBody.type,wan.name,wan)
  })
  siteBody.lans.forEach(lan => {
      if (lan.hasOwnProperty('name')) {
          if (lan.name!='LAN1') {
              cy.get('[data-cy=siteLanList]').then(() => {
                  if (Cypress.$('[data-cy=siteLanList]').length < parseInt(lan.name.charAt(lan.name.length - 1))) {
                      cy.log('siteLanList.length < lan ' + lan.name.charAt(lan.name.length-1))
                      cy.get('.el-icon-circle-plus').eq(1).click()
                  }
              })
          }
          setSiteLan(siteBody.type,lan.name,lan)
      }
    })
  if (siteBody.hasOwnProperty("wifi")){
    setSiteWifi(siteBody.wifi)
  }
  cy.clickButtonWithLable('确 定')
}

export function createWebUnion(unionBody){
  cy.contains('添加').click()
  cy.contains(unionBody.unionType).click()
  if(unionBody.unionType == "Hub-spoken"){
    cy.get('[data-cy="unionDialog"]').within(() => { 
      cy.typeElinputWithLable('Hub站点',unionBody.hubSite)
      cy.typeMultiElinputWithLable('spoken站点', unionBody.spokenSites)
      if(unionBody.office){cy.checkCheckBoxWithLable('互联网模式')}
      else{cy.unCheckCheckBoxWithLable('互联网模式')}
      if(unionBody.private){cy.checkCheckBoxWithLable('专线模式')}
      else{cy.unCheckCheckBoxWithLable('专线模式')}
      cy.typeInputWithLable('限速',unionBody.bondSpeed)
      cy.clickButtonWithLable('确 定')
    })
  }
  else if(unionBody.unionType == "普通"){
    cy.get('[class=el-dialog]').within(() => { 
      cy.typeElinputWithLable('站点1',unionBody.site1)
      cy.typeElinputWithLable('站点2', unionBody.site2)
      if(unionBody.office){cy.checkCheckBoxWithLable('互联网模式')}
      else{cy.unCheckCheckBoxWithLable('互联网模式')}
      if(unionBody.private){cy.checkCheckBoxWithLable('专线模式')}
      else{cy.unCheckCheckBoxWithLable('专线模式')}
      cy.typeInputWithLable('限速',unionBody.bondSpeed)
      cy.clickButtonWithLable('确 定')
    })
  }
  else {}
}

const timeLable = ["今天","昨天","前天","本月","上月","最近2天","最近一周","最近5分钟","最近1小时","最近12小时","最近24小时"]
const selectTimeLable = ["昨天","一周前"]

export function changeViewByTimeLable(timeText){
  cy.get('[data-cy="displayTime"]').click()
  cy.contains(timeText).click()
}

export function checkButton(){
  cy.get('[data-cy="displayTime"]').click()
  cy.get('[data-cy="timePickerStart"]').click()
  cy.get('[aria-label="前一年"]').click()
  cy.get('[aria-label="上个月"]').click()
  cy.get('[aria-label="后一年"]').click()
  cy.get('[aria-label="下个月"]').click()
  cy.get('[class="el-picker-panel__footer"]').contains("确定").click({force: true})
  cy.get('[data-cy="timePickerApply"]').click({force: true})
}

export function changeViewSelectLable(timeText){
  cy.get('[data-cy="displayTime"]').click()
  cy.get('[data-cy="timePickerStart"]').click()
  cy.get('button').contains(timeText).click()
}

export function walkTimeTable(){
  timeLable.forEach(time => {
    changeViewByTimeLable(time)
  })
  checkButton()
  cy.get('[data-cy="displayTime"]').click()
  cy.get('[data-cy="timePickerStart"]').click()
  selectTime("2018-04-22 12:43:22",0)
  cy.get('[data-cy="timePickerEnd"]').click()
  selectTime("2018-04-23 15:23:25",1)
  cy.get('[data-cy="timePickerApply"]').click({force: true})
}


const month = ["一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"]
export function selectTime(time,index){
  var ymd= time.split(" ")[0].split("-")
  var tm = time.split(" ")[1].split(":")
  cy.get('[class="el-picker-panel__body-wrapper"]').eq(index).within( ()=> {
    cy.get('[class="el-date-picker__header-label"]').contains("年").click()
    cy.get('[aria-label="前一年"]').click()
    cy.contains(ymd[0]).click()
    cy.contains(month[parseInt(ymd[1])-1]).click()
    cy.get('[class="el-picker-panel__content"]').contains(ymd[2]).click()
    cy.get('[placeholder="选择时间"]').click()
    cy.get('[class="el-time-spinner__wrapper el-scrollbar"]').eq(0).contains(parseInt(tm[0])-1).click()
    cy.get('[class="el-time-spinner__wrapper el-scrollbar"]').eq(1).contains(parseInt(tm[1])-1).click()
    cy.get('[class="el-time-spinner__wrapper el-scrollbar"]').eq(2).contains(parseInt(tm[2])-1).click()
  })
  cy.get('[class="el-time-panel__footer"]').eq(index).contains("确定").click()
  cy.get('[class="el-picker-panel__footer"]').eq(index).contains("确定").click()
}

export function searchArea(content){
  cy.get('[data-cy="popSearch"]').clear().type(content)
}

export function searchPop(content){
  cy.get('input[class="el-select__input"]').clear().type(content)
}

export function checkPopList(content){
  cy.get('li.el-select-dropdown__item').filter(':visible').contains(content)
}

export function checksearchPopNum(num){
  cy.get('li.el-select-dropdown__item:visible').should(($tb)=>{
    expect($tb).to.have.length(num)
   })
}

export function addPoptoCode(){
  cy.get('li.el-select-dropdown__item:visible').click({ multiple: true })
  cy.contains('配置服务').click()
  cy.contains('button', '确 定').click()
}

export function showSidebar(show){
  cy.get('div[id=hamburger-container]').then((div) => {
    if (div.hasClass('is-active')) {
         if (!(show)) { div.click()}
    } else {
         if (show) {div.click()}          
    }
  })
}

export function ClickSidebarMenu(menu){
  showSidebar(true)
  cy.get('div>.sidebar-container').within( () => {
    cy.get('[slot="title"]').contains(menu).parents('li').then(($m) => {
      if ($m.hasClass('is-opened')) {
    } else
    {  cy.get('[slot="title"]').contains(menu).parents('li').click()}
    })

  })
}

export function checkSidebarMenuList(menu,expect_menu){
  cy.contains(menu).parents('li').parent('div').within( () => {
   cy.get('span')
   .each(($li, index, $lis) => {
     expect($li.text()).to.eq(expect_menu[index])
   })
  })
}

export function setSiteAudit(audit, mac){
  cy.get('[data-cy="audit"]').within( () => {
    if (audit){
      cy.checkCheckBoxWithLable('审计')
    }else{
      cy.unCheckCheckBoxWithLable('审计')
    }
  })
  if (audit){
    cy.get('[data-cy="auditMac"]').within( () => {
      cy.typeInputWithLable('MAC地址', mac)
    })
  }
  
}

export function setSiteAuth(auth){
  cy.get('[data-cy="auth"]').within( () => {
    if (auth){
      cy.checkCheckBoxWithLable('认证')
    }else{
      cy.unCheckCheckBoxWithLable('认证')
    }
  })
}

export function openSiteModifyPage(siteName, siteSN){
  cy.get('[data-cy="siteSearch"]').clear().type(siteName)
  cy.contains('共 1 条')
  rowContains('[data-cy=siteTable]',siteName,1,2,[siteSN])
  cy.get('[data-cy="siteTable"]').contains(siteName).parents('tr').within(() => {
   cy.contains('button', '编辑').click()
  })
  cy.contains('备注')
}

export function ClickSidebarSubMenu(menu,sub_menu,expect){
  cy.contains(menu).click()
  cy.contains(menu).parents('li').parent('div').within( () => {
   cy.contains(sub_menu).parent().click()
  })
  cy.get('[data-cy='+expect+']', { timeout: 2000 }).should('be.visible')
}

export function switchTomenu(menu){
  cy.contains(menu).click({force: true})
}

export function createAcl(acl){
  cy.get('[data-cy="addRule"]').click()
    cy.get('[data-cy="name"]').clear().type(acl.name)
    if(acl.site_name){cy.ClickSelectValue('[data-cy="selectSourceSite"]', acl.site_name)}
    cy.get('[data-cy="srcCIDR"]').clear()
    cy.get('[data-cy="dstCIDR"]').clear()
    if(acl.srcCIDR){cy.get('[data-cy="srcCIDR"]').type(acl.srcCIDR)}
    if(acl.dstCIDR){cy.get('[data-cy="dstCIDR"]').type(acl.dstCIDR)}
    if(acl.protocol){cy.ClickMultiDropDownValue('[data-cy="protocolNo"]', acl.protocol)}
    if(acl.dstPort){cy.get('[data-cy="dest_port"]').clear().type(acl.dstPort)}
    if(acl.strategy){
        cy.ClickDropDownValue('[data-cy="strategy"]', 'li.el-select-dropdown__item', acl.strategy)}
    if(acl.priority){cy.get('[data-cy="priority"]').clear().type(acl.priority)}
    cy.get('[data-cy="confirmEdit"]').click()
    cy.contains(acl.hint)
  }

export function modifyAreaCode(areaCode, hostname){
  searchArea(areaCode)
  cy.get('[data-cy="popConfigs"]').contains(areaCode).parents('tr').within(() => {
    cy.contains('button', '编辑').click()
  })
  cy.contains('button', '添加').click()
  searchPop(hostname)
  checkPopList(hostname)
  addPoptoCode()
  cy.contains('成功')
}

export  function updateacl(){
    cy.get('[data-cy="apply"]').click()
    cy.contains("应用成功")
  }

  
export function createrouter(router){
  cy.get('[data-cy="addRule"]').click()
    cy.get('[data-cy="name"]').clear().type(router.name)
    if(router.site_name){cy.typeMultiDropDownValue('input.el-cascader__search-input[placeholder="源站点"]',router.site_name,'li[class="el-cascader__suggestion-item"]',[router.site_name])}
    cy.get('[data-cy="srcCIDR"]').clear()
    cy.get('[data-cy="dstCIDR"]').clear()
    if(router.srcCIDR){cy.get('[data-cy="srcCIDR"]').type(router.srcCIDR)}
    if(router.dstCIDR){cy.get('[data-cy="dstCIDR"]').type(router.dstCIDR)}
    if(router.protocol){cy.ClickMultiDropDownValue('[data-cy="protocolNo"]', router.protocol)}
    if(router.srcPort){cy.get('[data-cy="srcPort"]').clear().type(router.srcPort)}
    if(router.dstPort){cy.get('[data-cy="dest_port"]').clear().type(router.dstPort)}
    if(router.site_name){cy.ClickMultiDropDownValue('[data-cy="siteSelect"]',[router.nextHop])}
    if(router.site_name){
      cy.get('div[class="selectSlot"]').within(() => {
        cy.contains(router.nextHop).parent('div').find('input').clear().type(100)
        cy.contains('确定').click()
      })
    }
    if(router.priority){cy.get('[data-cy="priority"]').clear().type(router.priority)}
    cy.get('[data-cy="confirmEdit"]').click()
    cy.contains(router.hint)
  }

export function modifyRouter(modify_router){
  cy.get('[data-cy="rules"]').contains(modify_router.name).parents('tr').within(() => {
    cy.contains('button', '编辑').click()
  })
    if(modify_router.srcCIDR){cy.get('[data-cy="srcCIDR"]').clear().type(modify_router.srcCIDR)}
    if(modify_router.dstCIDR){cy.get('[data-cy="dstCIDR"]').clear().type(modify_router.dstCIDR)}
    if(modify_router.srcPort){cy.get('[data-cy="srcPort"]').clear().type(modify_router.srcPort)}
    if(modify_router.dstPort){cy.get('[data-cy="dest_port"]').clear().type(modify_router.dstPort)}
    if(modify_router.nextHop){
      cy.ClickDropDownValue('[data-cy="nextHop"]', 'li.el-select-dropdown__item', modify_router.nextHop)}
    if(modify_router.priority){cy.get('[data-cy="priority"]').clear().type(modify_router.priority)}
    if(modify_router.action=='confirm'){
      cy.get('[data-cy="confirmEdit"]').click()
      cy.contains('更新成功')
    }
    else{
    cy.get('[data-cy="cancelEdit"]').click()}
}

export function updaterouter(){
    cy.get('[data-cy="apply"]').click()
    cy.contains("应用成功")
  }

  export function changeAlarmPanelView(panel_name) {
    cy.contains(panel_name).click({force: true})
  }
  
  export function setAlertGroup(rule){
    cy.get('[data-cy="name"]').within(() => {
      cy.get('input').clear().type(rule.name)
    })
    rule.contacts.forEach(contacts => {
      cy.get('[data-cy="addLinkman"]').contains("新增联系人").click()
      cy.get('[data-cy="userName"]').last().within(() => {
        cy.get('input').clear().type(contacts.userName)
      })
      cy.get('[data-cy="mobile"]').last().within(() => {
        cy.get('input').clear().type(contacts.mobile)
      })
      cy.get('[data-cy="email"]').last().within(() => {
        cy.get('input').clear().type(contacts.email)
      })
    })
    cy.get('[data-cy="deleteLinkman"]').first().click()
    cy.contains('确 定').click()
  }
  
  export function modifyAlertGroup(user){
    cy.get('[data-cy="userName"]').last().within(() => {
      cy.get('input').clear().type(user.userName)
    })
    cy.get('[data-cy="mobile"]').last().within(() => {
      cy.get('input').clear().type(user.mobile)
    })
    cy.get('[data-cy="email"]').last().within(() => {
      cy.get('input').clear().type(user.email)
    })
    cy.get('[data-cy="deleteLinkman"]').first().click()
    cy.contains('确 定').click()
  }
  
  export function setAlertRule(rule){
    cy.get('[data-cy="groups"]').within(() => {
      cy.get('span > .el-icon-arrow-up').filter(':visible').click()
    })
    rule.alertGroup.forEach(group => {
      cy.get('li.el-select-dropdown__item').filter(':visible').contains(group).click()
    })
    cy.contains('告警上限').click()
    cy.get('[data-cy="name"]').within(() => {
      cy.get('span > .el-icon-arrow-up').click()
    })
    rule.alertType.forEach(aType => {
      cy.get('li.el-select-dropdown__item').filter(':visible').contains(aType).click()
    })
    cy.contains('告警上限').click()
    cy.get('[data-cy="severity"]').within(() => {
      cy.get('span > .el-icon-arrow-up').click()
    })
    rule.severity.forEach(se => {
      cy.get('li.el-select-dropdown__item').contains(se).click()
    })
    cy.contains('告警上限').click()
    cy.get('[data-cy="groupDialog"]').within(() => {
      cy.get('button.el-button--primary').filter(':visible').click({ multiple: true })
    })
  }  

  export function createWebRole(role,webRoleInfo,all=0,companyName=''){
    if (companyName != ''){
      cy.ClickMultiDropDownValueUnVisiable('[data-cy="company"]', [companyName])
    }
    cy.get('[role="dialog"]').within(()=>{
      cy.typeInputWithLable('角色名称',role.role)
      cy.typeInputWithLable('角色描述',role.desc)
      if (all){
        chooseAllWebRoleAuth()
      }else {
        clearWebRoleAuth()
        for (const roleInfo of webRoleInfo){
            clickRole(roleInfo.level, roleInfo.roleList)
        }
    }
    cy.contains('确认').click()
  })
}

export function clearWebRoleAuth(){
    cy.get('[role="tree"]').children('[role="treeitem"]').children('[class="el-tree-node__content"]').children('label').click({ multiple: true ,force: true})
    cy.get('[role="tree"]').children('[role="treeitem"]').children('[class="el-tree-node__content"]').children('label').click({ multiple: true ,force: true})
}

export function checkLevel2RoleList(mode, level1, expectList,expectGList=[]){
  let checkList = (mode == 'global') ? expectList.concat(expectGList) : expectList 
  cy.get('[role="tree"]').children('[role="treeitem"]').children('[class="el-tree-node__content"]').contains(level1).parents('[role="treeitem"]').children('[role="group"]').children('[role="treeitem"]').not('[style="display: none;"]').should('have.length',checkList.length).then(level2Items =>{
    for (const treeItem of level2Items){
      cy.wrap(treeItem).children('[class="el-tree-node__content"]').invoke('text').then((text) => {
        checkList.includes(text.trim())
    })
    } 
  })
}

export function checkLevel1RoleList(checkList){
  cy.get('[role="tree"]').children('[role="treeitem"]').should('have.length', checkList.length).each(($treeItem, i) => {
    cy.get('[role="tree"]').children('[role="treeitem"]').eq(i).children('[class="el-tree-node__content"]').contains(checkList[i])
  })
}

export function clickRole(level,roleList){

  cy.get('[role="tree"]').children('[role="treeitem"]').children('[class="el-tree-node__content"]').contains(roleList[0]).parent('div').parent('[role="treeitem"]').within(()=>{
  if (level == 1){
    cy.contains(roleList[0]).parent('[class="el-tree-node__content"]').children('[class="el-checkbox"]').click()
  }else if (level == 2){
    cy.contains(roleList[1]).parents('[class="el-tree-node__content"]').within(()=>{
      cy.get('[class="el-checkbox"]').click()
    })
  }else{
    cy.contains(roleList[1]).parent('[class="el-tree-node__content"]').parent('[role="treeitem"]').children('[role="group"]').within(()=>{
      cy.contains(roleList[2]).parents('[class="el-tree-node__content"]').within(()=>{
        cy.get('[class="el-checkbox__inner"]').click()
      })
    })
  }

})
}

export function chooseAllWebRoleAuth(){
  cy.get('[role="tree"]').children('[role="treeitem"]').children('[class="el-tree-node__content"]').children('label').click({ multiple: true ,force: true})
  cy.get('[role="tree"]').children('[role="treeitem"]').children('[class="el-tree-node__content"]').children('label').click({ multiple: true ,force: true})
  cy.get('[role="tree"]').children('[role="treeitem"]').children('[class="el-tree-node__content"]').children('label').click({ multiple: true ,force: true})
}

export function setGlobalUser(user, companyList=[], accountType='公司'){
  cy.contains('新建').click()
  if (accountType == '全局') {
    cy.ClickSelectValue2('[data-cy="accountType"]',accountType)
    cy.ClickMultiDropDownValueUnVisiable('[data-cy="companyList"]', companyList)
  } else if (accountType == '公司'){
    cy.ClickSelectValue2('[data-cy="company"]',companyList[0])
  }
  setCommonUser(user)
}

export function setCommonUser(user){
  cy.get('[data-cy=userForm]').within(() => { 
    cy.typeInputWithLable('用户名',user.username)
    cy.typeInputWithLable('密码',user.password)
    user.roles.forEach(role =>{
      cy.typeElinputWithLable('角色',role)
    })
    cy.checkCheckBoxWithLable('启用状态')
    cy.typeInputWithLable('联系方式',user.contact)       
  })
  cy.contains('确认').click() 
}

export function setUser(user){
  cy.contains('新建').click()
  setCommonUser(user)
}

export function setDistributorUser(user){
    cy.contains('新建').click()
        .then(() => {
            cy.get('form').within(() => {
                cy.typeElinputWithLable('账号类型', '渠道')
                cy.typeInputWithLable('渠道名称', user.company)
                cy.typeInputWithLable('用户名',user.username)
                cy.typeInputWithLable('密码',user.password)
                cy.typeElinputWithLable('角色',"admins")
                cy.checkCheckBoxWithLable('启用状态')
                cy.typeInputWithLable('联系方式',user.contact)
            })
        })
    cy.contains('确认').click()
}

export function checkRightAuth(authScope,globalView=false,companyName=''){

  //check auth right
  authScope.forEach(scope => {
    var as = scope.roleList
    var shouldCheck = true
    
    if (globalView){ 
      var expectRole = menuList.admin_g_view
    }else {
      var expectRole = menuList.admin_c_view}
    
    if (!Object.keys(expectRole).includes(as[0])){shouldCheck = false}
    if ((scope.level > 1) && ! expectRole[as[0]].includes(as[1])){shouldCheck = false}
   
    if (shouldCheck && scope.checkRole != []){ 
        ClickSidebarMenu(as[0])
        if (scope.level == 1){
          var level2CheckItem = expectRole[as[0]].slice(1, -1)
        }else{
          var level2CheckItem = [as[1]]
        }
        level2CheckItem.forEach(level2 => {
            cy.contains(level2).click({force:true})
            switch (level2) {
              case "站点注册": check_zdzc_auth(scope.checkRole,globalView)
              break;
              case "设备管理": check_sbgl_auth(scope.checkRole)
              break;
              case "拓扑管理": check_tpgl_auth(scope.checkRole,globalView,companyName)
              break;
              case "区域码管理": if (!globalView){check_qymgl_auth(scope.checkRole)}
              break;
              case "区域码管理(全局)": if (globalView) {check_qymgl_auth(scope.checkRole)}
              break;
              case "防火墙": check_fhqgl_auth(scope.checkRole)
              break; 
              case "路由管理": check_lygl_auth(scope.checkRole)
              break;
              case "策略管理": check_clgl_auth(scope.checkRole,globalView)
              break;    
              case "审计配置": check_sjpz_auth(scope.checkRole)
              break;    
              case "设备告警": check_sbgj_auth(scope.checkRole)
              break;     
              case "个人账号": check_grzh_auth(scope.checkRole)
              break;  
              case "角色管理": check_jsgl_auth(scope.checkRole,globalView)
              break;
              case "公司管理": check_gsgl_auth(scope.checkRole)
              break;
              case "行政区划": check_yzqh_auth(scope.checkRole)
              break;
              case "Pop点管理": check_pop_auth(scope.checkRole)
              break;
              case "服务管理": check_fwgl_auth(scope.checkRole)
              break;
              case "数据分析": check_sjfx_auth()
              break;
              case "实时监控": check_ssjk_auth()
              break;
              case "上网日志": check_swrz_auth()
              break;
              case "统计报表": check_tjbb_auth()
              break;
              case "操作日志": check_czrz_auth()
              break;
              case "登录日志": check_dlrz_auth()
              break;
              default: console.log(`Sorry, new add item`);
           }
          })
        
      }
    })
}

export function check_zdzc_auth(authNum,globalView){
    if (globalView){authNum = 'r'}
    if (authNum == 'w'){
      //全局用户的编辑和添加功能在站点的用例中测试
      cy.contains("编辑")
      cy.contains('添加')
      cy.contains('批量建站')
    }else{
        cy.contains('添加').should('not.exist')
        cy.contains('批量建站').should('not.exist')
        cy.contains("详情").click()
        cy.get('[data-cy=siteDialog]').within(() => { 
                cy.contains("内网网段").parent('div').within(() => {
                if (authNum == 'r'){
                      cy.get('[class="el-textarea is-disabled"]').should('exist')
                }else{
                     cy.get('[class="el-textarea"]').should('exist')
            }
          })
        cy.contains("取 消").click()
      })
    }

}

export function check_sbgl_auth(authNum){
  if (authNum == 'r'){
    cy.contains('批量告警处理').should('not.exist')
    cy.contains('重启').should('not.exist')
    cy.get('[role="switch"]').should('have.class','el-switch is-disabled')
  }else{
    cy.contains('批量告警处理').click()
    cy.contains('重启').click()
    cy.contains('确定').click()
    cy.get('[role="switch"]').should('not.have.class','is-disabled')
  }
  cy.contains('详情').click()
  cy.url().should('contain', 'deviceDetail')
}

export function check_tpgl_auth(authNum,globalView,companyName){
  if (globalView){authNum = 'r'}
  if (authNum == 'r'){
    //全局用户的编辑和添加功能在union的用例中测试
    cy.contains('添加').should('not.exist')
    cy.contains('编辑').should('not.exist')
    cy.contains('删除').should('not.exist')
  }else{
    cy.contains('添加')
    cy.contains('编辑')
    cy.contains('删除')
  }
  cy.contains('拓扑网络图')
  if (globalView){
    cy.TypeAndSearch('[data-cy="unionSearch"]', companyName)
  }
  cy.contains('共 1 条')
}

export function check_fhqgl_auth(authNum){
  cy.wait(1000)
  if (authNum == 'r'){
    cy.contains('新增规则').should('not.exist')
    cy.contains('应用').should('not.exist')
  }else{
    createAcl(testFirewallBody.aclAuthBody)
    updateacl()
  }
}

export function check_qymgl_auth(authNum){
  if (authNum == 'r'){
    cy.contains('编辑').should('not.exist')
    cy.contains('共 304 条')
  }else{
    modifyAreaCode(saasSearchPatternBody.shanghaiCode.areaCode, testServiceBody.putSaasBody.hostname)
  }
}

export function check_lygl_auth(authNum){
  if (authNum == 'r'){
    cy.contains('新增规则').should('not.exist')
    cy.contains('应用').should('not.exist')
  }else{
    createrouter(testRouterBody.routerAuthBody)
    updaterouter()
  }
}
export function check_sbgj_auth(authNum){
  changeAlarmPanelView("告警组设置")
  if (authNum == 'r'){
    cy.contains('新增').should('not.exist')
  }else{
    cy.get('[data-cy=addReceiver]').filter(':visible').click()
    setAlertGroup(alert.alertGroup)
    cy.contains("创建成功")
  }
}

export  function check_clgl_auth(authNum, globalView){
  if (((authNum == 'r_apply') || (authNum == 'r_all')) && !globalView){
    cy.get('[role="tab"]').contains('策略应用').click()
    cy.contains('批量删除').should('not.exist')
    cy.contains('新增策略').should('not.exist')
    cy.contains('策略数')
  }
  if ((authNum == 'r_all')||(authNum == 'w_companyView')&&globalView) {
    cy.get('[role="tab"]').contains('策略模板').click()
    cy.contains('批量导入').should('not.exist')
    cy.contains('新增').should('not.exist')
    cy.contains('编辑').should('not.exist')
    cy.contains('删除').should('not.exist')
    cy.contains('批量删除').should('not.exist')
    cy.contains('导出 Excel')
    cy.contains('模板名称')
    cy.get('[role="tab"]').contains('规则标识').click()
    cy.contains('批量导入').should('not.exist')
    cy.contains('新增').should('not.exist')
    cy.contains('编辑').should('not.exist')
    cy.contains('删除').should('not.exist')
    cy.contains('批量删除').should('not.exist')
    cy.contains('导出 Excel')
    cy.contains('规则名称')
    cy.get('[role="tab"]').contains('场景管理').click()
    cy.contains('新增场景').should('not.exist')
    cy.contains('编辑').should('not.exist')
    cy.contains('删除').should('not.exist')
    cy.contains('批量删除').should('not.exist')
    cy.contains('模板数')
  }

  if (authNum == 'r_apply'){
    cy.get('[role="tab"]').contains('策略模板').should('not.exist')
    cy.get('[role="tab"]').contains('规则标识').should('not.exist')
    cy.get('[role="tab"]').contains('场景管理').should('not.exist')
  }
  
  if (((authNum == 'w_apply') || (authNum == 'w_companyView') || (authNum == 'w')) && !globalView) {
    cy.get('[role="tab"]').contains('策略应用').click()
    cy.contains('批量删除')
    cy.contains('新增策略')
    cy.contains('策略数')
  }

  if ((authNum == 'w')||((authNum == 'w_companyView')&& !globalView)) {
    //实际创建放入在策略管理的用例里面
    cy.get('[role="tab"]').contains('策略模板').click()
    cy.contains('批量导入')
    cy.contains('新增')
    cy.contains('编辑')
    cy.contains('删除')
    cy.contains('批量删除')
    cy.contains('导出 Excel')
    cy.contains('模板名称')
    cy.get('[role="tab"]').contains('规则标识').click()
    cy.contains('批量导入')
    cy.contains('新增')
    cy.contains('编辑')
    cy.contains('删除')
    cy.contains('批量删除')
    cy.contains('导出 Excel')
    cy.contains('规则名称')
    cy.get('[role="tab"]').contains('场景管理').click()
    cy.contains('新增场景')
    cy.contains('编辑')
    cy.contains('删除')
    cy.contains('批量删除')
    cy.contains('模板数')
  }

}
export function check_sjpz_auth(authNum){
  var tabList = ["全局配置", "认证参数","备份配置"]
  for (const tab of tabList){
        cy.get('[role="tab"]').contains(tab).click()
        if (authNum == 'r'){
           cy.contains('保存').should('be.disabled')}
        else{
          cy.contains('保存')
        }
      }
  cy.get('[role="tab"]').contains('认证黑白名单').click()
  cy.contains('查询')
  if (authNum == 'r'){
    cy.contains('新增').should('be.disabled')
    cy.contains('删除').should('be.disabled')}
 else{
    cy.contains('新增')
    cy.contains('删除')}
  
}
export function check_sjfx_auth(){
  cy.contains("网络服务使用情况")
  cy.contains("网站访问情况统计")
  cy.contains("用户流量TOP10")
}
export function check_ssjk_auth(){
  cy.contains("在线用户")
  cy.contains("实时IP监控")
  cy.contains("实时网站访问")
}
export function check_swrz_auth(){
  cy.contains("上下线日志")
  cy.contains("网络连接日志")
  cy.contains("DNS解析日志")
}
export function check_tjbb_auth(){
  cy.contains("导出报表")
}
export function check_czrz_auth(){
  cy.get('[data-cy="logTable"]').should('exist')
}
export function check_dlrz_auth(){
  cy.get('[data-cy="logTable"]').should('exist')
}

export function check_grzh_auth(authNum){
  if (authNum == 'r'){
    cy.contains('新建').should('not.exist')
  }else{
    setUser(UserBody.checkAuthUser)
    cy.contains("创建成功")
  }
}

export function check_jsgl_auth(authNum, globalView){
  if (authNum == 'r'){
    cy.contains('新建').should('not.exist')
  }else{
    if (globalView){
      cy.contains('新建')
    }
    else{
        cy.get('[data-cy="createRole"]').click()
        createWebRole(RoleBody.webAuthRole,[], 1)
        cy.contains('创建成功')
    }
  }
}

export function check_gsgl_auth(authNum){
  if (authNum == 'r'){
    cy.contains('添加').should('not.exist')
    cy.contains('编辑').should('not.exist')
  }else{
    setCompany(testCompanyBody.testCompanyForUser)
    cy.contains('创建成功')
  }
}

export function check_yzqh_auth(authNum){
  if (authNum == 'r'){
    cy.contains('新建区划').should('not.exist')
    cy.contains('恢复默认').should('not.exist')
  }else{
    defaultRegionTemplate()
  }
}

export function check_pop_auth(authNum){
  if (authNum == 'r'){
    cy.contains('删除').should('not.be.visible')
    cy.contains('新增').should('not.exist')
    cy.contains('批量操作').should('not.exist')
  }else{
    cy.contains('删除')
    cy.contains('新增')
    cy.contains('批量操作')
  }
}

export function check_fwgl_auth(authNum){
  if (authNum == 'r'){
    cy.contains('删除').should('not.be.visible')
    cy.contains('新增').should('not.exist')
    cy.contains('编辑').should('not.exist')
    cy.contains('批量操作').should('not.exist')
  }else{
    cy.contains('删除')
    cy.contains('新增')
    cy.contains('编辑')
    cy.contains('批量操作')
  }
}

export function enableSiteAuthAudit(siteName, deviceId, auth, audit, siteMac){
  openSiteModifyPage(siteName, deviceId)
  setSiteAudit(audit, siteMac)
  setSiteAuth(auth)
  cy.clickButtonWithLable('确 定')
  cy.contains('更新成功')
}

export function configAudit(url, port){
  changeAuditPanelView('全局配置')
  cy.get('[data-cy="auditGlobalConfig"]').within(() => {
      cy.checkCheckBoxWithLable('启用审计')
      cy.typeInputWithLable('云审计服务', url)
      cy.typeValueBydatacy('[data-cy="auditGlobalConfig.serverPort"]', port)
      cy.contains('保存').click()
  })
}

export function enableAudit(url, port){
  configAudit(url, port)
  cy.contains('保存成功') 
}

export function enableAuth(innerUrl, outUrl, redirectUrl, outPort, innerPort, bondTimeout, noTrafficTimeout, authType, authTypeParam){
  configAuth(innerUrl, outUrl, redirectUrl, outPort, innerPort, bondTimeout, noTrafficTimeout, authType, authTypeParam)
  cy.contains('保存成功') 
}

export function configAuth(innerUrl, outUrl, redirectUrl, outPort, innerPort, bondTimeout, noTrafficTimeout, authType, authTypeParam){
    changeAuditPanelView('认证参数')
    cy.get('[data-cy="second-pane"]').within(() => {
        cy.checkCheckBoxWithLable('启用认证')
        cy.contains('服务器')
        cy.typeInputWithLable('内网用认证URL', innerUrl)
        cy.typeInputWithLable('外网用认证URL', outUrl)
        cy.typeValueBydatacy('[data-cy="authConfig.intranetPort"]', outPort)
        cy.typeValueBydatacy('[data-cy="authConfig.portalPort"]', innerPort)
        cy.typeInputWithLable('重定向URL', redirectUrl)
        cy.typeInputWithLable('绑定超时', bondTimeout)
        cy.typeInputWithLable('无流量超时', noTrafficTimeout)
    })
    if (authType == 'Radius认证'){
      configAuthRadius(authTypeParam.ip, authTypeParam.port, authTypeParam.radiusType, authTypeParam.radiusKey)
    }else{
      configLdapRadius(authTypeParam.ip, authTypeParam.port, authTypeParam.adminAccount, authTypeParam.password, authTypeParam.rootDN)
    }
    cy.get('[data-cy="second-pane"]').within(() => {
        cy.contains('保存').click()
    })
}

export function changeAuditPanelView(panel_name) {
  cy.contains(panel_name).click({force: true})
}

function configAuthRadius(radiusIp, radiusPort, radiusType, radiusKey){
  cy.get('[data-cy="authConfigType"] input:visible').invoke('val').then(text=>{
    if (text == 'Radius认证'){

    }else{
      cy.ClickSelectValue('[data-cy="authConfigType"]>div .el-select', 'Radius认证')
    }
  })
  cy.typeInputWithLable('IP地址', radiusIp)
  cy.typeInputWithLable('端口', radiusPort)
  cy.get('[data-cy="authConfig.radiusServer.authMethod"] input:visible').invoke('val').then(text=>{
    if (text == radiusType){

    }else{
      cy.ClickSelectValue('[data-cy="authConfig.radiusServer.authMethod"]>div .el-select', radiusType)
    }
  })
  cy.typeInputWithLable('秘钥', radiusKey)
}

function configLdapRadius(ldapIp, ldapPort, adminAccount, password, rootCN){
  cy.get('[data-cy="authConfigType"] input:visible').invoke('val').then(text=>{
    if (text == 'LDAP认证'){

    }else{
      cy.ClickSelectValue('[data-cy="authConfigType"]>div .el-select', 'LDAP认证')
    }
  })
  cy.typeInputWithLable('IP地址', ldapIp)
  cy.typeInputWithLable('端口', ldapPort)
  cy.typeInputWithLable('管理员账号', adminAccount)
  cy.typeInputWithLable('密码', password)
  cy.typeInputWithLable('根节点DN', rootCN)
}

export function setCompany(company){
  cy.contains('添加').click()
  cy.get('[data-cy=companyDialog]').within(() => { //will find by data-cy (new company dialog)
    cy.typeInputWithLable('公司',company.name)
    cy.typeInputWithLable('所属渠道',company.channel)
    cy.typeInputWithLable('公司英文名',company.englishName)
    cy.typeInputWithLable('联系人',company.linkman)
    cy.typeInputWithLable('固定电话',company.contact)
    cy.typeInputWithLable('手机',company.mobile)
    cy.typeTextareaWithLable('备注',[company.remark])
    cy.typeInputWithLable('邮箱',company.mail)
    cy.typeInputWithLable('地址',company.address)
    cy.typeInputWithLable('英文地址',company.englishAddress)
    cy.clickElcascaderWithLable("城市/地区")
  })
  cy.get('[class=el-cascader-panel]').within(() => {
    company.city.forEach(address => {
      cy.get('li').contains(address).click()
    })
  })
  cy.clickButtonWithLable('确 定')
}

export function defaultRegionTemplate(){
  cy.contains('button','恢复默认').click({force: true})
  cy.contains('确定').click()
  cy.contains('重置成功')
}

export {user, password}
