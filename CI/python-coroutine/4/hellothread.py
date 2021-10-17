# -*- encoding=utf-8 -*-


import time
import threading


def loop():
    while True:
        print('hello python thread.')
        print('thread id = {}.'.format(threading.get_native_id()))
        time.sleep(1)


cnt = 0

def consumer():
    global cnt
    while True:
        if cnt <= 0:
            time.sleep(1)
            continue
        cnt -= 1
        print('I am a consumer. cnt = {}, thread id = {}'.format(cnt, threading.get_native_id()))
        time.sleep(1)


def producer():
    global cnt
    while True:
        cnt += 1
        print('I am a producer. cnt = {}, thread id = {}'.format(cnt, threading.get_native_id()))
        time.sleep(1)

    
if __name__ == '__main__':

    # loop()
    print('active_count = {}.'.format(threading.active_count()))
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    print('active_count = {}.'.format(threading.active_count()))
    t2.start()
    print('active_count = {}.'.format(threading.active_count()))
