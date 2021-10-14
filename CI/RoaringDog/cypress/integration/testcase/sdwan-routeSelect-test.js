import {deletePopByPopId,putPop,createCompanyByData, deleteCompanyByName, deleteAllUnions,deleteAllSites, createSiteByData, createSpiTags, createSpiTemplate,deleteAllSpiTags,deleteAllSpiTemp, createUnion, deleteAllSpiScenario, createSpiScenario,deleteAllSpiStrategy} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView,rowContains,rowUnflod,rowContainsVisible,changeToGlobalView,} from '../utils/web-utils'
import {testServiceBody, popBody, PopTypeSaas, testSpiTagBody, testSpiTemplateBody,testScenarioBody,testStrategyBody} from '../utils/variables-utils'
import {checkSpiTagInfoWithConsul, checkSpiDispatchInfoWithConsul, checkSpiDispatchEmptyWithConsul} from '../utils/consulCheck-utils'

const protocol = {"1" : "ICMP" , "6": "TCP","17":"UDP"}

export function changeSpiPanelView(panel_name) {
  cy.contains(panel_name).click({force: true})
}

export function changeSiteSpiView(siteName) {
  cy.contains(siteName).click({force: true})
}

export function setRule(rule){
  cy.get('[data-cy="addRule"]').click()
  typeRule(rule)
}

export function setFailRule(rule){
  cy.get('[data-cy="addRule"]').click()
  inputRule(rule)
  cy.get('[data-cy="rules"]').within(() => {
    cy.contains("确认").click()
  })
  cy.contains("创建失败")
  cy.get('[data-cy="rules"]').within(() => {
    cy.contains("取消").click()
  })
}

export function inputRule(rule){
  cy.get('[data-cy="rules"]').within(() => {
    if (rule.hasOwnProperty("srcCIDR")){
      cy.get('[data-cy="srcCIDR"]').clear().type(rule.srcCIDR)
    }
    if (rule.hasOwnProperty("dstCIDR")){
      cy.get('[data-cy="dstCIDR"]').clear().type(rule.dstCIDR)
    }
    if (rule.hasOwnProperty("srcPort")){
      cy.get('[data-cy="srcPort"]').clear().type(rule.srcPort)
    }
    if (rule.hasOwnProperty("dstPort")){
      cy.get('[data-cy="dstPort"]').clear().type(rule.dstPort)
    }
    cy.get('[data-cy="l4proto"]').click()
  })
  rule.l4proto.forEach(prot => {
    cy.get('li.el-select-dropdown__item').contains(protocol[prot]).click()
  })
  cy.contains("协议").click({force: true})
}

export function typeRule(rule){
  inputRule(rule)
  cy.get('[data-cy="rules"]').within(() => {
    cy.contains("确认").click()
    cy.contains("确认").should('not.exist')
  })
}

export function modifyRule(rule){
  cy.get('[data-cy="ruleSearch"]').clear().type(rule.search)
  cy.get('[data-cy="editRule"]').filter(':visible').eq(0).click()
  typeRule(rule)
}

export function deleteRule(rule){
  cy.get('[data-cy="ruleSearch"]').clear().type(rule.search)
  cy.get('[data-cy="deleteRule"]').filter(':visible').eq(0).click()
}

export function setTag(tag){
  cy.get('[data-cy="tagName"]').within(() => {
  cy.typeInputWithLable('规则名称', tag.name)
  })
  tag.rules.forEach(rule => {
     setRule(rule)
  })
  cy.contains("确 定").click()
}

export function setFailTag(tag){
  cy.get('[data-cy="tagName"]').within(() => {
  cy.typeInputWithLable('规则名称', tag.name)
  })
  tag.rules.forEach(rule => {
     setRule(rule)
  })
  tag.fail_rules.forEach(rule => {
    setFailRule(rule)
 })
  cy.contains("确 定").click()
}

export function modifyTag(tag){
  cy.get('[data-cy="tagName"]').within(() => {
      cy.get('input').should('have.value', tag.name)
  })
  tag.rules.forEach(rule => {
    modifyRule(rule)
  })
  cy.contains("确 定").click()
}

export function ChangeRuleInTag(tag){
  cy.get('[data-cy="tagName"]').within(() => {
      cy.get('input').should('have.value', tag.name)
  })
  tag.delete_rules.forEach(rule => {
    deleteRule(rule)
  })
  cy.get('[data-cy="ruleSearch"]').clear()
  tag.add_rules.forEach(rule => {
    setRule(rule)
  })
  cy.contains("确 定").click()
}

export function setTemplate(template){
  let template_c = {}
  cy.get('[data-cy="tempActionTemplateName"]').within(() => {
  cy.typeInputWithLable('模板名', template.name)
  })
  template_c = configTemplate(template)
  return template_c
}

export function setTemplateFail(template){
  let template_c = {}
  cy.get('[data-cy="tempActionTemplateName"]').within(() => {
  cy.typeInputWithLable('模板名', template.name)
  })
  template_c = configTemplateFail(template)
}

export function modifyTemplate(template){
  cy.get('[data-cy="tempActionTemplateName"]').within(() => {
     cy.get('input').should('have.value', template.name)
  })
  configTemplate(template)
}

export function configTemplateFail(template){
  if (template.actions.hasOwnProperty("saas")){
    if (template.actions.saas.enable){
      cy.checkCheckBoxWithDatacy('[data-cy="saasenable"]')
      setSaasParamFail(template.actions.saas.saasType, template.actions.saas.saasConfig)
    }else
    {
      cy.uncheckCheckBoxWithDatacy('[data-cy="saasenable"]')
    }
  }
  }

export function configTemplate(template){
  if (template.actions.hasOwnProperty("saas")){
    if (template.actions.saas.enable){
      cy.checkCheckBoxWithDatacy('[data-cy="saasenable"]')
      setSaasParam(template.actions.saas.saasType, template.actions.saas.saasConfig)
    }else
    {
      cy.uncheckCheckBoxWithDatacy('[data-cy="saasenable"]')
    }
  }
  if (template.actions.hasOwnProperty("transportPolicy")){
      if (template.actions.transportPolicy.enable){
          cy.checkCheckBoxWithDatacy('[data-cy="transportPolicyenable"]')
          cy.ClickSelectValue('[id="transportPolicy"]',template.actions.transportPolicy.param.policy)
          if (template.actions.hasOwnProperty("fec")){
              if (template.actions.transportPolicy.enable){
                   cy.checkCheckBoxWithDatacy('[data-cy="fecEnable"]')

                  }
              else{cy.uncheckCheckBoxWithDatacy('[data-cy="fecEnable"]')
            }
          }
      }else{
           cy.uncheckCheckBoxWithDatacy('[data-cy="transportPolicyenable"]')}
}
  if (template.actions.hasOwnProperty("priority")){
     if (template.actions.priority.enable){
         cy.checkCheckBoxWithDatacy('[data-cy=priorityenable]')
         cy.ClickDropDownValue('[id="priority"]','.el-scrollbar__view',template.actions.priority.param.level)

     }else
    {
      cy.get('[data-cy=priorityenable]').within(() => {
        cy.uncheckCheckBoxWithDatacy('[data-cy=priorityenable]')
      })
    }
  }

  if (template.actions.hasOwnProperty("wan")){
    if (template.actions.wan.enable){
        cy.checkCheckBoxWithDatacy('[data-cy=wanenable]')
        cy.ClickDropDownValue('[id="selectWan"]','.el-scrollbar__view',template.actions.wan.param.policy)
        if (template.actions.wan.param.hasOwnProperty("ports")){cy.ClickMultiDropDownValue('[id=selectWanList]',template.actions.wan.param.ports)}
    }else
   {
        cy.uncheckCheckBoxWithDatacy('[data-cy=wanenable]')
   }
 }

 if (template.actions.hasOwnProperty("analyze")){
  if (template.actions.analyze.enable){
      cy.checkCheckBoxWithDatacy('[data-cy=analyzeenable]')
  }else
 {
      cy.uncheckCheckBoxWithDatacy('[data-cy=analyzeenable]')
 }
}

if (template.actions.hasOwnProperty("office")){
  if (template.actions.office.enable){
      cy.checkCheckBoxWithDatacy('[data-cy=officeenable]')
  }else
 {
      cy.uncheckCheckBoxWithDatacy('[data-cy=officeenable]')
 }
 } 
}

function selectListInput(datacy, index, value){
    cy.get(datacy).eq(index).within(() =>{
        cy.get('input').click()
     })
     cy.get('.el-scrollbar').filter(':visible').within(() =>{
         cy.get('li[class^=el-select-dropdown__item]').contains(value).should('be.visible').click({force: true})
    })
  }

  export function setSaasParamFail(saasType,saasConfig){
    cy.get('[data-cy="saasExit"] input:visible').invoke('val').then(text=>{
      if (text == saasType){
  
      }else{
        cy.ClickSelectValue('[data-cy="saasExit"]>div .el-select', saasType)
      }
    })
    cy.get('[data-cy="saasButton"]').click()
    cy.get('[data-cy="addSaaSExit"]').click()
    selectListInput('[data-cy="portService"]:visible', 0, saasConfig.saasList[0].saasName)
    cy.get('[data-cy="portService"]:visible').eq(1).within(() =>{
      cy.get('input').click()
   })
   cy.get('.el-scrollbar').filter(':visible').within(() =>{
       cy.get('li[class^=el-select-dropdown__item]').contains(saasConfig.saasList[0].saasName+'(').should('not.exist')
  })
  }

export function setSaasParam(saasType,saasConfig){
  cy.get('[data-cy="saasExit"] input:visible').invoke('val').then(text=>{
    if (text == saasType){

    }else{
      cy.ClickSelectValue('[data-cy="saasExit"]>div .el-select', saasType)
    }
  })
  cy.get('[data-cy="saasButton"]').click()
  if ( saasType == '自动出口'){
      cy.get('[data-cy="saasConfigs"]').within(() => {
         cy.get('[data-cy="agent"]').eq(0).click()
      })
      }
  else {
       cy.get('[aria-label="SAAS指定出口配置"]').within(() => {
       cy.typeValueBydatacy('[data-cy="dns"]', saasConfig.agent)
       cy.typeValueBydatacy('[data-cy="ttl"]', saasConfig.ttl)
       })
       cy.get('[data-cy="deleteSaaSExit"]').then(exits => {
        const exitCount = Cypress.$(exits).length;
        if (saasConfig.saasList.length>exitCount){
          var i
          for(i=0;i<(saasConfig.saasList.length-exitCount);i++){
             cy.get('[data-cy="addSaaSExit"]').click()}}
        else {
          var i
          for(i=0;i<(exitCount-saasConfig.saasList.length);i++){
            cy.get('[data-cy="deleteSaaSExit"]').eq(exitCount-1-i).click()
          }
        }
       });
       saasConfig.saasList.forEach((saas, index) => {
        cy.get('[data-cy="portCarrier"]:visible').eq(index).find('input').invoke('val').then(text=>{
          if (text == saas.saasPort){
   
       }else{
        selectListInput('[data-cy="portService"]:visible', index, saas.saasName)
        selectListInput('[data-cy="portCarrier"]:visible', index, saas.saasPort)
       }
     })
        })
    }
  cy.get('.el-drawer__open').filter(':visible').click({force:true})
}

export function getProtString(protList){
  let protString = ""
  protList.forEach(prot => {
    protString = protString + protocol[prot] + " "
  })
  return protString.trim()
}

export function chooseRuleByPro(proList){
  proList.forEach(pro => {
    cy.get('[data-cy="rules"]').contains(pro).parents('tr').within(() => {
      cy.get('[class="el-checkbox"]').click()
    })
  })
}

export function chooseTemplateByName(nameList){
  nameList.forEach(name => {
    cy.get('#pane-second').contains(name).parent('div').within(() => {
      cy.get('[data-cy="templateChecked"]').click()
    })
  })
}

export function clickComfirm(){
  cy.get('.dialog-footer').filter(':visible').within(() => {
    cy.get("button.el-button.el-button--primary").filter(':visible').click()
})
}

export function transfer_panel_all_Select(){
    cy.get('.el-transfer-panel').eq(0).within(() => {
        cy.get('label[class=el-checkbox]').filter(':visible').click()
    })
    cy.get('.el-transfer__buttons').filter(':visible').within(() => {
        cy.get('button').filter(':visible').eq(1).click()
    })
  }

export function transfer_panel_Select_dedicate_scenario(scenarioName){
    cy.get('.el-transfer-panel').eq(0).within(() => {
        cy.get('input').filter(':visible').clear().type(scenarioName)
        cy.get('label[class=el-checkbox]').filter(':visible').click()
    })
    cy.get('.el-transfer__buttons').filter(':visible').within(() => {
        cy.get('button').filter(':visible').eq(1).click()
    })
  }

  export function transfer_panel_DeSelect_dedicate_scenario(scenarioName){
    cy.get('.el-transfer-panel').eq(1).within(() => {
        cy.get('input').filter(':visible').clear().type(scenarioName)
        cy.get('label[class=el-checkbox]').filter(':visible').click()
    })
    cy.get('.el-transfer__buttons').filter(':visible').within(() => {
        cy.get('button').filter(':visible').eq(0).click()
    })
  }

export function table_batch_delete(table_datecy, deletecy){
  cy.get(table_datecy).get('.el-table__header-wrapper').within(() => {
      cy.get('label[class=el-checkbox]').filter(':visible').click()
  })
  cy.get(deletecy).filter(':visible').click()
}

export function delete_confirm(){
  cy.contains("是否继续").parents('.el-message-box').within(() => {
    cy.contains("确定").click()
  })
  cy.contains("删除成功")
}


before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
  //删除公司
  cy.get('@company').then(company => {
    cy.get('@site').then(site => {
      cy.get('@info').then(t_info => {
        deleteAllSpiStrategy(t_info.token)
        deleteAllSpiScenario(t_info.token)
        deleteAllSpiTemp(t_info.token)
        deleteAllSpiTags(t_info.token)
        deletePopByPopId(t_info.token,testServiceBody.putCompanySaasBody.popId,PopTypeSaas)
        deletePopByPopId(t_info.token,testServiceBody.putSaasBody.popId,PopTypeSaas)
        deletePopByPopId(t_info.token,popBody.testpop2.popId)
        deletePopByPopId(t_info.token,popBody.testpop.popId)
        putPop(t_info.token,popBody.testpop2)
        putPop(t_info.token,popBody.testpop)
        putPop(t_info.token,testServiceBody.putSaasBody)
        putPop(t_info.token,testServiceBody.putCompanySaasBody)
        deleteAllUnions(t_info.token,company.testCompanySpi.name)
        deleteAllSites(t_info.token,company.testCompanySpi.name)
        deleteCompanyByName(t_info.token,company.testCompanySpi.name)
        deleteCompanyByName(t_info.token,company.testCompanySTSpi.name)
        createCompanyByData(t_info.token,company.testCompanySpi)
        createCompanyByData(t_info.token,company.testCompanySTSpi)
        createSiteByData(t_info.token, company.testCompanySpi.name,site.SpiGwSiteBody)
        createSiteByData(t_info.token, company.testCompanySpi.name,site.SpiSeSiteBody)
        createSiteByData(t_info.token, company.testCompanySpi.name,site.SpiPaSiteBody)
        createSiteByData(t_info.token, company.testCompanySpi.name,site.SpiDecidateSiteBody)
        createUnion(t_info.token, company.testCompanySpi.name,site.SpiGwSiteBody.name,site.SpiPaSiteBody.name)
        createSpiTags(t_info.token, company.testCompanySpi.name,testSpiTagBody.SpiTagAllIP)
        createSpiTags(t_info.token, company.testCompanySpi.name,testSpiTagBody.SpiTagAllIPUdp)
        createSpiTags(t_info.token, company.testCompanySpi.name,testSpiTagBody.SpiTagSaas)
        createSpiTags(t_info.token, company.testCompanySpi.name,testSpiTagBody.SpiTagModifySaas)
        createSpiTags(t_info.token, company.testCompanySTSpi.name,testSpiTagBody.SpiSTTagSaas)
        createSpiTags(t_info.token, 'all',testSpiTagBody.SpiGTagSaas)
        createSpiTags(t_info.token, 'all',testSpiTagBody.SpiGTagModifySaas)
        createSpiTemplate(t_info.token, company.testCompanySpi.name,testSpiTemplateBody.SpiTemplateSaas)
        createSpiTemplate(t_info.token, company.testCompanySpi.name,testSpiTemplateBody.SpiModifyTemplateSaas)
        createSpiTemplate(t_info.token, 'all',testSpiTemplateBody.SpiTemplateGlobalSaas)
        createSpiTemplate(t_info.token, company.testCompanySTSpi.name,testSpiTemplateBody.SpiTemplateSTSaas)
        createSpiTemplate(t_info.token, company.testCompanySpi.name,testSpiTemplateBody.SpiTemplatePro)
        createSpiTemplate(t_info.token, company.testCompanySpi.name,testSpiTemplateBody.SpiTemplateDelete)
        createSpiTemplate(t_info.token, company.testCompanySpi.name,testSpiTemplateBody.SPITemplateDedicate)
        createSpiScenario(t_info.token, company.testCompanySpi.name,testSpiTemplateBody.SpiTemplateSaas.name,testScenarioBody.SpiScenarioSaas)
        createSpiScenario(t_info.token, company.testCompanySpi.name,testSpiTemplateBody.SPITemplateDedicate.name,testScenarioBody.SpiScenarioDedicate)
        createSpiScenario(t_info.token, company.testCompanySpi.name,testSpiTemplateBody.SpiTemplatePro.name,testScenarioBody.SpiScenarioPro)
        createSpiScenario(t_info.token, company.testCompanySTSpi.name,testSpiTemplateBody.SpiTemplateSTSaas,testScenarioBody.SpiScenarioST)
        createSpiScenario(t_info.token, 'all',testSpiTemplateBody.SpiTemplateGlobalSaas,testScenarioBody.SpiScenarioG)
        cy.reload()
      }) 
    })
    }) 
})

//SDWANDEV-4005
describe('routeSelect page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/spiManage',this.info)
    changeSiteCompanyView(this.company.testCompanySpi.name)
    })

    it('create and delete spi tag test', function(){
      changeSpiPanelView("规则标识")
      cy.get('[data-cy=addActionTemplate]').filter(':visible').click()
      setTag(testSpiTagBody.SpiAddTag)
      cy.contains("创建成功")
      let checkList = [testSpiTagBody.SpiAddTag.name,0,600]
      rowContains('[data-cy="spiTagTable"]',testSpiTagBody.SpiAddTag.name,2, 4 ,checkList)
      cy.get('[data-cy="tagSearch"]').type(testSpiTagBody.SpiAddTag.name)
      cy.get('[data-cy="spiTagTable"]').contains(testSpiTagBody.SpiAddTag.name).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("确定").filter(':visible').click()
      cy.contains("删除成功")
    })

    it('create spi tag test failure', function(){
      changeSpiPanelView("规则标识")
      cy.get('[data-cy=addActionTemplate]').filter(':visible').click()
      setFailTag(testSpiTagBody.SpiAddTFail)
      cy.get('[data-cy="tagSearch"]').clear().type(testSpiTagBody.SpiAddTFail.name)
      cy.contains('共 1 条').filter(':visible')
      })

    it('search spi tag test', function(){
      changeSpiPanelView("规则标识")
      cy.get('[data-cy="tagSearch"]').clear().type(testSpiTagBody.SpiTagSaas.name)
      cy.contains('共 1 条').filter(':visible')
      //cy.get('[data-cy="tagSearch"]').clear().type(testSpiTagBody.SpiTagSaas.rules[0].dstCIDR)
      cy.get('[data-cy="tagSearch"]').clear().type('onenote')
      cy.contains('共 2 条').filter(':visible')
      cy.get('[data-cy="tagSearch"]').clear().type(testSpiTagBody.SpiTagAllIPUdp.rules[0].dstCIDR)
      cy.contains('共 2 条').filter(':visible')
    })

    it('create and delete spi template test', function(){
      changeSpiPanelView("策略模板")
      cy.get('[data-cy=addTemplate]').filter(':visible').click()
      cy.ClickSelectValue('#templateImport',testSpiTemplateBody.SpiTemplateAdd.tagName)
      cy.contains("选择Tag").parents('[class="el-dialog"]').within(()=>{
        cy.contains("确 定").click()
      })
      setTemplate(testSpiTemplateBody.SpiTemplateAdd)
      clickComfirm()
      cy.contains("创建成功")
      let checkList = [testSpiTemplateBody.SpiTemplateAdd.tagName,'开']
      rowContains('[data-cy="actionTemplates"]',testSpiTemplateBody.SpiTemplateAdd.name,2, 3 ,checkList)
      changeSpiPanelView("规则标识")
      //table_batch_delete('[data-cy="spiTagTable"]','[data-cy="batchDeleteTag"]')
      //cy.contains("是否继续").parents('.el-message-box').within(() => {
      //  cy.contains("确定").click()
      //})
      //cy.contains("删除失败")
      changeSpiPanelView("策略模板")
      cy.get('[data-cy="actionTemplates"]').contains(testSpiTemplateBody.SpiTemplateAdd.name).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("确定").click()
    })

    it('modify spi template test', function(){
      let template_c = {}
      changeSpiPanelView("策略模板")
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiTemplateModify.name)
      cy.get('[data-cy="actionTemplates"]').contains(testSpiTemplateBody.SpiTemplateModify.name).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      modifyTemplate(testSpiTemplateBody.SpiTemplateModify)
      clickComfirm()
      cy.contains("更新成功")
      let checkList = [testSpiTemplateBody.SpiTemplateModify.tagName,'开','可靠']
      rowContainsVisible('[data-cy="actionTemplates"]',testSpiTemplateBody.SpiTemplateModify.name,2, 4,checkList)
    })

      it('delete spi template test', function(){
      changeSpiPanelView("策略模板")
      cy.get('[data-cy="actionTemplates"]').contains(testSpiTemplateBody.SpiTemplateDelete.name).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("确定").click()
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiTemplateDelete.name)
      cy.contains('共 0 条').filter(':visible')
    })
    
    it('search spi template test by name and Tag', function(){
      changeSpiPanelView("策略模板")
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiTemplateSaas.name)
      cy.contains('共 1 条').filter(':visible')
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiTemplateAdd.name)
      cy.contains('共 0 条').filter(':visible')
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiTemplateGlobalSaas.tagName)
      cy.contains('共 1 条').filter(':visible')
      cy.get('[data-cy="templateSearch"]').clear().type("wrongTag")
      cy.contains('共 0 条').filter(':visible')
    })

    it('create and delete spi Scenario test', function(){
      changeSpiPanelView("场景管理")
      cy.get('[data-cy=addScenario]').filter(':visible').click()
      cy.get('[data-cy="spiScenarioForm"]').within(() => {
        cy.typeInputWithLable('场景名', testScenarioBody.SpiScenarioAdd.name)
        })
      transfer_panel_all_Select()
      clickComfirm()
      cy.contains("创建成功").should('be.visible')
      cy.get('[data-cy="spiScenarioTable"]').should('be.visible')
      let checkList = [testScenarioBody.SpiScenarioAdd.name,'',1]
      rowContains('[data-cy="spiScenarioTable"]',testScenarioBody.SpiScenarioAdd.name,2, 4 ,checkList)

      changeSpiPanelView("策略模板")
      //table_batch_delete('[data-cy="actionTemplates"]','[data-cy="batchDeleteTemplate"]')
      //cy.contains("确定").click()
      //cy.contains("模板被场景引用，删除失败")
      changeSpiPanelView("场景管理")
      cy.get('[data-cy="spiScenarioTable"]').contains(testScenarioBody.SpiScenarioAdd.name).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("确定").click()
      cy.contains("删除成功")
    }) 
    
    it('create and delete spi CPE Strategy test', function(){
      changeSpiPanelView("策略应用")
      cy.get('[data-cy=addStrategy]').filter(':visible').click()
      cy.ClickMultiDropDownValue('.el-select__input',testStrategyBody.SpiStrategyAdd.siteList)
      transfer_panel_Select_dedicate_scenario(testScenarioBody.SpiScenarioSaas.name)
      clickComfirm()
      cy.contains("创建成功").should('be.visible')
      checkSpiTagInfoWithConsul(this.info.token,this.company.testCompanySpi.name,'Saas')
      checkSpiDispatchInfoWithConsul(this.info.token,this.company.testCompanySpi.name,testStrategyBody.SpiStrategyAdd.siteList[0])
      checkSpiDispatchInfoWithConsul(this.info.token,this.company.testCompanySpi.name,testStrategyBody.SpiStrategyAdd.siteList[1])
      cy.get('[data-cy="spiStrategyTable"]').should('be.visible')
      let checkList = [testSpiTagBody.SpiTagSaas.name,1]
      rowContains('[data-cy="spiStrategyTable"]',testStrategyBody.SpiStrategyAdd.siteList[0],3, 4 ,checkList)
      rowContains('[data-cy="spiStrategyTable"]',testStrategyBody.SpiStrategyAdd.siteList[1],3, 4 ,checkList)

      changeSpiPanelView("场景管理")
      cy.get('[data-cy="spiScenarioTable"]').contains(testScenarioBody.SpiScenarioSaas.name).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("是否继续").parents('.el-message-box').within(() => {
        cy.contains("确定").click()
      })
      cy.contains("删除失败")
      changeSpiPanelView("策略应用")
      cy.get('[data-cy="strategySearch"]').clear().type(testScenarioBody.SpiScenarioSaas.name)
      cy.get('[data-cy="spiStrategyTable"]').contains(testStrategyBody.SpiStrategyAdd.siteList[0]).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      delete_confirm()
      cy.get('[data-cy="spiStrategyTable"]').contains(testStrategyBody.SpiStrategyAdd.siteList[1]).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      delete_confirm()
      checkSpiTagInfoWithConsul(this.info.token,this.company.testCompanySpi.name,'Empty')
      checkSpiDispatchEmptyWithConsul(this.info.token,this.company.testCompanySpi.name,testStrategyBody.SpiStrategyAdd.siteList[0])
      checkSpiDispatchEmptyWithConsul(this.info.token,this.company.testCompanySpi.name,testStrategyBody.SpiStrategyAdd.siteList[1])
    })

    it('modify spi CPE Strategy test', function(){
      changeSpiPanelView("策略应用")
      cy.get('[data-cy=addStrategy]').filter(':visible').click()
      cy.ClickMultiDropDownValue('.el-select__input',testStrategyBody.SpiStrategyModify.siteList)
      transfer_panel_Select_dedicate_scenario(testScenarioBody.SpiScenarioSaas.name)
      clickComfirm()
      cy.contains("创建成功").should('be.visible')
      cy.get('[data-cy="spiStrategyTable"]').should('be.visible')
      cy.get('[data-cy="strategySearch"]').clear().type(testScenarioBody.SpiScenarioSaas.name)
      cy.get('[data-cy="spiStrategyTable"]').contains(testStrategyBody.SpiStrategyModify.siteList[0]).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      transfer_panel_Select_dedicate_scenario(testScenarioBody.SpiScenarioPro.name)
      clickComfirm()
      cy.contains("更新成功").should('be.visible')
      cy.get('[data-cy="spiStrategyTable"]').contains(testStrategyBody.SpiStrategyModify.siteList[0]).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      transfer_panel_DeSelect_dedicate_scenario(testScenarioBody.SpiScenarioSaas.name)
      clickComfirm()
      cy.contains("更新成功").should('be.visible')
      checkSpiTagInfoWithConsul(this.info.token,this.company.testCompanySpi.name,'allIpUdp')
      checkSpiDispatchInfoWithConsul(this.info.token,this.company.testCompanySpi.name,testStrategyBody.SpiStrategyModify.siteList[0])
      cy.get('[data-cy="strategySearch"]').clear().type(testScenarioBody.SpiScenarioPro.name)
      cy.get('[data-cy="spiStrategyTable"]').contains(testStrategyBody.SpiStrategyModify.siteList[0]).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      delete_confirm()
    })

    it('search CPE Strategy test', function(){
      changeSpiPanelView("策略应用")
      cy.get('[data-cy=addStrategy]').filter(':visible').click()
      cy.ClickMultiDropDownValue('.el-select__input',testStrategyBody.SpiStrategyAdd.siteList)
      transfer_panel_Select_dedicate_scenario(testScenarioBody.SpiScenarioSaas.name)
      clickComfirm()
      cy.contains("创建成功").should('be.visible')
      cy.get('[data-cy="strategySearch"]').clear().type(testScenarioBody.SpiScenarioSaas.name)
      cy.contains('共 2 条')
      cy.get('[data-cy="strategySearch"]').clear().type(testStrategyBody.SpiStrategyAdd.siteList[0])
      cy.contains('共 1 条').filter(':visible')
      cy.get('[data-cy="strategySearch"]').clear().type(testStrategyBody.SpiStrategyAdd.siteList[1])
      cy.contains('共 1 条').filter(':visible')
      table_batch_delete('[data-cy="spiStrategyTable"]','[data-cy="batchDeleteStrategy"]')
      delete_confirm()
      cy.contains("删除成功")
    })

    //SDWANDEV-3933
    it('delete spi tag fail in global view test', function(){
      changeToGlobalView("spiManage",this.info)
      changeSpiPanelView("规则标识")
      cy.get('[data-cy="tagSearch"]').type(testSpiTagBody.SpiGTagSaas.name)
      cy.get('[data-cy="spiTagTable"]').contains(testSpiTagBody.SpiGTagSaas.name).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("确定").filter(':visible').click()
      cy.contains("删除失败")
    })

    it('create and delete global spi tag test', function(){
      changeToGlobalView("spiManage",this.info)
      changeSpiPanelView("规则标识")
      let checkListC = [this.company.testCompanySpi.name,testSpiTagBody.SpiTagAllIP.name,0,600]
      rowContains('[data-cy="spiTagTable"]',testSpiTagBody.SpiTagAllIP.name,2, 5 ,checkListC)
      cy.get('[data-cy=addActionTemplate]').filter(':visible').click()
      setTag(testSpiTagBody.SpiAddTag)
      cy.contains("创建成功")
      let checkList = ['all',testSpiTagBody.SpiAddTag.name,0,600]
      rowContains('[data-cy="spiTagTable"]',testSpiTagBody.SpiAddTag.name,2, 5 ,checkList)
      cy.get('[data-cy="tagSearch"]').type(testSpiTagBody.SpiAddTag.name)
      cy.get('[data-cy="spiTagTable"]').contains(testSpiTagBody.SpiAddTag.name).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("确定").filter(':visible').click()
      cy.contains("删除成功")
    })

    it('modify  global spi tag test', function(){
      changeToGlobalView("spiManage",this.info)
      changeSpiPanelView("规则标识")
      cy.get('[data-cy="tagSearch"]').type(testSpiTagBody.SpiGTagSaas.name)
      cy.get('[data-cy="spiTagTable"]').contains(testSpiTagBody.SpiGTagSaas.name).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      modifyTag(testSpiTagBody.SpiGModifyTag)
      cy.contains("更新成功")
      let checkList = ['all',testSpiTagBody.SpiGModifyTag.name,0,600]
      rowContains('[data-cy="spiTagTable"]',testSpiTagBody.SpiGModifyTag.name,2, 5 ,checkList)
      rowUnflod('[data-cy="spiTagTable"]',testSpiTagBody.SpiGModifyTag.name)
      testSpiTagBody.SpiGModifyTag.rules.forEach(rule => {
        cy.contains(rule.dstCIDR)
      })
      
    })

    it('spi tag company and global auth test', function(){
      changeSpiPanelView("规则标识")
      cy.get('[data-cy="tagSearch"]').clear().type(testSpiTagBody.SpiSTTagSaas.name)
      cy.contains('共 0 条').filter(':visible')
      cy.get('[data-cy="tagSearch"]').clear().type(testSpiTagBody.SpiGTagSaas.name)
      cy.contains('共 1 条').filter(':visible')
      changeToGlobalView("spiManage",this.info)
      changeSpiPanelView("规则标识")
      cy.get('[data-cy="tagSearch"]').clear().type(testSpiTagBody.SpiSTTagSaas.name)
      cy.contains('共 1 条').filter(':visible')
      cy.get('[data-cy="tagSearch"]').clear().type(testSpiTagBody.SpiGTagSaas.name)
      cy.contains('共 1 条').filter(':visible')
      cy.get('[data-cy="tagSearch"]').clear().type(testSpiTagBody.SpiTagSaas.name)
      cy.contains('共 1 条').filter(':visible')
    })
    
    it('global spi template can only select global tag test', function(){
      changeToGlobalView("spiManage",this.info)
      changeSpiPanelView("策略模板")
      cy.get('[data-cy=addTemplate]').filter(':visible').click()
      cy.get('#templateImport').click()
      cy.get('.el-scrollbar').filter(':visible').get('li[class=el-select-dropdown__item]').contains(testSpiTemplateBody.SpiTemplateSaas.tagName).should('not.exist')
      cy.get('.el-scrollbar').filter(':visible').get('li[class=el-select-dropdown__item]').contains(testSpiTemplateBody.SpiTemplatePro.tagName).should('not.exist')
      // cy.get('[style="z-index: 2008;"] > .el-dialog > .el-dialog__footer > .dialog-footer > .el-button--default').click()
    })
    
    it('create and delete global spi template test', function(){
      changeToGlobalView("spiManage",this.info)
      changeSpiPanelView("策略模板")
      cy.get('[data-cy=addTemplate]').filter(':visible').click()
      cy.ClickSelectValue('#templateImport',testSpiTemplateBody.SpiTemplateGAdd.tagName)
      cy.get('[class="el-dialog"]').filter(':visible').within(() => {
        cy.contains("确 定").click()
      })
      setTemplate(testSpiTemplateBody.SpiTemplateGAdd)
      clickComfirm()
      cy.contains("创建成功")
      let checkList = ['all',testSpiTemplateBody.SpiTemplateGAdd.tagName]
      rowContains('[data-cy="actionTemplates"]',testSpiTemplateBody.SpiTemplateGAdd.tagName,1, 2 ,checkList)
      cy.get('[data-cy="actionTemplates"]').contains(testSpiTemplateBody.SpiTemplateGAdd.tagName).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("确定").click()
    })

    //SDWANDEV-3936
    it('spi template company and global auth test', function(){
      changeSpiPanelView("策略模板")
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiTemplateSTSaas.name)
      cy.contains('共 0 条').filter(':visible')
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiTemplateGlobalSaas.name)
      cy.contains('共 1 条').filter(':visible')
      changeSpiPanelView("场景管理")
      cy.get('[data-cy="scenarioSearch"]').clear().type(testScenarioBody.SpiScenarioST.name)
      cy.contains('共 0 条').filter(':visible')
      cy.get('[data-cy="scenarioSearch"]').clear().type(testScenarioBody.SpiScenarioG.name)
      cy.contains('共 1 条')
      changeToGlobalView("spiManage",this.info)
      changeSpiPanelView("策略模板")
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiTemplateSTSaas.name)
      cy.contains('共 1 条').filter(':visible')
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiTemplateGlobalSaas.name)
      cy.contains('共 1 条').filter(':visible')
      changeSpiPanelView("场景管理")
      cy.get('[data-cy="scenarioSearch"]').clear().type(testScenarioBody.SpiScenarioST.name)
      cy.contains('共 1 条')
      cy.get('[data-cy="scenarioSearch"]').clear().type(testScenarioBody.SpiScenarioG.name)
      cy.contains('共 1 条')
    })

    it('modify global spi template test', function(){
      changeToGlobalView("spiManage",this.info)
      changeSpiPanelView("策略模板")
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiTemplateGlobalSaas.name)
      cy.get('[data-cy="actionTemplates"]').contains(testSpiTemplateBody.SpiTemplateGlobalSaas.name).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      modifyTemplate(testSpiTemplateBody.SpiTemplateGModify)
      clickComfirm()
      cy.contains("更新成功")
      let checkList = [testSpiTemplateBody.SpiTemplateGModify.tagName,'开','可靠']
      rowContainsVisible('[data-cy="actionTemplates"]',testSpiTemplateBody.SpiTemplateGModify.name,3, 5,checkList)
    })

    it('check import export SPI Tag file', function(){
      changeSpiPanelView("规则标识")
      cy.contains('批量导入').click()
      cy.get('[class="el-message-box"]').within(() => {
        cy.contains('确定').click()
      })
      const fileName = 'import_spiTags.xlsx';
      cy.get('[class="drop"]').attachFile(fileName, { subjectType: 'drag-n-drop' });
      cy.get('[data-cy="confirmEdit"]').click()
      cy.contains("成功")
      changeToGlobalView("spiManage",this.info)
      changeSpiPanelView("规则标识")
      cy.get('[data-cy="tagSearch"]').clear().type('QOS')
      cy.contains('共 3 条').filter(':visible')
      table_batch_delete('[data-cy="spiTagTable"]','[data-cy="batchDeleteTag"]')
      delete_confirm()
      cy.contains('导出 Excel').click()
      cy.get('[class="el-message-box"]').within(() => {
        cy.contains('确定').click()
      })
    })

    it('check import export spi template file', function(){
      changeToGlobalView("spiManage",this.info)
      changeSpiPanelView("策略模板")
      cy.get('[data-cy="importTemplates"]').filter(':visible').click()
      cy.get('[class="el-message-box"]').within(() => {
        cy.contains('确定').click()
      })
      const fileName = 'import_spiTemplate.xlsx';
      cy.get('[class="drop"]').attachFile(fileName, { subjectType: 'drag-n-drop' });
      cy.get('[data-cy="confirmEdit"]').click()
      cy.contains("成功")
      changeSiteCompanyView(this.company.testCompanySpi.name)
      changeSpiPanelView("策略模板")
      cy.get('[data-cy="templateSearch"]').clear().type('QOS')
      cy.contains('共 1 条').filter(':visible')
      table_batch_delete('[data-cy="actionTemplates"]','[data-cy="batchDeleteTemplate"]')
      delete_confirm()
      cy.get('[data-cy="exportTemplates"]').click()
      cy.get('[class="el-message-box"]').within(() => {
        cy.contains('确定').click()
      })
    })

      it('modify spi tag test', function(){
      changeSpiPanelView("规则标识")
      cy.get('[data-cy="tagSearch"]').type(testSpiTagBody.SpiModifyTag.name)
      cy.get('[data-cy="spiTagTable"]').contains(testSpiTagBody.SpiModifyTag.name).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      modifyTag(testSpiTagBody.SpiModifyTag)
      cy.contains("更新成功")
      let checkList = [testSpiTagBody.SpiModifyTag.name,0,600]
      rowContains('[data-cy="spiTagTable"]',testSpiTagBody.SpiModifyTag.name,2, 4 ,checkList)
      rowUnflod('[data-cy="spiTagTable"]',testSpiTagBody.SpiModifyTag.name)
      testSpiTagBody.SpiModifyTag.rules.forEach(rule => {
        cy.contains(rule.dstCIDR)
      })
    })

    it('modify spi Rule CPE Strategy test', function(){
      changeSpiPanelView("策略应用")
      cy.get('[data-cy=addStrategy]').filter(':visible').click()
      cy.ClickMultiDropDownValue('.el-select__input',testStrategyBody.SpiStrategyModify.siteList)
      transfer_panel_Select_dedicate_scenario(testScenarioBody.SpiScenarioSaas.name)
      clickComfirm()
      cy.contains("创建成功").should('be.visible')
      changeSpiPanelView("规则标识")
      cy.get('[data-cy="tagSearch"]').type(testSpiTagBody.SpiTagSaas.name)
      cy.get('[data-cy="spiTagTable"]').contains(testSpiTagBody.SpiTagSaas.name).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      ChangeRuleInTag(testSpiTagBody.SpiChangeTagRules)
      cy.contains("更新成功")
      checkSpiTagInfoWithConsul(this.info.token,this.company.testCompanySpi.name,'saasNew')
      checkSpiDispatchInfoWithConsul(this.info.token,this.company.testCompanySpi.name,testStrategyBody.SpiStrategyModify.siteList[0]+'2')
      changeSpiPanelView("策略应用")
      cy.get('[data-cy="strategySearch"]').clear().type(testScenarioBody.SpiScenarioSaas.name)
      cy.get('[data-cy="spiStrategyTable"]').contains(testStrategyBody.SpiStrategyModify.siteList[0]).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      delete_confirm()
    })
    
    //SDWANDEV-4007
    it('change spi Scenario test', function(){
      changeSpiPanelView("策略应用")
      cy.get('[data-cy=addStrategy]').filter(':visible').click()
      cy.ClickMultiDropDownValue('.el-select__input',testStrategyBody.SpiStrategyModify.siteList)
      transfer_panel_Select_dedicate_scenario(testScenarioBody.SpiScenarioSaas.name)
      clickComfirm()
      cy.contains("创建成功").should('be.visible')
      changeSpiPanelView("场景管理")
      cy.get('[data-cy="scenarioSearch"]').clear().type(testScenarioBody.SpiScenarioSaas.name)
      cy.get('[data-cy="spiScenarioTable"]').contains(testScenarioBody.SpiScenarioSaas.name).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      transfer_panel_all_Select()
      clickComfirm()
      cy.contains("更新成功").should('be.visible')
      checkSpiTagInfoWithConsul(this.info.token,this.company.testCompanySpi.name,'all')
      changeSpiPanelView("策略应用")
      cy.get('[data-cy="strategySearch"]').clear().type(testScenarioBody.SpiScenarioSaas.name)
      cy.get('[data-cy="spiStrategyTable"]').contains(testStrategyBody.SpiStrategyModify.siteList[0]).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      delete_confirm()
    })

    //SDWANDEV-4693
    it('create and delete spi saas Designated export template test', function(){
      changeSpiPanelView("策略模板")
      cy.get('[data-cy=addTemplate]').filter(':visible').click()
      cy.ClickSelectValue('#templateImport',testSpiTemplateBody.SpiSAASDesignatedTemplateAdd.tagName)
      cy.contains("选择Tag").parents('[class="el-dialog"]').within(()=>{
        cy.contains("确 定").click()
      })
      setTemplate(testSpiTemplateBody.SpiSAASDesignatedTemplateAdd)
      clickComfirm()
      cy.contains("创建成功")
      let checkList = [testSpiTemplateBody.SpiSAASDesignatedTemplateAdd.tagName,'开']
      rowContains('[data-cy="actionTemplates"]',testSpiTemplateBody.SpiSAASDesignatedTemplateAdd.tagName,2, 3 ,checkList)      
      cy.get('[data-cy="actionTemplates"]').contains(testSpiTemplateBody.SpiSAASDesignatedTemplateAdd.name).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      cy.contains("确定").click()
    })

    //SDWANDEV-4659
    it('create saas Designated same export fail template test', function(){
          changeSpiPanelView("策略模板")
          cy.get('[data-cy=addTemplate]').filter(':visible').click()
          cy.ClickSelectValue('#templateImport',testSpiTemplateBody.SpiSAASDesignatedTemplateAdd.tagName)
          cy.contains("选择Tag").parents('[class="el-dialog"]').within(()=>{
            cy.contains("确 定").click()
          })
         setTemplateFail(testSpiTemplateBody.SpiSAASDesignatedTemplateAdd)

        })

    //SDWANDEV-4651
    it('create and delete Dedicate CPE Strategy test', function(){
      changeSpiPanelView("策略应用")
      cy.get('[data-cy=addStrategy]').filter(':visible').click()
      cy.ClickMultiDropDownValue('.el-select__input',testStrategyBody.SpiStrategyDedicate.siteList)
      transfer_panel_Select_dedicate_scenario(testScenarioBody.SpiDedicateScenario.name)
      clickComfirm()
      cy.contains("创建成功").should('be.visible')
      checkSpiDispatchInfoWithConsul(this.info.token,this.company.testCompanySpi.name,testStrategyBody.SpiStrategyDedicate.siteList[0])
      cy.get('[data-cy="spiStrategyTable"]').should('be.visible')
      let checkList = [testSpiTemplateBody.SPITemplateDedicate.tagName,1]
      rowContains('[data-cy="spiStrategyTable"]',testStrategyBody.SpiStrategyDedicate.siteList[0],3, 4 ,checkList)
      cy.get('[data-cy="strategySearch"]').clear().type(testScenarioBody.SpiDedicateScenario.name)
      cy.get('[data-cy="spiStrategyTable"]').contains(testStrategyBody.SpiStrategyDedicate.siteList[0]).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      delete_confirm()
    })

    //SDWANDEV-4657
    it('delete saas not allow', function(){
      visitAndSetPageUserInfo('/service',this.info)
      changeToGlobalView("service",this.info)
      cy.get('[data-cy=popSearch]').clear().type(testServiceBody.putSaasBody.popId)
      cy.contains('button', '删除').eq(0).click()
      cy.contains('button', '确定').click()
      cy.contains('禁止删除已被策略模板引用的SaaS服务')
      
  })

    //SDWANDEV-4660
    it('modify spi dedicate template CPE Strategy test', function(){
      changeSpiPanelView("策略应用")
      cy.get('[data-cy=addStrategy]').filter(':visible').click()
      cy.ClickMultiDropDownValue('.el-select__input',testStrategyBody.SpiStrategyDedicate.siteList)
      transfer_panel_Select_dedicate_scenario(testScenarioBody.SpiDedicateScenario.name)
      clickComfirm()
      cy.contains("创建成功").should('be.visible')
      changeSpiPanelView("策略模板")
      cy.get('[data-cy="templateSearch"]').clear().type(testSpiTemplateBody.SpiSAASDedicateTemplateModify.name)
      cy.get('[data-cy="actionTemplates"]').contains(testSpiTemplateBody.SpiSAASDedicateTemplateModify.name).parents('tr').within(() => {
        cy.contains("编辑").click()
      })
      modifyTemplate(testSpiTemplateBody.SpiSAASDedicateTemplateModify)
      clickComfirm()
      cy.contains("更新成功")
      checkSpiDispatchInfoWithConsul(this.info.token,this.company.testCompanySpi.name,testStrategyBody.SpiStrategyDedicate.siteList[0]+'2')
      changeSpiPanelView("策略应用")
      cy.get('[data-cy="strategySearch"]').clear().type(testScenarioBody.SpiDedicateScenario.name)
      cy.get('[data-cy="spiStrategyTable"]').contains(testStrategyBody.SpiStrategyDedicate.siteList[0]).parents('tr').within(() => {
        cy.contains("删除").click()
      })
      delete_confirm()
    })


  })
