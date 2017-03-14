#!/usr/bin/python
#-*-coding:utf-8 -*-
'''
	依赖库：xlrd
	安装方法：pip install xlrd
	作用: 读取excel 数据

__Author__ = yaole
'''
import xlrd
excel = xlrd.open_workbook('1.xlsx') 
sheet = excel.sheets()[0]
# 打印第一行数据
print(sheet.row_values(0)) 
# 打印第二列数据
print(sheet.col_values(1))


'''
	写excel 数据
	依赖库：xlwt
	安装方法：pip install xlwt

'''


import xlwt
f = xlwt.Workbook() #创建工作簿
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
sheet1.write(0,0,u'呵呵')
f.save('2.xlsx')




