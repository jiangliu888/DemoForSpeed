# -*- coding: UTF-8 -*-
def f00():
    print("===")
    while True:
        res = yield 4
        print("res:",res)
# g = f00()
# print(next(g))
# print("*********")
# print(next(g))

# g = f00()
# print(next(g))
# print("*"*20)
# print(g.send(7))

class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step 
    def __iter__(self):
        t.self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step
for x in reversed(FloatRange(1, 20, 2)):
    print(x)
