###
#### python version: 2.7
#### 

from zipfile import ZipFile
import re
import sys


class Docx2Text(object):
	def __init__(self,docxName):
		self.__docxName = docxName
		self.xml 	    = str(ZipFile(self.__docxName).read('word/document.xml'))

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




class ParseIRS(Docx2Text):
	def __init__(self,docxName):
		Docx2Text.__init__(self,docxName)
		self.__xml = self.xml
		self.__startIndex = 0
		self.__endIndex = 0
		

	def findOffsetAddr(self,xml):
		return super(ParseIRS,self).findParagraph(xml)

	def parseOneTable(self,tableXml):
		
		self.__endIndex = self.__xml.index(tableXml) 
	
		oneTable  = super(ParseIRS,self).parseTable(tableXml)
		newXml = self.__xml[self.__startIndex:self.__endIndex] # cut off the xml

		paragraph = self.findOffsetAddr(newXml)[-1]  # find the lastest paragraph,which is always the base address

		offsetAddr = super(ParseIRS,self).findText(paragraph) 

		self.__startIndex  = self.__endIndex
		return offsetAddr,oneTable


	def parseIrs(self):
		resultTable = []
		tableXmls = super(ParseIRS,self).findTable(self.__xml)
		for tableXml in tableXmls:
			offsetAddr,oneTable = self.parseOneTable(tableXml)
			resultTable.append([offsetAddr,oneTable])
		return resultTable



def writeFile(tableList,filename):
	splitSign = ','

	def writeOnetable(tablelist):
		for row in tablelist:
			if len(row)==11:
				[bit,attr,hwPro,defau,descirption,mnem,chipRev,pwrDm,s,p,e]=row
				f.write(splitSign+bit+splitSign+attr+splitSign+hwPro+splitSign+defau+splitSign+mnem+splitSign+pwrDm+splitSign+s+splitSign+p+splitSign+e+splitSign)
				f.write('\n')
	with open(filename,'w+')as f:
		for item in tableList:
			offsetAddr = item[0]
			oneTable   = item[1]
			f.write(offsetAddr.replace('Default','\tDefault'))
			f.write('\n')
			writeOnetable(oneTable)




docName		= sys.argv[1]
if __name__ == "__main__":

	if docName.split('.')[-1] != 'docx':
		print('please input a docx file')
		exit()

	irsName = ParseIRS(docName)
	tableList = irsName.parseIrs()
	writeFile(tableList,'irs1.txt')
	print("parse done")
