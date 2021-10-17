# -*- encoding=utf-8 -*-

import os

import prettytable

import utils
from const import CalcType
from modules.downloader import Downloader
from modules.hasher import Hasher
from modules.storager import Storager


class Scheduler:
    """调度模块
    """

    def __init__(self):
        self.downloader = Downloader()
        self.hasher = Hasher()
        self.storager = Storager()

    def _wrap_path(self, md5):
        filename = '{}.jpg'.format(md5)
        STORAGE_PATH = os.path.join('.', 'images')
        path = os.path.join(STORAGE_PATH, filename)
        return path

    def set_calc_type(self, type_):
        self.downloader.set_calc_type(type_)
        self.hasher.set_calc_type(type_)
        self.storager.set_calc_type(type_)

    def process(self):
        time_statictics = {}
        time_statictics['network_time'] = []
        time_statictics['cpu_time'] = []
        time_statictics['disk_time'] = []
        
        timer = utils.Timer()
        # 1. 加载图片url列表
        url_list = utils.urllist()
        # 2. 调度下载模块
        timer.tick()
        content_list = self.downloader.process(url_list)
        time_cost = timer.tock()
        time_statictics['network_time'].append(time_cost)

        # 3. 调度哈希模块
        timer.tick()
        md5_list = self.hasher.process(content_list)
        time_cost = timer.tock()
        time_statictics['cpu_time'].append(time_cost)
        
        # 4. 调度存储模块
        item_list = []
        for content, md5 in zip(content_list, md5_list):
            path = self._wrap_path(md5)
            item = (content, path)
            item_list.append(item)
        timer.tick()
        self.storager.process(item_list)
        time_cost = timer.tock()
        time_statictics['disk_time'].append(time_cost)
        return time_statictics

    def statictics(self, single_log, multi_log, multiprocess_log, pycoroutine_log):
        table = prettytable.PrettyTable(['类型', '单线程总耗时', '多线程总耗时', '多线程提升率', '多进程总耗时', '多进程提升率', '协程总耗时', '协程提升率'])
        network_row = ['network']
        cpu_row = ['cpu']
        disk_row = ['disk']
        # 单线程数据
        network_row.append(single_log['network_time'][0])
        cpu_row.append(single_log['cpu_time'][0])
        disk_row.append(single_log['disk_time'][0])
        # 多线程数据
        network_row.append(multi_log['network_time'][0])
        cpu_row.append(multi_log['cpu_time'][0])
        disk_row.append(multi_log['disk_time'][0])

        # 多线程提升率
        time_ = single_log['network_time'][0] - multi_log['network_time'][0]
        lift_rate = '%.4f%%' % ((time_ / single_log['network_time'][0]) * 100)
        network_row.append(lift_rate)

        time_ = single_log['cpu_time'][0] - multi_log['cpu_time'][0]
        lift_rate = '%.4f%%' % ((time_ / single_log['cpu_time'][0]) * 100)
        cpu_row.append(lift_rate)
        
        time_ = single_log['disk_time'][0] - multi_log['disk_time'][0]
        lift_rate = '%.4f%%' % ((time_ / single_log['disk_time'][0]) * 100)
        disk_row.append(lift_rate)

        # 多进程数据
        network_row.append(multiprocess_log['network_time'][0])
        cpu_row.append(multiprocess_log['cpu_time'][0])
        disk_row.append(multiprocess_log['disk_time'][0])

        # 多进程提升率
        time_ = single_log['network_time'][0] - multiprocess_log['network_time'][0]
        lift_rate = '%.4f%%' % ((time_ / single_log['network_time'][0]) * 100)
        network_row.append(lift_rate)

        time_ = single_log['cpu_time'][0] - multiprocess_log['cpu_time'][0]
        lift_rate = '%.4f%%' % ((time_ / single_log['cpu_time'][0]) * 100)
        cpu_row.append(lift_rate)
        
        time_ = single_log['disk_time'][0] - multiprocess_log['disk_time'][0]
        lift_rate = '%.4f%%' % ((time_ / single_log['disk_time'][0]) * 100)
        disk_row.append(lift_rate)

        # 协程运行数据
        network_row.append(pycoroutine_log['network_time'][0])
        cpu_row.append(pycoroutine_log['cpu_time'][0])
        disk_row.append(pycoroutine_log['disk_time'][0])

        # 协程运行提升率
        time_ = single_log['network_time'][0] - pycoroutine_log['network_time'][0]
        lift_rate = '%.4f%%' % ((time_ / single_log['network_time'][0]) * 100)
        network_row.append(lift_rate)

        time_ = single_log['cpu_time'][0] - pycoroutine_log['cpu_time'][0]
        lift_rate = '%.4f%%' % ((time_ / single_log['cpu_time'][0]) * 100)
        cpu_row.append(lift_rate)
        
        time_ = single_log['disk_time'][0] - pycoroutine_log['disk_time'][0]
        lift_rate = '%.4f%%' % ((time_ / single_log['disk_time'][0]) * 100)
        disk_row.append(lift_rate)

        table.add_row(network_row)
        table.add_row(cpu_row)
        table.add_row(disk_row)
        print(table)

if __name__ == '__main__':
    scheduler = Scheduler()
    # 单线程运行
    scheduler.set_calc_type(CalcType.SingleThread)
    singlethread_time = scheduler.process()
    # 多线程运行
    scheduler.set_calc_type(CalcType.MultiThread)
    multithread_time = scheduler.process()
    # 多进程运行
    scheduler.set_calc_type(CalcType.MultiProcess)
    multiprocess_time = scheduler.process()
    # 协程运行
    scheduler.set_calc_type(CalcType.PyCoroutine)
    pyprocess_time = scheduler.process()
    # 合并数据
    scheduler.statictics(singlethread_time, multithread_time, multiprocess_time, pyprocess_time)
