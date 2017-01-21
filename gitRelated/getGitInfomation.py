import os
import re
import time

def findCommitId(string): #input is string
	wholeCommitID	= re.findall(r'commit(.*?)\n',string)#get the line of commit id 
	commitIDFilter=[item.strip() for item in wholeCommitID if re.search('[0-9a-fA-F]{40}',item)]  #get commit id from the line and return list
	return commitIDFilter
def findCommitModule(string):
	string=string.replace("\ncommit","\ncommitcommit")
	allChangeFilesRegex=re.compile(r'commit\b[\s\S]+?\ncommit',re.DOTALL) #get commit log from one commit id,which include commit id,diff files, diff content etc.
	commitInfoList = allChangeFilesRegex.findall(string) #return list by commit id
	return commitInfoList
	
def findChangeFiles(string):
	changeFilesReg	= re.compile(r'--git(.*?)index',re.DOTALL)#get the content of the change files in git log
	
	changeFiles		= changeFilesReg.findall(string)
	changeFiles		= [item.split()[0][1:] for item in changeFiles]#split the change files
	return changeFiles
	
def findAuthor(string): #get author infomation
	authorReg	= re.compile(r'Author:[\s\S]*?<[\s\S]+?.com>')
	authorContent = [re.search(r'<(.*?)>',item).group()[1:-1] for item in authorReg.findall(string)]
	return authorContent
	
def findTime(string):
	timePattern	= re.compile(r"[\s\S]{3} [\s\S]{3} [0-9]{1,2} [0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{4}")
	commitTime	= [time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(item.split('\n')[0].replace('Date:','').strip(),r'%a %b %d %H:%M:%S %Y')) for item in timePattern.findall(string)]
	return commitTime
def findCommitMessage(text):
	commitPartReg 	= re.compile(r'\bDate[\s\S]+?\n\n[\s\S]*\n\n',re.DOTALL)
	commitContent	= [item.split('\n')[2].strip() for item in commitPartReg.findall(text)]
	return commitContent


if __name__ == "__main__":
	wholeCommitInfo=os.popen('git log -p')  
	wholeCommitContent=wholeCommitInfo.readlines() #get the whole git log content 
	string		= ''.join(wholeCommitContent) #transfer to string

	#commitID	= findCommitId(string)
	#for item in commitID:
	#	print(item)
	commitModule=findCommitModule(string) #split modules by commit id 
	#print(commitModule[0])
	for item in commitModule:
		print('{0:25}{1:25}{2:20}'.format(''.join(findTime(item)),''.join(findAuthor(item)),''.join(findCommitId(item))))
		print('  commit message:'+''.join(findCommitMessage(item)))
		for line in findChangeFiles(item):
			print('    '+line)
		#if r'Revert "Patch RTC read RxA-D patch"' in item:
		#	print(item)
		#	exit()
	exit()
	print(''.join(findCommitMessage(commitModule)),''.join(findTime(commitModule)))
	exit()
	authorList = findAuthor(string)
	for item in authorList:
		print(item)
	
	print(findAuthor(commitModule[0]))
	for one in commitModule:
		if '9606b870f110e53619819980f44d9f2af312aead' in findCommitId(one):
			print(one)
			
		#print(findCommitId(one)) 
		#for item in findChangeFiles(one):
			#print(item)