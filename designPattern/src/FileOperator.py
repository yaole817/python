


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