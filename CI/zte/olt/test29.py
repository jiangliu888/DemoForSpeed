# -*- coding: UTF-8 -*-
from functools import update_wrapper,wraps
from inspect import signature

def typeassert(*ty_args,**ty_kargs):
    def decorator(func):
        # 获取函数参数和类型的映射关系  func ->a,b
        # d = {'a':int,'b':str}
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args,**ty_kargs).arguments
        def wrapper(*args,**kargs):
            # arg in d,instance(arg,d[arg])
            for name,obj in sig.bind(*args,**kargs).arguments.items():
                if name in btypes:
                    if not in btypes:
                        if not isinstance(obj,btypes[name]):
                            raise TypeError('"%s" must be "%s"' %(name,btypes[name]))
            return func(*args,**kargs)
        return wrapper
    return decorator
@typeassert(int,str,list)
def f(a,b,c):
    print(a,b,c)

f(1,'a',[1,2,3])