# -*- encoding=utf-8 -*-


import os
import time
import multiprocessing


def consumer(cnt):
    while True:
        # cnt = queue.get()
        cnt -= 1
        print('I am a consumer. cnt = {}. process id = {}'.format(cnt, os.getpid()))
        time.sleep(1)


def producer(cnt):
    cnt = 0
    while True:
        # queue.put(cnt)
        cnt += 1
        print('I am a producer. cnt = {}. process id = {}'.format(cnt, os.getpid()))
        time.sleep(1)


if __name__ == '__main__':
    # 父进程
    # queue = multiprocessing.Queue()
    cnt = 0
    # 子进程1
    p1 = multiprocessing.Process(target=producer, args=(cnt, ))
    # 子进程2
    p2 = multiprocessing.Process(target=consumer, args=(cnt, ))
    p1.start()
    p2.start()
