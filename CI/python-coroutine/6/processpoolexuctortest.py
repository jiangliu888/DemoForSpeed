# -*- encoing=utf-8 -*-


import os
import time
from concurrent.futures import ProcessPoolExecutor


pp = ProcessPoolExecutor(10)


def _task():
    for i in range(2):
        print('this is a _task. i = {}. process id = {}'.format(i, os.getpid()))
        time.sleep(1)
    return time.time()

futures = []
for i in range(10):
    future = pp.submit(_task)
    futures.append(future)

for future in futures:
    print(future.result())
