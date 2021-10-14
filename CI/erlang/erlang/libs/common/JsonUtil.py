import json
import os
from deepdiff import DeepDiff


def load_json_file(filename):
    print '***********'
    print os.getcwd()
    with open(filename, "r") as fp:
        return json.load(fp)


def load_json(data):
    return json.loads(data)


def dump_json(data):
    return json.dumps(data)


def are_same(expected, actual, excluded=None, ignore_order=True):
    ret = DeepDiff(actual, expected, ignore_order=ignore_order, exclude_paths=excluded)
    print 'DeepDiff_return:{}'.format(ret)
    return False if ret else True


def i_eval(body):
    ret = body.replace("false", "False").replace("true", "True").replace("none", "None")
    print ret
    return eval(ret)
