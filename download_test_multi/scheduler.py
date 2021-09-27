# -*- coding: UTF-8 -*-

import prettytable
import os
import utils
from modules.downloader import Downloader
from modules.Hasher import Hasher
from modules.storager import Storager
from const import CalcType
class Scheduler:

    def __init__(self):
        self.downloader = Downloader()
        self.hasher = Hasher()
        self.storager = Storager()

    def set_calc_type(self,type_):
        self.downloader.set_calc_type(type_)
        self.hasher.set_calc_type(type_)
        self.storager.set_calc_type(type_)

    def _wrap_path(self,md5):
        filename = '{}.jpg'.format(md5)
        STROAGE_PATH = os.path.join('.','images')
        path = os.path.join(STROAGE_PATH,filename)
        return path

    def process(self):

        time_statictics = {}
        time_statictics['network_time'] = []
        time_statictics['cpu_time'] = []
        time_statictics['disk_time'] = []

        time = utils.Timer()
        # 1、加载图片url列表
        url_list = utils.urllist()
        # 2、调度下载模块
        time.tick()
        content_list = self.downloader.process(url_list)
        time_statictics['network_time'].append(time.tock())
        # 3、调度哈希模块
        time.tick()
        md5_list = self.hasher.process(content_list)
        time_statictics['cpu_time'].append(time.tock())
        for md5 in md5_list:
            print(md5)
        # 4、调度存储模块
        item_list = []
        for content,md5 in zip(content_list, md5_list):
            path = self._wrap_path(md5)
            item = (content, path)
            item_list.append(item)
        time.tick()
        self.storager.process(item_list)
        time_statictics['disk_time'].append(time.tock())
        return time_statictics

    def staticics(self,time_single,time_multi):
        #定义表格行列
        table = prettytable.PrettyTable(['类型','单线程总耗时','多线程总耗时','差值'])
        network_row = ['network']
        cpu_row = ['cpu']
        disk_row = ['disk']
        #单线程
        network_row.append(time_single['network_time'][0])
        cpu_row.append(time_single['cpu_time'][0])
        disk_row.append(time_single['disk_time'][0])
        #多线程
        network_row.append(time_multi['network_time'][0])
        cpu_row.append(time_multi['cpu_time'][0])
        disk_row.append(time_multi['disk_time'][0])

        time_ = time_single['network_time'][0] - time_multi['network_time'][0]
        lift_rate = '%.4f%%' % ((time_ / time_single['network_time'][0]) * 100)
        network_row.append(lift_rate)

        time_ = time_single['cpu_time'][0] - time_multi['cpu_time'][0]
        lift_rate = '%.4f%%' % ((time_ / time_single['cpu_time'][0]) * 100)
        cpu_row.append(lift_rate)
        
        time_ = time_single['disk_time'][0] - time_multi['disk_time'][0]
        lift_rate = '%.4f%%' % ((time_ / time_single['disk_time'][0]) * 100)
        disk_row.append(lift_rate)

        table.add_row(network_row)
        table.add_row(cpu_row)
        table.add_row(disk_row)        
        print(table)

if __name__ == "__main__":
    scheduler = Scheduler()
    # 单线程
    scheduler.set_calc_type(CalcType.SingleThread)
    time_single = scheduler.process()
    # 多线程
    scheduler.set_calc_type(CalcType.MultiThread)
    time_multi = scheduler.process()
    scheduler.staticics(time_single,time_multi)

