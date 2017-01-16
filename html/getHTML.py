import urllib.request
with urllib.request.urlopen('http://www.baidu.com') as response:
	html = response.read()
	print(html)


