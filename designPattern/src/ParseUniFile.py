
import FileOperator

class UniFile():
	def __init__(self,fileList):
		self.__fileList = fileList
		self.__strFile = []

	def __translateStr(self,string):
		s = ''
		for i in string:
			if  ord(i) >0 and ord(i) <255: s+=i
		return s

	def __extractUniFile(self):
		for line in self.__fileList:
			newLine = self.__translateStr(line)
			self.__strFile.append(newLine)
		return self.__strFile
		
	def extractEnUsLines(self):

		enUsLines = []
		newLineList = self.__extractUniFile()
		for line in newLineList:
			if 'en-US' in line and "#string" in line:
				enUsLines.append(line)
		return enUsLines
	def parseUniFile(self):
		newLines = self.extractEnUsLines()
		stringDict={}
		for line in newLines:
			stringList = line.split()
			start = line.index('"')+1
			end = line.rindex('"')
			stringDict[stringList[1]] = line[start:end]
		return stringDict

if __name__ == '__main__':
	filepath = '../res/CND003.uni'
	uniFileList = FileOperator.readFile(filepath)
	

	unifile = UniFile(uniFileList)
	#newLineList = unifile.extractEnUsLines()
	#FileOperator.printList(newLineList)
	stringDict = unifile.parseUniFile()
	FileOperator.printDict(stringDict)
