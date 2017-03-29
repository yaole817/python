#!/usr/bin/python
#-*-coding:utf-8 -*-

import pymysql
import os


def openFile(filename):
	with open(filename,'rb') as f:
		lines = f.readlines()
	return lines

if __name__ == '__main__':
	filenames=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.csv']
	lines = openFile(filenames[0])
	stock_code,title = lines.pop(0),lines.pop(0)
	conn = pymysql.connect(host='10.28.120.60',
						   port=3306,
						   user='root',
						   passwd='yao',
						   db='stock')
	cursor = conn.cursor()
	cursor.execute('create table %s (日期 varchar(20) primary key, 开盘价 varchar(20),最高价 varchar(20),收盘价 varchar(20),最低价 varchar(20),交易量(股) varchar(20),交易金额(元) varchar(20))',[stock_code])

	for line in lines:
		print(line)
		exit()
	
#cursor.execute("DROP TABLE IF EXISTS USER")