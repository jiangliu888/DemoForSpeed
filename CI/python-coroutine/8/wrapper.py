# -*- encoding=utf-8 -*-


class CoroutineWrapper:
    """生成器协程适配器
    重写生成器的方法：send、next
    使得生成器可以在调度器loop里面去执行
    """

    def __init__(self, loop, gen):
        # YieldLoop
        self.loop = loop
        # 生成器
        self.gen = gen
        # 生成器上下文
        self.context = None
        pass

    def send(self, val):
        """重写生成器的send方法
        """
        val = self.gen.send(val)
        self.context = val
        self.loop.add_runnables(self)
    
    def throw(self, tp, *rest):
        return self.gen.throw(tp, *rest)

    def close(self):
        return self.gen.close()
        
    def __next__(self):
        val = next(self.gen)
        self.context = val
        self.loop.add_runnables(self)

    def __getattr__(self, name):
        return getattr(self.gen, name)

    def __str__(self):
        return 'coroutinewrapper: {}, context: {}'.format(self.gen.__name__, self.context)