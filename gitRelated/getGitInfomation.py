import os
import re
import time

def getWholeCommitString(): #get the whole infomation by use git command and tranfer to string
	wholeCommitInfo		= os.popen('git log --name-status')  
	wholeCommitContent	= wholeCommitInfo.readlines() #get the whole git log content 
	string				= ''.join(wholeCommitContent) #transfer to string
	return string #return is string

def getCommitBlock(string): # sperate commit string block by commit id
	string=string.replace("\ncommit","\ncommit\ncommit") 
	allChangeFilesRegex=re.compile(r'\ncommit\b[\s\S]+?\ncommit',re.DOTALL) #get commit log from one commit id,which include commit id,diff files, diff content etc.
	commitInfoList = allChangeFilesRegex.findall(string) #return list by commit id
	return commitInfoList #return is a list

def getCommitId(string): #input is string
	wholeCommitID	= re.findall(r'\ncommit (.*?)\n',string)#get the line of commit id 
	commitIDFilter=[item.strip() for item in wholeCommitID if re.search('[0-9a-fA-F]{40}',item)]  #get commit id from the line and return list
	return commitIDFilter

def getChangeFiles(string):
	changeFilesReg	= re.compile(r'diff --git(.*?)\n')#get the content of the change files in git log
	
	changeFiles		= changeFilesReg.findall(string)
	changeFiles		= [item.split()[1][1:] for item in changeFiles]#split the change files
	return changeFiles #return is a list
def getChangeFilesNew(string):
	changeFilesReg	= re.compile(r'\n[MAD]\t[\s\S]*?\n',re.DOTALL)#get the content of the change files in git log
	
	changeFiles		= changeFilesReg.findall(string)
	changeFiles		= [item[2:].strip() for item in changeFiles]#split the change files
	return changeFiles #return is a list
def getAuthor(string): #get author infomation
	authorReg	= re.compile(r'Author:[\s\S]*?<[\s\S]+?>\n')
	authorContent = [re.search(r'<(.*?)>',item).group()[1:-1] for item in authorReg.findall(string)]
	return authorContent #return is a list
	
def getTime(string): #get the time of commite, and transfer to standard format
	timeReg		= re.compile(r"[\s\S]{3} [\s\S]{3} [0-9]{1,2} [0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{4}")
	commitTime	= [time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(item.split('\n')[0].replace('Date:','').strip(),r'%a %b %d %H:%M:%S %Y')) for item in timeReg.findall(string)]
	return commitTime #return is a list
	 
def getCommitMessage(string): # split commit message from commit infomation string
	commitPartReg 	= re.compile(r'\bDate[\s\S]+?\n\n[\s\S]*\n\n',re.DOTALL)
	commitContent	= [item.split('\n')[2].strip() for item in commitPartReg.findall(string)]
	return commitContent #return is a list

workPath	= r'D:\BIOS\CHX001-IOE\BYO-A0CodeBase\AsiaPkg\Asia'
if __name__ == "__main__":
	os.chdir(workPath)			#change the path to project path
	
	string = getWholeCommitString() 
	#print(string)
	
	#exit()
	commitBlock=getCommitBlock(string) #split block by commit id 

	for item in commitBlock: 
		print('{0:25}{1:30}{2:20}'.format(''.join(getTime(item)),''.join(getAuthor(item)),'\t'.join(getCommitId(item))))
		print('    commit message:   '+''.join(getCommitMessage(item)))
		for line in getChangeFilesNew(item):
			print('    '+line)
		#if '(YSW-2016010601) Force PEG to x2 Link-Width Capability for avoiding CND003_A0 Credit Design Issue' in item:
		#	print(item)
		#	exit()



