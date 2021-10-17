# -*- encoding=utf-8 -*-

import time
import random
import string
from queue import deque

from loop import coroutine, YieldLoop


# 求等差数列
@coroutine
def test1():
    # 1 - 10000 所有奇数的和
    sum = 0
    for i in range(1, 11):
        if i % 2 == 1:
            sum += yield i
    print('sum =', sum)

# YieldLoop.instance().add_coroutine(test1())
# YieldLoop.instance().run_until_complete()


# 生产者-消费者模型
@coroutine
def producer(q):
    while True:
        good = ''.join(random.sample(string.ascii_letters+string.digits, 8))
        q.append(good)
        cnt = len(q)
        print('producer produce good. cnt =', cnt)
        if cnt > 0:
            yield


@coroutine
def consumer(q):
    while True:
        while len(q) <= 0:
            print('q is empty.')
            yield
        good = q.popleft()
        print('consumer consum good = {}, cnt = {}'.format(good, len(q)))
        time.sleep(1)


q = deque()
YieldLoop.instance().add_coroutine(producer(q))
YieldLoop.instance().add_coroutine(producer(q))
YieldLoop.instance().add_coroutine(producer(q))
YieldLoop.instance().add_coroutine(producer(q))
YieldLoop.instance().add_coroutine(consumer(q))
YieldLoop.instance().run_until_complete()
