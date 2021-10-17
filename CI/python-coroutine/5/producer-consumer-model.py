# -*- encoding=utf-8 -*-


import threading


cnt = 0

def consumer():
    global cnt
    while True:
        cnt -= 1


def producer():
    global cnt
    while True:
        cnt += 1

    
if __name__ == '__main__':

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()