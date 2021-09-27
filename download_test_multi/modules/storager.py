# -*- coding: UTF-8 -*-

from PIL import Image,ImageFile
from modules.base import BaseModule
from modules.executor import thread_pool_executor as tp

class Storager(BaseModule):

    def _process(self,item):

        content,path = item
        print('path:{}'.format(path))
        content = Image.fromarray(content.astype('uint8')).convert('L')
        content.save(path)

    def _process_singlethread(self,list_info):

        for item in list_info:
            self._process(item)

    def _process_multithread(self, list_info):
        task_list = []
        for item in list_info:
            task = tp.submit(self._process,(item))
            task_list.append(task)
        for task in task_list:
            task.result()
            
         
