# -*- encoding=utf-8 -*-


import inspect
import functools
from queue import deque

from wrapper import CoroutineWrapper


def coroutine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        # 判断gen是不是生成器
        if inspect.isgenerator(gen):
            coro = CoroutineWrapper(YieldLoop.instance(), gen)
            return coro
        else:
            raise RuntimeError('[CoroutineWrapper] error. \
                type({}) is not supported.'.format(type(gen)))
    return wrapper


class YieldLoop:

    current = None
    runnables = deque()

    # 单例模式
    @classmethod
    def instance(cls):
        if not YieldLoop.current:
            YieldLoop.current = YieldLoop()
        return YieldLoop.current

    def add_runnables(self, coro):
        self.runnables.append(coro)

    def add_coroutine(self, coro):
        """添加协程到调度器
        """
        # 对类型进行判断
        assert isinstance(coro, CoroutineWrapper), 'isinstance(coro) != CoroutineWrapper'
        self.add_runnables(coro)
        
    def run_coroutine(self, coro):
        """执行协程
        """
        try:
            # print('run coro:', coro)
            coro.send(coro.context)
            # next(coro)
        except StopIteration as e:
            print('coroutine {} stop.'.format(coro))

    def run_until_complete(self):
        while YieldLoop.runnables:
            # print('runnables:', YieldLoop.runnables)
            coro = YieldLoop.runnables.popleft()
            self.run_coroutine(coro)