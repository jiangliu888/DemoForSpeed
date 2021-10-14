# -*- coding: UTF-8 -*-
from functools import wraps
import time

def warn(timeout):
    timeout = [timeout]
    def decorator(func):
        def wrapper(*arg,**karg):
            start = time.time()
            res = func(*arg,**karg)
            userd = time.time() - start
            if used >timeout:
                msg = '"%s":%s > %s' % (func.__name__,used,timeout)
                logging.warn(msg)
            return res      

        def setTimeout(k):
            """ python3 中nonlocal变量 声明嵌套下的变量
            nonlocal timeout """
            timeout[0] = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator

from random import randint
@warn(2)
def test():
    print("=====")
    while randint(0,1):
        time.sleep(0.5)

test.setTimeout(1)
for _ in range(30):
    test()