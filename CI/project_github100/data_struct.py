# -*- coding: UTF-8 -*-
import random
""" 生成验证码 """
def generate_code(code_len = 4):

    all_char  = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_char)-1
    code = ''

    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code +=all_char[index]
    return code
print(generate_code())

def get_suffix(filename,has_dot=False):
    
    pos = filename.rfind('.')
    if 0 < pos <len(filename)-1:
        index = pos if has_dot else pos+1
        return filename[index:]
    else:
        return ''