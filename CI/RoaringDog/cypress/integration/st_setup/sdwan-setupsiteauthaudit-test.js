import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView, enableSiteAuthAudit, enableAuth, enableAudit} from '../utils/web-utils'
import {auditParam, authParam, testSiteBody} from '../utils/variables-utils'
import {exec_cmd_on_local} from '../utils/consulCheck-utils'


before(function(){
  cy.fixture("companies/companies.json").as('company')
  getToken()
  exec_cmd_on_local("bash /e2e/RoaringDog/test/prepSTAuthtest.sh")
})

describe('auth audit page test', function() {
   beforeEach(function () {
    visitAndSetPageUserInfo('/auditConfig',this.info)
    changeSiteCompanyView(this.company.testCompanyST.name)
   })

    if (testSiteBody.hasOwnProperty('testSTNanchang')) {
        it('config auth audit param', function () {
            enableAudit(auditParam.auditUrl, auditParam.auditPort)
            enableAuth(authParam.authInnerUrl, authParam.authOutUrl, authParam.redirectUrl, authParam.authOutPort, authParam.authInnerPort, authParam.bindTimeout, authParam.noTrafficTimeout, 'Radius认证', authParam.radiusParam)
            cy.wait(4000)
            visitAndSetPageUserInfo('/site', this.info)
            enableSiteAuthAudit(testSiteBody.testSTNanchang.name, testSiteBody.testSTNanchang.sn, false, true, auditParam.siteSTNanchangMac)
        })
    }
})
