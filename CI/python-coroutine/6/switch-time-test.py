# -*- encoding = utf-8 -*-
# 上下文切换成本测试
#

import queue
import threading
from multiprocessing import Queue, Process

def test_process_context_switch():
    """多进程上下文切换成本的测试
    """
    
    def pass_token1(queue1, queue2):
        for i in range(100000):
            queue2.put(0)
            queue1.get()


    def pass_token2(queue1, queue2):
        for i in range(100000):
            queue1.put(1)
            queue2.get()


    queue1 = Queue()
    queue2 = Queue()
    p1 = Process(target=pass_token1, args=(queue1, queue2))
    p2 = Process(target=pass_token2, args=(queue1, queue2))
    p1.start()
    p2.start()


def test_thread_context_switch():
    """多线程上下文切换成本的测试
    """
    
    def pass_token1(queue1, queue2):
        for i in range(100000):
            queue2.put(0)
            queue1.get()


    def pass_token2(queue1, queue2):
        for i in range(100000):
            queue1.put(1)
            queue2.get()


    queue1 = queue.Queue()
    queue2 = queue.Queue()
    t1 = threading.Thread(target=pass_token1, args=(queue1, queue2))
    t2 = threading.Thread(target=pass_token2, args=(queue1, queue2))
    t1.start()
    t2.start()


if __name__ == '__main__':
    # test_process_context_switch()
    test_thread_context_switch()