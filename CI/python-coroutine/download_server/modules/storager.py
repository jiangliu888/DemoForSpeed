# -*- encoding=utf-8 -*-


from PIL import Image

from modules.base import BaseModule
from modules.executors import thread_pool_executor as tp
from modules.executors import process_pool_executor as pp


class Storager(BaseModule):
    """存储模块
    """

    def _process(self, item):
        content, path = item
        print('save path: {}'.format(path))
        content = Image.fromarray(content.astype('uint8')).convert('RGB')
        content.save(path)

    def _process_singlethread(self, list_):
        # item =(content, path)
        for item in list_:
            self._process(item)

    def _process_multithread(self, list_):
        task_list = []
        for item in list_:
            task = tp.submit(self._process, (item))
            task_list.append(task)
        for task in task_list:
            task.result()
        
    def _process_multiprocess(self, list_):
        task_list = []
        for item in list_:
            task = pp.submit(self._process, (item))
            task_list.append(task)
        for task in task_list:
            task.result()

    def _process_coroutine(self, list_):
        return self._process_multithread(list_)
