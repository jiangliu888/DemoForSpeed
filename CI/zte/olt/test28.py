# -*- coding: UTF-8 -*-
from functools import update_wrapper,wraps
def func_print(func):
    @wraps(func)
    def wrapper(*args,**kargs):
        print("*****")
        func(*args,**kargs)
    return wrapper

@func_print
def func1():
    print("========")

func1()
print(func1.__name__)