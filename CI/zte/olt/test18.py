# -*- coding: UTF-8 -*-

""" __new__() 是一种负责创建类实例的静态方法
    它无需使用 staticmethod 装饰器修饰，且该方法会优先 __init__() 初始化方法被调用 
    覆写 __new__() 的实现将会使用合适的参数调用其超类的 super().__new__()，并在返回之前修改实例"""
class IntTuple(tuple):
    #先于__init__被调用\# cls为类对象的父类，在python中类也是对象
    def __new__(cls,iterable):
        g = (x for x in iterable if isinstance(x,int) and x>0)
        # 返回一个类对象，这个类对象传给下面__init__()方法中的self
        return super(IntTuple,cls).__new__(cls,g)

    def __init__(self,iterable):
        super(IntTuple,self).__init__(iterable)

t = IntTuple([1,-1,'abc',6,['x','y'],3])
print t