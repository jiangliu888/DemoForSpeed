from erlang.libs.insight.interface.InsightInterface import InsightInterface
from erlang.libs.variables import InterfacePathVariables


class InsightKeyword(object):
    def __init__(self):
        pass

    @staticmethod
    def portal_login(username=InterfacePathVariables.INSIGHT_USER, password=InterfacePathVariables.INSIGHT_PASSWORD):
        res_code = InsightInterface.login(username, password)
        assert res_code == 201, '{} is not 201'.format(res_code)

    @staticmethod
    def portal_put_pop_cac_eac(dev_id, cac, eac, ne_type):
        body = {"type": ne_type,
                "cac": int(cac),
                "eac": int(eac)}
        res_code = InsightInterface.put_pop_routecode(dev_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def portal_put_er_cac_eac(device_id_list, cac_list, eac_list):
        assert len(device_id_list) == len(eac_list)
        map(lambda x, y, z: InsightKeyword.portal_put_pop_cac_eac(x, y, z, "ER"), device_id_list, cac_list, eac_list)

    @staticmethod
    def portal_put_pop_status(dev_id, status):
        body = {"status": status}
        res_code = InsightInterface.put_pop_status(dev_id, body)
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def portal_put_pop_saasServices(dev_id, end_point, phy_port):
        body = \
            {
                "serviceId": int(end_point),
                "iface": phy_port
            }
        res_code = InsightInterface.put_pop_saasServices(str(dev_id), [body])
        assert res_code == 200, '{} is not 200'.format(res_code)

    @staticmethod
    def portal_delete_ne(dev_id):
        res_code = InsightInterface.delete_ne(dev_id)
        assert res_code == 204, '{} is not 204'.format(res_code)

    @staticmethod
    def portal_get_alarm(companyId, status):
        _, res_content = InsightInterface.get_alarm(companyId, status)
        return res_content['alerts']

    @staticmethod
    def get_alarm_by_code_and_deviceOrNeId(companyId, status, code, alertName, severity, siteName, deviceId, neId):
        alerts = InsightKeyword.portal_get_alarm(companyId, status)
        return filter(lambda x: (int(x['code']) == int(code) if "code" in x else 1) and (x['labels']['deviceId'] == deviceId if "deviceId" in x['labels'] else x['labels']['neId'] == neId) and x['labels']['alertname'] == alertName and x['labels']['severity'] == severity and x['labels']['siteName'] == siteName and x['labels']['neId'] == neId, alerts)
