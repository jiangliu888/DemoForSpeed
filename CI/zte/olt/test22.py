# -*- coding: UTF-8 -*-
""" class Rectangel:
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

rect1 = Rectangel(5,3)
rect2 = Rectangel(4,4)
rect1.area() > rect2.area() """
""" 
class Rectangel:
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __lt__(self,obj):
        print('in__lt__')
        return self.area() < obj.area()

    def __le__(self,obj):
        print('in__le__')
        return self.area() <= obj.area()
rect1 = Rectangel(5,3)
rect2 = Rectangel(4,4)

print(rect1 < rect2) 
print(rect1 <= rect2) """


from functools import total_ordering
from abc import ABCMeta, abstractmethod

"""  把运算符重载的函数都放到公共的抽象基类中，这样可以避免其他的类都要写运算符的函数，
 其他的函数中只要实现area()的方法就可以了
 再定义一个抽象的接口，能比较的都要实现这个area,否则不能进行比较 """
@total_ordering
class Shape(object): 
    
    def area(self):   # 描述一下抽象的接口，它的子类都要实现这个接口
        pass

    def __lt__(self,obj):
        print('in__lt__')
        if not isinstance(obj,Shape):
            raise TypeError('obj is not Shape')
        return self.area() < obj.area()

    def __eq__(self,obj):
        if not isinstance(obj,Shape):
            raise TypeError('obj is not Shape')
        print('in__eq__')
        return self.area() == obj.area()

#继承
class Rectangel(Shape):
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self,r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14

rect1 = Rectangel(5,3)
rect2 = Rectangel(4,4)
c1 = Circle(3)

print(rect1 < c1)
print(c1 > rect2)
print(rect1 < rect2) # rect1.__lt__(rect2)
print(rect1 >= rect2)