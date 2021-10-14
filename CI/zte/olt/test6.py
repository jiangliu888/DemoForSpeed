# -*- coding: UTF-8 -*-
#zero, one, two, three, fous, five, six, seven, eight, nine = range(10)
 
'''
如何让字典保持有序
实际案例：
    某编程竞赛系统，对参赛选手编程进行计时，选手完成题目后，把
    该选手解题用时记录到字典中，以便按选手名查询成绩。1
比赛结束后，需要按照选手成绩来打印成绩。
'''
'''解决方案：
        使用collections.OrderedDict
        以OrderedDict替代内置Dict，一次将选手成绩存入OrderedDict'''
# 首先创建选手
from collections import OrderedDict
from time import time
from random import randint
players = list('ABCDEFGH')
start = time()#考试开始时间
PlayersTime = OrderedDict()# 创建一个有序的字典
for i in range(8):
    # 等待一个选手的输入就等于一个选手的考试结束的
    Userinput = input("请输入>>:")
    #输入以后这个选手就离场
    p = players.pop(randint(0,7-i))
    # 结束的时间
    end = time()
    # 打印每个选手考完试的信息
    print(i+1,p,'%.3f'% (end-start))
    PlayersTime[p] = (i+1,'%.3f'% (end-start))
#print(PlayersTime)
for key in PlayersTime:
    print(key,PlayersTime[key]) 