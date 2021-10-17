# -*- encoding=utf-8 -*-


import time
import threading


class SimpleThreadPool:
    """简化的线程池实现
    """

    def process(self):
        while True:
            if len(self.queue) == 0:
                time.sleep(1)
                continue
            task = self.queue.pop()
            task()

    def __init__(self, size):
        self.pool = []
        self.queue = []
        for i in range(size):
            self.pool.append(threading.Thread(target=self.process))

    def submit(self, task):
        self.queue.append(task)

    def start(self):
        for thread in self.pool:
            thread.start()


def _task():
    for i in range(2):
        print('this is a _task. i = {}. thread id = {}'.format(i, threading.get_native_id()))
        time.sleep(1)


if __name__ == '__main__':
    pool = SimpleThreadPool(10)
    pool.start()
    for i in range(10):
        pool.submit(_task)
