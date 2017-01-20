import os
import re

reNum=re.compile('[0-9a-fA-F]')
def exractCommitInfo():
	commitAllInfor		= os.popen(r"git log --oneline --graph")
	commitAllInforList	= commitAllInfor.readlines()
	list=[]
	for m in commitAllInforList:
		str=''
		for index in range(len(m)):
			if(reNum.match(m[index])):
				str=m[index:]
				break
		if(str):list.append(str)

	commitIdList=[]
	for line in list:
		commitId=line[0:7]
		commitInfo=line[7:].strip()
		set=(commitId,commitInfo)
		commitIdList.append(set)
	return commitIdList
if __name__ == "__main__":
	list=exractCommitInfo()
	
	for line in list:
		#print(line[0])
		print(line[1])
	print(len(list))
