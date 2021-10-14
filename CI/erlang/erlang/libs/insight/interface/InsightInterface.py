from erlang.libs.common import JsonUtil
from erlang.libs.common.InsightRequest import InsightRequest
from erlang.libs.variables import InterfacePathVariables


class InsightInterface(object):

    Login_PATH = "/api/v1/tokens"
    Ne_PATH = '/api/v1/ne'
    Alarm_PARH = '/api/v1/mgr/alerts'

    @classmethod
    def login(cls, username, password):
        data = {"username": username, "password": password}
        InterfacePathVariables.INSIGHT_HEADERS = {"Content-Type": "application/json;charset=UTF-8"}
        rcv = InsightRequest.post(cls.Login_PATH, JsonUtil.dump_json(data))
        rsp = JsonUtil.load_json(rcv.content)
        InsightRequest.token = rsp['token']
        InterfacePathVariables.INSIGHT_HEADERS = {"Content-Type": "application/json;charset=UTF-8",
                                                  'Authorization': 'Bearer ' + InsightRequest.token}
        return rcv.status_code

    @classmethod
    def put_pop_routecode(cls, dev_id, body):
        rcv = InsightRequest.put(cls.Ne_PATH + '/' + str(dev_id) + '/routeCode', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_pop_status(cls, dev_id, body):
        rcv = InsightRequest.put(cls.Ne_PATH + '/' + str(dev_id) + '/status', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def put_pop_saasServices(cls, dev_id, body):
        rcv = InsightRequest.put(cls.Ne_PATH + '/' + str(dev_id) + '/service/saas', JsonUtil.dump_json(body))
        return rcv.status_code

    @classmethod
    def delete_ne(cls, dev_id):
        rcv = InsightRequest.delete(cls.Ne_PATH + '/' + str(dev_id))
        return rcv.status_code

    @classmethod
    def get_alarm(cls, companyId, status):
        rcv = InsightRequest.get('{}?companyId={}&status={}'.format(cls.Alarm_PARH, companyId, status))
        return rcv.status_code, JsonUtil.load_json(rcv.content) if rcv.status_code != 404 else []
