import httplib
import re
import logging
import traceback


def post(uri, data, headers=None):
    return send("POST", uri, data, headers)


def patch(uri, data, headers=None):
    return send("PATCH", uri, data, headers)


def put(uri, data, headers=None):
    return send("PUT", uri, data, headers)


def delete(uri, headers=None, data=''):
    return send("DELETE", uri, data, headers)


def delete_with_data(uri, data, headers=None):
    return send("DELETE", uri, data, headers)


def get(uri, headers=None, data=""):
    return send("GET", uri, data, headers)


def send(method, uri, data, headers):
    if not headers:
        headers = {}
    protocol, host, path = analyze_url(uri)
    for attempts in range(3):
        try:
            conn = open_conn(host, protocol)
            log_http_req(method, uri, data, headers)
            conn.request(method, path, data, headers)
            return get_http_response(conn)
        except httplib.InvalidURL:
            logging.error("\nException Raise When Connection Request")
            traceback.print_exc()


def open_conn(host, protocol):
    return httplib.HTTPConnection(host) if (protocol == 'http') else httplib.HTTPSConnection(host)


def get_http_response(conn):
    res = conn.getresponse()
    ret = HttpResponse(res.status, res.read(), res.getheaders())
    log_http_rsp(ret)
    conn.close()
    return ret


def analyze_url(url):
    if "http" not in url:
        url = "http://" + url
    pattern = r"^(http|https)://([0-9:\.]+)(.*)"
    res = re.match(pattern, url)
    return res.group(1), res.group(2), res.group(3)


def log_http_rsp(rcv):
    logging.info("http response status code: %d" % rcv.status_code)
    logging.info("http response headers: %s" % rcv.headers)
    logging.info("http response body: %s" % rcv.content)


def log_http_req(method, uri, data, headers):
    logging.info("http {0} uri: {1}".format(method, uri))
    logging.info("http request header: {0}".format(headers))
    logging.info("http request body: {0}".format(data))


class HttpResponse:
    def __init__(self, status, content, headers):
        self.status_code = status
        self.content = content
        self.headers = headers
