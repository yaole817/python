#!/usr/bin/python
#-*-coding:utf-8 -*-


import os
import re
import sys
##############################################################################
####
####		正则表达式，匹配双引号中间的字符
####
##############################################################################

pattern = re.compile('"(.*)"') 

ReleaseText = 'tag:'

#############################################################################

def translateStr(string):
####################################################
##		将byte类型转换为字符并剔除byte为0 的字符
##
#####################################################
	s = ''
	for i in range(len(string)):
		if(string[i]==0 or string[i]>127):continue
		s += chr(string[i])
	return s

def readFileAsAscii(filename):
##########################################################
###
###		读取文件并提取纯英文字符
###
#################################################################
	lineList	= []
	with open(filename,'rb') as f:
		lines=f.readlines()
		for i in lines:
			lineNew		= translateStr(i).strip()
			lineList.append(lineNew)
	return lineList
def readFileAsBinary(filename):
	with open(filename,'rb') as f:
		lines=f.readlines()
	return lines
	

def getTagInformation(string):
##############################################################################
####
####		从字符串中提取提取tag信息，返回tag值
####
##############################################################################
	
	tagString = ''
	if ReleaseText in string:
		tagStringList = string
		tagIndex = 0
		tagStringListSplit=tagStringList.split()
		while True:
			tagIndex = tagStringListSplit.index(ReleaseText)+1
			if ReleaseText in string:
				if r'R' in tagStringListSplit[tagIndex]:break
			else:break
			tagStringListSplit = tagStringListSplit[tagIndex:]
		return tagStringListSplit[tagIndex].replace(',','')
	else:return False


	
def getMotherBoardName(list,biosVison,mothreBoard):
##############################################################################
####
####		从字符串中提取BIOS Version
####
##############################################################################
	motherBoardName = ''
	for num in range(len(list)):
		if r'STR_MISC_BIOS_VERSION' in list[num]:
			motherBoardName		= pattern.search(list[num])
			if motherBoardName :
				motherBoardName = motherBoardName.group().replace('\"','')
				cutOffIndex	= motherBoardName.index('-')+1
				biosVersionName = mothreBoard+'-'+biosVison
				list[num]= list[num].replace(motherBoardName,biosVersionName)
				break
	return list,num
def writeFile(filename,list):
##############################################################################
####
####		写文件，将处理好的文件写回到原来文件中
####
##############################################################################
	with open(filename,'wb') as f:
		for i in list:
			f.write(i)	

timePatten = re.compile(r'\d{4}-\d{2}-\d{2}')
def getTimeInformation(string):
##############################################################################
####
####		分离时间
####
##############################################################################	
	timeString		= timePatten.search(string).group(0)
	year = timeString[:4]
	mouth = timeString[5:7]
	day	= timeString[8:10]
	return year,mouth,day
	
	
timeReversePatten = re.compile(r'\d{2}/\d{2}/\d{4}')
def replaceBiosReleaseDate(list,year,mouth,day):
##############################################################################
####
####		将时间改为commit的时间
####
##############################################################################
	for num in range(len(list)):
		if r'STR_MISC_BIOS_RELEASE_DATE' in list[num]:
			biosReleaseDate		= timeReversePatten.search(list[num]).group(0)
			#print(biosReleaseDate)
			newdata				= day+'/'+mouth+'/'+year;
			list[num]			= list[num].replace(biosReleaseDate,newdata)
			break
	return list,num
def replaceBinaryString(string):
	s=b''
	#print(string)
	for j in range(len(string)):
		s+=b'\x00'+string[j].encode('utf-8')
	return s+b"\x00\n"
	
	
biosNamePath = '..\Project\Kunlun\ZXD\Build\BiosInfo.uni'
if __name__ == "__main__":
	
	if os.path.exists("..\.git") == False:    #如果不是git工程，则退出
		print("Error :  this is not a git project")
		exit()   
	#####################################################################################
	##
	## 				以下是对于non-Asia部分的版本号获取的处理
	##
	#####################################################################################
	commitInfor			= os.popen(r"git rev-parse HEAD")
	commitShort			= commitInfor.read()[:7]
	
	commitAllInfor		= os.popen(r"git log --oneline --decorate --graph")
	commitAllInforList	= commitAllInfor.readline()
	
	commitTimeInfor		= os.popen(r'git log --pretty=format:%ci').readline()
	year,mouth,day		= getTimeInformation(commitTimeInfor)
	
	if ReleaseText in commitAllInforList:
		biosName = 'nonAisa-'+ getTagInformation(commitAllInforList) 
	else:
		biosName = 'nonAsia-'+'D' + commitShort
	#####################################################################################
	##
	## 				以下是对于Asia部分的版本号获取的处理
	##
	#####################################################################################
	os.chdir("..\ASIA")
	asisCommitInfor			= os.popen(r"git rev-parse HEAD")
	asiaCommitShort			= asisCommitInfor.read()[:7]
	
	asiaCommitAllInfor		= os.popen(r"git log --oneline --decorate --graph")
	asiaCommitAllInforList	= asiaCommitAllInfor.readline()
	
	asiaCommitTimeInfor		= os.popen(r'git log --pretty=format:%ci').readline()
	year,mouth,day			= getTimeInformation(commitTimeInfor)
	
	if ReleaseText in asiaCommitAllInforList:
		biosName += '(Aias-' + getTagInformation(asiaCommitAllInforList)+')' 
	else:
		biosName += '(Aias-'+'D' + asiaCommitShort+')'
	#os.chdir("..\biosName")
	#####################################################################################
	##
	## 				以下是对于文件的处理
	##
	#####################################################################################
	binaryFileList		= readFileAsBinary(biosNamePath)
	
	pureEnglishSource 	= readFileAsAscii(biosNamePath)
	
	motherBoardName		= sys.argv[1]
	
	list,indexNum	= getMotherBoardName(pureEnglishSource,biosName,motherBoardName)
	binaryFileList[indexNum] = replaceBinaryString(pureEnglishSource[indexNum])
	
	list,indexNum	= replaceBiosReleaseDate(list,year,mouth,day)
	binaryFileList[indexNum] = replaceBinaryString(pureEnglishSource[indexNum])
	
	writeFile(biosNamePath,binaryFileList)
	

	