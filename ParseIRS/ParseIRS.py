from zipfile import ZipFile
import re


class Docx2Text:
	def __init__(self,docxName):
		self._docxName = docxName
		self.xml 	   = str(ZipFile(self._docxName).read('word/document.xml'))
	
	def findParagraph(self,xml):
		paragraphPattern= re.compile(r'.*(<w:p w)(.*?)(</w:p>)')
		pargraphTuple	= paragraphPattern.findall(xml)
		result = []
		for line in pargraphTuple:
			tuple2xml	= ''.join(line)
			result.append(tuple2xml)
		return result
	
	def findTable(self,xml):
		tablePattern 	= re.compile(r"(<w:tbl>)(.*?)(</w:tbl>)")
		tblTuple		= tablePattern.findall(xml)
		result = []
		for item in tblTuple:
			tuple2xml	= ''.join(item)
			result.append(tuple2xml)
		return result

	def parseTable(self,tableXml):
		tableRowPattern	= re.compile(r'<w:tr(.*?)</w:tr>')
		tableColPattern	= re.compile(r'<w:tc>(.*?)</w:tc>')
		oneTable=[]
		rows	= tableRowPattern.findall(tableXml)
		for row in rows:
			colTable=[]
			cols = tableColPattern.findall(row)
			for col in cols:
				colTable.append(self.findText(col))
			oneTable.append(colTable)

		return oneTable

	def findText(self,xml):
		textPattern		= re.compile('.*?(<w:t>|<w:t xml:space="preserve">)(?P<H2>.*?)</w:t>')
		textTuple		= textPattern.findall(xml)
		s =''
		for m in textTuple:
			s+=m[1]
		return s

class ParseIRS():
	def __init__(self,docxName):
		self.irsName = docxName
		self.__startIndex = 0
		self.__endIndex =0
		self.__irs = Docx2Text(self.irsName)

	def findOffsetAddr(self,xml):
		return self.__irs.findParagraph(xml)

	def parseOneTable(self,tableXml):
		
		self.__endIndex = self.__irs.xml.index(tableXml)
	
		oneTable  = self.__irs.parseTable(tableXml)
		newXml = self.__irs.xml[self.__startIndex:self.__endIndex]

		paragraph = self.findOffsetAddr(newXml)[-1]

		offsetAddr = self.__irs.findText(paragraph)

		return offsetAddr,oneTable


	def parseIrs(self):
		tableXmls = self.__irs.findTable(self.__irs.xml)

		with open("debug.txt",'w+')as f:
			for tableXml in tableXmls:
				offsetAddr,oneTable = self.parseOneTable(tableXml)
				f.write(offsetAddr)
				f.write('\n')
				for row in oneTable:
					f.write('|'.join(row))
					f.write('\n')



def writeFile(fileList,newFilename):
	with open("debug.txt",'w+')as f:
		for line in newFilename:
			f.write(line)
			f.write('\n')

docName		= 'IRS_CHX002_D18F0_xHCICtrl_R091.docx'
resultList=[]

if __name__ == "__main__":


	irsName = ParseIRS(docName)
	irsName.parseIrs()



	#for tableXml in tableXmls:
	#	text= docx.findText(tableXml)
	#print text
	#writeFile('irs.txt',text[5])
	#writeFile('irs.txt',text[7])