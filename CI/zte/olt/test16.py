# -*- coding: UTF-8 -*-
import csv
from xml.etree.ElementTree import Element,ElementTree
from e2 import pretty

def csvtoxml(fname):
    with open(fname,'r',encoding='gbk') as f:
        reader = csv.reader(f)  # 读取csv，要先创建一个reader
        headers = next(reader)  # 读取csv的头部信息

        root = Element('Data')  # 为xml创建一个根元素
        # 迭代csv文件中的每一行
        for row in reader:
            eRow = Element('Row')  # 每一行创建一个row元素
            root.append(eRow)
            # 同时迭代tag(headers)，text(row)
            for tag, text in zip(headers,row):
                e = Element(tag)  # 为headers中每一个创建一个xml中的元素
                e.text = text
                eRow.append(e)  # 将孙元素加入到父元素中去，构建好层级
    pretty(root)  # 进行格式的美化
    return ElementTree(root)  # 创建一个elementtree，即一个xml对象

if __name__ == "__main__":
    et = csvtoxml('yikang.csv')
    # 调用write方法把xml对象写入文件中，生成一个xml文件
    et.write('yikang.xml')

e2.py:

def pretty(e,level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child,level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level
