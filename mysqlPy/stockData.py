#!/usr/bin/python
#-*-coding:utf-8 -*-

import pymysql
import os
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

import re

idPattern = re.compile('[\d]{6}')

def openFile(filename):
	with open(filename,'rb') as f:
		lines = f.readlines()
	return lines

work_path = os.getcwd()
data_path = r'/home/yao/python/stock_data'
if __name__ == '__main__':
	os.chdir(data_path)
	filenames=[x for x in os.listdir(r'/home/yao/python/stock_data') if os.path.isfile(x) and os.path.splitext(x)[1]=='.csv']
	#os.chdir(work_path)
	
	
	conn = pymysql.connect(host='127.0.0.1',user='root',passwd='yao',db='myStock',port=3306,charset='utf8')
	cursor = conn.cursor()
	#result = cursor.execute("SHOW TABLES;")
	#print(result)
	#cursor.execute("DROP TABLE IF EXISTS USER1;")
	for file in filenames:
		lines = openFile(file)
		try:
			stock_id,title = lines.pop(0),lines.pop(0)
			print(stock_id)
			stock_id = idPattern.findall(stock_id)[0]
			#print(id_num)
			#stock_id = stock_id[-8:-2]

			print(stock_id)
			#exit()
			cursor.execute("DROP TABLE IF EXISTS SZ%s"%(stock_id))
			cursor.execute("CREATE TABLE SZ%s (ID INT AUTO_INCREMENT PRIMARY KEY,myDATE VARCHAR(20), OPENP_RICE VARCHAR(20),HIGH_PRICE VARCHAR(20),CLOSED_PRICE VARCHAR(20),LOW_PRICE VARCHAR(20),TOTLE_NUMBE VARCHAR(20),TOTLE_PRICE VARCHAR(20));"%(stock_id))
			print('SZ'+stock_id+'is starting ....')
			conn.commit()
			result = cursor.execute("SHOW TABLES;")
			for line in lines:
				line=line.strip().split(',')
				timeArray = time.strptime(line[0], "%Y-%m-%d")
				#转换成新的时间格式(20160505)
				dt_new = time.strftime("%Y%m%d",timeArray)
				#print dt_new
				cursor.execute("INSERT INTO SZ%s (myDATE,OPENP_RICE,HIGH_PRICE,CLOSED_PRICE,LOW_PRICE,TOTLE_NUMBE,TOTLE_PRICE) VALUES (%s, %s,%s,%s,%s, %s,%s);"% (stock_id,dt_new,line[1],line[2],line[3],line[4],line[5],line[6]))
				conn.commit()
			print('SZ'+stock_id+'is done')
		#input()
		except:
			print(file)
			continue
