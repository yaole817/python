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

	def extractComplateExpression(self,string,findExpression):
		storeIndexStart = string.index(findExpression)
		storeIndexEnd   = storeIndexStart
		for i in range(len(string)):
			storeIndexEnd = i+1
			if ')' == string[i] \
			and self.judgeStringComplate(string[storeIndexStart:storeIndexEnd]) \
			and i>storeIndexStart:
				return string[storeIndexStart:storeIndexEnd]

	def decodeTwoParameterFunction(self,string,keyword):
		keyString = self.extractComplateExpression(string,keyword).replace(keyword,'')
		for i in range(len(keyString)):
			if ',' == keyString[i]:
				leftString 	= keyString[:i].strip()
				rightString = keyString[i+1:].strip()
				if self.judgeStringComplate(leftString +')') and self.judgeStringComplate('('+rightString):
					return leftString[1:],rightString[:-1]



class StoreReplace(complateExpression):
	def __init__(self):
		self.newLines 	= []
		
	def storeReplace(self,leftString,rightString):
		return rightString + ' = ' + leftString

	def replaceFileStore(self,lines):
		for line in lines:
			if 'Store' in line:
				store = self.extractComplateExpression(line,'Store')
				leftString,rightString = self.decodeTwoParameterFunction(store)
				newString = self.storeReplace(leftString,rightString)
				line = line.replace(store,newString)
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
	fileList =  [x for x in os.listdir('.') if os.path.splitext(x)[1]=='.asl']
	testString = 'fhadsfkhfdsafjkasl()Store (Or (_DGS, Local0), _DGS)tdfgdklh,()'
	#lines = replaceFileStore('Gpe.asl')
	#writeFile('newGpe.asl',lines)
	filepathList = getAllfile()
	for item in filepathList:
		if os.path.splitext(item)[1]=='.asl':
			print item
			lines = readFile(item)
			store_replace = StoreReplace()
			newLines = store_replace.replaceFileStore(lines)
			#print newLines
			writeFile(item,newLines)

'''
	for item in filepathList:
		if os.path.splitext(item)[1]=='.asl':
			print item
			lines = replaceFileStore(item)
			writeFile(item,lines)
'''