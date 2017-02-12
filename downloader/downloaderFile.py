'''
from request lib downloader files which the url can just be http

'''
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
with open ('RomeoAndJuliet.txt','w')as f:
	f.write(res.content)
