normalPlatform = {
    "ubuntu": ["amd64"],
    "openwrt": ["amd64", "arm"]
}

full_cpe_service_name_and_dep_list = {
    "aiwan-cpe": {
        "dependency": ["aiwan-config"],
        "path": ""
    },
    "aiwan-config": {
        "dependency": None,
        "path": ""
    },
    "aiwan-orion-client": {
        "dependency": None,
        "path": ""
    },
    "aiwan-thruster": {
        "dependency": None,
        "path": ""
    },
    "aiwan-log-agent": {
        "dependency": None,
        "path": ""
    }
}

full_cpe_service_body_list = [
    {
        "name": "aiwan-cpe",
        "platform": normalPlatform
    },
    {
        "name": "aiwan-config",
        "platform": {
            "ubuntu": ["amd64"]
        }
    },
    {
        "name": "aiwan-orion-client",
        "platform": normalPlatform
    },
    {
        "name": "aiwan-thruster",
        "platform": normalPlatform
    },
    {
        "name": "aiwan-log-agent",
        "platform": normalPlatform
    },
]
