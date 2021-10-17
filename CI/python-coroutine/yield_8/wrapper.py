# -*- encoding=utf-8 -*-


class CoroutineWrapper():
    def __init__(self,loop,gen):
        self.loop = loop
        self.gen = gen
        self.context = None

    def send(self,val):
        val = self.gen.send(val)
        self.context = val
        self.loop.add_runnables(self)

    def __next__(self):
        val = next(self.gen)
        self.context = val
        self.loop.add_runnables(self)

    def throw(self,tp,*rest):
        return self.gen.throw(tp,*rest)

    def __getattr__(self,name):
        return getattr(self.gen,name)

    def close(self):
        return self.gen.close()

    def __str__(self):
        return 'coroutinewrapper:{},context:{}'.format(self.gen,self.context)


    

