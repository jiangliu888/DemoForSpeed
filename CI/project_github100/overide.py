# -*- coding: UTF-8 -*-
from random import randint

def add(a=0,b=0,c=0):
    return a+b+c

print(add())
print(add(1))
print(add(1,2))


def add1(*args):
    total = 0 
    print(args)
    for val in args:
        total += val
    return total

print(add1(1,2,3,4,5,6))