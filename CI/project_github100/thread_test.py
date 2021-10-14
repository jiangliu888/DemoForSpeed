# -*- coding: UTF-8 -*-
from random import randint
from threading import Thread
from time import time,sleep

class DownlaodTask(Thread):
    def __init__(self,filename):
        super(DownlaodTask,self).__init__()
        self._filename = filename
    # 业务逻辑
    def run(self):
        print "{}".format(self._filename)
        time_to_download = randint(1,2)
        sleep(time_to_download)
        print "{},{}".format(self._filename,time_to_download)

def main():
    start = time()
    t1 = DownlaodTask('11111')
    t1.start()
    t2 = DownlaodTask('22222')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print "{}".format(end-start)

if __name__=="__main__":
    main()
