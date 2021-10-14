# -*- coding: UTF-8 -*-
# 生成器对象也是可迭代对象，即拥有__iter__、next()
class PrimeNumber:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def isPrimeNum(self,k):
        if k < 2:
            return False
        for i in range(2,k):
            if k % i== 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start,self.end):
            if self.isPrimeNum(k):
                yield k
for x in PrimeNumber(1,100):
    print x