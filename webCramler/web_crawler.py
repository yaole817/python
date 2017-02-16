#!/usr/bin/python
#-*-coding:utf-8 -*-
'''
version: python 3.5
function : web crawler
addition: save web .jpg,.png,.gif
entryPoint:http://www.douban.com/

'''
import urllib.request
import re
import os
def writeFile(filename,myString):
	with open(filename,'wb') as f:
		f.write(myString)
def downloadPage(url):
 	request = urllib.request.Request(url)
 	response = urllib.request.urlopen(request)
 	data = response.read()
 	return data

if __name__=='__main__':
	#url='http://open.163.com/movie/2017/2/8/K/MCBG6TO95_MCBO5F18K.html'
	weburl = 'http://www.douban.com/'
	webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 
	req = urllib.request.Request(url=weburl, headers=webheader) 
	webPage=urllib.request.urlopen(req)
	data = webPage.read()
	num=1
	for link,t in set(re.findall(r'(https?://[\S]*?.(jpg|png|gif))', str(data))):  #正则表达式查找所有的图片
		#print(link)
		image= downloadPage(link)
		name = link.split('/')[-1]
		if not os.path.isdir('picture'):  
			os.mkdir('picture') 
		print("正在下载第%d张..."%num)
		num+=1
		writeFile('picture/'+name,image)
			
	#writeFile('debug.html',data.decode('UTF-8')
	#print(type(webPage))
	#print(webPage.geturl())
	#print(webPage.info())
	#print(webPage.getcode())