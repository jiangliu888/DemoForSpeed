# -*- coding: UTF-8 -*-
import struct
import array

f = open('test.wav', 'rb')
# 读取文件前44个字节的数据
info = f.read(44)
# 解析二进制数据--声道数
print struct.unpack('h', info[22:24])
# WAV文件中data部分的大小 / 数据类型的大小 -> buffer的大小
f.seek(0, 2)
n = (f.tell() - 44) / 2
buf = array.array('h', (0 for _ in xrange(n)))
# 将数据读至buf中
f.seek(44)
f.readinto(buf)
for i in xrange(n):
    # 数据处理，相当于将音频文件的声音变小
    buf[i] /= 8

f.close()
# 创建demo.wav
f = open('demo.wav', 'wb')
# 将test.wav中前44个字节的数据写入文件
f.write(info)
# 将buf中的数据写入文件
buf.tofile(f)
f.close()
