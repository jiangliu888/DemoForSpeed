auth_schema = \
    {
        "type": "object",
        "properties":
            {
                "token": {"type": "string"},
                "expiresIn": {"type": "integer"},
                "companyList":
                    {
                        "type": "array",
                        "items":
                            {
                                "type": "object",
                                "properties":
                                    {
                                        "name": {"type": "string"},
                                        "companyId": {"type": "string"}
                                    },
                                "required": ["name", "companyId"],
                                "additionalProperties": False
                            }
                    }
            },
        "required": ["token", "expiresIn", "companyList"],
        "additionalProperties": False

    }

sites_schema = \
    {
        "type": "object",
        "properties": {
            "devices": {
                "description": "all devices",
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required":
                        ["sn", "siteName", "siteId", "neId", "companyId", "status",
                         "haStatus", "model", "interfaceInfo"],
                    "properties": {
                        "sn": {"type": "string"},
                        "siteName": {"type": "string"},
                        "siteId": {"type": "string"},
                        "neId": {"type": "string"},
                        "companyId": {"type": "string"},
                        "status": {"type": "string"},
                        "haStatus": {"type": "string"},
                        "model": {"type": "string"},
                        "interfaceInfo":
                            {
                                "type": "array",
                                "items":
                                    {
                                        "type": "object",
                                        "required": [
                                            "logicName", "physicalName"
                                        ],
                                        "properties": {
                                            "logicName": {"type": "string"},
                                            "physicalName": {"type": "array"}
                                        },
                                        "additionalProperties": False
                                    }
                            }
                            }
                }
            },
            "total": {
                "description": "total number",
                "type": "integer"
            }
        },
        "required": ["devices", "total"],
        "additionalProperties": False
    }

alert_schema = \
    {
        "type": "object",
        "properties": {
            "alerts": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["status", "labels", "annotations", "startsAt", "endsAt"],
                    "properties": {
                        "status": {"type": "string"},
                        "labels": {
                            "type": "object",
                            "required": ["alertname", "alertCode", "deviceId", "neId", "companyId",
                                         "companyName", "siteName", "severity"],
                            "properties": {
                                "alertname": {"type": "string"},
                                "alertCode": {"type": "string"},
                                "deviceId": {"type": "string"},
                                "neId": {"type": "string"},
                                "companyId": {"type": "string"},
                                "companyName": {"type": "string"},
                                "siteName": {"type": "string"},
                                "severity": {"type": "string"}
                            },
                            "additionalProperties": False
                        },
                        "annotations": {
                            "type": "object",
                            "required": ["description"],
                            "properties": {
                                "description": {"type": "string"}
                            },
                            "additionalProperties": False
                        },
                        "startsAt": {"type": "string"},
                        "endsAt": {"type": "string"}
                    }
                }
            },
            "total": {"type": "integer"},
        },
        "required": ["alerts", "total"],
        "additionalProperties": False
    }

bandwidth_schema = \
    {
        "type": "object",
        "required": ["metric", "data"],
        "properties":
            {
                "metric": {"type": "string", "pattern": "^BANDWIDTH$"},
                "data": {
                    "type": "array",
                    "items":
                        {
                            "type": "object",
                            "required": ["deviceId", "interfaceType", "instance", "values"],
                            "additionalProperties": False,
                            "properties":
                                {
                                    "deviceId": {"type": "string"},
                                    "interfaceType": {"type": "string"},
                                    "instance": {"type": "string"},
                                    "values":
                                        {
                                            "type": "array",
                                            "items":
                                                {
                                                    "type": "object",
                                                    "required": ["timestamp", "number1", "number2"],
                                                    "properties":
                                                        {
                                                            "timestamp": {"type": "number"},
                                                            "number1": {"type": "string"},
                                                            "number2": {"type": "string"}
                                                        },
                                                    "additionalProperties": False
                                                }
                                        }
                                }
                        }
                }
            },
        "additionalProperties": False,
    }
device_system_schema = \
    {
        "type": "object",
        "required": ["metric", "data"],
        "additionalProperties": False,
        "properties":
            {
                "metric": {"type": "string", "pattern": "^SYSTEM$"},
                "data":
                    {
                        "type": "array",
                        "items":
                            {
                                "type": "object",
                                "required": ["deviceId", "instance", "values"],
                                "additionalProperties": False,
                                "properties":
                                    {
                                        "deviceId": {"type": "string"},
                                        "instance": {"type": "string"},
                                        "values": {
                                            "type": "array",
                                            "items":
                                                {
                                                    "type": "object",
                                                    "required": ["timestamp", "number1"],
                                                    "additionalProperties": False,
                                                    "properties":
                                                        {
                                                            "timestamp": {"type": "number"},
                                                            "number1": {"type": "string"}
                                                        }
                                                }
                                        }
                                    }
                            }
                    }
            }

    }

network_schema = \
    {
        "type": "object",
        "required": ["metric", "data"],
        "additionalProperties": False,
        "properties": {
            "metric": {"type": "string", "pattern": "^NETWORK$"},
            "data": {"type": "array",
                     "items": {
                         "type": "object",
                         "required": [
                             "deviceId", "instance",
                             "localWanId", "remoteWanId",
                             "values"
                         ],
                         "additionalProperties": False,
                         "properties": {
                             "deviceId": {"type": "string"},
                             "localWanId": {"type": "string"},
                             "instance": {"type": "string"},
                             "remoteWanId": {"type": "string"},
                             "values": {
                                 "type": "array",
                                 "items": {
                                     "type": "object",
                                     "required": ["timestamp", "number1", "number2", "number3"],
                                     "properties": {
                                         "timestamp": {"type": "number"},
                                         "number1": {"type": "string"},
                                         "number2": {"type": "string"},
                                         "number3": {"type": "string"}
                                     },
                                     "additionalProperties": False
                                 }
                             }
                         }
                     }
                     }
        }
    }
