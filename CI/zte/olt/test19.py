# -*- coding: UTF-8 -*-
class Player(object):
    def __init__(self,uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

class Player2(object):
    # 声明类实例化对象所有的属性名，禁止实例属性的动态绑定。即该实例没有了__dict__属性。
    __slots__ = ['uid','name','stat','level'] 
    def __init__(self,uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level