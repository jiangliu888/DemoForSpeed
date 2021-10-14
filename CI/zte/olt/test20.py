# -*- coding: UTF-8 -*-
from telnetlib import Telnet
from sys import stdin,stdout
from collections import deque
class TelnetClient(object):
    def __init__(self,addr,port=23):
        self.addr = addr
        self.port = port
        self.tn = None  # 初始化构造的时候，为空

    def start(self):
       # raise Exception('Text')  # 手动产生一个异常，测试在异常的情况下，程序仍然能够正常退出
        t = self.tn.read_until('login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)
        # password，输入密码
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]): t = t[len(user) + 1:] # 实际注释这行也是Ok的
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until('$ ')
        stdout.write(t) # 在屏幕输出$，可以理解成print
        while True:
            uinput = stdin.readline() # 获取用户在命令行$后输入的命令，可以理解成input
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput) # 执行命令
            t = self.tn.read_until('$ ')# 读取直到遇到了给定的字符串expected或超时秒数。
            stdout.write(t[len(uinput) + 1:])
           # stdout.write(t)
    def cleanup(self):
        """ self.tn.close()
        self.tn = None """

    def __enter__(self):
        self.tn = Telnet(self.addr,self.port)  # telnet的连接对象
        self.history = deque()  # 创建一个队列，来存储telnet操作的历史记录
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
       # print 'In exit'
        self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt','w') as f:
            f.writelines(self.history)  # 写入用户的操作历史记录
        # return True  # 可以压制with语句中的异常，使在外面捕获不到，即END可以成功打印

# 通过上下文管理器来调用,client是__enter__的返回值
with  TelnetClient('127.0.0.1') as client:
    client.start()