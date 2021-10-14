# -*- coding: UTF-8 -*-
import body_check
from erlang.libs.authAudit.AuthKeyword import AuthKeyword
from erlang.libs.common.JsonUtil import are_same
from CheckConsul import call_funcion


def check_raduis():
    expectBody = body_check.raduisBody
    body = AuthKeyword.get_raduis()
    print "Auth portal is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, []) == True


def check_ldap():
    expectBody = body_check.ldapBody
    body = AuthKeyword.get_ldap()
    print "Auth portal is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, []) == True


def check_timeout():
    expectBody = body_check.timeoutBody
    body = AuthKeyword.get_timeout()
    print "Auth portal is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, []) == True

def check_navUrl():
    expectBody = body_check.navUrlBody
    body = AuthKeyword.get_navUrl()
    print "Auth portal is {}\nand expect is {}".format(body, expectBody)
    assert are_same(expectBody, body, []) == True

def check_black_white_list(argList):
    black_list = argList[0]
    nameType = argList[1]
    content = argList[2]
    expectNum = argList[3]
    nameTypeList = {'domain': 1,'ip': 2,'mac': 3}
    body = AuthKeyword.get_black_white_list(black_list, nameTypeList[nameType], content) 
    assert int(expectNum) == body['totalcount']

if __name__ == "__main__":
    match = \
        {
            'raduis': check_raduis,
            'ldap': check_ldap,
            'timeout': check_timeout,
            'navUrl': check_navUrl,
            'blackWhiteList': check_black_white_list
        }
    call_funcion(match)

