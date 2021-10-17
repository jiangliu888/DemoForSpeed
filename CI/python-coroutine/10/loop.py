# -*- encoding=utf-8 -*- 

import socket
import select
from queue import deque

class Future:
    """可等待对象 Future
    """

    def __init__(self, loop):
        self.loop = loop
        self.done = False
        self.co = None

    def set_coroutine(self, co):
        self.co = co

    def set_done(self):
        """设置已完成
        """
        self.done = True

    # 生成器 __next__() next(gen)
    # await <可等待对象>
    def __await__(self):
        if not self.done:
            # 让出CPU
            yield self
        return

    
class SocketWrapper:
    """套接字协程适配器
    """

    def __init__(self, sock, loop):
        sock.setblocking(False)
        self.sock = sock
        self.loop = loop

    def fileno(self):
        return self.sock.fileno()

    def create_future_for_events(self, events):
        """
        1. 为套接字创建future
        2. register_handler
        """
        future = self.loop.create_future()

        def handler():
            # 可等待对象完成
            future.set_done()
            self.loop.unregister_handler(self.fileno())
            if future.co:
                # 继续调度
                self.loop.add_coroutine(future.co)

        self.loop.register_handler(self.fileno(), events, handler)
        return future

    async def accept(self):
        while True:
            try:
                sock, addr = self.sock.accept()
                return SocketWrapper(sock=sock, loop=self.loop), addr
            except BlockingIOError:
                future = self.create_future_for_events(select.EPOLLIN)
                # 让出CPU
                await future

    async def recv(self, backlog):
        while True:
            try:
                return self.sock.recv(backlog)
            except BlockingIOError:
                future = self.create_future_for_events(select.EPOLLIN)
                await future
        
    async def send(self, data):
        while True:
            try:
                return self.sock.send(data)
            except BlockingIOError:
                future = self.create_future_for_events(select.EPOLLOUT)
                await future


class EventLoop:

    current = None
    runnables = deque()
    epoll = select.epoll()
    handlers = {}

    @classmethod
    def instance(self):
        if not EventLoop.current:
            EventLoop.current = EventLoop()
        return EventLoop.current

    def create_future(self):
        return Future(loop=self)

    def create_listen_socket(self, ip='localhost', port=8999):
        """创建listen的套接字
        """
        sock = socket.socket()
        # 可以重用地址
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((ip, port))
        sock.listen()
        return SocketWrapper(sock=sock, loop=self)

    def register_handler(self, fileno, events, handler):
        self.handlers[fileno] = handler
        self.epoll.register(fileno, events)

    def unregister_handler(self, fileno):
        self.epoll.unregister(fileno)
        self.handlers.pop(fileno)

    def run_coroutine(self, co):
        try:
            # 生成器 send 一样
            # 进行协程的一次调度
            future = co.send(None)
            future.set_coroutine(co)
        except Exception as e:
            print(e)
            print('coroutine {} stopped'.format(co.__name__))

    def run_forever(self):
        while True:
            while self.runnables:
                self.run_coroutine(co=self.runnables.popleft())

            events = self.epoll.poll(1)
            for fileno, event in events:
                # 回调
                handler = self.handlers.get(fileno)
                handler()

    def add_coroutine(self, co):
        self.runnables.append(co)


class TCPServer:

    def __init__(self, loop):
        self.loop = loop
        self.listen_sock = self.loop.create_listen_socket()
        self.loop.add_coroutine(self.serve_forever())
    
    async def handle_client(self, sock):
        while True:
            data = await sock.recv(1024)
            if not data:
                print('client disconnected')
                break
            await sock.send(data.upper())


    async def serve_forever(self):
        while True:
            sock, addr = await self.listen_sock.accept()
            print('client connect addr = {}'.format(addr))
            self.loop.add_coroutine(self.handle_client(sock))


if __name__ == '__main__':
    loop = EventLoop.instance()
    server = TCPServer(loop)
    loop.run_forever()
    