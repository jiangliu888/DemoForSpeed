# -*- coding: UTF-8 -*-

from const import CalcType

class BaseModule:
    
    def __init__(self):
        self.calc_type = CalcType.SingleThread
    
    def set_calc_type(self, type_):
        self.calc_type = type_

    def _process_singlethread(self,list_info):
        #调用父类时，抛出异常
        raise NotImplementedError
       
    def _process(self,url):
        raise NotImplementedError
    
    def process(self,list_info):
        if self.calc_type == CalcType.SingleThread:
            return self._process_singlethread(list_info)
        elif self.calc_type == CalcType.MultiThread:
            return self._process_multithread(list_info)

    def _process_multithread(self, list_info):
        raise NotImplementedError