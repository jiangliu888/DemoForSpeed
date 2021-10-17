# -*- encoding=utf-8 -*-


import hashlib

from scipy import signal
from PIL import Image, ImageFile

from modules.base import BaseModule
from modules.executors import thread_pool_executor as tp
from modules.executors import process_pool_executor as pp


class Hasher(BaseModule):
    """哈希模块
    """

    def _process(self, item):
        # 卷积
        cov = [[[0.1], [0.05], [0.1]]]
        img = signal.convolve(item, cov)
        img = Image.fromarray(img.astype('uint8')).convert('RGB')
        # 哈希
        md5 = hashlib.md5(str(img).encode('utf-8')).hexdigest()
        return md5

    def _process_singlethread(self, list_):
        md5_list = []
        for img in list_:
            md5 = self._process(img)
            md5_list.append(md5)
        return md5_list

    
    def _process_multithread(self, list_):
        md5_list = []
        task_list = []
        for img in list_:
            task = tp.submit(self._process, (img))
            task_list.append(task)
        for task in task_list:
            md5 = task.result()
            md5_list.append(md5)
        return md5_list

    def _process_multiprocess(self, list_):
        md5_list = []
        task_list = []
        for img in list_:
            task = pp.submit(self._process, (img))
            task_list.append(task)
        for task in task_list:
            md5 = task.result()
            md5_list.append(md5)
        return md5_list

    def _process_coroutine(self, list_):
        return self._process_multithread(list_)
    