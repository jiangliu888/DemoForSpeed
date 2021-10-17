# -*- encoding=utf-8 -*-
# 服务端

import socket


# 1. 创建套接字
server = socket.socket()
print('server.fileno:', server.fileno())

# 2. 绑定套接字
server.bind(('127.0.0.1', 8999))

# 3. 监听套接字
server.listen(1)

# 4. 接受连接
s, addr = server.accept()
print('s.fileno:', s.fileno())

print('connect addr:', addr)

while True:
    # 接受信息
    content = s.recv(1024)
    if not content:
        break
    # 发送信息
    s.send(content.upper())
    print('server recv content:', content)
