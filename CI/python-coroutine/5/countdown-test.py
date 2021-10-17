# -*- encoding=utf-8 -*-


import threading


cnt = 100000000

def countdown():
    global cnt
    while cnt > 0:
        cnt -= 1


if __name__ == '__main__':
    # countdown()

    t1 = threading.Thread(target=countdown)
    t2 = threading.Thread(target=countdown)
    t1.start()
    t2.start()

