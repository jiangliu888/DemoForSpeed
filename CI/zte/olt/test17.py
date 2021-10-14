# -*- coding: UTF-8 -*-
import xlrd,xlwt

rbook = xlrd.open_workbook('shizhan\score.xlsx')  # 创建一个读的工作薄对象
rsheet = rbook.sheet_by_index(0) # 读取工作薄中的第一张表

nc = rsheet.ncols # 要增加的新列的列坐标

rsheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,'总分',None)  # 添加新列并对新列的内容属性进行定义

# 进行迭代计算总分
for row in range(1,rsheet.nrows):
    t = sum(rsheet.row_values(row,1))  # 获取一行的值返回一个列表，从1列开始，即却除了姓名,并进行求和
    rsheet.put_cell(row,nc,xlrd.XL_CELL_NUMBER,t,None)  # 将计算的结果存入单元格
     

wbook = xlwt.Workbook()  # 创建一个写的工作簿的对象
wsheet = wbook.add_sheet(rsheet.name)  # 添加一张表，与上面rsheet的相同
style = xlwt.easyxf('align:vertical center, horizontal center')  # 水平居中和垂直居中

# 遍历上面rsheet表的每一个单元格进行写入
for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r,c,rsheet.cell_value(r,c),style)

wbook.save('output.xls')  # 结果进行保存