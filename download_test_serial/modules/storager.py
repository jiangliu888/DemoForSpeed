# -*- coding: UTF-8 -*-

from PIL import Image,ImageFile
from modules.base import BaseModule

class Storager(BaseModule):

    def _process(self,item):

        content,path = item
        print('path:{}'.format(path))
        content = Image.fromarray(content.astype('uint8')).convert('L')
        content.save(path)

    def _process_singlethread(self,list_info):

        for item in list_info:
            self._process(item)