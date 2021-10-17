# -*- coding: UTF-8 -*-
from functools import wraps
from threading import RLock

def singleton(cls):
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args,**kwarg):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwarg)
        return instances[cls]
    return wrapper               