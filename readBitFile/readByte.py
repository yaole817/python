# python version: 3+
# not compilable with python 2.7
def extractAsciiCode(filename):
	lineList	= []
	with open(filename,'rb') as f:	
		data_string	= f.read()

		for i in data_string:
			lineList.append(hex(i))
	return lineList

lenthNum =	48
if __name__ == "__main__":
	hexList 	= extractAsciiCode('1.fd')
	with open('output.txt','w+') as f:
		for i in range(len(hexList)):
			f.write('{0:5}'.format(hexList[i]))
			if(i%lenthNum == (lenthNum-1)):
				f.write('\n')
