# -*- coding: UTF-8 -*-
# def foo():
#     b='bbb'

#     def fo():
#         a = "acc"
#         print(a)
#         print(b)

#     fo()

# if __name__ =='__main__':
#     a = 'aaa'
#     foo()

class A(object):
    num = "类属性"
    
    def func1(self): # self : 表示实例化类后的地址id
        print("func1")
        print(self)
    @classmethod    
    def func2(cls):  # cls : 表示没用被实例化的类本身
        print("func2")
        print(cls)
        print(cls.num)
        cls().func1()

A.func2()