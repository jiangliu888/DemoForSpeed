# -*- coding: UTF-8 -*-
from itertools import islice
class FloatRange:
    def __init__(self,start,end,step=0.1):
        self.start = start
        self.end = end
        self.step = step 
    def __iter__(self):
        t.self.start
        while t <= self.end:
            yield t
            t +=self.step
    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -=self.step
for x in reversed(FloatRange(1,20,2)):
    print 10


list0 = list(range(1,20))
for x in islice(list0,1,10):
    print(x)#截取到的数据是[6,7,8,9,10]