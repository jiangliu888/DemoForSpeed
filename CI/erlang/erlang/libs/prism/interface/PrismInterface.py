from erlang.libs.common import JsonUtil
from erlang.libs.common.PrismRequest import PrismRequest


class PrismInterface(object):
    ALERTS_PATH = 'api/v1/mgr/alerts'
    ALERT_GROUP_PATH = '/api/v1/mgr/groups'
    ALERT_RULES_PATH = '/api/v1/mgr/rules'
    OPERATE_PARH = '/api/v1/mgr/tasks'
    SERVICE_PATH = '/api/v1/mgr/services'
    VERSION_PATH = '/api/v1/mgr/versions'
    RELEASES_PATH = '/api/v1/mgr/releases'
    POLICIES_PATH = '/api/v1/mgr/policies'
    JOBs_PATH = '/api/v1/mgr/jobs'

    @classmethod
    def get_alert(cls, companyId, status, limit):
        res = PrismRequest.get(cls.ALERTS_PATH + "?company={},status={},limit={}".format(companyId, status, limit))
        return JsonUtil.load_json(res.content)

    @classmethod
    def get_dedicate_alert(cls, company_id, deviceId, neId, status, alarmName, limit):
        res = PrismRequest.get(cls.ALERTS_PATH + "/detail?labels.companyId={}&labels.deviceId={}&labels.neId={}&status={}&labels.alertname={}&limit={}".format(company_id, deviceId, neId, status, alarmName, limit))
        return JsonUtil.load_json(res.content)

    @classmethod
    def post_alertGroup(cls, data):
        res = PrismRequest.post(cls.ALERT_GROUP_PATH, JsonUtil.dump_json(data))
        return res.status_code, JsonUtil.load_json(res.content)['id']

    @classmethod
    def post_alertGroup_by_id(cls, grpId, data):
        res = PrismRequest.post(cls.ALERT_GROUP_PATH + "/{}".format(grpId), JsonUtil.dump_json(data))
        return res

    @classmethod
    def get_alertGroup(cls, grpId):
        res = PrismRequest.get(cls.ALERT_GROUP_PATH + "?id={}".format(grpId)).content
        return res

    @classmethod
    def del_alertGroup(cls, grpId):
        res = PrismRequest.delete(cls.ALERT_GROUP_PATH + "/{}".format(grpId))
        return res

    @classmethod
    def post_alertRule(cls, data):
        res = PrismRequest.post(cls.ALERT_GROUP_PATH, JsonUtil.dump_json(data))
        return res.status_code, JsonUtil.load_json(res.content)['id']

    @classmethod
    def put_alertRule_by_ruleId(cls, ruleId, data):
        res = PrismRequest.put(cls.ALERT_RULES_PATH + "/{}".format(ruleId), JsonUtil.dump_json(data))
        return res

    @classmethod
    def del_alertRule(cls, ruleId):
        res = PrismRequest.delete(cls.ALERT_RULES_PATH + "/{}".format(ruleId))
        return res

    @classmethod
    def get_alertRule(cls, ruleId, companyId):
        res = PrismRequest.get(cls.ALERT_RULES_PATH + "?id={}&company={}".format(ruleId, companyId))
        return res

    @classmethod
    def get_operate_task(cls, taskId):
        res = PrismRequest.get(cls.OPERATE_PARH + "/{}".format(taskId))
        return res

    # post, get, put, del service
    @classmethod
    def post_services(cls, data):
        res = PrismRequest.post(cls.SERVICE_PATH, JsonUtil.dump_json(data))
        return res.status_code, JsonUtil.load_json(res.content)['id']

    @classmethod
    def get_services(cls, service_Id):
        res = PrismRequest.get(cls.SERVICE_PATH + "/{}".format(service_Id))
        return res.status_code, JsonUtil.load_json(res.content)

    @classmethod
    def put_services(cls, service_Id, data):
        res = PrismRequest.put(cls.SERVICE_PATH + "/{}".format(service_Id), JsonUtil.dump_json(data))
        return res

    @classmethod
    def del_services(cls, service_Id):
        res = PrismRequest.delete(cls.SERVICE_PATH + "/{}".format(service_Id))
        return res

    #  post, get, put, del version
    @classmethod
    def post_versions(cls, data):
        res = PrismRequest.post(cls.VERSION_PATH, JsonUtil.dump_json(data))
        return res.status_code, JsonUtil.load_json(res.content)['id']

    @classmethod
    def get_versions(cls, version_Id):
        res = PrismRequest.get(cls.VERSION_PATH + "/{}".format(version_Id))
        return res.status_code, JsonUtil.load_json(res.content)

    @classmethod
    def get_versions_by_filter(cls, service_Ids=None, version=None):
        get_path = cls.VERSION_PATH + "?" if (service_Ids or version) else cls.VERSION_PATH
        if service_Ids:
            get_path += "&service={}".format(','.join(service_Ids))
        if version:
            get_path += "&version={}".format(version)
        res = PrismRequest.get(get_path)
        return res.status_code, JsonUtil.load_json(res.content)

    @classmethod
    def put_versions(cls, version_Id, data):
        res = PrismRequest.put(cls.VERSION_PATH + "/{}".format(version_Id), JsonUtil.dump_json(data))
        return res

    @classmethod
    def del_versions(cls, version_Id):
        res = PrismRequest.delete(cls.VERSION_PATH + "/{}".format(version_Id))
        return res

    #  post, get, put, del release
    @classmethod
    def post_releases(cls, data):
        res = PrismRequest.post(cls.RELEASES_PATH, JsonUtil.dump_json(data))
        return res.status_code, JsonUtil.load_json(res.content)['id']

    @classmethod
    def get_releases(cls, release_Id):
        res = PrismRequest.get(cls.RELEASES_PATH + "/{}".format(release_Id))
        return res.status_code, JsonUtil.load_json(res.content)

    @classmethod
    def get_releases_by_filter(cls, name=None, before=None, after=None):
        get_path = cls.RELEASES_PATH + "?" if (name or before or after) else cls.RELEASES_PATH
        if name:
            get_path += "&name={}".format(name)
        if before:
            get_path += "&before={}".format(before)
        if after:
            get_path += "&after={}".format(after)
        res = PrismRequest.get(get_path)
        return res.status_code, JsonUtil.load_json(res.content)

    @classmethod
    def put_releases(cls, release_Id, data):
        res = PrismRequest.put(cls.RELEASES_PATH + "/{}".format(release_Id), JsonUtil.dump_json(data))
        return res

    @classmethod
    def del_releases(cls, release_Id):
        res = PrismRequest.delete(cls.RELEASES_PATH + "/{}".format(release_Id))
        return res

    #  post, get, put, del policy
    @classmethod
    def post_policies(cls, data):
        res = PrismRequest.post(cls.POLICIES_PATH, JsonUtil.dump_json(data))
        return res.status_code, JsonUtil.load_json(res.content)['id']

    @classmethod
    def get_policies(cls, policy_Id):
        res = PrismRequest.get(cls.POLICIES_PATH + "/{}".format(policy_Id))
        return res.status_code, JsonUtil.load_json(res.content)

    @classmethod
    def put_policies(cls, policy_Id, data):
        res = PrismRequest.put(cls.POLICIES_PATH + "/{}".format(policy_Id), JsonUtil.dump_json(data))
        return res

    @classmethod
    def del_policies(cls, policy_Id):
        res = PrismRequest.delete(cls.POLICIES_PATH + "/{}".format(policy_Id))
        return res

    # get, put job
    @classmethod
    def get_job(cls, job_Id):
        res = PrismRequest.get(cls.JOBs_PATH + "/{}".format(job_Id))
        return res.status_code, JsonUtil.load_json(res.content)

    @classmethod
    def put_job(cls, job_Id, data):
        res = PrismRequest.put(cls.JOBs_PATH + "/{}".format(job_Id), JsonUtil.dump_json(data))
        return res

    @classmethod
    def get_jobs_by_common_filter(cls, state=None, companyIds=None, siteIds=None, neIds=None):
        get_path = cls.JOBs_PATH + "?limit=0&skip=0"
        if state:
            get_path += "&state={}".format(state)
        if companyIds:
            get_path += "&company={}".format(','.join(companyIds))
        if siteIds:
            get_path += "&site={}".format(','.join(siteIds))
        if neIds:
            get_path += "&ne={}".format(','.join(neIds))
        res = PrismRequest.get(get_path)
        return res.status_code, JsonUtil.load_json(res.content)

    @classmethod
    def get_jobs_by_upgrade_filter(cls, release=None, service=None, targetVer=None):
        get_path = cls.JOBs_PATH + "?action=upgrade"
        if release:
            get_path += "&release={}".format(release)
        if service:
            get_path += "&service={}".format(service)
        if targetVer:
            get_path += "&targetVer={}".format(targetVer)
        res = PrismRequest.get(get_path)
        return res.status_code, JsonUtil.load_json(res.content)
