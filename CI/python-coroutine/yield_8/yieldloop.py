# -*- encoding=utf-8 -*-
from queue import deque
from wrapper import CoroutineWrapper
import functools
import inspect

def coroutine(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        gen = func(*args,**kwargs)
        if inspect.isgenerator(gen):
            coro = CoroutineWrapper(YieldLoop.isinstance,gen)
            return coro
        else:
            raise RuntimeError('[CoroutineWrapper] error. \
                type({}) is not support'.format(type(gen)))
    
    return wrapper



class YieldLoop():

    runnables =deque()
    current = None
    @classmethod
    def instance(cls):
        if not YieldLoop.current:
            YieldLoop.current = YieldLoop()
        return YieldLoop.current

    def add_coroutine(self,coro):
        assert isinstance(coro,CoroutineWrapper),'isinstance(roro)!=CoroutineWrapper'
        self.runnables.append(coro)

    def run_until_complete(self):
        while YieldLoop.runnables:
            coro = YieldLoop.runnables.pop()
            self.run_coroutine(coro)
    
    def run_coroutine(self,coro):
        try:
            coro.send(coro.context)
        except StopIteration as e:
            print("corotine {} stop".format(coro))

    def add_runnables(self,coro):
        self.runnables.append(coro)

