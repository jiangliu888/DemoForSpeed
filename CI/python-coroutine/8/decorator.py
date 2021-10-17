# -*- encoding=utf-8 -*-
#
# 装饰器的使用方法
# 

# @log

import time
# functools.wraps
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('print from log. call {}. call time = {}'.format(func.__name__, int(time.time())))
        return func(*args, **kwargs)
    return wrapper


@log
def function():
    # print('call function. call time = {}'.format(int(time.time()))
    print('Hello World. Hello function...')


@log
def function2():
    print('call function. call time = {}'.format(int(time.time())))
    pass

function()
print('name =', function.__name__)
# function2()
