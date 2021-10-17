# -*- encoding=utf-8 -*- 


import os
import time
import multiprocessing


def loop():
    while True:
        print('hello python process.')
        print('process id = {}, parent process id = {}'.format(os.getpid(), os.getppid()))
        time.sleep(1)


cnt = 0

def consumer():
    global cnt
    while True:
        if cnt <= 0:
            print('cnt <= 0. continue...')
            time.sleep(1)
            continue
        cnt -= 1
        print('I am a consumer. cnt = {}, process id = {}'.format(cnt, os.getpid()))
        time.sleep(1)


def producer():
    global cnt
    while True:
        cnt += 1
        print('I am a producer. cnt = {}, process id = {}'.format(cnt, os.getpid()))
        time.sleep(1)


if __name__ == '__main__':
    # loop()

    p1 = multiprocessing.Process(target=consumer)
    p2 = multiprocessing.Process(target=producer)
    p1.start()
    p2.start()
