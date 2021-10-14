import base64

import requests
import requests.adapters


class RestClient(object):
    requests.adapters.DEFAULT_POOLSIZE = 2000
    headers = {"content-type": "application/json", "connection": "close"}

    @classmethod
    def post(cls, url, data, token=None):
        try:
            if token:
                headers = {"content-type": "application/json", "connection": "close",
                           "Authorization": "Bearer {}".format(token)}
            else:
                headers = cls.headers
            return requests.post(url, data={}, json=data, headers=headers)
        except Exception as e:
            print("Failed to post {} {}".format(url, data))
            print(e)

    @classmethod
    def get(cls, url):
        try:
            return requests.get(url)
        except Exception as e:
            print("Failed to get {}".format(url))
            print(e)

    @classmethod
    def ok(cls, response):
        if response and response.status_code >= 200 and response.status_code < 300:
            return True
        else:
            return False