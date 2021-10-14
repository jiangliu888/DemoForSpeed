import {createCompany, deleteCompanyByName} from '../utils/basic-utils'
import {checkCompanyInfoWithConsul, checkCompEncryptionWithConsul} from '../utils/consulCheck-utils'
import {getToken, visitAndSetPageUserInfo,rowContains,changeToGlobalView, setCompany} from '../utils/web-utils'
import {testCompanyBody} from '../utils/variables-utils'

before(getToken)


export function updateCompanyEncryption(company, aes) {
      cy.get('[data-cy=companyTable]').contains(company.name).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
      })
      cy.get('[data-cy=companyDialog]').within(() => {
          cy.typeElinputWithLable('加密算法', aes)
          cy.contains('确 定').click()
      })
      cy.contains('更新成功')
}

describe('company page test', function() {

  beforeEach(function () {
    visitAndSetPageUserInfo('/companyMessage',this.info)
    //删除公司
      deleteCompanyByName(this.info.token,testCompanyBody.testCompany.name)
      deleteCompanyByName(this.info.token,testCompanyBody.testCompanyModify.name)
    //创建公司
      createCompany(this.info.token,testCompanyBody.testCompanyModify)
    cy.reload()
    changeToGlobalView("companyMessage",this.info)
   })

    it('create and delete company test', function(){
      setCompany(testCompanyBody.testCompany)
      cy.contains('创建成功')
      cy.get('@info').then(t_info => {
        checkCompanyInfoWithConsul(t_info.token,testCompanyBody.testCompany.name)
      })
      //确定公司添加成功
      rowContains('[data-cy=companyTable]',testCompanyBody.testCompany.name,3,5,[testCompanyBody.testCompany.contact,testCompanyBody.testCompany.address])
      //delete company
      cy.get('[data-cy=companyTable]').contains(testCompanyBody.testCompany.name).parents('tr').within(() => {
        cy.contains('button', '删除').click()
      })
      cy.get('[class="el-message-box__btns"]').contains("确定").click()
    })

    it('modify company test', function(){
      cy.get('[data-cy=companyTable]').contains(testCompanyBody.testCompanyModify.name).parents('tr').within(() => {
        cy.contains('button', '编辑').click()
      })
      cy.get('[data-cy=companyDialog]').within(() => { //will find by data-cy (new company dialog)
        cy.typeInputWithLable('公司英文名','test-Company1') // Only yield inputs within dialog
        cy.typeInputWithLable('联系人','tester1') // Only yield inputs within dialog
        cy.typeInputWithLable('固定电话','test-phone1')
        cy.typeInputWithLable('手机','18696198901')
        cy.typeTextareaWithLable('备注',['test-remark'])
        cy.typeInputWithLable('邮箱','test-mail@test.com')
        cy.typeInputWithLable('地址','测试地址1')
        cy.contains('确 定').click()
      })
      cy.contains('更新成功')
      //check modify success
      rowContains('[data-cy=companyTable]',testCompanyBody.testCompanyModify.name,3,5,['test-phone1','测试地址1'])
    })

    it('modify company encryption', function () {
        // 4326
        updateCompanyEncryption(testCompanyBody.testCompanyModify, 'AES-256')
        checkCompEncryptionWithConsul(this.info.token, testCompanyBody.testCompanyModify.name, 'AES-256', 32)
        updateCompanyEncryption(testCompanyBody.testCompanyModify, 'AES-192')
        checkCompEncryptionWithConsul(this.info.token, testCompanyBody.testCompanyModify.name, 'AES-192', 32)
        updateCompanyEncryption(testCompanyBody.testCompanyModify, 'DES')
        checkCompEncryptionWithConsul(this.info.token, testCompanyBody.testCompanyModify.name, 'DES', 32)
        updateCompanyEncryption(testCompanyBody.testCompanyModify, '3DES')
        checkCompEncryptionWithConsul(this.info.token, testCompanyBody.testCompanyModify.name, '3DES', 32)
        updateCompanyEncryption(testCompanyBody.testCompanyModify, 'AES-128')
        checkCompEncryptionWithConsul(this.info.token, testCompanyBody.testCompanyModify.name, 'AES-128', 16)
    })
})
