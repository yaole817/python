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

titlePat = re.compile(r'(?<=strong>).*?(?=</strong>)')
pricePat = re.compile(r'(?<="center">)[\s\d.-]*(?=</div>)',re.DOTALL)
timePat  = re.compile(r"<a target='_blank'.*?>.*?(?=</a>)",re.DOTALL)
blockPat = re.compile(r'<tr .*?>(.*?)</tr>',re.DOTALL)
tBody    = re.compile(r'<table.*?>(.*?)</table>',re.DOTALL)
stockIdPat = re.compile(r'(?<=th colspan="7">).*?\([\d]{6}\)(?=<)',re.DOTALL)
class stock:
	def __init__(self,web_data):
		self.wb_data 	= web_data
		self.title 		= ''
		self.stockId 	= ''
	def __getPrice__(self,data):
		'''
			get the price of one stock,which include high price,low price,open price, closed price
			totle number and totle price
		'''
		#print(data)
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
		if len(block)==0:
			raise "no page"
		return block 
	def __getTitle__(self,data):
		'''
			get the title of the table,it always in the first row
		'''
		title = titlePat.findall(data)
		return title

	def getStockId(self,data):
		'''
			get the stock name and stock id
		'''
		id=stockIdPat.findall(data)
		if len(id)>0:
			id = id[0].strip()
		else:
			id =''
		return id
	def getDayStock(self):
		'''
			1. get the table's html
			2. frome the table get the table's row data line by line
			3. extract the interesting thing we wanted
			4. assign the value to the variable
		'''
		table_body 	= self.__getTBody__(self.wb_data)
		self.stockId= self.getStockId(table_body)
		row_data  	= self.__getRowData__(table_body)
		self.title = ','.join(self.__getTitle__(row_data[0])).strip()
		
		row_data.pop(0)
		oneDaySocket =[]
		for item in row_data:
			time  = ''.join(self.__getTime__(item)).strip()
			price = ','.join(self.__getPrice__(item)).strip().replace('\t','')
			if time !='':
				oneDaySocket.append((time+','+price))
			else:
				oneDaySocket.append(price)
			#print(oneDaySocket[])
		return oneDaySocket
 

def getOneWholeStockData(stock_id,year,quarter): 
	myurl = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vMS_MarketHistory/stockid/%s.phtml?year=%s=&jidu=%s'%(stock_id,str(year),str(quarter))
	#print(myurl)
	wb_data = requests.get(myurl,headers=psudoWebHeader)
	content = wb_data.content
	mystock = stock(content)
	data = mystock.getDayStock()
	stockId    = mystock.stockId
	stockTitle = mystock.title
	return stockId,stockTitle,data
def getStockId(num):
	'''
		transfer number to stock number
	'''
	base_id='000000'
	lenOfNum = len(str(num))
	id = base_id[:-lenOfNum]+str(num)
	return id


stock_num=153300
if __name__ == '__main__':
	while stock_num<1000000:
		stock_id = getStockId(stock_num)
		result = []
		year  = 2017
		jidu  = 1
		stockId=''
		stockTitle=''
		try:
			print('starting...')
			while True:
				stockId,stockTitle,data=getOneWholeStockData(stock_id,year,jidu)
				#if len(data) is 0 :break
				print(stockId)
				print(str(year)+u'年第'+str(jidu)+u'季度数据...')
				jidu-=1
				if jidu==0:
					year-=1
					jidu=4
				result.extend(data)
				#time.sleep(3)
		except:
			filename = stockId.replace('*','')
			with open('D:\stock_data\\'+filename+'.csv','wb')as f:
				f.write(stockId+'\n')
				f.write(stockTitle+'\n')	
				for item in result:
					f.write(item+'\n')
			print('ending...')
		print(stock_id)
		stock_num+=1
