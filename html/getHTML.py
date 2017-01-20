# only support python 3 or later
import urllib.request
from bs4 import soup
with urllib.request.urlopen('http://www.baidu.com') as response:
	html = response.read()
	print(html)


