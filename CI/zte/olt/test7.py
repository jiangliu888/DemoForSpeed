# -*- coding: UTF-8 -*-
from collections import deque
from random import randint
import pickle
history = deque([],5)
N = randint(0,100)

def guess(k):
    if k == N:
        return True
    elif k<N:
        print("%s 小了" % k)
    else:
        print("%s 大了" % k)
    return False
while True:
    print('pls input number or h')
    line = input(">>:")
    pickle.dump(line,open('history','w'))
    if line.isdight():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'h':
        print(list(history))