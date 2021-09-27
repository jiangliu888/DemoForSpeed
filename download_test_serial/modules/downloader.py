# -*- coding: UTF-8 -*-
""" 
变量
1.  前带_的变量:  标明是一个私有变量, 只用于标明, 外部类还是可以访问到这个变量  _private_value
2.  前带两个_ ,后带两个_ 的变量:  标明是内置变量,
3.  大写加下划线的变量:  标明是不会发生改变的全局变量  USER_CONSTANT
函数:
1.  前带_的变量: 标明是一个私有函数, 只用于标明,
2.  前带两个_ ,后带两个_ 的函数:  标明是特殊函数 """

import requests
from PIL import Image,ImageFile
import numpy as np

from const import CalcType
from modules.base import BaseModule

class Downloader(BaseModule):
    
    def __init__(self):
        # 继承BaseModule的初始化方法
        super(Downloader,self).__init__()
          
    def _process(self,url):
        print('url:{}'.format(url))
        response = requests.get(url)
        content = response.content
        #图片转numpy数组        
        parser = ImageFile.Parser()
        parser.feed(content)
        img = parser.close()
        img = np.array(img)
        return img
    
    def _process_singlethread(self,list_info):
        response_list = []
        for url in list_info:
            img = self._process(url)
            response_list.append(img)
        return response_list