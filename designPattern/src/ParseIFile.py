class setupOption():
	def __init__(self,string):
		_name 		  = ''
		_defaultValue = 0
		_optionValue  = {}
		_conditon 	  = ''




class ParseIFile():
	def __init__(self,fileName):
		_fileName = fileName


	def readFile():
		with open(self._fileName,'r') as f:
			lines = f.readlines()
			return lines

if __name__ == '__main__':

	conditionList=[]
	oneofList 	 =[]
	lines		 =[]
	newLines	 =[]
	with open('Advanced.i','r')as f:
		lines = f.readlines()
	for line in lines:
		if 'suppressif' in line:
			conditionList.append(line)
		if 'endif' in line:
			conditionList.pop()
		if 'endoneof' in line and len(conditionList)>0:
			newLines.append(conditionList[-1])
		newLines.append(line)
	import re
	oneofPattern = re.compile(r'oneof.*?endoneof',re.DOTALL)
	oneofStringList = oneofPattern.findall(''.join(newLines))
	with open('newAdvanced.i','w') as f:
		for line in oneofStringList:
			f.write(line)
			f.write('\n')






