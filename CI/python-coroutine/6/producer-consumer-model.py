# -*- encoding=utf-8 -*-


import multiprocessing


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

    p1 = multiprocessing.Process(target=producer)
    p2 = multiprocessing.Process(target=consumer)
    p1.start()
    p2.start()