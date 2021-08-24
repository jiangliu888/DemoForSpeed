
import {getDataByCompanyName} from '../utils/basic-utils'
import {exec_cmd_on_local} from '../utils/consulCheck-utils'


export function checkAuditCorpInfo(token, companyName){
  getDataByCompanyName(token, companyName)
  cy.get('@createData').then(createData => {
    expect(createData).to.not.equal("")
    let cmd = "export PYTHONPATH=../erlang;export PYTHONHTTPSVERIFY=0;python cypress/integration/utils/python-util/CheckAudit.py \"['check_corp']\" " + companyName + " " + createData
    exec_cmd_on_local(cmd)
  })
}

export function checkAuditCorpApInfo(token, companyName, siteName, siteMac, checkIn){
  getDataByCompanyName(token, companyName)
  cy.get('@createData').then(createData => {
    expect(createData).to.not.equal("")
    let cmd = "export PYTHONPATH=../erlang;export PYTHONHTTPSVERIFY=0;python cypress/integration/utils/python-util/CheckAudit.py \"['check_ap']\" " + createData+ " " + siteName + " " + siteMac + " " + checkIn
    exec_cmd_on_local(cmd)
  })
}

export function checkAuthLdapTimeoutNavUrlInfo(){
  let cmd = "export PYTHONPATH=../erlang;export PYTHONHTTPSVERIFY=0;python cypress/integration/utils/python-util/CheckAuth.py \"['ldap','timeout','navUrl']\" "
  exec_cmd_on_local(cmd)
}

export function checkAuthRaduisInfo(){
  let cmd = "export PYTHONPATH=../erlang;export PYTHONHTTPSVERIFY=0;python cypress/integration/utils/python-util/CheckAuth.py \"['raduis']\" "
  exec_cmd_on_local(cmd)
}

export function checkBlackWhiteInfo(blackList, nameType, content, expectNum){
  let cmd = "export PYTHONPATH=../erlang;export PYTHONHTTPSVERIFY=0;python cypress/integration/utils/python-util/CheckAuth.py \"['blackWhiteList']\" "+ blackList+ " " + nameType + " " + content+ " " + expectNum
  exec_cmd_on_local(cmd)
}