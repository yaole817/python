
def readFile(filename):
	with open(filename,'r')as f:
		lines = f.readlines()
	return lines
	
lines= readFile('build1.log')
last_string=''
for line in lines:
	if ('\\') in line:
		line=line.split('\\')
		last_string=line[-1]
	if line == last_string:
		print(line)