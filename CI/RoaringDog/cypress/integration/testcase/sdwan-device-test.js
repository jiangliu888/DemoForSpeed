import {
    deleteCompanyByName,
    deleteAllSites,
    createCompanyByData,
    createSiteByData,
    initCpeGlobalConf,
    deleteUser,
    createUser,
    deletePopByPopId,
    getPopNEidByPopId,
    getLogsNumber,
    createPOP,
    deleteAllUnions,
    deleteAllUsers,
    deleteAllRole,
    deleteAllGlobalUsersExceptAdmin, createRole, createUnion
} from '../utils/basic-utils'
import {getToken, visitAndSetPageUserInfo, changeSiteCompanyView, editWebSite,createWebSite, rowContains,ClickRow,createWebUnion,changeToGlobalView,ClickSidebarSubMenu,CheckWebSiteReadonly, checkHomeCodeRow} from '../utils/web-utils'
import {
    putDevicePopBody, putDevicePop2Body, testPopBody,
    UserBody, RoleBody
} from '../utils/variables-utils'
import {
    checkNeAlertWithConsul, exec_cmd_on_host,
} from '../utils/consulCheck-utils'


before(function () {
  cy.fixture("companies/companies.json").as('company')
  cy.fixture("companies/sites/sites.json").as('site')
  getToken()
  exec_cmd_on_local("bash /e2e/RoaringDog/test/prepDevicetest.sh")
  cy.reload()
  // cy.get('@company').then(company => {
  //     cy.get('@info').then(t_info => {
  //     createRole(t_info.token, 'all', RoleBody.deviceRole)
  //     createUser(t_info.token,UserBody.devideTestUser)
  //   })
  // })
})

describe('device page test', function() {
   beforeEach(function () {
       visitAndSetPageUserInfo('/device',this.info)
       changeToGlobalView("device", this.info)
   })

    it('Search by Company and SN', function(){
        //  SDWANDEV-4469
        changeSiteCompanyView('Distributor-company')
        cy.get('[data-cy="deviceSearch"]').clear().type('pany12')
        cy.get('[data-cy="deviceSearch"]').parent().next().click()
        cy.contains('共 1 条')
        changeToGlobalView("device",this.info)
        cy.get('[data-cy="deviceSearch"]').clear().type('pany12')
        cy.get('[data-cy="deviceSearch"]').parent().next().click()
        cy.contains('共 4 条')
     })

    it('Alarm Control Test', function () {
        // SDWANDEV-4363
        changeSiteCompanyView('Distributor-company')
        // default is unchecked
        cy.get('[data-cy=deviceTable]').get('tr').each(($li, index, $lis) => {
            cy.get('td').eq(6).within(() => {
                cy.get('[class="el-switch"]')
            })
        })
        // inhibition on (one cpe)
        cy.get('[data-cy=deviceTable]').contains(this.site.DistributorSiteBody.sn[0]).parents('tr').eq(0).get('td').eq(6).click()
        checkNeAlertWithConsul(this.site.DistributorSiteBody.sn, 0)
        // inhibition on (all)
        cy.get('[data-cy=deviceTable]').contains('资产序列号').parents('tr').within(() => {
            cy.get('input[type="checkbox"]').click({force: true})
        })
        cy.contains('批量告警处理').click()
        cy.get('[class="el-message-box"]').contains("抑制").click()
        cy.contains('批处理成功')
        // check all cpes' consul configs
        var disComSites = ['3001', '3002', '3003', 'pany12-']
        disComSites.forEach(siteSn => {
            cy.log(siteSn)
            checkNeAlertWithConsul(siteSn, 0)
        })
        // inhibition off (one cpe)
        cy.get('[data-cy=deviceTable]').contains(this.site.DistributorSiteBody.sn[0]).parents('tr').eq(0).get('td').eq(6).click()
        checkNeAlertWithConsul(this.site.DistributorSiteBody.sn, 1)
        // inhibition off (all)
        cy.get('[data-cy=deviceTable]').contains('资产序列号').parents('tr').within(() => {
            cy.get('input[type="checkbox"]').click({force: true})
        })
        cy.contains('批量告警处理').click()
        cy.get('[class="el-message-box"]').contains("激活").click()
        cy.contains('批处理成功')
        // check all cpes' consul configs
        var disComSites = ['3001', '3002', '3003', 'pany12-']
        disComSites.forEach(siteSn => {
            checkNeAlertWithConsul(siteSn, 1)
        })
        //check the operation log of device
        getLogsNumber(this.info.token,{resourceType:'device',action:'update',company:this.company.testCompanyDevice.name,username:'admin',detail:'激活告警'})
        cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(5)})
        getLogsNumber(this.info.token,{resourceType:'device',action:'update',company:this.company.testCompanyDevice.name,username:'admin',detail:'抑制告警'})
        cy.get('@logsNumber').then(logsNumber =>{expect(logsNumber).to.equal(5)})
    })

    it('Jump to Site Page', function () {
        // SDWANDEV-4367
        changeToGlobalView("device", this.info)
        cy.get('[data-cy="deviceSearch"]').clear().type('pany12')
        cy.get('[data-cy="deviceSearch"]').parent().next().click()
        cy.contains('共 4 条')
        // Check company name
        cy.get('[data-cy="deviceTable"]').get('tr').eq(1).within(() => {
            cy.get('td').eq(1).contains('Distributor-company')
            // Click site
            cy.get('td').eq(2).click()
        })
            .then(() => {
                cy.url().should('include', '/site')
                cy.contains('配置')
                cy.contains('共 1 条')
            })
    })
    
    it('HomeCode failed including 4G', function () {
        // SDWANDEV-4702
        cy.get('[data-cy="deviceSearch"]').clear().type('300')
        cy.get('[data-cy="deviceSearch"]').parent().next().click()
        checkHomeCodeRow('3001', ['选区失败', putDevicePop2Body.hostname])
        checkHomeCodeRow('3006', ['选区失败', '选区失败', '选区失败'])
    })

    it('HomeCode with single wan succeeded', function () {
        // SDWANDEV-4703
        cy.get('[data-cy="deviceSearch"]').clear().type('300')
        cy.get('[data-cy="deviceSearch"]').parent().next().click()
        checkHomeCodeRow('3004', [putDevicePop2Body.hostname])
        // TODO: 悬停
    })

    it('HomeCode with multi-wans succeeded', function () {
        // SDWANDEV-4704
        cy.get('[data-cy="deviceSearch"]').clear().type('300')
        cy.get('[data-cy="deviceSearch"]').parent().next().click()
        checkHomeCodeRow('3002', [putDevicePop2Body.hostname, putDevicePopBody.hostname])
    })

    it('HomeCode with multi-wans succeeded and failed', function () {
        // SDWANDEV-4705
        cy.get('[data-cy="deviceSearch"]').clear().type('pany12')
        cy.get('[data-cy="deviceSearch"]').parent().next().click()
        checkHomeCodeRow('pany12-', [putDevicePop2Body.hostname, '选区失败', putDevicePop2Body.hostname])
    })

    it.skip('Non-admin global mode can also check the homeCode', function () {
        // SDWANDEV-4706
        cy.get('[data-cy="deviceSearch"]').clear().type('pany12')
        cy.get('[data-cy="deviceSearch"]').parent().next().click()
        // TODO: login with non-admin
        checkHomeCodeRow('pany12-', [putDevicePop2Body.hostname, '选区失败', putDevicePop2Body.hostname])
    })

    it('The device page should show up even device=0', function () {
        // SDWANDEV-4716
        cy.get('[data-cy="deviceSearch"]').clear().type('aaa')
        cy.get('[data-cy="deviceSearch"]').parent().next().click()
        cy.contains('暂无数据')
        // when bug SDWANDEV-4714 is fixed can check this point
        //cy.contains('共 0 条')
    })
})
