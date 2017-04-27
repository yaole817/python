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

def getAllfile():
	scan	= ScanFile('.')
	files	= scan.scan_files()
	return files

def readFile(filename):
	with open(filename,'r')as f:
		lines	= f.readlines()
	return lines

def blockType(path):
	lines = readFile(path)
	base_name =''
	file_type =''
	for line in lines:
		if 'BASE_NAME'  in line:
			base_name = line.split('=')[-1].strip()
		if 'MODULE_TYPE' in line:
			file_type = line.split('=')[-1].strip()
	#print base_name,file_type
	return base_name,file_type

if __name__ == '__main__':
	path = 'D:\BIOS\BYO-A0CodeBase\\'
	#path = 'D:\BIOS\EDKII_Porting\\'
	os.chdir(path)


	filepathList = getAllfile()
	infPathList =  [x for x in filepathList if os.path.splitext(x)[1]=='.inf']
	for item in infPathList:
		#if 'ASIA' in item or 'Build' in item:
		#	continue
		base_name,file_type = blockType(item)
		infName = item.split('\\')[-1]
		if file_type == 'DXE_CORE':
			print infName



