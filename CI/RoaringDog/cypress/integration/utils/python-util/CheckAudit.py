# -*- coding: UTF-8 -*-
from datetime import datetime, timedelta
import body_check
from erlang.libs.authAudit.AuditKeyword import AuditKeyword
from erlang.libs.common.JsonUtil import are_same
from CheckConsul import call_funcion

def get_service_code(createData):
    nine_hours_from_service = datetime.strptime(createData.split('.')[0],"%Y-%m-%dT%H:%M:%S") + timedelta(hours=8)
    serviceCode =  nine_hours_from_service.strftime("%Y%m%d%H%M%S")
    return serviceCode


def get_corp(companyName, createData):
    serviceCode = get_service_code(createData)
    print u'{}{}'.format(companyName,serviceCode)
    body = AuditKeyword.get_corp(companyName, serviceCode)
    return body


def get_corp_ap(createData):
    serviceCode = get_service_code(createData)
    body = AuditKeyword.get_corp_ap(serviceCode)
    return body


def check_corp(argList):
    companyName = argList[0]
    createData = argList[1]
    body = get_corp(companyName, createData)
    expectBody = body_check.corpBody[companyName]
    print "company audit is {}\nand expect is {}".format(body, expectBody)
    assert expectBody['totalcount'] == body['totalcount']


def check_corp_ap(argList):
    createData = argList[0]
    siteName = argList[1]
    apMac = argList[2]
    checkIn = argList[3]
    body = get_corp_ap(createData)
    expectBody = body_check.corpAPBody
    expectBody["apid"] = unicode(apMac.replace(':',''), "utf-8")
    expectBody["devmac"] = unicode(apMac, "utf-8")
    expectBody['apname'] = unicode(siteName, "utf-8")
    eimData = [x for x in body["eimdata"] if x['devmac'] == unicode(apMac, "utf-8")]
    if checkIn == 'True':
        print "company audit is {}\nand expect is {}".format(eimData[0], expectBody)
        assert are_same(expectBody, eimData[0], ["root['address']"]) == True
    else:
        assert len(eimData) == 0


def delete_corps(argList):
    corps = argList
    print corps
    ret = [AuditKeyword.delete_corp(x) for x in corps]
    print ret

if __name__ == "__main__":
    match = \
        {
            'check_corp': check_corp,
            'delete_corps': delete_corps,
            'check_ap': check_corp_ap
        }
    call_funcion(match)