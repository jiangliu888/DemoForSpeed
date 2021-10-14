# -*- coding: UTF-8 -*-
import re

def mysplit(s,ds):
    res = list(s)
    for i in ds:
        t = []
        map(lambda x:t.extend(x.split(i)),res)
        res = t
    return [x for x in res if x]
s='ab;cd|ef+hi,/ds\tef;sd fe.usad\txyz'
print(mysplit(s,';|/,.\t'))

print(re.split(r'[;|/,.\t+ ]+',s))

 