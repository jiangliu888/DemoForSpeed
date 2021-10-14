# -*- coding: UTF-8 -*-
""" 
将函数视为“一等公民”
    函数可以赋值给变量
    函数可以作为函数的参数
    函数可以作为函数的返回值 """

def add(x,y):
    z=x+y
    print z

a=add(3,4)
print(add(3,4))
print(a)