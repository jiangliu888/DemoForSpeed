import {companyBodyTemplate, siteTemp, unionTemplate, testCPEGlobalConfigBody} from "./variables-utils"

const companyUrl = '/api/v1/companies'
const userUrl = '/api/v1/users'
const roleUrl = '/api/v1/roles'
const managerUrl = '/api/v1/controllerManagers/12'
const openflowUrl = '/api/v1/controllerOpenflows/12'
const netAlgConfigUrl = '/api/v1/controllerAlgorithms/pattern'
const globalConfigUrl = '/api/v1/cpeGlobal'
const saasSearchPattern = '/api/v1/saasSearchPatterns'
const popConfigUrl = '/api/v1/popConfigs'
const popUrl = '/api/v1/pops'
const cpeGlobalConfUrl = '/api/v1/cpeGlobal'
const mgrGroupUrl = '/api/v1/mgr/groups'
const mgrRuleUrl = '/api/v1/mgr/rules'
const logUrl = '/api/v1/logs/operations'


export function getLogsNumber (token,options){
  // action: add, del, update
  // options格式: {resourceType:'site',action:'add',company:'Company1Log'}
  var {resourceType='',action='',company='',username='',detail=''} = options
  cy.log(resourceType)
  cy.log(action)
  if (company){
    getIdByCompanyName(token, company)
    cy.get('@companyId').then(companyId=>{
      cy.request({
        method:'GET', 
        url:logUrl, 
        auth: {'bearer':token},
        qs:{'resourceType':resourceType,'action':action,'companyId':companyId,'username':username,'detail':detail,'limit':40,'sort':-1}
      }).its('body.total').as('logsNumber')
    })  
  } else {
    cy.request({
      method:'GET', 
      url:logUrl, 
      auth: {'bearer':token},
      qs:{'resourceType':resourceType,'action':action,'username':username,'detail':detail,'limit':40,'sort':-1}
    }).its('body.total').as('logsNumber')
  }
  
}

export function createManager (token, body) {
  cy.request({
    method:'PUT', 
    url:managerUrl , 
    auth: {'bearer':token},
    body:body
  })
}

export function createOpenflow (token, body) {
  cy.request({
    method:'PUT', 
    url:openflowUrl , 
    auth: {'bearer':token},
    body:body
  })
}

export function createNetAlg (token, body) {
  cy.request({
    method:'PUT', 
    url:netAlgConfigUrl , 
    auth: {'bearer':token},
    body:body
  })
}

export function createGlobalConfig (token, body) {
  cy.request({
    method:'PUT', 
    url:globalConfigUrl , 
    auth: {'bearer':token},
    body:body
  })
}

export function createSaasSearchPatternByCode (token, Code, body) {
  getIdByAreaCode(token,Code)
  cy.get('@codeId').then(codeId => {
    if(codeId != ""){
      body._id = codeId
      cy.request({
        method:'PUT', 
        url:saasSearchPattern + "/" + Code, 
        auth: {'bearer':token},
        body:body
      })
    }
  })
}

export function getIdByAreaCode(token, Code) {
  cy.request({
    method:'GET', 
    url:saasSearchPattern, 
    auth: {'bearer':token}
  }).its('body.results').as('codesInfo').then(($codesInfo) => {
    let re_code = $codesInfo.find(function(codeInfo){
      if(codeInfo.areaCode == Code){
        return codeInfo
      }
    })
    if (typeof(re_code) != "undefined")
    {
      cy.wrap(re_code._id).as("codeId")
    }
    else{
      cy.wrap("").as("codeId")
    }
  })
}

export function deletePop(token, neid){
  cy.request({
    method:'DELETE', 
    url:popConfigUrl + "/" + neid , 
    failOnStatusCode: false,
    auth: {'bearer':token}
  })
}

export function deletePopByPopId(token, popId, popType = 6){
  getPopNEidByPopId(token,popId,popType)
  cy.get('@neId').then(neId => {
    if(neId != ""){
      deletePop(token,neId)
    }
  })
}

export function putPop(token, body){
  cy.request({
    method:'PUT', 
    url:popConfigUrl + "/4" , 
    auth: {'bearer':token},
    body:body
  })
}

export function initCpeGlobalConf (token){
  let tmp = JSON.parse(JSON.stringify(testCPEGlobalConfigBody.ST))
  tmp.controllers[0].mode = "gateway"
  tmp.controllers[1].mode = "parallel"
  tmp.controllers[2].mode = "series"
  cy.request({
    method:'PUT',
    url:cpeGlobalConfUrl,
    auth: {'bearer':token},
    body:tmp
  })
}

export function createCompany (token, body){
  cy.request({
    method:'POST', 
    url:companyUrl, 
    auth: {'bearer':token},
    body:body
  }).its('body').as('companyInfo')
}

export function createAlertGroup (token, companyName, body){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      body.companyId = companyId
      cy.request({
        method:'POST', 
        url:mgrGroupUrl, 
        auth: {'bearer':token},
        body:body
      }).its('body.id').as('AlertGroupId')
    }
  })
}

export function createAlertRule (token, companyName, body, alertId){
  body.groups = [alertId]
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      body.companyId = companyId
      cy.request({
        method:'POST', 
        url:mgrRuleUrl, 
        auth: {'bearer':token},
        body:body
      }).its('body.id').as('AlertRuleId')
    }
  })
}

export function deleteAllAlertRule(token, companyName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        cy.request({
          method:'GET', 
          url:mgrRuleUrl + "?companyId=" + companyId, 
          auth: {'bearer':token},
          failOnStatusCode: false
        }).then((response) => {
          if (response.status != 404){
            response.body.forEach(rule => {
              deleteAlertRule(token, rule.ruleId)
          })
        }
       })
      }
  })  
}

export function deleteAlertRule (token, ruleId) {
  cy.request({
    method:'DELETE', 
    url:mgrRuleUrl + "/" + ruleId, 
    auth: {'bearer':token}
  })
}

export function deleteAllAlertGroup(token, companyName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        cy.request({
          method:'GET', 
          url:mgrGroupUrl + "?companyId=" + companyId, 
          auth: {'bearer':token},
          failOnStatusCode: false
        }).then((response) => {
          if (response.status != 404){
            response.body.forEach(group => {
              deleteAlertGroup(token, group.groupId)
          })
        }
       })
      }
  })  
}

export function deleteAlertGroup (token, groupId) {
  cy.request({
    method:'DELETE', 
    url:mgrGroupUrl + "/" + groupId, 
    auth: {'bearer':token}
  })
}

export function createCompanyByData(token, data){
  let tmp = JSON.parse(JSON.stringify(companyBodyTemplate))
  tmp.name = data.name
  if (data.hasOwnProperty('channel')) {tmp.channel = data.channel}
  createCompany(token,tmp)
}

export function modifyCompany (token, companyId, body) {
  cy.request({
    method:'PUT', 
    url:companyUrl + "/" + companyId, 
    auth: {'bearer':token},
    body:body
  })
}

export function deleteCompany (token, companyId) {
  cy.request({
    method:'DELETE', 
    url:companyUrl + "/" + companyId, 
    auth: {'bearer':token}
  })
}

export function deleteSite (token, companyId, siteId) {
  cy.request({
    method:'DELETE', 
    url:companyUrl + "/" + companyId + "/sites/" + siteId, 
    auth: {'bearer':token}
  })
}

export function deleteUnion(token, companyId, unionId) {
  cy.request({
    method:'DELETE', 
    url:companyUrl + "/" + companyId + "/unions/" + unionId, 
    auth: {'bearer':token}
  })
}

export function deleteSaasRule(token, companyId, ruleId) {
  cy.request({
    method:'DELETE', 
    url:companyUrl + "/" + companyId + "/saasRules/" + ruleId, 
    auth: {'bearer':token}
  })
}

export function deleteSaasTemplate(token, companyId, templateId) {
  cy.request({
    method:'DELETE', 
    url:companyUrl + "/" + companyId + "/saasTemplates/" + templateId, 
    auth: {'bearer':token}
  })
}

export function deleteAllUnions(token, companyName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        cy.request({
          method:'GET', 
          url:companyUrl + "/" + companyId + "/unions", 
          auth: {'bearer':token}
        }).its('body.results').as('unionsInfo').then(($unionsInfo) => {
           $unionsInfo.forEach(union => {
           deleteUnion(token, companyId, union.unionId)
        })
        })
      }
   })  
}

export function deleteAllSites(token, companyName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        cy.request({
          method:'GET', 
          url:companyUrl + "/" + companyId + "/sites", 
          auth: {'bearer':token}
        }).its('body.results').as('sitesInfo').then(($sitesInfo) => {
          $sitesInfo.forEach(site => {
           deleteSite(token, companyId, site.siteId)
         })
       })
      }
  })  
}

export function deleteAllSaasRules(token, companyName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        cy.request({
          method:'GET', 
          url:companyUrl + "/" + companyId + "/saasRules", 
          auth: {'bearer':token}
        }).its('body.results').as('saasRulesInfo').then(($saasRulesInfo) => {
          $saasRulesInfo.forEach(rule => {
           deleteSaasRule(token, companyId, rule.saasRuleId)
         })
       })
      }
  })  
}

export function deleteAllSaasTemplates(token, companyName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        cy.request({
          method:'GET', 
          url:companyUrl + "/" + companyId + "/saasTemplates", 
          auth: {'bearer':token}
        }).its('body.results').as('saasTemplatesInfo').then(($saasTemplatesInfo) => {
          $saasTemplatesInfo.forEach(template => {
            deleteSaasTemplate(token, companyId, template.saasTemplateId)
         })
       })
      }
  })  
}

export function deleteAllUsers(token, companyName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        let url = userUrl + '?companyId=' + companyId
        cy.request({
          method:'GET', 
          url:url, 
          auth: {'bearer':token}
        }).its('body.results').as('usersInfo').then(($usersInfo) => {
          $usersInfo.forEach(user => {
            if (user.company == companyName){
              deleteUserByName(token, user.username)
            }
         })
       })
      }
  })  
}

export function deleteAllGlobalUsersExceptAdmin(token){
  getIdByCompanyName(token, "all")
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        let url = userUrl + '?companyId=' + companyId
        cy.request({
          method:'GET', 
          url:url, 
          auth: {'bearer':token}
        }).its('body.results').as('usersInfo').then(($usersInfo) => {
          $usersInfo.forEach(user => {
            if (user.companyId == companyId && user.username != "admin"){
              deleteUser(token, user.username)
            }
         })
       })
      }
  })  
}

export function getIdByCompanyName(token, companyName) {
  cy.request({
    method:'GET', 
    url:companyUrl, 
    auth: {'bearer':token}
  }).its('body.results').as('companiesInfo').then(($companiesInfo) => {
    let com = $companiesInfo.find(function(comInfo){
      if(comInfo.name == companyName){
        return comInfo
      }
    })
    if (typeof(com) != "undefined")
    {
      cy.wrap(com.companyId).as("companyId")
    }
    else{
      cy.wrap("").as("companyId")
    }
  })
}



export function getDataByCompanyName(token, companyName) {
  cy.request({
    method:'GET', 
    url:companyUrl, 
    auth: {'bearer':token}
  }).its('body.results').as('companiesInfo').then(($companiesInfo) => {
    let com = $companiesInfo.find(function(comInfo){
      if(comInfo.name == companyName){
        return comInfo
      }
    })
    if (typeof(com) != "undefined")
    {
      cy.wrap(com.createdAt).as("createData")
    }
    else{
      cy.wrap("").as("createData")
    }
  })
}

export function deleteCompanyByName (token, companyName) {
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      deleteCompany (token, companyId)
    }
  })
}

export function createSite (token, companyName, body){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      body.companyId = companyId
      cy.request({
        method:'POST', 
        url:companyUrl + "/" + companyId + "/sites", 
        auth: {'bearer':token},
        body:body
      }).its('body').as('siteInfo')
    }
  })
}


export function modifySite(token, companyName, siteName,body){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    getIdBySiteName(token,companyId,siteName)
    cy.get('@siteId').then(siteId=>{
      if(companyId != "" && siteId != ""){
        body.companyId = companyId
        body['siteId'] = siteId
        body['__v'] = 0
        body['companyName'] = companyName
        cy.request({
          method:'PUT', 
          url:companyUrl + "/" + companyId + "/sites" + "/" + siteId, 
          auth: {'bearer':token},
          body:body
        }).its('body').as('siteInfo')
      }
    })  
  })
}

export function modifySiteBWByData(token, companyName, data,bwValue){
  let tmp = JSON.parse(JSON.stringify(siteTemp))
  let body = tmp[data.type]
  body.config.sn = data.sn
  body.name = data.name
  body.config.bandwidth = bwValue
  if ("lanNet" in  data){
    body.config.privateAddrs = data.lanNet
    body.config.lan[0].lanIp = data.lanIp
    body.config.lan[0].gateway = data.lanGateway
  }
  if("hub" in data){
    body.haConfig.isHub = true
  }
  if("longitude" in data){
    body.haConfig.longitude = data.longitude
    body.haConfig.latitude = data.latitude
  }
  if("remark" in data){
    body.remark = data.remark
  }
  modifySite(token, companyName, data.name,body)
}


export function createSiteByData(token, companyName, data){
  let tmp = JSON.parse(JSON.stringify(siteTemp))
  let body = tmp[data.type]
  body.config.sn = data.sn
  body.name = data.name
  if ("lanNet" in  data){
    body.config.privateAddrs = data.lanNet
    body.config.lan[0].lanIp = data.lanIp
    body.config.lan[0].gateway = data.lanGateway
  }
  if("hub" in data){
    body.haConfig.isHub = true
  }
  if("longitude" in data){
    body.haConfig.longitude = data.longitude
    body.haConfig.latitude = data.latitude
  }
  if("remark" in data){
    body.remark = data.remark
  }
  createSite(token, companyName, body)
}

export function createUnion (token, companyName, siteName, site1Name){
  getIdByCompanyName(token, companyName)
  let body = unionTemplate
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      body.companyId = companyId
      body.name = siteName + "-" + site1Name
      getIdBySiteName(token,companyId,siteName)
      cy.get('@siteId').then(siteId => {
        body.site1 = siteId
      })
      getIdBySiteName(token,companyId,site1Name)
      cy.get('@siteId').then(siteId => {
        body.site2 = siteId
      })
      cy.request({
        method:'POST',
        url:companyUrl + "/" + companyId + "/unions",
        auth: {'bearer':token},
        body:body
      })
    }
  })
}

export function createSpiTags (token, companyName, body){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      body.companyId = companyId
      cy.request({
        method:'POST', 
        url:companyUrl + "/" + companyId + "/spiTags", 
        auth: {'bearer':token},
        body:body
      }).its('body').as('spiTagsInfo')
    }
  })
}

export function deleteAllSpiTags(token){
  getIdByCompanyName(token, "all")
  cy.get('@companyId').then(companyId => {
    cy.request({
      method:'GET', 
      url:companyUrl + "/" + companyId  + "/spiTags", 
      auth: {'bearer':token}
    }).its('body.results').as('spiTagsInfo').then(($tagsInfo) => {
      $tagsInfo.forEach($spitag => {
        cy.request({
          method:'DELETE', 
          url:companyUrl+ "/" + companyId + "/spiTags/" + $spitag.spiTagId, 
          auth: {'bearer':token}
        })
      }) 
    })
  })
}

export function deleteAllSpiTemp(token){
  getIdByCompanyName(token, "all")
  cy.get('@companyId').then(companyId => {
      cy.request({
        method:'GET', 
        url:companyUrl + "/" + companyId  +"/actionTemplates", 
        auth: {'bearer':token}
      }).its('body.results').as('actionTempInfo').then(($tempInfo) => {
        $tempInfo.forEach($spitemp => {
         cy.request({
          method:'DELETE', 
          url:companyUrl+ "/" + companyId + "/actionTemplates/" + $spitemp.actionTemplateId, 
          auth: {'bearer':token}
      })
    }) 
  })
})
}

export function deleteAllSpiScenario(token){
  getIdByCompanyName(token, "all")
  cy.get('@companyId').then(companyId => {
      cy.request({
        method:'GET', 
        url:companyUrl + "/" + companyId  +"/spiScenarios", 
        auth: {'bearer':token}
      }).its('body.results').as('scenario').then(($scenarioInfo) => {
        $scenarioInfo.forEach($spiscenario => {
         cy.request({
          method:'DELETE', 
          url:companyUrl+ "/" + companyId + "/spiScenarios/" + $spiscenario.spiScenarioId, 
          auth: {'bearer':token}
      })
    }) 
  })
})
}

export function deleteAllSpiStrategy(token){
  getIdByCompanyName(token, "all")
  cy.get('@companyId').then(companyId => {
      cy.request({
        method:'GET', 
        url:companyUrl + "/" + companyId  +"/spiStrategys", 
        auth: {'bearer':token}
      }).its('body.results').as('strategy').then(($strategyInfo) => {
        $strategyInfo.forEach($spistrategy => {
         cy.request({
          method:'DELETE', 
          url:companyUrl+ "/" + companyId + "/spiStrategys/" + $spistrategy.spiStrategyId, 
          auth: {'bearer':token}
      })
    }) 
  })
})
}

export function createSpiTemplate (token, companyName, body){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      body.companyId = companyId
      getIdBySpiTagName(token,companyId,body.tagName)
      cy.get('@spiTagId').then(spiTagId => {
          if(spiTagId != ""){
            body.tag = spiTagId[0]
            body.tagId = spiTagId[1]
          }
        })
      cy.request({
        method:'POST', 
        url:companyUrl + "/" + companyId + "/actionTemplates", 
        auth: {'bearer':token},
        body:body
      }).its('body').as('actionTemplatesInfo')
    }
  })
}

export function createSpiScenario (token, companyName, templateName, body){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      body.companyId = companyId
      getIdBySpiTemplateName(token,companyId,templateName)
      cy.get('@spiTemplateId').then(spiTemplateId => {
          if(spiTemplateId != ""){
            body.templateList = [spiTemplateId]
          }
        })
      cy.request({
        method:'POST', 
        url:companyUrl + "/" + companyId + "/spiScenarios", 
        auth: {'bearer':token},
        body:body
      }).its('body').as('actionScenariosInfo')
    }
  })
}

export function createQos(token,companyName,siteName,body){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      body.companyId = companyId
      getIdBySiteName(token,companyId,siteName)
      cy.get('@siteId').then(siteId => {
        if(siteId != ""){
          body.siteId = siteId
        } 
        cy.request({
          method:'POST', 
          url:companyUrl + "/" + companyId + "/sites/" + siteId + "/qosConfs", 
          auth: {'bearer':token},
          body:body
        }).its('body').as('qosInfo')
      })
    }
  })
}

export function getIdBySpiTagName(token, companyId, SpiTagName) {
  cy.request({
    method:'GET', 
    url:companyUrl + "/" + companyId + "/spiTags", 
    auth: {'bearer':token}
  }).its('body.results').as('spiTagInfo').then(($tagInfo) => {
    let tag = $tagInfo.find(function(tagInfo){
      if(tagInfo.name == SpiTagName){
        return tagInfo
      }
    })
    var ids = []
    if (typeof(tag) != "undefined")
    {
      ids.push(tag.tag)
      ids.push(tag.spiTagId)
      cy.wrap(ids).as("spiTagId")
    }
    else{
      cy.wrap("").as("spiTagId")
    }
  })
}

export function getIdBySpiTemplateName(token, companyId, SpiTemplateName) {
  cy.request({
    method:'GET', 
    url:companyUrl + "/" + companyId + "/actionTemplates", 
    auth: {'bearer':token}
  }).its('body.results').as('spiTemplateInfo').then(($templateInfo) => {
    let template = $templateInfo.find(function(templateInfo){
      if(templateInfo.name == SpiTemplateName){
        return templateInfo
      }
    })
    if (typeof(template) != "undefined")
    {
      cy.wrap(template.actionTemplateId).as("spiTemplateId")
    }
    else{
      cy.wrap("").as("spiTemplateId")
    }
  })
}

export function getIdBySpiRulePriority(token, companyId, rulePriority) {
  cy.request({
    method:'GET', 
    url:companyUrl + "/" + companyId + "/spiRules", 
    auth: {'bearer':token}
  }).its('body.results').as('spiRuleInfo').then(($rulesInfo) => {
    let rule = $rulesInfo.find(function(ruleInfo){
      if(ruleInfo.priority == rulePriority){
        return ruleInfo
      }
    })
    if (typeof(rule) != "undefined")
    {
      cy.wrap(rule.spiRuleId).as("ruleId")
    }
    else{
      cy.wrap("").as("ruleId")
    }
  })
}

export function getIdByTemplateName(token, companyId, templateName) {
  cy.request({
    method:'GET', 
    url:companyUrl + "/" + companyId + "/saasTemplates", 
    auth: {'bearer':token}
  }).its('body.results').as('saasTemplates').then(($saasTemplateInfo) => {
    let template = $saasTemplateInfo.find(function(templateInfo){
      if(templateInfo.name == templateName){
        return templateInfo
      }
    })
    if (typeof(template) != "undefined")
    {
      cy.wrap(template.saasTemplateId).as("saasTemplateId")
    }
    else{
      cy.wrap("").as("saasTemplateId")
    }
  })
}

export function getIdBySiteName(token, companyId, siteName) {
  cy.request({
    method:'GET', 
    url:companyUrl + "/" + companyId + "/sites", 
    auth: {'bearer':token}
  }).its('body.results').as('sitesInfo').then(($sitesInfo) => {
    let site = $sitesInfo.find(function(siteInfo){
      if(siteInfo.name == siteName){
        return siteInfo
      }
    })
    if (typeof(site) != "undefined")
    {
      cy.wrap(site.siteId).as("siteId")
    }
    else{
      cy.wrap("").as("siteId")
    }
  })
}

export function getIdByUnionName(token, companyId, unionName) {
  cy.request({
    method:'GET', 
    url:companyUrl + "/" + companyId + "/unions", 
    auth: {'bearer':token}
  }).its('body.results').as('unionsInfo').then(($unionsInfo) => {
    let union = $unionsInfo.find(function(unionInfo){
      if(unionInfo.name == unionName){
        return unionInfo
      }
    })
    if (typeof(union) != "undefined")
    {
      cy.wrap(union.unionId).as("unionId")
    }
    else{
      cy.wrap("").as("unionId")
    }
  })
}


export function deleteSiteByName (token, companyName, siteName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      getIdBySiteName(token, companyId, siteName)
      cy.get('@siteId').then(siteId => {
        if(siteId != ""){
          deleteSite(token, companyId, siteId)
        }
      })
    }
  })
}

export function getSiteNEidByName (token, companyId, siteName){
  cy.request({
    method:'GET', 
    url:companyUrl + "/" + companyId + "/sites", 
    auth: {'bearer':token}
  }).its('body.results').as('sitesInfo').then(($sitesInfo) => {
    let site = $sitesInfo.find(function(siteInfo){
      if(siteInfo.name == siteName){
        return siteInfo
      }
    })
    if (typeof(site) != "undefined")
    {
      cy.wrap(site.config.neid).as("neId")
    }
    else{
      cy.wrap("").as("neId")
    }
  })
}

export function getSiteNEidsByNameList (token, companyId, siteNameList){
  cy.request({
    method:'GET', 
    url:companyUrl + "/" + companyId + "/sites", 
    auth: {'bearer':token}
  }).its('body.results').as('sitesInfo').then(($sitesInfo) => {
    let site = $sitesInfo.filter(function(siteInfo){
      return siteNameList.includes(siteInfo.name)
    })
    let neIds = site.map(function(st){
      return st.config.neid
    })
    if (typeof(neIds) != "undefined")
    {
      cy.wrap(neIds).as("neIds")
    }
    else{
      cy.wrap([""]).as("neIds")
    }
  })
}

export function getPopNEidByPopId (token, PopId, PopType){
  cy.request({
    method:'GET', 
    url:popConfigUrl, 
    auth: {'bearer':token}
  }).its('body.results').as('popsInfo').then(($popsInfo) => {
    let pop = $popsInfo.find(function(popInfo){
      if(popInfo.popId == PopId && popInfo.popType == PopType){
        return popInfo
      }
    })
    if (typeof(pop) != "undefined")
    {
      cy.wrap(pop.neId).as("neId")
    }
    else{
      cy.wrap("").as("neId")
    }
  })
}

export function createPOP (token, body){
  cy.request({
    method:'GET', 
    url:popUrl, 
    auth: {'bearer':token}
  }).its('body.results').as('popsInfo').then(($popsInfo) => {
    let pop = $popsInfo.find(function(popInfo){
      if(popInfo.hostname == body.hostname){
        return popInfo
      }
    })
    body['tags'] = pop.tags
    body['ips'] = pop.ips
    body['geo'] = pop.geo
    body['saasServices'] = pop.saasServices
    cy.request({
      method:'PUT', 
      url:popConfigUrl + "/4", 
      auth: {'bearer':token},
      body:body
    }).its('body').as('npopInfo')
  })
}

export function getSiteNEidBycomNameAndStName (token, companyName, siteName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      getSiteNEidByName(token,companyId, siteName)
    }
  })
}

export function getRoleIdByNameAndCompanyId (token, companyId, roleNameList){
  cy.request({
    method:'GET', 
    url:roleUrl + "?skip=0&limit=20&sort=%2Bid&page=1&companyId=" + companyId, 
    auth: {'bearer':token}
  }).its('body.results').as('rolesInfo').then(($rolesInfo) => {
    let roles = $rolesInfo.filter(function(roleInfo){
      return roleNameList.includes(roleInfo.role) 
    })
    let roleIds = roles.map(function(role){
      return role.roleId
    })
    if (typeof(roleIds) != "undefined")
    {
      cy.wrap(roleIds).as("roleIds")
    }
    else{
      cy.wrap([""]).as("roleIds")
    }
  })
}

export function createUser (token, body){
  let tmp = JSON.parse(JSON.stringify(body))
  getIdByCompanyName(token, tmp.company)
  cy.log(tmp.company)
  cy.get('@companyId').then(companyId => {
    cy.log(companyId)
    if(companyId != ""){
      tmp.companyId = companyId
      getRoleIdByNameAndCompanyId(token, companyId, body.roles)
      cy.get('@roleIds').then(roleIds => {
        tmp.rolesId = roleIds
        cy.request({
          method:'POST', 
          url:userUrl, 
          auth: {'bearer':token},
          body:tmp
        }).its('body').as('userInfo')
      })
    }
  })
}

export function createRole (token, companyName, body){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
      body.companyId = companyId
      cy.request({
        method:'POST', 
        url:roleUrl, 
        auth: {'bearer':token},
        body:body
      }).its('body').as('roleInfo')
    }
  })
}

export function deleteAllRole(token, companyName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        cy.request({
          method:'GET', 
          url:roleUrl + "?skip=0&limit=20&sort=%2Bid&page=1&companyId=" + companyId, 
          auth: {'bearer':token}
        }).its('body.results').as('rolesInfo').then(($rolesInfo) => {
          $rolesInfo.forEach(role => {
            if (role.companyId == companyId){
              deleteRole(token, role.roleId)
            }
         })
       })
      }
  })  
}

export function deleteAllGlobalRole(token, companyName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        cy.request({
          method:'GET', 
          url:roleUrl + "?skip=0&limit=20&sort=%2Bid&page=1&companyId=" + companyId, 
          auth: {'bearer':token}
        }).its('body.results').as('rolesInfo').then(($rolesInfo) => {
          $rolesInfo.forEach(role => {
            if ((role.companyId == companyId) && (role.extra.globalMode)){
              deleteRole(token, role.roleId)
            }
         })
       })
      }
  })  
}

export function deleteRolebyName(token, companyName, roleName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        cy.request({
          method:'GET', 
          url:roleUrl + "?skip=0&limit=20&sort=%2Bid&page=1&companyId=" + companyId, 
          auth: {'bearer':token}
        }).its('body.results').as('rolesInfo').then(($rolesInfo) => {
          $rolesInfo.forEach(role => {
            if ((role.companyId == companyId) && (role.role == roleName)) {
                deleteRole(token, role.roleId)
            }
         })
       })
      }
  })  
}

export function deleteRole (token, roleId) {
  cy.request({
    method:'DELETE', 
    url:roleUrl + "/" + roleId, 
    auth: {'bearer':token}
  })
}

export function modifyUser (token, userName, body) {
  cy.request({
    method:'PUT', 
    url:userUrl + "/" + userName, 
    auth: {'bearer':token},
    body:body
  })
}

export function deleteUser (token, userName) {
  getIdByCompanyName(token, 'all')
  cy.get('@companyId').then(companyId => {
    if(companyId != ""){
        let url = userUrl + '?companyId=' + companyId
        cy.request({
        method:'GET', 
        url:url, 
        auth: {'bearer':token}
        }).its('body.results').as('usersInfo').then(($usersInfo) => {
            let user = $usersInfo.find(function(userInfo){
            if(userInfo.username == userName){
            return userInfo
         }
        })
        if (typeof(user) != "undefined"){
          cy.request({
           method:'DELETE', 
           url:userUrl + "/" + userName, 
           auth: {'bearer':token}
         })
        }
      })
    }
  })
}

export function deleteUserByName (token, userName) {
cy.request({
        method:'DELETE', 
        url:userUrl + "/" + userName, 
        auth: {'bearer':token}
      })
}


export function checkCPENeidbyName(token, companyId, siteName, model){
  getSiteNEidBycomNameAndStName (token, companyId, siteName)
  cy.get('@neId').then(neId => {
    if(neId != ""){
      cy.wrap({'type':neId & 15})
    }  
  }).its('type').should('eq',model)
}

export function modifyCPEGlobalConfig(cpe_config){
  cy.typeInputWithLable('regUrl',cpe_config.regUrl)
  cy.typeInputWithLable('authUrl',cpe_config.authUrl)
  cy.typeInputWithLable('collectdAddr',cpe_config.collectdAddr)
  cy.typeInputWithLable('collectdPort',cpe_config.collectdPort)
  cy.typeInputWithLable('salt',cpe_config.salt)
  cy.typeInputWithLable('prismAddr',cpe_config.prismAddr)
  var i
  for (i=0;i<3;i++) {
    cy.get('[data-cy=addController]').click()
    cy.get('[data-cy=managerSpecificIp]').eq(i).clear().type(cpe_config.controllers[i].domain)
    cy.get('input[data-cy=managerSpecificPort]').eq(i).clear().type(cpe_config.controllers[i].port)
    cy.get('div[data-cy=managerSpecificPort]').eq(i).click()
    if (cpe_config.controllers[i].mode != '网关'){
        cy.get('.el-scrollbar').filter(':visible').get('li[class=el-select-dropdown__item]').filter(':visible').contains(cpe_config.controllers[i].mode).should('be.visible').click({force: true})}
  }
  cy.contains('CPE全局配置').parent('div').within(() => {
    cy.get('[data-cy=cpeConfigUpdate]').click()
  })
  cy.contains('更新成功')
}
