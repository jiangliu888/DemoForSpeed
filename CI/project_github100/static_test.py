# -*- coding: UTF-8 -*-
from math import sqrt

class Triangle(object):

    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_vaild(a,b,c):
        return a+ b > c and b+c > a and a+c >b

    def parimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.parimeter() / 2
        return sqrt(half * (half - self._a)*(half - self._b)*(half - self._c))

def main():
    a,b,c = 3,4,5
    if Triangle.is_vaild(a,b,c):
        t = Triangle(a,b,c)
        print(t.parimeter)
        print(t.area)
    else:
        print('error')

if __name__=='__main__':
    main()