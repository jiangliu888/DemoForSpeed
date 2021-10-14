# -*- coding: UTF-8 -*-

s1 = '\'hello,world!\''
s2 = '\n\\hello,world!\\\n'
print s1,s2

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print s1,s2

#不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r
s1 = r'\'hello,world!\''
s2 = r'\n\\hello,world!\\\n'
print s1,s2

str1 = 'Ai !'
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(20, ' '))
str2='abc1234'
# 检查字符串是否由数字构成
print(str2.isdigit())
# 检查字符串是否以字母构成
print(str2.isalpha())
# 检查字符串是否以数字和字母构成
print(str2.isalnum())


