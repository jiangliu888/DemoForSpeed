# -*- coding: UTF-8 -*-
companyBody = {
    "best_ai_wan":{
        "name" : "best_ai_wan"
    },
    "testCompany":{
        "name" :"testCompany"
    }
}

companyEncryptionBody = {"key":"HWyKw5eNdewkQdjC","algorithm":"AES-128","format":"256"}

cpeglobalconfigneBody = {
	"salt": 'salt-cpe.test.netgrounder.com',
	"regUrl": "https://controller-st.netgrounder.com:9001/api/v1/ne/cpe",
	"authUrl": "https://authserver-st.netgrounder.com",
	"collectdAddr": "10.194.20.105",
	"collectdPort": "6789",
	'prismAddr': '10.194.20.105:9877',
	"controllers": [
		{
			"domain": "controller-st.netgrounder.com",
			"port": 6633,
			"mode": "gateway"
		},
		{
			"domain": "controller-st.netgrounder.com",
			"port": 6633,
			"mode": "parallel"
		},
		{
			"domain": "controller-st.netgrounder.com",
			"port": 6653,
			"mode": "series"
		}
	]
}

siteBody = {
    "guangzhou":{
	    "id": "9d353c7a-07b1-44d7-9181-5f9f4d15c4ad",
	    "name": "guangzhou",
		"sn": ["1004"],
	    "config": {
		    "neId": 1004,
			'dynamicEnable': False,
		    "nets": [
			    "172.19.43.0/24"
		    ],
		    "privateAddrs": [],
		    "publicAddrs": []
	    }
    },
    "beijing":{
	    "id": "1c6293ad-914f-44a9-9dc3-30b1ad60cb0b",
	    "name": "beijing",
		"sn": ["1002"],
		"config": {
		    "neId": 1002,
			'dynamicEnable': False,
		    "nets": [],
		    "privateAddrs": [
			    "10.193.0.0/26",
			    "10.193.0.64/27",
			    "10.193.0.96/30",
			    "10.193.0.100/32"
		    ],
		    "publicAddrs": []
	    }
    },
    "nanjing":{
	    "id": "29201375-9c0a-4a50-b8df-853266dfb238",
	    "name": "nanjing",
		"sn": ["1005"],
		"config": {
		    "neId": 1005,
			'dynamicEnable': False,
		    "nets": [
			    "172.19.14.0/24"
		    ],
		    "privateAddrs": [],
		    "publicAddrs": [
			    {
				    "iface": "enp1s0f0",
				    "index": 0,
				    "publicIp": "10.194.14.2"
			    },
			    {
				    "iface": "enp1s0f0",
				    "index": 1,
				    "publicIp": "10.196.14.2"
			    }
		    ]
	    }
    },
	"site-2081":{
		"id": "6e0f18af-c2c0-4e35-ac5a-599e100b5e24",
		"name": "site-2081",
		"sn": ["2081"],
		"config": {
			"neId": 402,
			'dynamicEnable': False,
			"nets": [
				"192.168.88.0/24"
			],
			"privateAddrs": [],
			"publicAddrs": []
		}
	},
	"site-2082":{
		"id": "e949bcae-4631-463e-9703-d3a137c9110b",
		"name": "site-2082",
		"sn": ["2082"],
		"config": {
			"neId": 418,
			'dynamicEnable': False,
			"nets": [
				"192.168.90.0/24"
			],
			"privateAddrs": [],
			"publicAddrs": []
		}
	},
	"site-2083":{
		"id": "63d422b7-d4cc-42c7-9620-8a7f3f452184",
		"name": "site-2083",
		"sn": ["2083"],
		"config": {
			"neId": 434,
			'dynamicEnable': False,
			"nets": [
				"192.168.93.0/24"
			],
			"privateAddrs": [],
			"publicAddrs": []
		}
	},
	"site-2084":{
		"id": "03c9dff3-a204-49d8-a88f-d99d16a04d7e",
		"name": "site-2084",
		"sn": ["2084"],
		"config": {
			"neId": 450,
			'dynamicEnable': False,
			"nets": [
				"192.168.93.0/24",
				"192.168.101.0/24"
			],
			"privateAddrs": [],
			"publicAddrs": []
		}
	},
	"site-2085": {
		"id": "010ad8d3-bcb6-4a4d-a08b-1144638e9b21",
		"name": "site-2085",
		"sn": ["2085"],
		"config": {
			"neId": 784,
			'dynamicEnable': False,
			"nets": [],
			"privateAddrs": [],
			"publicAddrs": []
		}
	},
	"site-2086":{
		"id": "7a39ed44-9c51-476a-9865-a3b48146b63c",
		"name": "site-2086",
		"sn": ["2086"],
		"config": {
			"neId": 800,
			'dynamicEnable': False,
			"nets": [
				"192.168.95.0/24"
			],
			"privateAddrs": [],
			"publicAddrs": []
		}
	},
	"site-2087":{
		"id": "1f61a22e-6615-4626-8ce7-00dffc7f2c77",
		"name": "site-2087",
		"sn": ["2087"],
		"config": {
			"neId": 816,
			'dynamicEnable': False,
			"nets": [
				"192.168.96.0/24"
			],
			"privateAddrs": [],
			"publicAddrs": []
		}
	},
	"site-2088":{
		"id": "a0619a4d-f436-4534-aab7-a4ff60b2ffb3",
		"name": "site-2088",
		"sn": ["2088"],
		"config": {
			"neId": 353,
			'dynamicEnable': False,
			"nets": [
				"192.168.98.0/24"
			],
			"privateAddrs": [],
			"publicAddrs": []
		}
	},
	"site-2089":{
		"id": "ca6dfca1-3d5f-4c22-94a1-6f88581af820",
		"name": "site-2089",
		"sn": ["2089"],
		"config": {
			"neId": 369,
			'dynamicEnable': False,
			"nets": [
				"192.168.99.0/24",
				"192.168.100.0/24"
			],
			"privateAddrs": [],
			"publicAddrs": []
		}
	}
}

siteRateLimitBody = {
    "guangzhou": {
	    "bandwidth": 1048576,
	    "burst": 10,
	    "latency": 10
    },
    "beijing": {
	    "bandwidth": 1048576,
	    "burst": 10,
	    "latency": 10
    },
    "nanjing": {
	    "bandwidth": 1048576,
	    "burst": 10,
	    "latency": 10
    },
    "site-2081": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    },
    "site-2082": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    },
    "site-2083": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    },
    "site-2084": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    },
    "site-2085": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    },
    "site-2086": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    },
    "site-2087": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    },
    "site-2088": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    },
    "site-2089": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    }
}

unionBody = {
    "un-pasite-un-gwsite":{
	    "name": "un-pasite-un-gwsite",
	    "siteA": "83d18ee9-1ec5-4a7e-abc2-2eb200c1c206",
	    "siteB": "4181198b-d8c2-4f7b-ac1c-fd8d41c63e02",
	    "privateNet": False,
	    "officeNet": True,
	    "transportMode": 1
    },
    "un-pasite-un-sesite":{
	    "name": "un-pasite-un-sesite",
	    "siteA": "83d18ee9-1ec5-4a7e-abc2-2eb200c1c206",
	    "siteB": "3a5939e2-53bb-4588-86a7-7d1fc942cff5",
	    "privateNet": False,
	    "officeNet": True,
	    "transportMode": 1
    },
    "un-sesite-un-gwsite":{
	    "name": "un-sesite-un-gwsite",
	    "siteA": "3a5939e2-53bb-4588-86a7-7d1fc942cff5",
	    "siteB": "4181198b-d8c2-4f7b-ac1c-fd8d41c63e02",
	    "privateNet": False,
	    "officeNet": True,
	    "transportMode": 1
    }
}

unionRateLimitBody = {
    "un-pasite-un-gwsite": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    },
    "un-pasite-un-sesite": {
	    "bandwidth": 10240,
	    "burst": 10,
	    "latency": 10
    },
    "un-sesite-un-gwsite": {
	    "bandwidth": 1048576,
	    "burst": 10,
	    "latency": 10
    }
}

deviceRuleBody = {
    "2011": [
	    {
		    "name": "aiwan_rule0",
		    "src_ipaddr": "172.19.43.0",
		    "src_network": "172.19.43.0/24",
		    "dest_network": "172.19.14.0/24",
		    "to_idc": True,
		    "to_net": False
	    },
	    {
		    "name": "aiwan_rule1",
		    "src_ipaddr": "192.168.1.1",
		    "src_network": "172.19.43.0/24",
		    "dest_network": "172.19.14.0/24",
		    "to_idc": False,
		    "to_net": True
	    }
    ]
}

spiTagsBody = {
	"Saas": 	[{
		"rules": [
			{
				"dstDomain": ".*\\.onenote\\.com"
			},
			{
				"dstCIDR": "8.8.8.8/32"
			}
		],
		"tag": 3,
		"name": "SPISaas"
	}],
	"allIpUdp": 	[{
		"rules": [
			{
				"dstCIDR": "128.0.0.0/1",
				"l4proto":"17"
			},
			{
				"dstCIDR": "0.0.0.0/1"
			}
		],
		"tag": 2,
		"name": "allIpUdp"
	}],
	"Empty": [],
	"saasNew": 	[{
		"rules": [
			{
				"dstDomain": ".*\\.biying\\.com",
				'l4proto': '1,6',
				'icmpCode': 0, 
				'icmpType': 8, 
			},
			{
				"dstCIDR": "8.8.8.8/32"
			}
		],
		"tag": 3,
		"name": "SPISaas"
	}],
	'all': [
    {
        'rules': [
            {
                'srcPort': '5021',
                'dstDomain': 'www.baidu.com',
                'l4proto': '17',
                'srcCIDR': '172.19.14.125/32',
                'dstPort': '5021'
            },
            {
                'dstCIDR': '0.0.0.0/1'
            }
        ],
        'tag': 2,
        'name': 'allIpUdp'
    },
    {
        'rules': [
            {
                'icmpCode': 0,
                'icmpType': 8,
                'dstDomain': '.*\\.biying\\.com',
                'l4proto': '1,6'
            },
            {
                'dstCIDR': '8.8.8.8/32'
            }
        ],
        'tag': 3,
        'name': 'SPISaas'
    },
    {
        'rules': [
            {
                'dstDomain': '.*\\.onenote\\.com'
            },
            {
                'dstCIDR': '8.8.8.8/32'
            }
        ],
        'tag': 4,
        'name': 'SPIModifySaas'
    },
    {
        'rules': [
            {
                'dstCIDR': '0.0.0.0/1',
                'dstPort': '5021',
                'l4proto': '6',
                'srcCIDR': '187.19.14.125/32'
            },
            {
                'dstCIDR': '8.8.8.8/32'
            }
        ],
        'tag': 32768,
        'name': 'GlobalSaas'
    }
]}

spiDispatchBody = {
	"spi-gwsite":
[
	{
		"priority": 1000,
		"actions": [
			{
				"name": "saas",
				"param": [
					{
						"agent": "8.8.8.8",
						"ttl": 600
					},
					{
						"code": "135004189",
						"ttl": 600
					}
				]
			}
		]
	}
],
"spi-sesite":
[
	{
		"priority": 1000,
		"actions": [
			{
				"name": "saas",
				"param": [
					{
						"agent": "8.8.8.8",
						"ttl": 600
					},
					{
						"code": "135004189",
						"ttl": 600
					}
				]
			}
		]
	}
],
"spi-pasite":
[
	{
		"priority": 1000,
		"actions": [
			{
				"name": "saas",
				"param": [
					{
						'code': '135004189',
						"ttl": 600
					},
					{
						"code": "135004189",
						"ttl": 600
					}
				]
			}
		]
	}
],
"spi-pasite2":
[
	{
		"priority": 1000,
		"actions": [
			{
				"name": "saas",
				"param": [
					{
						"code": "135004189",
						"ttl": 600
					},
					{
						"agent": "8.8.8.8",
						"ttl": 600
					}
				]
			}
		]
	}
],
"spi-dedicate-gwsite":
[
        {
                "priority": 1000,
                "actions": [
                        {
                                "name": "saas",
                                "param": [
                                        {
                                                "ttl": 600,
                                                "agent": "8.8.8.8"
                                        },
                                        {
                                                "ttl": 600,
                                                "agent": "8.8.8.8"
                                        }
                                ],
                                "appointment": [
                                        {
                                                "serviceId": 344,
                                                "carrierId": 0
                                        },
                                        {
                                                "serviceId": 328,
                                                "carrierId": 13
                                        }
                                ]
                        }
                ]
        }
],
"spi-dedicate-gwsite2":
[
        {
                "priority": 1000,
                "actions": [
                        {
                                "name": "saas",
                                "param": [
                                        {
                                                "ttl": 200,
                                                "agent": "8.8.8.9"
                                        },
                                        {
                                                "ttl": 200,
                                                "agent": "8.8.8.9"
                                        }
                                ],
                                "appointment": [
                                        {
                                                "serviceId": 344,
                                                "carrierId": 0
                                        }
                                ]
                        }
                ]
        }
],
"Empty": []
	}

vportPreferenceBody = {
    "guangzhou" : [
	    {
		    "portId": {
			    "iface": "eth0",
			    "index": 0
		    },
		    "preferHomeCode": {
			    "cac": 4,
			    "eac": 5,
			    "preferIp": "10.194.20.3"
		    },
		    "preferCac": 4,
		    "preferGroups": [
			    "101",
                "102"
		    ]
	    },
	    {
		    "portId": {
			    "iface": "eth1",
			    "index": 0
		    },
		    "preferHomeCode": {
			    "cac": 4,
			    "eac": 4,
			    "preferIp": "10.196.20.4"
		    }
	    }
    ],
    "beijing":[
	    {
		    "portId": {
			    "iface": "enp1s0f0",
			    "index": 0
		    },
		    "preferHomeCode": {
			    "cac": 4,
			    "eac": 4,
			    "preferIp": "10.196.20.4"
		    },
		    "preferGroups": [
			    "101"
		    ]
	    }
    ],
    "nanjing":[
	    {
		    "portId": {
			    "iface": "enp1s0f0",
			    "index": 0
		    },
		    "preferHomeCode": {
			    "cac": 4,
			    "eac": 4,
			    "preferIp": "10.196.20.4"
		    },
		    "preferGroups": [
			    "103"
		    ]
	    },
	    {
		    "portId": {
			    "iface": "enp1s0f0",
			    "index": 1
		    },
		    "preferHomeCode": {
			    "cac": 4,
			    "eac": 5,
			    "preferIp": "10.194.20.3"
		    }
	    }
    ],
	"site-2081":[
		{
			"portId": {
				"iface": "wan",
				"index": 0
			}
		},
		{
			"portId": {
				"iface": "lan3",
				"index": 0
			}
		}
	],
	"site-2082":[
		{
			"portId": {
				"iface": "wan",
				"index": 0
			}
		},
		{
			"portId": {
				"iface": "lan3",
				"index": 0
			}
		}
	],
	"site-2083":[
		{
			"portId": {
				"iface": "wan",
				"index": 0
			}
		}
	],
	"site-2084":[
		{
			"portId": {
				"iface": "wan",
				"index": 0
			}
		}
	],
	"site-2085":[
		{
			"portId": {
				"iface": "enps0s0",
				"index": 0
			}
		}
	],
	"site-2086":[
		{
			"portId": {
				"iface": "enps0s0",
				"index": 0
			}
		}
	],
	"site-2087":[
		{
			"portId": {
				"iface": "enps0s0",
				"index": 0
			}
		},
		{
			"portId": {
				"iface": "enps0s0",
				"index": 1
			}
		}
	],
	"site-2088":[
		{
			"portId": {
				"iface": "eth0",
				"index": 0
			}
		},
		{
			"portId": {
				"iface": "eth1",
				"index": 0
			}
		}
	],
	"site-2089":[
		{
			"portId": {
				"iface": "eth0",
				"index": 0
			}
		}
	]
}

vportRateLimitBody = {
    "guangzhou" :[
	    {
		    "portId": {
			    "iface": "eth0",
			    "index": 0
		    },
		    "rateLimit": {
			    "bandwidth": 1024000,
			    "burst": 100,
			    "latency": 10,
			    "ratio": 0
		    }
	    },
	    {
		    "portId": {
			    "iface": "eth1",
			    "index": 0
		    },
		    "rateLimit": {
			    "bandwidth": 1024000,
			    "burst": 100,
			    "latency": 10,
			    "ratio": 0
		    }
	    }
    ],
    "beijing":[
	    {
		    "portId": {
			    "iface": "enp1s0f0",
			    "index": 0
		    },
		    "rateLimit": {
			    "bandwidth": 1024000,
			    "burst": 100,
			    "latency": 10,
			    "ratio": 0
		    }
	    }
    ],
    "nanjing":[
	    {
		    "portId": {
			    "iface": "enp1s0f0",
			    "index": 0
		    },
		    "rateLimit": {
			    "bandwidth": 1024000,
			    "burst": 100,
			    "latency": 10,
			    "ratio": 0
		    }
	    },
	    {
		    "portId": {
			    "iface": "enp1s0f0",
			    "index": 1
		    },
		    "rateLimit": {
			    "bandwidth": 1024000,
			    "burst": 100,
			    "latency": 10,
			    "ratio": 0
		    }
	    }
    ],
	"site-2081":[
		{
			"portId": {
				"iface": "wan",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		},
		{
			"portId": {
				"iface": "lan3",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		}
	],
	"site-2082":[
		{
			"portId": {
				"iface": "wan",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		},
		{
			"portId": {
				"iface": "lan3",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		}
	],
	"site-2083":[
		{
			"portId": {
				"iface": "wan",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		}
	],
	"site-2084":[
		{
			"portId": {
				"iface": "wan",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		}
	],
	"site-2085":[
		{
			"portId": {
				"iface": "enps0s0",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		}
	],
	"site-2086":[
		{
			"portId": {
				"iface": "enps0s0",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		}
	],
	"site-2087":[
		{
			"portId": {
				"iface": "enps0s0",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		},
		{
			"portId": {
				"iface": "enps0s0",
				"index": 1
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		}
	],
	"site-2088":[
		{
			"portId": {
				"iface": "eth0",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		},
		{
			"portId": {
				"iface": "eth1",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		}
	],
	"site-2089":[
		{
			"portId": {
				"iface": "eth0",
				"index": 0
			},
			"rateLimit": {
				"bandwidth": 10240,
				"burst": 100,
				"latency": 10,
				"ratio": 0
			}
		}
	]
}

netConfigBody = {
    "guangzhou" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
    "beijing" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
    "nanjing" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
	"site-2081" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
	"site-2082" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
	"site-2083" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
	"site-2084" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
	"site-2085" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
	"site-2086" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
	"site-2087" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
	"site-2088" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    },
	"site-2089" :{
	    "mtu": 1400,
	    "keepAlive": 10,
	    "strategy": 2
    }
}

wifiBody = {
    "1004": [
		{
			"name": "wifi-iface",
			"options": [
				{
					"name": "ssid",
					"value": "testwifi"
				},
				{
					"name": "encryption",
					"value": "psk2"
				},
				{
					"name": "key",
					"value": "12345678"
				},
				{
					"name": "network",
					"value": "lan"
				},
				{
					"name": "macfilter",
					"value": "allow"
				},
				{
					"name": "maclist",
					"value": "00:83:09:00:15:d4"
				},
				{
					"name": "maclist",
					"value": "00:83:09:00:15:d5"
				},
				{
					'name': 'device',
					'value': 'radio0'
				},
				{
					'name': 'mode',
					'value': 'ap'
				},
				{
					'name': 'disabled', 
					'value': '0'
				}
			]
		}
	]
}

startupBody = {
	"1004": {
		"mode": "gateway",
		"tunnelPort": 6868,
		"interface": [
			{
				"name": "eth0",
				"type": "WAN",
				"mode": "FIA",
				"proxy": True,
				'usage': 'normal'
			},
			{
				"name": "eth1",
				"type": "WAN",
				"mode": "FIA",
				"proxy": True,
				'usage': 'normal'
			},
			{
				"name": "tun1",
				"type": "LAN",
				"mode": "FIA",
				"pair": "eth0"
			}
		],
		"reportInterval": 10,
		"scoreInterval": 10
	},
	"1020": {
		"mode": "gateway",
		"tunnelPort": 6868,
		"interface": [
			{
				"name": "wan",
				"type": "WAN",
				"mode": "FIA",
				"proxy": True,
				'usage': 'normal'
			},
			{
				"name": "tun1",
				"type": "LAN",
				"mode": "FIA",
				"pair": "wan"
			}
		],
		"reportInterval": 10,
		"scoreInterval": 10
	},
	"1021":{
		"mode": "gateway",
		"tunnelPort": 6868,
		"interface": [
			{
				"name": "eth0.3",
				"type": "WAN",
				"mode": "FIA",
				"proxy": True,
				'usage': 'normal'
			},
			{
				"name": "eth0.4",
				"type": "WAN",
				"mode": "FIA",
				"proxy": True,
				'usage': 'normal'
			},
			{
				"name": "tun1",
				"type": "LAN",
				"mode": "FIA",
				"pair": "eth0.3"
			}
		],
		"reportInterval": 10,
		"scoreInterval": 10
	},
	"1030":{
		"mode": "gateway",
		"tunnelPort": 6868,
		"interface": [
			{
				"name": "wan",
				"type": "WAN",
				"mode": "FIA",
				"proxy": True,
				'usage': 'normal'
			},
			{
				"name": "tun1",
				"type": "LAN",
				"mode": "FIA",
				"pair": "wan"
			}
		],
		"reportInterval": 10,
		"scoreInterval": 10
	},
	"3020":{
		"mode": "gateway",
		"tunnelPort": 8989,
		"interface": [
			{
				"name": "wan",
				"type": "WAN",
				"mode": "FIA",
				"proxy": True,
				'usage': 'normal'
			},
			{
				"name": "lan3",
				"type": "WAN",
				"mode": "FIA",
				"proxy": True,
				'usage': 'normal'
			},
			{
				"name": "tun1",
				"type": "LAN",
				"mode": "FIA",
				"pair": "wan"
			},
			{
				"name": "wwan0",
				"type": "WAN",
				"mode": "MIA",
				"proxy": True,
				'usage': 'backup'
			}
		],
		"reportInterval": 60,
		"scoreInterval": 60,
		"natNet": "100.64.0.0/16"
	},
	"1002" : {
		"mode": "series",
		"tunnelPort": 4000,
		"interface": [
			{
				"name": "enp1s0f0",
				"type": "WAN",
				"mode": "FIA",
				"proxy": True,
				'usage': 'normal'
			},
			{
				"name": "enp1s0f1",
				"type": "LAN",
				"mode": "FIA",
				"pair": "enp1s0f0"
			}
		],
		"reportInterval": 10,
		"scoreInterval": 10
	},
	"2009" : {
		"mode": "series",
		"tunnelPort": 8989,
		"interface": [
			{
				"name": "enp1s0f0",
				"type": "WAN",
				"mode": "FIA",
				"proxy": True,
				"usage": "normal",
				"gw-mac": "11:22:33:44:55:66",
				"static-ip": "10.192.20.1"
			},
			{
				"name": "enp1s0f1",
				"type": "LAN",
				"mode": "FIA",
				"pair": "enp1s0f0"
			},
			{
				"name": "enp1s0f2",
				"type": "LAN",
				"mode": "DIA"
			}
		],
		"reportInterval": 60,
		"scoreInterval": 60
	}
}

networkBody = {
	"1004" : [
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "eth0"
				},
				{
					"name": "proto",
					"value": "dhcp"
				}
			]
		},
		{
			"interface": "wan2",
			"options": [
				{
					"name": "ifname",
					"value": "eth1"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "10.194.12.2"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "gateway",
					"value": "10.194.12.1"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "eth2"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "172.19.43.0"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
				  "name": "type",
				  "value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		},
		{
			"interface": "aiwanlan2",
			"options": [
				{
					"name": "ifname",
					"value": "eth3"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.1.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"internet": True
		}
	],
	"1020" : [
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "wan"
				},
				{
					"name": "proto",
					"value": "dhcp"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "lan0"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "172.19.45.0"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		}
	],
	"1021" :[
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "eth0.3"
				},
				{
					"name": "proto",
					"value": "dhcp"
				}
			]
		},
		{
			"interface": "wan2",
			"options": [
				{
					"name": "ifname",
					"value": "eth0.4"
				},
				{
					"name": "proto",
					"value": "dhcp"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "eth0.1"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "172.19.45.0"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		},
		{
			"interface": "aiwanlan2",
			"options": [
				{
					"name": "ifname",
					"value": "eth0.2"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "172.19.46.0"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"internet": True
		}
	],
	"1030":[
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "wan"
				},
				{
					"name": "proto",
					"value": "dhcp"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "lan0 lan1 lan2"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "172.19.45.0"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		}
	],
	"3020": [
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "wan"
				},
				{
					"name": "proto",
					"value": "dhcp"
				}
			]
		},
		{
			"interface": "wan2",
			"options": [
				{
					"name": "ifname",
					"value": "lan3"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "10.194.12.2"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "gateway",
					"value": "10.194.12.1"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "lan0"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "172.19.43.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": True
		}
	],
	"2081":[
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "wan"
				},
				{
					"name": "proto",
					"value": "pppoe"
				},
				{
					"name": "username",
					"value": "123456"
				},
				{
					"name": "password",
					"value": "234567"
				}
			]
		},
		{
			"interface": "wan2",
			"options": [
				{
					"name": "ifname",
					"value": "lan3"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.89.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "gateway",
					"value": "192.168.89.254"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "lan0 lan1 lan2"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.88.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		}
	],
	"2082":[
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "wan"
				},
				{
					"name": "proto",
					"value": "dhcp"
				}
			]
		},
		{
			"interface": "wan2",
			"options": [
				{
					"name": "ifname",
					"value": "lan3"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.91.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "gateway",
					"value": "192.168.91.254"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "lan0"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.90.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		},
		{
			"interface": "aiwanlan2",
			"options": [
				{
					"name": "ifname",
					"value": "lan1 lan2"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.92.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		}
	],
	"2083":[
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "wan"
				},
				{
					"name": "proto",
					"value": "pppoe"
				},
				{
					"name": "username",
					"value": "347j874"
				},
				{
					"name": "password",
					"value": "dhfuguw"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "lan0 lan1 lan2"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.93.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		}
	],
	"2084":[
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "wan"
				},
				{
					"name": "proto",
					"value": "dhcp"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "lan0"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.94.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		},
		{
			"interface": "aiwanlan2",
			"options": [
				{
					"name": "ifname",
					"value": "lan1 lan2"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.101.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		}
	],
	"2088":[
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "eth0"
				},
				{
					"name": "proto",
					"value": "dhcp"
				}
			]
		},
		{
			"interface": "wan2",
			"options": [
				{
					"name": "ifname",
					"value": "eth1"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.97.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "gateway",
					"value": "192.168.97.254"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "eth2"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.98.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		}
	],
	"2089":[
		{
			"interface": "wan",
			"options": [
				{
					"name": "ifname",
					"value": "eth0"
				},
				{
					"name": "proto",
					"value": "pppoe"
				},
				{
					"name": "username",
					"value": "456739Jd"
				},
				{
					"name": "password",
					"value": "sfsfdf"
				}
			]
		},
		{
			"interface": "lan",
			"options": [
				{
					"name": "ifname",
					"value": "eth1"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.99.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		},
		{
			"interface": "aiwanlan2",
			"options": [
				{
					"name": "ifname",
					"value": "eth2"
				},
				{
					"name": "proto",
					"value": "static"
				},
				{
					"name": "ipaddr",
					"value": "192.168.100.1"
				},
				{
					"name": "netmask",
					"value": "255.255.255.0"
				},
				{
					"name": "type",
					"value": "bridge"
				}
			],
			"idc": True,
			"internet": False
		}
	]
}

managerBody = {
	"global": [
		{
			"ip": "127.0.0.1",
			"port": 65535
		},
		{
			"ip": "127.0.0.2",
			"port": 80
		},
		{
			"ip": "127.0.0.1",
			"port": 33333
		},
		{
			"ip": "127.0.0.2",
			"port": 81
		}
	],
	"specific": {
	}
}

openflowBody = {
	"global": [
		{
			"ip": "127.0.0.1",
			"port": 6633
		},
		{
			"ip": "127.0.0.1",
			"port": 6653
		},
		{
			"ip": "127.0.0.1",
			"port": 6634
		},
		{
			"ip": "127.0.0.1",
			"port": 6654
		}
	],
	"specific": {
	}
}

saasSearchPattern = {
    "0X8054400" :{
		"matcher": {
			"region": 1,
			"country": 1,
			"area": 5,
			"district": 16
		},
		"proxyServices": [
			328
		]
	},
	"0X8058580" :{
		"matcher": {
			"region": 1,
			"country": 1,
			"area": 6,
			"district": 22
		},
		"proxyServices": [
			328
		]
	}
}

companySaasSearchPattern = {
    "0X8040000" :{
		"matcher": {
			"region": 1,
			"country": 1,
			"area": 0,
			"district": 0
		},
		"proxyServices": [
			328
		]
	}
}

companyAcls = {
	"FullAcl":{"name":"FullAcl","siteId":"0f485214-9d5b-4afb-8705-c8f3aeaae668","priority":499,"protocol":"6,17,1","srcCIDR":"192.168.0.0/1","dstCIDR":"192.168.255.254","dstPort":"22,5000-6000","strategy":"permit"},
	"OnlyPort":{"name":"OnlyPort","siteId":"0f485214-9d5b-4afb-8705-c8f3aeaae668","priority":500,"dstPort":"22,5000-5500,65535","strategy":"permit"}
}

companyRouters = {
	"FullRouter":{"name":"FullRouter","siteId":"0f485214-9d5b-4afb-8705-c8f3aeaae668","priority":499,"protocol":"6,17,1","srcCIDR":"192.168.0.0/1","srcPort":"65535","dstCIDR":"192.168.255.254","dstPort":"22,5000-6000","nextHop":"0f485214-9d5b-4afb-8705-c8f3aeaae668"},
	"OnlyPort":{"name":"OnlyPort","siteId":"0f485214-9d5b-4afb-8705-c8f3aeaae668","priority":500,"srcPort":"0","dstPort":"22,5000-5500,65535","nextHop":"0f485214-9d5b-4afb-8705-c8f3aeaae668"}
}

anycastSearchPattern = {
    "0X8054400" :{
		"matcher": {
			"region": 1,
			"country": 1,
			"area": 5,
			"district": 16
		},
		"proxyServices": [
			327,
			343
		]
	},
	"0X8058580" :{
		"matcher": {
			"region": 1,
			"country": 1,
			"area": 6,
			"district": 22
		},
		"proxyServices": [
			327,
			343
		]
	}
}

netAlgConfigBody = {
	"upperBandwidth": 100,
	"lowerBandwidth": 20,
	"upperBwPercent": 200,
	"lowerBwPercent": 30,
	"maxLossIn15Min": 1.8,
	"avgLossIn60Min": 0.8,
	"maxLossRatio": 10,
	"forwardingCost": 5,
	"weightCoefficient": 5
}

popBody = {
    "X223328": {
		"routeCode": {
			"cac": 4,
			"eac": 1
		},
		"status": {"status":"NORMAL"}
	},
	"X223313": {
		"routeCode": {
			"cac": 4,
			"eac": 11
		},
		"status": {"status":"NORMAL"}
	},
	"X223315": {
		"routeCode": {
			"cac": 4,
			"eac": 2
		},
		"status": {"status":"NORMAL"}
	}
}

corpBody = {
    "CompanyAudit":{u'eimdata': [], u'totalcount': 1, u'result': 0}
}

raduisBody =  {u'authtype': u'PAP', u'serverport': u'1812', u'result': 0, u'serverip': u'192.168.0.122'}

ldapBody = {u'ldapserver': u'192.168.0.8', u'admindn': u'cn=admin,dc=subao,dc=com', u'rootdn': u'dc=subao,dc=com', u'result': 0, u'ldapport': u'398'}

timeoutBody = {u'idletime': u'1799', u'result': 0, u'authtime': u'7199'}

navUrlBody = {u'navurl': u'http://www.netskyper.com', u'result': 0}

cpeAuditBody = {
   'default':{'auditServer': ':3080', 'enable': 0},
   'configDisable':{
	"auditServer": "https://139.224.41.89:3080",
	"enable": 0},
   'configEnable':{
		"auditServer": "https://139.224.41.89:3080",
		"enable": 1},
	}

cpeAuthBody = {
    'default':{'authServer': ':8006', 'enable': 0},
	'configDisable':{
		"authServer": "https://10.192.20.91:8006",
		"enable": 0},
	'configEnable':{
		"authServer": "https://10.192.20.91:8006",
		"enable": 1}
	}

corpAPBody = {u'apname': u'audit-gwsite1', u'linename': u'', u'telphone': u'', u'longitude': u' ', u'apid': u'02004c4f4f50', u'devmac': u'02:00:4c:4f:4f:50', u'address': u'guanghzou', u'latitude': u' '}


