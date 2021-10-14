# -*- coding: UTF-8 -*-
import csv
from xml.etree.ElemenTree import Element, ElementTree
import requests
from StringIO import StringIO
from xml_pretty import pretty

from Queue import Queue 

class DownloadThread(Thread):
    def __init__(self,sid,queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        self.url %= str(sid).rjust(6,'0')
        self.queue = queue

    def download(self,url):
        response = requests.get(url,timeout=3)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        print('download',self.sid)
        # 1
        data = self.download(self.url)
        # 2 (sid,data)
        # lock
        self.queue.put((self.sid,data))

        
class ConvertThread(Thread,queue):
    def __init__(self):
        Thread.__init__(self)
        self.queue = queue

    def csvToxml(self,scsv,fxml):
        reader = csv.reader(scsv)
        header = reader.next()
        headers = map(lambda h: h.replace( , ),headers)
    
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

    def run(self):
        #1 sid,data
        while True:
            sid,data = self.queue.get()
            print('Convert',sid)
            if sid == -1:
                break
            if data:
            fname = str(sid).rjust(6,'0') +'.xml'
            with open(fname,'wb') as wf:
                self.csvToxml(data,wf)

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

q = Queue()
dThreads = [DownloadThreadI(i,q) for i in xrange(1,11)]
cThread = ConvertThread(q)
for t in dThreads:
    t.start()
cThread.start()

for t in dThreads:
    t.join()

q.put((-1,None))
