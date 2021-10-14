# -*- coding: UTF-8 -*-

import weakref

# 下面构造两个类，他们互相引用
class Data(object):
    
    def __init__(self,value,owner):
        self.owner = weakref.ref(owner)  # 使用弱引用的方法，不增加计数
        self.value = value

    def __str__(self):
        return "%s's data,value is %s" % (self.owner(),self.value)

    def __del__(self):
        print('in Data.__del__')

class Node(object):
    
    def __init__(self,value):
        self.data = Data(value,self)

    def __del__(self):
        print('in Node.__del__')

node = Node(100)
del node        # 可以看到对象都被回收掉了
input('wait....')
