
def readFile(filename):
	with open(filename,'r')as f:
		lines	= f.readlines()
	return lines
def deleteCNote(myList):
	string=''.join(myList)
	import re
	comment1=re.compile(r'/\*[\s\S]*?\*/',re.DOTALL)
	comment1Text=comment1.findall(string)
	for line in comment1Text:
		string=string.replace(line,'\n')
	comment2=re.compile(r'//[\s\S]*?\n')
	while r'//' in string:
		comment2Text=comment2.findall(string)
		for line in comment2Text:
			string = string.replace(line,'\n')
	return string.split('\n')
	
def writeFile(filename,myList):
	with open(filename,'w')as f:
		f.write(''.join(line.rstrip()+'\n' for line in myList if line.rstrip()!=''))
	
def writeFile(filename,myList):
	with open(filename,'w')as f:
		f.write(''.join(line.rstrip()+'\n' for line in myList if line.rstrip()!=''))
if __name__ == "__main__":
	
	lines=readFile('AcpiPState.c')
	str	= deleteCNote(lines)
	writeFile('debug.txt',str)
			