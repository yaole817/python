#coding=utf-8
import re

def readFile(filepath):
    with open(filepath,'rb') as f:
        return f.readlines()

filePathCH = "chinese.txt"
chinesePattern = re.compile(r'[\u4E00-\u9FA5\s]+')
# chinesePattern = re.compile(r'[你]+')
def extractChinesCharacter(string):
    return chinesePattern.findall(string)
if __name__ == "__main__":
    contentCh = readFile(filePathCH)
    for line in contentCh:
        line = line.decode('utf-8')
        print(','.join(extractChinesCharacter(line)))
