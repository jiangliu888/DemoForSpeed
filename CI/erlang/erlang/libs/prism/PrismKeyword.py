import time
from datetime import datetime
from datetime import timedelta
from erlang.libs.prism.interface.PrismInterface import PrismInterface
from erlang.libs.variables import PrismVariables


class PrismKeyword(object):
    def __init__(self):
        pass

    @staticmethod
    def get_cpe_last_dedicate_alarm(company_id, deviceId, neId, status, alarmName, beginTime):
        ret = PrismInterface.get_dedicate_alert(company_id, deviceId, neId, status, alarmName, 1)
        print ret
        alarm_b_utc_time = datetime.strptime(ret["alerts"][0]["startsAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
        alarm_b_time = (alarm_b_utc_time + timedelta(hours=8)).strftime('%s')
        print alarm_b_time
        return ret["alerts"] if int(alarm_b_time) > int(beginTime) else []

    @staticmethod
    def create_service_by_os_and_arch(name, osType_l, arch_l):
        platform = {}
        assert len(osType_l) == len(arch_l), 'os lenth should eq arch lenth'
        for i in len(osType_l):
            platform[osType_l[i]] = arch_l[i]
        body = {"name": name,
                "platform": platform}
        res_code, serviceId = PrismInterface.post_services(body)
        assert res_code == 201, '{} is not 201'.format(res_code)
        return serviceId

    @staticmethod
    def create_service(data):
        res_code, serviceId = PrismInterface.post_services(data)
        assert res_code == 201, '{} is not 201'.format(res_code)
        return serviceId

    @staticmethod
    def create_version(service, version, path, depeendency_ser_l=None, depeendency_ver_l=None):
        body = {
            "service": service,
            "version": version,
            "path": path
        }

        def gen_dep(ser, ver):
            return {"service": ser, "version": ver}

        if depeendency_ser_l:
            assert len(depeendency_ser_l) == len(depeendency_ver_l), 'dependency is not right'
            dep = map(lambda s, v: gen_dep(s, v), depeendency_ser_l, depeendency_ver_l)
            body["dependency"] = dep

        res_code, versionId = PrismInterface.post_versions(body)
        assert res_code == 201, '{} is not 201'.format(res_code)
        return versionId

    @staticmethod
    def create_release(name, versionId_l, time, rollback=True, restore=False, appointed_scope=None, appointed_Ids=None):
        body = {
            "time": time,
            "name": name,
            "versionId": versionId_l,
            "rollback": rollback,
            "restore": restore
        }
        if appointed_scope:
            body["appointed"] = {
                "scope": appointed_scope,
                "id": appointed_Ids
            }

        res_code, releaseId = PrismInterface.post_releases(body)
        assert res_code == 201, '{} is not 201'.format(res_code)
        return releaseId

    @staticmethod
    def create_policy(name, day_l, hour_l, company_l, site_l):
        body = {
            "name": name,
            "company": company_l,
            "site": site_l,
            "localTime": {
                "dayOfWeek": day_l,
                "hourOfDay": hour_l
            }
        }

        res_code, policyId = PrismInterface.post_policies(body)
        assert res_code == 201, '{} is not 201'.format(res_code)
        return policyId

    @staticmethod
    def create_full_cpe_service():
        seviceId_l = []
        for value in PrismVariables.full_cpe_service_body_list:
            seviceId_l.append(PrismKeyword.create_service(value))
        return seviceId_l

    @staticmethod
    def delete_full_cpe_service():
        serviceName_list = map(lambda x: x["name"], PrismVariables.full_cpe_service_body_list)
        for ser in serviceName_list:
            res = PrismInterface.del_services(ser)
            assert res.status_code == 200, '{} is not 201'.format(res.status_code)

    @staticmethod
    def create_full_cpe_version(version):
        versionId_list = []
        for k, v in PrismVariables.full_cpe_service_name_and_dep_list:
            if v["dependency"]:
                dep_v_l = [version for i in range(len(v["dependency"]))]
                versionId_list.append(PrismKeyword.create_version(k, version, v["path"], dep_v_l))
            else:
                versionId_list.append(PrismKeyword.create_version(k, version, v["path"]))
        return versionId_list

    @staticmethod
    def create_full_cpe_release(time, release_name, version):
        PrismKeyword.create_full_cpe_service()
        versionId_l = PrismKeyword.create_full_cpe_version(version)
        releaseId = PrismKeyword.create_release(release_name, versionId_l, time)
        return releaseId

    @staticmethod
    def create_release_patch(release_name, patch_release_name, time, appoint_scope, scopeId_l, version, ser_name_l, path_l, depeendency_ser_l_l=None, depeendency_ver_l_l=None):
        assert len(ser_name_l) == len(path_l), 'service and service path is not right'
        res_code, body = PrismInterface.get_releases_by_filter(release_name)
        assert res_code == 200, '{} is not 200'.format(res_code)
        versionId_l_keep = filter(lambda x: PrismInterface.get_versions(x)[1]["service"] not in ser_name_l, body["versionId"])
        versionId_l_new = []
        if depeendency_ser_l_l:
            assert all(len(depeendency_ver_l_l) == len(depeendency_ver_l_l), len(ser_name_l) == len(depeendency_ser_l_l)), 'dependency is not right'
            versionId_l_new = map(lambda s, p, ds, dv: PrismKeyword.create_version(s, version, p, ds, dv), ser_name_l, path_l, depeendency_ser_l_l, depeendency_ver_l_l)
        else:
            versionId_l_new = map(lambda s, p: PrismKeyword.create_version(s, version, p), ser_name_l, path_l)
        patch_release_Id = PrismKeyword.create_release(patch_release_name, versionId_l_keep + versionId_l_new, time, appoint_scope, scopeId_l)
        return patch_release_Id
