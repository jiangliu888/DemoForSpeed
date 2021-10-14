# -*- coding: UTF-8 -*-
# 方法一
s = '  abc  123             '
print s.strip()  # 去掉两端的空格
print s.lstrip()  # 去掉左端的空格
print s.rstrip()  # 去掉右端的空格

s = '---abc+++'
print s.strip('-+')  # abc

# 方法二
s = 'abc:123'
print s[:3] + s[4:]  # abc123

# 方法三
# 只能替换单个字符
s = '\tabc\t123\txyz'
print s.replace('\t', '')  # abc123xyz
# 可以替换多个不同字符
import re
s = '\tabc\t123\txyz\rwe\r'
print re.sub('[\t\r]', '', s)  # abc123xyzwe

#方法四
# 将abc替换成xyz，将xyz替换成abc，做成一个加密的效果
import string
s = 'abc1234324xyz'
print s.translate(string.maketrans('abcxyz', 'xyzabc'))  #xyz1234324abc

s = 'abc\refg\n234\t'
print s.translate(None, '\t\r\n')  # abcefg234


# unicode 字符串
u = u'ni\u0301 ha\u030c, chi\u0304 fa\u0300n'
print u.translate({0x0301: None})  # ni hǎ, chī fàn  去掉了ni 上面的音调符号
print u.translate(dict.fromkeys([0x0301, 0x030c, 0x0304, 0x0300]))  # ni ha, chi fan  去掉了所有的音调符号