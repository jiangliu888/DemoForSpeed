# -*- coding: UTF-8 -*-
#存在重复计算，添加缓存 
def fb(n,cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = fb(n-1,cache) + fb(n-2,cache)
    return cache[n]
print(fb(50))
# cache不会因为memo()函数结束而消失，
# 闭包就是引用了外部变量的内部函数
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
#@memo等价于fb = memo(fb)
@memo
def fb(n):
    if n <= 1:
        return 1
    return fb(n-1) + fb(n-2)

print(fb(50)) 