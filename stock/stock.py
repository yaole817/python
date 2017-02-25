#!/usr/bin/python
#-*-coding:utf-8 -*-

'''
tools : python 2.7
function: scrapy the stock data
autrhor: yaole
'''
import requests,re
import time
from bs4 import BeautifulSoup       
psudoWebHeader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
myurl = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/000672.phtml'


titlePat = re.compile(r'(?<=<strong>).*?(?=</strong>)')
pricePat = re.compile(r'(?<="center">).*?(?=</div>)')
timePat  = re.compile(r"<a target='_blank'.*?>.*?(?=</a>)",re.DOTALL)
blockPat = re.compile(r'<tr .*?>(.*?)</tr>',re.DOTALL)
tBody    = re.compile(r'<table.*?>(.*?)</table>',re.DOTALL)
class stock:
	def __init__(self,web_data):
		self.wb_data 	= web_data
		self.time  		= ''
		self.openPrice 	= ''
		self.highPrice 	= ''
		self.closePrice = ''
		self.lowPrice   = ''
		self.totleNumber= ''
		self.totlePrice = ''
	def __getTitle__(self,data):
		'''
			get the table title
		'''
		title = titlePat.findall(data)
		return title
	def __getPrice__(self,data):
		'''
			get the price of one stock,which include high price,low price,open price, closed price
			totle number and totle price
		'''
		price = pricePat.findall(data)
		return price
	def __getTime__(self,data):
		'''
			from the web data,extract the time
		'''
		tim  = timePat.findall(data)
		tim  = [item[item.index('>')+1:].strip() for item in tim]
		return tim
	def __getTBody__(self,data):
		'''
			from the web data,extract the table's html
		'''
		table = tBody.findall(data)
		return ''.join(table)
	def __getRowData__(self,data):
		'''
			get one row data from table
		'''
		block = blockPat.findall(data)
		return block 
	def getDayStock(self):
		'''
			1. get the table's html
			2. frome the table get the table's row data line by line
			3. extract the interesting thing we wanted
			4. assign the value to the variable
		'''
		web_table = self.__getTBody__(self.wb_data)
		row_data  = self.__getRowData__(web_table)
		oneDaySocket =[]
		for item in row_data:
			time  = ''.join(self.__getTime__(item))
			self.time =time
			price = ','.join(self.__getPrice__(item))
			oneDaySocket.append((time+','+price))
		return oneDaySocket


if __name__ == '__main__':
	wb_data = requests.get(myurl,headers=psudoWebHeader)
	content = wb_data.content
	mystock = stock(content)
	data = mystock.getDayStock()
	for item in data:
		print item
	exit()
	data    = timePat.findall(content)
	#print(data)
	for item in data:
		print(item)
