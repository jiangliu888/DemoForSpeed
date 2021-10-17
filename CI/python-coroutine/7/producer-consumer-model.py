# -*- encoding=utf-8 -*-
#
# 使用生成器实现生产者-消费者模型
#


import time

# 消费者
def consumer():
    cnt = yield
    while True:
        if cnt <= 0:
            # 暂停、让出CPU
            cnt = yield cnt
        cnt -= 1
        time.sleep(1)
        print('consumer consum 1 cnt. cnt =', cnt)


# 生产者 (调度器)
def producer(cnt):
    gen = consumer()
    # 激活生成器
    next(gen)
    gen.send(cnt)
    while True:
        cnt += 5
        print('producer producer 5 cnt. cnt =', cnt)
        # 调度消费者
        current = int(time.time())
        if current % 7 == 0:
            cnt = gen.send(cnt)
        else:
            time.sleep(1)


if __name__ == '__main__':
    producer(0)
