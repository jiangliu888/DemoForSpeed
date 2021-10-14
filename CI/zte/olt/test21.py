# -*- coding: UTF-8 -*-
from math import pi

class Circle(object):
    def __init__(self,radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('wrong type')
        self.radius = float(value)

    def getArea(self):
        return self.radius ** 2 * pi
    # 第一个参数为c.R的时候调用的方法，第二个参数为c.R=xxx时调用的方法
    R = property(getRadius, setRadius)

c = Circle(3.2)
print(c.R)
#会报错
c.R = 'abc'
print(c.R)