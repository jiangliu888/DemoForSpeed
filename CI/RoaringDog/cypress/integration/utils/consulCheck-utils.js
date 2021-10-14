
import {getIdByCompanyName,getIdBySiteName,getIdByUnionName,getIdBySaasRuleName,getSiteNEidByName,getPopNEidByPopId} from '../utils/basic-utils'
const pythonLogPath = "cypress/results/pythoncmd.log"
const cmdLogPath = "cypress/results/cmd.log"

export function checkSite(token, companyName, siteName, sn){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    getSiteNEidByName(token,companyId, siteName)
    cy.get('@neId').then(neId => {
      expect(neId).to.not.equal("")
      checkSiteInfoWithConsul(token, companyId, siteName, neId, sn)
      checkSiteNEInfoWithConsul(neId, siteName)
    })
  })
}

export function checkDevice(token, companyName, siteName, sn){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    getSiteNEidByName(token,companyId, siteName)
    cy.get('@neId').then(neId => {
      expect(neId).to.not.equal("")
      checkAiwanInfoWithConsul(sn, neId, companyId)
      checkAiwanStartupWithConsul(sn)
    })
  })
}

export function checkSiteInfoWithConsul(token, companyId, siteName, neId){
  getIdBySiteName(token, companyId, siteName)
  cy.get('@siteId').then(siteId => {
    expect(siteId).to.not.equal("")
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['site','siteRateLimit']\" " + companyId + " " + siteId + " " + siteName + " " + neId
    exec_cmd_on_local(cmd)
  })
}

export function checkUnionInfoWithConsul(token, companyName, unionName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    getIdByUnionName(token, companyId, unionName)
    cy.get('@unionId').then(unionId => {
      expect(unionId).to.not.equal("")
      let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['union','unionRateLimit']\" " + companyId + " " + unionId + " " + unionName
      exec_cmd_on_local(cmd)
    })
  })
}

export function checkSiteNEInfoWithConsul(neId, siteName){
  let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['nePreference','neRateLimit','neNetConfig']\" " + neId + " " + siteName
  exec_cmd_on_local(cmd)
}

export function checkAiwanInfoWithConsul(sn, neId, companyId){
  let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['info']\" " + sn + " " + neId + " " + companyId
  exec_cmd_on_local(cmd)
}

export function checkNeAlertWithConsul(sn, alertEnable){
  let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['neAlert']\" " + sn + ' ' + alertEnable
  exec_cmd_on_local(cmd)
}

export function checkAiwanStartupWithConsul(sn){
  let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['startup']\" " + sn
  exec_cmd_on_local(cmd)
}

export function checkSystemWithConsul(sn){
  checkSystemNetworkWithConsul(sn)
  checkSystemWifiWithConsul(sn)
}

export function checkSystemNetworkWithConsul(sn){
  let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['network']\" " + sn
  exec_cmd_on_local(cmd)
}

export function checkSystemWifiWithConsul(sn){
  let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['wifi']\" " + sn
  exec_cmd_on_local(cmd)
}

export function checkCompEncryptionWithConsul(token, companyName, algorithm, keyLen){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
      expect(companyId).to.not.equal("")
      let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['encryption']\" " + companyId + " " + algorithm + " " + keyLen
      exec_cmd_on_local(cmd)
  })
}

export function checkCompanyInfoWithConsul(token, companyName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['company']\" " + companyId + " " + companyName
    exec_cmd_on_local(cmd)
  })
}

export function checkSaasRuleInfoWithConsul(token, companyName, saasRuleName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    getIdBySaasRuleName(token,companyId,saasRuleName)
    cy.get('@ruleId').then(ruleId => {
      expect(ruleId).to.not.equal("")
      let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['saasRule']\" " + ruleId + " " + saasRuleName
      exec_cmd_on_local(cmd)
    })
  })
}

export function checkSpiTagInfoWithConsul(token, companyName, tagsName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['spiTag']\" " + companyId + " " + tagsName
    exec_cmd_on_local(cmd)
  })
}

export function checkSpiDispatchInfoWithConsul(token, companyName, siteName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    getIdBySiteName(token,companyId,siteName.replace(/[0-9]/g, ''))
    cy.get('@siteId').then(siteId => {
      let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['spiDispatch']\" " + companyId + " " + siteName + " " + siteId
      exec_cmd_on_local(cmd)
    })    
  })
}

export function checkSpiDispatchEmptyWithConsul(token, companyName, siteName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    getIdBySiteName(token,companyId,siteName)
    cy.get('@siteId').then(siteId => {
      let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['spiDispatch']\" " + companyId + " Empty " + siteId
      exec_cmd_on_local(cmd)
    })
  })
}

export function checkGlobalConfigNeWithConsul(){
  let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['cpeglobalconfigne']\" "
  exec_cmd_on_local(cmd)
}

export function checkGaeaServiceWithConsul(){
  let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['manager','openflow','netAlgConfig']\" "
  exec_cmd_on_local(cmd)
}

export function checkSearchPatternWithConsul(code){
  let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['saasSearchPattern', 'anycastSearchPattern']\" " + code
  exec_cmd_on_local(cmd)
}

export function checkCompanySearchPatternWithConsul(token, companyName, code){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['companySaasSearchPattern']\" " + companyId + " "+ code
    exec_cmd_on_local(cmd)
  })
}

export function checkPopInfoWithConsul(token,popId,popType){
    getPopNEidByPopId(token,popId,popType)
    cy.get('@neId').then(neId => {
      expect(neId).to.not.equal("")
      let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['pop']\" " + popId + " " + neId
      exec_cmd_on_local(cmd)
    })
}

export function checkPopStatusWithConsul(token, popId, popType,popStatus){
  getPopNEidByPopId(token,popId,popType)
    cy.get('@neId').then(neId => {
      expect(neId).to.not.equal("")
      let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['pop_status']\" " + neId + " "+popStatus  
      exec_cmd_on_local(cmd)
    })
}

export function checkAclsWithConsul(token, companyName, siteName, aclName){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    getIdBySiteName(token, companyId, siteName)
    cy.get('@siteId').then(siteId => {
        expect(siteId).to.not.equal("")
        let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['acls']\" " + companyId + " " + siteId + " " + aclName
        exec_cmd_on_local(cmd)
      })
  })
}

export function checkroutersWithConsul(token, companyName, siteName, routerName, nextHop){
  getIdByCompanyName(token, companyName)
  cy.get('@companyId').then(companyId => {
    expect(companyId).to.not.equal("")
    getIdBySiteName(token, companyId, nextHop)
    cy.get('@siteId').then(nextHop => {
      expect(nextHop).to.not.equal("")
      getIdBySiteName(token, companyId, siteName)
      cy.get('@siteId').then(siteId => {
            expect(siteId).to.not.equal("")
            let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['routers']\" " + companyId + " " + siteId + " " + routerName + " " + nextHop
            exec_cmd_on_local(cmd)
      })
  })
})
}

export function checkAuthAuditConsul(deviceId, auth, audit){
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckConsul.py \"['neAuditAuth']\" " + deviceId+ " " + auth + " " + audit
    exec_cmd_on_local(cmd)
}

export function exec_cmd_on_host(host_ip,r_cmd){
  let cmd = 'sshpass -p rocks ssh -o StrictHostKeyChecking=no jenkins@' + host_ip + " '" + r_cmd + "'"
  cy.log(cmd)
  cy.exec(cmd,{ failOnNonZeroExit: false }).then(result => {
    cy.writeFile(pythonLogPath,r_cmd + "\ncmdError:\n" + result.stderr + "\n" + result.stdout + "\n", {flag: 'a+'})
    cy.log(result.stderr) 
    cy.log(result.stdout)
    cy.wrap(result.stdout).as('result')
    cy.wrap({'code':result.code})
}).its('code').should('eq',0)
}

export function add_server_port(){
  exec_cmd_on_host('10.194.20.105', 'cd /home/sdn/NoDelete; sh addport.sh')
}

export function del_server_port(){
  exec_cmd_on_host('10.194.20.105', 'cd /home/sdn/NoDelete; sh clearport.sh')
}

export function modify_cpe_type(sn, type){
  exec_cmd_on_host('10.194.20.105', 'cd /home/sdn/NoDelete; sh updatemodel.sh ' + sn + " " + type)
}

export function exec_cmd_on_local(cmd){
  cy.log(cmd)
  cy.exec(cmd,{ failOnNonZeroExit: false }).then(result => {
    cy.writeFile(pythonLogPath,cmd + "\ncmdError:\n" + result.stderr + "\n" + result.stdout + "\n", {flag: 'a+'})
    cy.log(result.stderr) 
    cy.log(result.stdout)
    cy.wrap({'code':result.code})
}).its('code').should('eq',0)
}

export function checkDeviceDeleted(neId){
  let cmd = "curl http://127.0.0.1:6126/api/v1/ne/" + neId
  exec_cmd_on_host("172.17.0.1", cmd)
  cy.get('@result').then(result => {
    expect(result).to.equal("DELETED")
  })
}