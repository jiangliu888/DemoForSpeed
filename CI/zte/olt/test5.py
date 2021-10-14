# -*- coding: UTF-8 -*-
from random import randint,sample

""" sample()是random 模块中的一个函数
表达式为 random.sample(sequence, k)
它的作用是从指定序列中随机获取指定长度的片断并随机排列，结果以列表的形式返回 """
def get_s(player):
    s1 = {k:randint(1,6) for k in sample(player,randint(3,6))}
    s2 = {k:randint(1,6) for k in sample(player,randint(3,6))}
    s3 = {k:randint(1,6) for k in sample(player,randint(3,6))}
    return s1,s2,s3

def public_keys(s1,s2,s3):
    res = []
    for key in s1:
        if key in s2 and key in s3:
            res.append(key)
    return res

if __name__ == '__main__':
    player = 'abcdef'
    s1,s2,s3 = get_s(player)
    print(public_keys(s1,s2,s3))