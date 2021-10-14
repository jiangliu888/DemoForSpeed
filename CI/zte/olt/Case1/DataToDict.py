#!/usr/bin/env python
# coding:utf-8
import xlrd
import data_config
import paramiko
from paramiko.py3compat import u
import time
import re
from functools import wraps
import numpy as np
np.set_printoptions(threshold=np.inf)
import pytest


class SSHClient1(object):    
    def __init__(self):
        self.readValue = data_config.Read_Excel()
        
    def close(self, ssh):
        ssh.close()
    
    def sshConnection(self, v_username, v_password, v_ip, v_port=22):
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 把要连接的机器添加到known_hosts文件中
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=v_ip, port=v_port, username=v_username, password=v_password)
        return ssh

    def sshGetGMKInfo(self, str):
        val = re.findall(r'TxPower        :\s+(.*)\s+', str)
        time.sleep(1)
        print(val)
        return val

    def sshGetONUInfo(self, str):
        val = re.findall(r'ONU Number: (\S+)/64', str)
        time.sleep(1)
        print(val)
        return val

    def sshExecByMany(self, s, m_cmd, exec_wait, exit_wait):
        ssh = s.invoke_shell()
        for v_cmd in m_cmd:
            ssh.send(v_cmd + '\n')
            time.sleep(exec_wait)
            # if v_cmd == 'exit':
            #     time.sleep(exit_wait)
        result = u(ssh.recv(65535))
        f = open('D:/2020/15_Coding/vscode/1.txt','w')
        # 优化log显示内容
        newResult = re.sub(r' --More--         ', '', result)
        f.writelines(newResult)
        f.close()
        return result    
    
    #F001:onu 开关操作
    def Run_shutdown(self):
        for i in range(1,30):
            m0_cmd = ['configure terminal'+'\n',
                  self.readValue.get_olt_if(),
                 self.readValue.do_onu_shutdown]
            m1_cmd = [self.readValue.do_show_onu_working()+ '\n'*110]
            print(self.readValue.do_show_onu_working())
            m2_cmd = [self.readValue.do_optical_module_info() + '\n'*22]
            #执行shutdown
            getClient.sshExecByMany(ssh, m0_cmd, 1, 1)
            #判断流程
            result1 = getClient.sshExecByMany(ssh, m1_cmd, 3, 1)
            InfoValue = getClient.sshGetONUInfo(result1)
            print(len(InfoValue))
            if InfoValue[0] == '0':
                print("All onu is working")
            else:
                print("ONU numeber is wrong")
                continue
            result2 = getClient.sshExecByMany(ssh, m2_cmd, 3, 1)
            print(result2)
            InfoValue1 = getClient.sshGetGMKInfo(result2)
            if InfoValue1[0] == 'N/A':
                print("GMK is shutdown")
            else:
                print("GMK is no shutdown")
                continue            
            time.sleep(10)
            m3_cmd = [self.readValue.do_onu_no_shutdown]
            #执行no shutdown
            result3 = getClient.sshExecByMany(ssh, m3_cmd, 1, 1)
            time.sleep(300)
            result4 = getClient.sshExecByMany(ssh, m1_cmd, 3, 1)
            InfoValue = getClient.sshGetONUInfo(result4)
            if InfoValue[0] == self.readValue.get_onu_sum():
                print("All onu is working")
            else:
                print("ONU numeber is wrong")
                continue
            result5 = getClient.sshExecByMany(ssh, m2_cmd, 3, 1)
            print(result5)
        getClient.close(ssh)
    #F002: onu restore 操作
    def Run_ONU_Store(self):
        num = 0
        while num <= self.readValue.get_onu_sum():           
            m0_cmd = ['configure terminal'+'\n',
                  self.readValue.get_mng_if(num),
                  self.readValue.do_onu_restore(),
                  self.readValue.do_exit()]
            #执行命令
            num += 1 
            result1 = getClient.sshExecByMany(ssh,m0_cmd,1,1)
            print(result1)
        else:
            print("执行结束")
        getClient.close(ssh)
    #F003: 光模块Power on操作
    def Run_GMK_Power(self):
         mutiCmdOpen = ['diag'+'\n',self.readValue.do_diag_cmd0(),'exe shell 0','exe admin', 'exe sh ftm',
                 self.readValue.do_diag_cmd1()]
        mutiCmdClose = ['diag'+'\n',self.readValue.do_diag_cmd0(), 'exe shell 0','exe admin','exe sh ftm',
                 self.readValue.do_diag_cmd1()]
        oneCmd = [self.readValue.do_show_onu_working()+'\n']
        
        for i in range(300):
            # ONU状态判断         
            showCmdResult0 = getClient.sshExecByOne(ssh, oneCmd, 2, 2)
            InfoValue = getClient.sshGetInfo(showCmdResult0)
            print(int(InfoValue[0]))
            print("ONU number is Info"+ ' '+ InfoValue[0])
            if (InfoValue != ' ' and int(InfoValue[0]) >= self.readValue.get_onu_sum()):
                print("All onu is working,next step is close the GMK")
                # close
                showCmdClose = getClient.sshExecByMany(ssh, mutiCmdClose, 1, 1)
                print(showCmdClose)
                InfoValue = getClient.sshExecByOne(ssh, oneCmd, 12, 1)
                InfoValueClose = getClient.sshGetInfo(InfoValue)
                if InfoValueClose[0] == '0':
                    print("GMK has no power")
                    time.sleep(1)        
                    # open   
                    showCmdOpen = getClient.sshExecByMany(ssh, mutiCmdOpen, 1, 1)
                    print(showCmdOpen)
                    time.sleep(300)
                else:
                    print("GMK has power")
            else:               
                print("Something is wrong and ONU Number is : " + InfoValue[0])
                break
            print("-----OK-----")
        getClient.close(ssh)
    #F004: ONU 衰减
    def Run_Onu_Att(self):
        num = 0
        while num <= self.readValue.get_onu_sum():           
            m0_cmd = [ self.readValue.do_onu_att()]
            #执行命令
            num += 1 
            result1 = getClient.sshExecByMany(ssh,m0_cmd,1,1)
            print(result1)
        else:
            print("执行结束")
        getClient.close(ssh)
    #F005: 清空ONU统计
    def Run_Clear_Staticis(self):
        num = 0
        while num <= self.readValue.get_onu_sum():           
            m0_cmd = ['configure terminal'+'\n',
                  self.readValue.get_mng_if(num),
                  self.readValue.do_onu_restore(),
                  self.readValue.do_exit()]
            #执行命令
            num += 1 
            result1 = getClient.sshExecByMany(ssh,m0_cmd,1,1)
            print(result1)
        else:
            print("执行结束")
        getClient.close(ssh)

if __name__ == '__main__':

    getClient = SSHClient1()
    ssh = getClient.sshConnection('zte', 'Zte154!@#', '10.230.183.146')
    # getClient.Run_shutdown()
    # getClient.Run_ONU_Store()
    # r = Read_Excel()
    # r.main()