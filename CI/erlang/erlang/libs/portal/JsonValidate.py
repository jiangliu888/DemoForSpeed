from jsonschema import validate
from jsonschema import ValidationError
from erlang.libs.variables import json_schema


schema_repo = {"alert info": json_schema.alert_schema, "site info": json_schema.sites_schema,
               "auth info": json_schema.auth_schema, "bandwidth info": json_schema.bandwidth_schema,
               "device system info": json_schema.device_system_schema, "network info": json_schema.network_schema
               }


class JsonValidate:
    @staticmethod
    def check_response_format(res, info_type):
        try:
            validate(res, schema_repo[info_type])
        except ValidationError as e:
            raise Exception(e.message)
