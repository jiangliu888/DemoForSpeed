# -*- coding: UTF-8 -*-
import time
import os

class Timer:
    """ 计时器 """
    def __init__(self):
        self.val = 0
    
    def tick(self):
        self.val = time.time()

    def tock(self):
        return round(time.time() - self.val,6)


def urllist():
    list_file = os.path.join('piclist/baidu.txt')
    url_list = []
    with open(list_file,'r') as f:
        url_list = [line.strip() for line in f]
    return url_list[:1]