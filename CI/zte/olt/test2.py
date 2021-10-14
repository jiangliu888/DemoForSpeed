# -*- coding: UTF-8 -*-
from random import randint
""" randint 包含左右索引，生成一个随机整数
range包含左索引，不包含右索引，生成一个列表。 """
""" _ 变量是临时变量，只用一次
for i in range 做了两件事 ，把值赋给i的同时，也会赋给_ ，而前者只赋给_ """
data = [randint(-10,10) for _ in range(10)]
#常规操作
res = []
for x in data:
    if x>0:
        res.append(x)
print res
#filter
data1=filter(lambda x:x>=0,data)
print data1
#列表解析
data2=[x for x in data if x>=0]
print data2 
d = {x: randint(20,100) for x in range(1,20)}
d1 = {k:v for k,v in d.iteritems() if v>80}
print d1

s = set(data)
s1 = {x for x in s if x%3 ==0}
print s1