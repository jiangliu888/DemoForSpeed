# -*- encoding=utf-8 -*-
# 客户端

import socket


client = socket.socket()
print('client.fileno:', client.fileno())

client.connect(('127.0.0.1', 8999))

while True:
    content = input('>>>')
    client.send(bytes(content, 'utf-8'))
    content = client.recv(1024)
    print('client recv content:', content)
