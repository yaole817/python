import os
class ScanFile(object):
	def __init__(self,directory,prefix=None,postfix=None):
		self.directory	= directory
		self.prefix		= prefix
		self.postfix	= postfix
        
	def scan_files(self):  
		files_list=[]  
          
		for dirpath,dirnames,filenames in os.walk(self.directory): 
			'''
			dirpath is a string, the path to the directory.  
			dirnames is a list of the names of the subdirectories in dirpath (excluding '.' and '..').
			filenames is a list of the names of the non-directory files in dirpath.
			'''
			for special_file in filenames:  
				if self.postfix:  
					special_file.endswith(self.postfix)  
					files_list.append(os.path.join(dirpath,special_file))  
				elif self.prefix:  
					special_file.startswith(self.prefix)
					files_list.append(os.path.join(dirpath,special_file))  
				else:  
					files_list.append(os.path.join(dirpath,special_file))
		return files_list  
    
	def scan_subdir(self):
		subdir_list=[]
		for dirpath,dirnames,files in os.walk(self.directory):
			subdir_list.append(dirpath)
		return subdir_list



class complateExpression:
	def judgeStringComplate(self,string):
		signDatabaseLeft = '('
		signDatabaseRight = ')'
		signList = []
		for item in string:
			if item in signDatabaseLeft:
				signList.append(item)
			elif item in signDatabaseRight:
				signList.pop(-1)
		if len(signList)==0:
			return True
		else:
			return False

	def extractComplateExpression(self,string,keyword):
		storeIndexStart = string.index(keyword)
		storeIndexEnd   = storeIndexStart
		for i in range(len(string)):
			storeIndexEnd = i+1
			if ')' == string[i] \
			and self.judgeStringComplate(string[storeIndexStart:storeIndexEnd]) \
			and i>storeIndexStart:
				return string[storeIndexStart:storeIndexEnd]

	def decodeFunctionParameter(self,string,keyword):
		keyString = self.extractComplateExpression(string,keyword).replace(keyword,'')
		keyString = keyString.strip()[1:-1] #clear outermost bracket
		parameterList = [] #  store parameter
		startIndex = 0
		for i in range(len(keyString)):
			if ',' == keyString[i]: # split the expression
				parameterString = keyString[startIndex:i].strip() 
				leftParameterString = keyString[i+1:].strip()
				if self.judgeStringComplate(parameterString ) and self.judgeStringComplate(leftParameterString):
					parameterList.append(parameterString)
					startIndex = i+1
		parameterList.append(keyString[startIndex:])
		return parameterList


class TwoParameterFunction(complateExpression):
	def __init__(self,expression,keyword): # expression must be like 'X==Y,X<=Y'
		self.newLines 	= []
		self.expression = expression  # 
		self.keyword 	= keyword
	def functionReplace(self,leftString,rightString):
		# replace expression with X by leftString and Y by rightString 
		return self.expression.replace('leftString',leftString).replace('rightString',rightString)

	def replaceFileFunction(self,lines):
		for line in lines:
			if self.keyword in line:
				function = self.extractComplateExpression(line,self.keyword)
				parameterList= self.decodeFunctionParameter(function,self.keyword)
				newString = self.functionReplace(parameterList[0],parameterList[1])
				line = line.replace(function,newString)
			self.newLines.append(line)
		return self.newLines


class ThreeParameterFunction(complateExpression):
	def __init__(self,three_par_exp,two_par_exp,keyword): # expression must be like 'X==Y,X<=Y'
		self.newLines 	= []
		self.two_par_exp = two_par_exp  #
		self.three_par_exp = three_par_exp
		self.keyword 	= keyword

	def functionReplace(self,expression,leftString,rightString,resultString):
		# replace expression with X by leftString and Y by rightString 
		return expression.replace('leftString',leftString).replace('rightString',rightString).replace('resultString',resultString)

	def replaceFileFunction(self,lines):
		import re
		reExpression = self.keyword+'[ ]*\(.'
		expressionPattern = re.compile(reExpression)
		for line in lines:
			if expressionPattern.findall(line)!=[]:
				function = self.extractComplateExpression(line,self.keyword)
				parameterList = self.decodeFunctionParameter(function,self.keyword)
				# judge the lenth of parameter
				if len(parameterList)==2:
					newString = self.functionReplace(self.two_par_exp,parameterList[0],parameterList[1],'')
				elif len(parameterList)==3:
					newString = self.functionReplace(self.three_par_exp,parameterList[0],parameterList[1],parameterList[2])
				line = line.replace(function,newString)
			self.newLines.append(line)
		return self.newLines


class OneParameterFunction(complateExpression):
	def __init__(self,expression,keyword): # expression must be like 'X==Y,X<=Y'
		self.newLines 	= []
		self.expression = expression  #
		self.keyword 	= keyword

	def functionReplace(self,expression,parameterString):
		# replace expression with X by leftString and Y by rightString 
		return expression.replace('parameterString',parameterString)

	def replaceFileFunction(self,lines):
		import re
		reExpression = self.keyword+'[ ]*\(.'
		expressionPattern = re.compile(reExpression)
		for line in lines:
			if expressionPattern.findall(line)!=[]:
				function = self.extractComplateExpression(line,self.keyword)
				parameterList = self.decodeFunctionParameter(function,self.keyword)
				# judge the lenth of parameter
				newString = self.functionReplace(self.expression,parameterList[0])
				line = line.replace(function,newString)
			self.newLines.append(line)
		return self.newLines

def getAllfile():
	scan	= ScanFile('..')
	files	= scan.scan_files()
	return files

def readFile(filename):
	with open(filename,'r')as f:
		lines	= f.readlines()
	return lines

def writeFile(filename,myList):
	with open(filename,'w')as f:
		for line in myList:
			f.write(line)

if __name__ == "__main__":
	path = 'D:\BIOS\BYO-A0-ACPI-restruct\AsiaPkg\Asia\PLATFORM\AcpiTables'
	os.chdir(path)

	dsdtPath = '..\..\..\..\PlatformPkg\AcpiTables\Dsdt\Dsdt.asl'
	'''
	fileList =  [x for x in os.listdir('.') if os.path.splitext(x)[1]=='.asl']
	testText = ['And((1,2),BCD,CDE)']
	
	Exp = ThreeParameterFunction(' resultString = leftString & rightString','leftString & rightString','And')
	parList  = Exp.replaceFileFunction(testText)
	print parList
	exit()
	'''
	#lines = replaceFileStore('Gpe.asl')
	#writeFile('newGpe.asl',lines)
	filepathList = getAllfile()
	filepathList.append(dsdtPath)
	for item in filepathList:
		if os.path.splitext(item)[1]=='.asl':
			print item
			lines = readFile(item)
			store_replace = OneParameterFunction('parameterString--','Decrement')
			newLines = store_replace.replaceFileFunction(lines)
			#print newLines
			writeFile(item,newLines)