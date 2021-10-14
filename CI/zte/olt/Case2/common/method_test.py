#!/usr/bin/env python
# coding:utf-8
import re
import time

def test_Exec_Many(login,m_cmd, exec_wait):
    ssh = login.invoke_shell()
    print("命令输入")
    for v_cmd in m_cmd:
        ssh.send(v_cmd + '\n')
        time.sleep(exec_wait)
    result = ssh.recv(65535)
    f = open('D:/2020/15_Coding/test.txt','w')
    newResult = re.sub(r' --More--         ', '', result)
    f.writelines(newResult)
    f.close()
    return result

def sshGetONUInfo(str):
        val = re.findall(r'ONU Number: (\S+)/64', str)
        time.sleep(1)
        print(val)
        return val