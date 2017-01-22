import os
import re
import time

def getCommitBlock(string):
	string=string.replace("\ncommit","\ncommit\ncommit")
	allChangeFilesRegex=re.compile(r'\ncommit\b[\s\S]+?\ncommit',re.DOTALL) #get commit log from one commit id,which include commit id,diff files, diff content etc.
	commitInfoList = allChangeFilesRegex.findall(string) #return list by commit id
	return commitInfoList

def getCommitId(string): #input is string
	wholeCommitID	= re.findall(r'\ncommit (.*?)\n',string)#get the line of commit id 
	commitIDFilter=[item.strip() for item in wholeCommitID if re.search('[0-9a-fA-F]{40}',item)]  #get commit id from the line and return list
	return commitIDFilter

def getChangeFiles(string):
	changeFilesReg	= re.compile(r'diff --git(.*?)\n')#get the content of the change files in git log
	
	changeFiles		= changeFilesReg.findall(string)
	changeFiles		= [item.split()[1][1:] for item in changeFiles]#split the change files
	return changeFiles
	
def getAuthor(string): #get author infomation
	authorReg	= re.compile(r'Author:[\s\S]*?<[\s\S]+.com>')
	authorContent = [re.search(r'<(.*?)>',item).group()[1:-1] for item in authorReg.findall(string)]
	return authorContent
	
def getTime(string): #get the time of commite, and transfer to standard format
	timeReg		= re.compile(r"[\s\S]{3} [\s\S]{3} [0-9]{1,2} [0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{4}")
	commitTime	= [time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(item.split('\n')[0].replace('Date:','').strip(),r'%a %b %d %H:%M:%S %Y')) for item in timeReg.findall(string)]
	return commitTime
	
def getCommitMessage(string):
	commitPartReg 	= re.compile(r'\bDate[\s\S]+?\n\n[\s\S]*\n\n',re.DOTALL)
	commitContent	= [item.split('\n')[2].strip() for item in commitPartReg.findall(string)]
	return commitContent


if __name__ == "__main__":
	wholeCommitInfo=os.popen('git log -p')  
	wholeCommitContent=wholeCommitInfo.readlines() #get the whole git log content 
	string		= ''.join(wholeCommitContent) #transfer to string

	#commitID	= findCommitId(string)
	#for item in commitID:
	#	print(item)
	commitBlock=getCommitBlock(string) #split modules by commit id 
	for item in commitBlock:
		print('{0:25}{1:25}{2:20}'.format(''.join(getTime(item)),''.join(getAuthor(item)),'\t'.join(getCommitId(item))))
		print('    commit message:   '+''.join(getCommitMessage(item)))
		for line in getChangeFiles(item):
			print('    '+line)
		#if r'd49614a0a86da0c87ae73650f87b06a5ec666be8' in item:
		#	print(item)
		#	exit()
	exit()
	print(''.join(getCommitMessage(commitBlock)),''.join(getTime(commitBlock)))
	exit()
	authorList = getAuthor(string)
	for item in authorList:
		print(item)
	
	print(getAuthor(commitBlock[0]))
	for one in commitBlock:
		if '9606b870f110e53619819980f44d9f2af312aead' in getCommitId(one):
			print(one)
			
		#print(findCommitId(one)) 
		#for item in findChangeFiles(one):
			#print(item)