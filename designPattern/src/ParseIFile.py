import FileOperator

class setupOption():
	def __init__(self,string):
		_name 		  = ''
		_defaultValue = 0
		_optionValue  = {}
		_conditon 	  = ''

class IFile():
	def __init__(self,fileList):
		self.__fileList = fileList
		self.__oneofList = []
		self.__conditionList = []

	def __addConditions2Oneof(self):
		conditionList = []
		for line in self.__fileList:
			if 'suppressif' in line:
				conditionList.append(line)
			if 'endif' in line:
				conditionList.pop()
			if 'endoneof' in line and len(conditionList)>0:
				self.__conditionList.append(conditionList[-1])
			self.__conditionList.append(line)

	def extractOneof(self):
		self.__addConditions2Oneof()
		import re
		oneofPattern = re.compile(r'oneof.*?endoneof',re.DOTALL)
		self.__oneofList = oneofPattern.findall(''.join(self.__conditionList))
		return self.__oneofList



if __name__ == '__main__':
	filename = "../res/Advanced.i"

	iFileList = FileOperator.readFile(filename)
	
	iFile = IFile(iFileList)
	newLineList = iFile.extractOneof()

	FileOperator.printList(newLineList)






