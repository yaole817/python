
import FileOperator

class UniFile():
	def __init__(self,fileList):
		self.__fileList = fileList
	



if __name__ == '__main__':
	filepath = 'CND003.uni'
	uniFileList = FileOperator.readFile(filepath)
	FileOperator.printList(uniFileList)

	unifile = UniFile(uniFileList)
