#!/usr/bin/env python
# coding:utf-8
import xlrd



class Read_Excel():
    def __init__(self):
        self.ponData = self.read_excle()

    def read_excle(self):
        work_book = xlrd.open_workbook(r"D:\2020\15_Coding\case1.xlsx")
        work_sheet = work_book.sheet_by_name("Sheet1")
        #获取总行数总列数
        row_Num = work_sheet.nrows
        col_Num = work_sheet.ncols
        #定义一个列表，存放每一行的内容
        data_list = []
        key_list = None
        for i in range(row_Num):
            #获取每一行的数据
            row_data = work_sheet.row_values(i)
            if i == 0:
                key_list = row_data
            else:
                data_dict = dict()
                for index,cel_data in enumerate(row_data):
                    #获取字典的key
                    key = key_list[index]
                    #字典赋值
                    data_dict[key] = cel_data
                data_list.append(data_dict)
        return data_list
    #获取olt接口
    def get_olt_if(self):        
        olt_if = self.ponData[0]['olt_if']        
        # for i in ponData:
        #     print(i)
        return olt_if
    #获取onu的数量
    def get_onu_sum(self):
        onu_sum = self.ponData[0]['onu_sum']
        return int(onu_sum)
    #获取单板槽位号
    def get_slot(self):
        slot_value = self.ponData[0]['slot']
        return slot_value
    #获取onu的type类型
    def get_onu_type(self):
        onu_type = self.ponData[0]['onu_type']
        return onu_type
    #获取onu的sn信息
    def get_onu_sn(self,n):         
        onu_sn = self.ponData[i]['onu_sn']
        return onu_sn
    #获取onu的接口
    def get_onu_if(self,n):
        onu_if = self.ponData[i]['onu_if']
        return onu_if    
    #获取远程的接口
    def get_mng_if(self,n):
        mng_if = self.ponData[n]['mng_if']
        return mng_if
    #ONU上线检测
    def do_show_onu_working(self):
        show_onu_working = self.ponData[0]['action']
        return show_onu_working
    #光模块信息查看
    def do_optical_module_info(self):
        optical_module_info = self.ponData[1]['action']
        return 
    #ONU restore
    def do_onu_restore(self):
        onu_restore = self.ponData[2]['action']
        return onu_restore
    #ONU shutdwon
    def do_onu_shutdown(self):
        onu_shutdown = self.ponData[3]['action']
        return onu_shutdown
    #ONU no shutdwon
    def do_onu_no_shutdown(self):
        onu_no_shutdown = self.ponData[4]['action']
        return onu_no_shutdown
    #向前退一步
    def do_exit(self):
        exit0 = self.ponData[5]['action']
        return exit0
    #diag命令1
    def do_diag_cmd0(self):
        diag_cmd0 = self.ponData[6]['action']
        return diag_cmd0
    #diag命令2
    def do_diag_cmd0(self):
        diag_cmd1 = self.ponData[7]['action']
        return diag_cmd1
    #获取 ONU 衰减
    def do_onu_att(self):
        onu_att = self.ponData[0]['attuention']
        return onu_att        