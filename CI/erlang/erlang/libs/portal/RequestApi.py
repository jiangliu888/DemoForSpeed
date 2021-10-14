import requests
import json
from erlang.libs.variables import PortalVariables


class RequestApi:
    def __init__(self):
        pass

    @staticmethod
    def authorize(user, psd):
        payload = {"username": user, "password": psd}
        res = requests.post(url=PortalVariables.url + PortalVariables.auth, json=payload)
        if res.status_code == 201:
            return res.status_code, json.loads(res.text)
        else:
            return res.status_code, res

    def create_company(self, name, channel=None):
        sc, res = self.authorize(PortalVariables.portal_user, PortalVariables.portal_psd)
        header = {'authorization': 'Bearer ' + res['token']}
        payload = PortalVariables.Company_body2
        payload['name'] = name
        if channel:
            payload['channel'] = channel
        res = requests.post(url=PortalVariables.url + PortalVariables.companyUrl, data=payload, headers=header)
        if res.status_code != 200:
            raise Exception('Create company failed! ' + 'status code: ' + '{}'.format(res.status_code))

    def delete_company(self, name):
        sc, res = self.authorize(PortalVariables.portal_user, PortalVariables.portal_psd)
        header = {'authorization': 'Bearer ' + res['token']}
        res = requests.get(url=PortalVariables.url + PortalVariables.companyUrl, headers=header)
        assert res.status_code == 200
        res = json.loads(res.text)
        cid = ''
        for i in res['results']:
            if i['name'] == name:
                cid = i['companyId']
                break
        if not cid:
            raise Exception('Can not find target, pls check the company name!')
        res = requests.delete(url=PortalVariables.url + PortalVariables.companyUrl + '/' + cid,
                              headers=header)
        if res.status_code != 204:
            raise Exception('Delete company failed! ' + 'status code: ' + '{}'.format(res.status_code))

    def create_account(self, account_name, pswd, company='', admin='true', active='true', channel=''):
        # _id, _scp = self.get_role_info('all')
        data = PortalVariables.Account_body
        data['username'] = account_name
        data['password'] = pswd
        data['company'] = company
        data['admin'] = admin
        data['enabled'] = active
        data['channel'] = channel
        # data['rolesId'] = _id
        # data['scope'] = _scp
        sc, res = self.authorize(PortalVariables.portal_user, PortalVariables.portal_psd)
        header = {'authorization': 'Bearer ' + res['token']}
        res = requests.post(url=PortalVariables.url + PortalVariables.userUrl, data=data, headers=header)
        assert res.status_code == 201, 'Create account failed! ' + 'status code:{}'.format(res.status_code)

    def delete_account(self, account_name):
        sc, res = self.authorize(PortalVariables.portal_user, PortalVariables.portal_psd)
        header = {'authorization': 'Bearer ' + res['token']}
        res = requests.delete(url=PortalVariables.url + PortalVariables.userUrl + '/' + account_name,
                              headers=header)
        assert res.status_code == 204, 'Delete account failed! ' + 'status code:{}'.format(res.status_code)

    def create_site(self, name, company_id, sn):
        data = PortalVariables.Site_body
        data['name'] = name
        data['companyId'] = company_id
        data['config']['sn'] = [sn]
        sc, res = self.authorize(PortalVariables.portal_user, PortalVariables.portal_psd)
        header = {'authorization': 'Bearer ' + res['token']}
        res = requests.post(url=PortalVariables.url + PortalVariables.companyUrl + '/' + company_id + '/sites',
                            json=data, headers=header)
        assert res.status_code == 200, 'Create site failed! ' + 'status code:{}'.format(res.status_code)

    def get_company_id(self, name):
        sc, res = self.authorize(PortalVariables.portal_user, PortalVariables.portal_psd)
        header = {'authorization': 'Bearer ' + res['token']}
        res = requests.get(url=PortalVariables.url + PortalVariables.companyUrl, headers=header)
        assert res.status_code == 200, 'Get company info failed!' + 'status code:{}'.format(res.status_code)
        res = json.loads(res.text)
        for i in res['results']:
            if i['name'] == name:
                return i['companyId']
        raise Exception('There is no company with the name input!')

    def get_site_info(self, account_name, account_psd, params=None):
        sc, res = self.authorize(account_name, account_psd)
        assert sc == 201, 'Get token failed!' + ' status code:{}'.format(sc)
        token_ = res['token']
        header = {'authorization': 'Bearer ' + token_}
        if params:
            res = requests.get(url=PortalVariables.url + PortalVariables.siteUrl + '?' + params, headers=header)
        else:
            res = requests.get(url=PortalVariables.url + PortalVariables.siteUrl, headers=header)
        if res.status_code == 200:
            return res.status_code, json.loads(res.text)
        else:
            return res.status_code, res

    def delete_site(self, company_name):
        c_id = self.get_company_id(company_name)
        sc, res = self.authorize(PortalVariables.portal_user, PortalVariables.portal_psd)
        header = {'authorization': 'Bearer ' + res['token']}
        res = requests.get(url=PortalVariables.url + PortalVariables.companyUrl + '/' + c_id + '/sites',
                           headers=header)
        res = json.loads(res.text)
        for i in res['results']:
            st_id = i['siteId']
            res = requests.delete(url=PortalVariables.url + PortalVariables.companyUrl + '/' + c_id + '/sites/' + st_id,
                                  headers=header)
            assert res.status_code == 204, 'Delete sites failed!' + 'status code:{}'.format(res.status_code)

    def create_alert_body(self, company_name, device_id, ne_id, name, status):
        company_id = self.get_company_id(company_name)
        PortalVariables.alarm_body["labels"]["companyName"] = company_name
        new_id = int(PortalVariables.alarm_body['alertId'], 16) + 1
        PortalVariables.alarm_body["alertId"] = hex(new_id).strip('0x')
        PortalVariables.alarm_body["labels"]["companyId"] = company_id
        PortalVariables.alarm_body["labels"]["deviceId"] = device_id
        PortalVariables.alarm_body["labels"]["neId"] = ne_id
        PortalVariables.alarm_body["labels"]["alertname"] = name
        if status == 'resolved':
            PortalVariables.alarm_body["startsAt"] = "2021-04-24T12:45:22.07127243+08:00"
            PortalVariables.alarm_body["status"] = status
        else:
            PortalVariables.alarm_body["startsAt"] = "2021-04-24T12:39:50.270397731+08:00"
            PortalVariables.alarm_body["status"] = status
        body = str(PortalVariables.alarm_body).replace('\'', '"')
        return body

    def get_alert_info(self, account_name, account_psd, params=None):
        sc, res = self.authorize(account_name, account_psd)
        assert sc == 201, 'Get token failed!' + ' status code:{}'.format(sc)
        token_ = res['token']
        header = {'authorization': 'Bearer ' + token_}
        if params:
            res = requests.get(url=PortalVariables.url + PortalVariables.alarmUrl + '?' + params, headers=header)
        else:
            res = requests.get(url=PortalVariables.url + PortalVariables.alarmUrl, headers=header)
        if res.status_code == 200:
            return res.status_code, json.loads(res.text)
        else:
            return res.status_code, res

    @staticmethod
    def alert_field_check(alerts_res, key, expect):
        expect = expect.split(',')
        if alerts_res['alerts'][0].get(key):
            for i in alerts_res['alerts']:
                assert i[key] in expect, '{}:{}'.format(key, i[key]) + 'is not in expect {}'.format(expect)
        else:
            for i in alerts_res['alerts']:
                assert i['labels'][key] in expect, '{}:{}'.format(key, i['labels'][key]) + \
                                                   'not in expect {}'.format(expect)

    def get_bandwidth_info(self, account_name, account_psd, params=None):
        sc, res = self.authorize(account_name, account_psd)
        assert sc == 201, 'Get token failed!' + ' status code:{}'.format(sc)
        token_ = res['token']
        header = {'authorization': 'Bearer ' + token_}
        if params:
            res = requests.get(url=PortalVariables.url + PortalVariables.bwUrl + '?' + params, headers=header)
        else:
            res = requests.get(url=PortalVariables.url + PortalVariables.bwUrl, headers=header)
        if res.status_code == 200:
            return res.status_code, json.loads(res.text)
        else:
            return res.status_code, res

    def get_device_system_info(self, account_name, account_psd, params=None):
        sc, res = self.authorize(account_name, account_psd)
        assert sc == 201, 'Get token failed!' + ' status code:{}'.format(sc)
        token_ = res['token']
        header = {'authorization': 'Bearer ' + token_}
        if params:
            res = requests.get(url=PortalVariables.url + PortalVariables.deviceSysUrl + '?' + params, headers=header)
        else:
            res = requests.get(url=PortalVariables.url + PortalVariables.deviceSysUrl, headers=header)
        if res.status_code == 200:
            return res.status_code, json.loads(res.text)
        else:
            return res.status_code, res

    def get_network_info(self, account_name, account_psd, params=None):
        sc, res = self.authorize(account_name, account_psd)
        assert sc == 201, 'Get token failed!' + ' status code:{}'.format(sc)
        token_ = res['token']
        header = {'authorization': 'Bearer ' + token_}
        if params:
            res = requests.get(url=PortalVariables.url + PortalVariables.networkUrl + '?' + params, headers=header)
        else:
            res = requests.get(url=PortalVariables.url + PortalVariables.networkUrl, headers=header)
        if res.status_code == 200:
            return res.status_code, json.loads(res.text)
        else:
            return res.status_code, res

    def create_role(self, company_name):
        company_id = self.get_company_id(company_name)
        data = PortalVariables.role_body
        data["companyId"] = company_id
        sc, res = self.authorize(PortalVariables.portal_user, PortalVariables.portal_psd)
        token_ = res['token']
        header = {'authorization': 'Bearer ' + token_}
        res = requests.post(url=PortalVariables.url + PortalVariables.roleUrl,
                            json=data, headers=header)
        assert res.status_code == 200, 'Create role failed! ' + 'status code:{}'.format(res.status_code)

    def get_role_info(self, company_name):
        company_id = self.get_company_id(company_name)
        sc, res = self.authorize(PortalVariables.portal_user, PortalVariables.portal_psd)
        token_ = res['token']
        header = {'authorization': 'Bearer ' + token_}
        res = requests.get(url=PortalVariables.url + PortalVariables.roleUrl + '?companyId=' + company_id,
                           headers=header)
        res = json.loads(res.text)
        print(res)
        return res["results"][0]["roleId"], res["results"][0]["scopes"]

    def delete_role(self, company_name):
        _id, _scp = self.get_role_info(company_name)
        sc, res = self.authorize(PortalVariables.portal_user, PortalVariables.portal_psd)
        token_ = res['token']
        header = {'authorization': 'Bearer ' + token_}
        res = requests.delete(url=PortalVariables.url + PortalVariables.roleUrl + '/' + _id,
                              headers=header)
        assert res.status_code == 204, 'Create role failed! ' + 'status code:{}'.format(res.status_code)


if __name__ == '__main__':
    pass
