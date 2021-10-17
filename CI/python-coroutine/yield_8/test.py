# -*- encoding=utf-8 -*-
from yieldloop import coroutine,YieldLoop

@coroutine
def test1():
    sum = 0
    for i in range(1,10001):
        if i % 2 == 1:
            sum += yield i
    print('sum =', sum)