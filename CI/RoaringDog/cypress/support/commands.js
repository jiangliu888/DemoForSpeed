// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add("login", (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add("drag", { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add("dismiss", { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite("visit", (originalFn, url, options) => { ... })
import 'cypress-file-upload';
Cypress.Commands.add('typeLogin', (username, password) => {
    cy.get('[name=username]').clear()
    cy.get('[name=username]').type(username).should('have.value',username)
    cy.get('[name=password]').clear()
    cy.get('[name=password]').type(password).should('have.value',password)
    cy.contains('button', '登录').click()
})

Cypress.Commands.add('logout', () => {
    cy.get('.el-dropdown-menu.el-popper').contains('退出登录').click({force: true})
})

Cypress.Commands.add('typeInputWithLable', (lableName, lableValue) => {
    cy.contains(lableName).parent('div').within(() => {
        if (lableValue == '') {
            cy.get('[class="el-input__inner"]').clear({force: true})
        }
        else {
            cy.get('[class="el-input__inner"]').clear({force: true}).type(lableValue)
        }
     })
})

Cypress.Commands.add('clearLableValue', (lableName, lableValue) => {
    cy.contains(lableName).parent('div').within(() => {
        cy.get('[class="el-input__inner"]').clear({force: true})
    })
})

Cypress.Commands.add('ClickInputWithLable', (lableName, lableValue) => {
    cy.contains(lableName).parent('div').within(() => {
        cy.get('[class="el-input__inner"]').click({force: true})
        cy.get('[class="el-input__inner"]').clear({force: true}).type(lableValue,{force: true})
     })
})

Cypress.Commands.add('typeElinputWithLable', (lableName, lableValue) => {
    cy.contains(lableName).parent('div').within(() => {
        cy.get('[class="el-scrollbar"]').contains(lableValue).click({force: true})
     })
})

Cypress.Commands.add('typeMultiElinputWithLable', (lableName, lableValueList) => {
    cy.contains(lableName).parent('div').within(() => {
        cy.get('[class="el-scrollbar"]').within(() => {
          lableValueList.forEach(lableValue => {
              cy.contains(lableValue).click({force: true})
            })
        })
     })
})

Cypress.Commands.add('typeTextareaWithLable', (lableName, lableValue) => {
    cy.contains(lableName).parent('div').within(() => {
        var values = lableValue.join('\r');
        cy.get('[class="el-textarea__inner"]').clear().type(values)
     })
})

Cypress.Commands.add('typeTextareaWithDataCy', (datacy, lableValue) => {
    cy.get(datacy).parent('div').within(() => {
        var values = lableValue.join('\r');
        cy.get('[class="el-textarea__inner"]').clear().type(values)
     })
})

Cypress.Commands.add('typeValueBydatacy', (datacy, Value) => {
    cy.get(datacy).within( ()=> {cy.get("input").clear().type(Value)})
})

Cypress.Commands.add('clearValueBydatacy', (datacy) => {
    cy.get(datacy).within( ()=> {cy.get("input").clear()})
})

Cypress.Commands.add('CheckDefaultInputValueBydatacy', (datacy, Value) => {
    cy.get(datacy).within( ()=> {cy.get("input").should('have.value', Value)})
})

Cypress.Commands.add('checkCheckBoxWithLable', (lableName) => {
    cy.contains(lableName).parent('div').within(() => {
        cy.get('[type="checkbox"]').check({force: true})
     })
})

Cypress.Commands.add('unCheckCheckBoxWithLable', (lableName) => {
    cy.contains(lableName).parent('div').within(() => {
        cy.get('[type="checkbox"]').uncheck({force: true})
     })
})

Cypress.Commands.add('CheckBoxWithLableDefault', (lableName, defaultVlaue) => {
    cy.contains(lableName).parent('div').within(() => {
        cy.get('div').should('have.class', defaultVlaue)
     })
})

Cypress.Commands.add('checkCheckBoxWithDatacy', (lableName) => {
    cy.get(lableName).within(() => {
        cy.get('[type="checkbox"]').check({force: true})
     })
})

Cypress.Commands.add('unCheckCheckBoxWithDatacy', (lableName) => {
    cy.get(lableName).within(() => {
        cy.get('[type="checkbox"]').uncheck({force: true})
     })
})

Cypress.Commands.add('clickElcascaderWithLable', (lableName) => {
    cy.contains(lableName).parent('div').within(() => {
        cy.get('[class="el-input__inner"]').click()
     })
})

Cypress.Commands.add('clickButtonWithLable', (lableName) => {
    cy.contains(lableName).click()
})

Cypress.Commands.add('checkGroupCheckBoxWithLable', (lableName) => {
    cy.get('[value="'+lableName+'"]').check({force: true})
})

Cypress.Commands.add('ClickSelectValue', (dataCyName, lableValue) => {
        cy.get(dataCyName).click()
        cy.get('.el-scrollbar').filter(':visible').get('li[class=el-select-dropdown__item]').contains(lableValue).should('be.visible').click({force: true})
})

Cypress.Commands.add('ClickSelectValue2', (dataCyName, lableValue) => {
    cy.get(dataCyName).click()
    cy.wait(400)
    cy.get('.el-scrollbar').filter(':visible').within(() =>{
        cy.get('li[class^=el-select-dropdown__item]').contains(lableValue).should('be.visible').click({force: true})
    })
})


Cypress.Commands.add('ClickDropDownValue', (dataCyName, dropDownDataCy,lableValue) => {
    cy.get(dataCyName).click()
    cy.get(dropDownDataCy).filter(':visible').contains(lableValue).should('be.visible').click({force: true})
})

Cypress.Commands.add('FilterSelectValue', (dataCyName, lableValue) => {
    cy.get(dataCyName).click()
    cy.get(dataCyName).within(() => {
        cy.get('input').clear().type(lableValue).should('have.value',lableValue)
    })
    cy.get('.el-scrollbar').filter(':visible').get('li[class=el-select-dropdown__item]').filter(':visible').contains(lableValue).click({force: true})
})

Cypress.Commands.add('SelectInputValue', (dataCyName, lableValue) => {
cy.get(dataCyName+' input:visible').invoke('val').then(text=>{
    if (text == lableValue){

    }else{
      cy.ClickSelectValue2(dataCyName, lableValue)
    }
  })
})

Cypress.Commands.add('ClickMultiDropDownValue', (lableName, lableValueList) => {
    cy.get(lableName).click()
    cy.get('li[class="el-select-dropdown__item"]').filter(':visible').within(() => {
        lableValueList.forEach(lableValue => {
            cy.contains(lableValue).filter(':visible').click({force: true})
        })
    })
})

Cypress.Commands.add('ClickMultiDropDownValueUnVisiable', (lableName, lableValueList) => {
    cy.get(lableName).click()
    cy.get('li[class="el-select-dropdown__item"]').within(() => {
        lableValueList.forEach(lableValue => {
            cy.contains(lableValue).click({force: true})
        })
    })
})

Cypress.Commands.add('TypeAndSearch', (datacy, searchValue) => {
    cy.get(datacy).clear().type(searchValue)
    cy.get(datacy).parent('div').find('button').click()
})

Cypress.Commands.add('setNumInTablePage', (number) => {
    cy.get('[class="pagination-container"]').find('[class="el-select el-select--mini"]').click()
    cy.get('.el-scrollbar').filter(':visible').within(() =>{
        cy.get('li[class^="el-select-dropdown__item"]').contains(number).should('be.visible').click({force: true})
    })
})

Cypress.Commands.add('typeMultiDropDownValue', (lableName, filter,dropDownDataCy,lableValueList) => {
    cy.get(lableName).clear().type(filter)
    cy.get(dropDownDataCy).filter(':visible').within(() => {
        lableValueList.forEach(lableValue => {
            cy.contains(lableValue).filter(':visible').click({force: true})
        })
    })
})

Cypress.Commands.add('getAttributes', { prevSubject: true,}, (subject, attr) => {
    const attrList = [];
    cy.wrap(subject).each($el => {
      cy.wrap($el)
        .invoke('attr', attr)
        .then(lid => {
          attrList.push(lid);
        });
    });
    return cy.wrap(attrList);
  }
)

