# -*- coding: UTF-8 -*-
import csv
from xml.etree.ElemenTree import Element, ElementTree
import requests
from StringIO import StringIO
from xml_pretty import pretty

def download(url):
    response = requests.get(url,timeout=3)
    if response.ok:
        return StringIO(response.content)

def csvToxml(scsv,fxml):
    reader = csv.reader(scsv)
    header = reader.next()
    headers = map(lambda h: h.replace('',''),headers)

    root = Element("Data")
    for row in reader:
        eRow = Element("Row")
        root.append(eRow)
        for tag,text in zip(headers,row):
            e = Element(tag)
            e.text = text
            eRow.append(e)

    pretty(root)
    et = ElementTree(root)
    et.write(fxml)

def handle(sid):
    print('Download...(%d)' % sid)
    url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
    url %= str(sid).rjust(6,'0')
    rf = download(url)
    if rf is None:return

    print('convert to xml...(%d)' % sid)
    fname = str(sid).rjust(6,'0') +'.xml'
    with open(fname,'wb') as wf:
        csvToxml(rf,wf)


# 方法一
from threading import Thread
t = Thread(target=handle,args=(1,)) # 创建一个线程对象，并处理第一支股票
t.start # 执行线程

# 方法二
class MyThread(Thread):
    def __init__(self,sid):
       Thread.__init__(self) # 调用父类的构造器
       self.sid = sid
   
   def run(self):
       handle(self.sid)

threads = []
for i in xrange(1,11):
    t = MyThread(i)
    threads.append(t)
    t.start()

for t in threads:
    t.join() # 阻塞函数等待子线程的退出，如果run函数没有执行完主线程函数不会退出,即下面没有打印
print('main thread')