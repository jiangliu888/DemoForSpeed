# -*- coding: UTF-8 -*-

from const import CalcType

class BaseModule:
    
    def __init__(self):
        self.calc_type = CalcType.SingleThread
    
    def _process_singlethread(self,list_info):
        #调用父类时，抛出异常
        raise NotImplementedError
       
    def _process(self,url):
        raise NotImplementedError
    
    def process(self,list_):
        if self.calc_type == CalcType.SingleThread:
            return self._process_singlethread(list_)
        else:
            pass