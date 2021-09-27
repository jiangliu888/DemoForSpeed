# -*- coding: UTF-8 -*-

import hashlib
from PIL import Image,ImageFile
from scipy import signal
from modules.base import BaseModule

class Hasher(BaseModule):
    """  给文件做md5加密 """
          
    def _process(self,item):
        #卷积
        cov = [[[0.1],[0.05],[0.1]]]
        img = signal.convolve(item,cov)
        img = Image.fromarray(img.astype('uint8')).convert('RGB')
        #哈希
        md5 = hashlib.md5(str(img).encode('utf-8')).hexdigest()
        return md5

    
    def _process_singlethread(self,list_info):
        #获取图片
        md5_list = []
        for img in list_info:
            md5 = self._process(img)
            md5_list.append(md5)
        return md5_list     