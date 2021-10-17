# -*- encoding=utf-8 -*-


import time
import threading
from concurrent.futures import ThreadPoolExecutor


def _task():
    for i in range(2):
        print('this is a _task. i = {}. thread id = {}'.format(i, threading.get_native_id()))
        time.sleep(1)
    return time.time()


tp = ThreadPoolExecutor(10)

futures = []
for i in range(10):
    # future对象
    future = tp.submit(_task)
    futures.append(future)
    
for future in futures:
    print(future.result())