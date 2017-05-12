


def readFile(filename):
	with open(filename,'r') as f:
		lines = f.readlines()
		return lines

def writeFile(fileList,newFilename):
	with open(newFilename,'w')as f:
		for line in fileList:
			f.write(line)
			f.write('\n')

def printList(fileList):
	for line in fileList:
		print(line)
def printDict(dict):
	for key in dict:
		print('{0:40}{1:20}'.format(key,'\t:'+dict[key]))

def extractPureText(stringList):
	def translateStr(string):
		s = ''
		for i in string:
			if  ord(i) >0 and ord(i) <255: s+=i
		return s
	newStringList = []
	for line in stringList:
		newLine = translateStr(line)
		newStringList.append(newLine)
	return newStringList
