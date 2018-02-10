import xlrd
import re
from Debug import Debug as Debug

class KeyWordSit():
    def __init__(self, label):
        self.__label = label

    def getSite(self, keyword):
        return self.getKeyWordSite(keyword)

    def getKeyWordSite(self, keyWord):
        i = 0
        for item in self.__label:
            if keyWord == item:
                return i
            i += 1

class SpeValue(object):
    def __init__(self):
        pass
    
    @property
    def initValue(self):
        return '-'

    @property
    def hwInitValue(self):
        return 'N'
    
    @property
    def romsipValue(self):
        return 'M'
    
    @property
    def dipValue(self):
        return 'D'

    def speValue(self, speString, lengthList):
        targetLength = int(lengthList[0]) - int(lengthList[-1]) + 1
        if type(speString) == type(0.0):  ## if default value is float, than it will be treated as a binary number
            currentNum = str(int(speString))
            currentNum = str(bin(int(currentNum, 2)))[2:]
            currentNumLength = len(currentNum)
            return ('0' * (targetLength  - currentNumLength) + currentNum)[::-1]
        
        elif speString.strip() == '':   ## SPE value is empty
            return self.initValue * targetLength
        
        elif speString.upper() == 'X':  ## SPE value is X
            return 'X' * targetLength
            
        elif speString.upper() == 'R':  ## SPE value is R
            return 'R' * targetLength

        elif '*' in speString.upper():  ## remove "*" in SPE value
            return self.speValue(speString.replace('*', ''), lengthList)
        
        elif 'HWINIT' in speString.upper():
            return self.hwInitValue * targetLength
        
        elif 'ROMSIP' in speString.upper():
            return self.romsipValue * targetLength

        elif 'DIP' in speString.upper():
            return self.dipValue * targetLength

        elif 'H' in speString.upper():  ## SPE value coding in Hexadecimal-coded
            currentNum = speString.upper().replace('H', '')
            currentNum = str(bin(int(currentNum, 16)))[2:]
            currentNumLength = len(currentNum)
            return ('0' * (targetLength  - currentNumLength) + currentNum)[::-1]

        elif 'B' in speString.upper():  ## SPE value coding in binary-coded
            currentNum = speString.upper().replace('B', '')
            currentNum = str(bin(int(currentNum, 2)))[2:]
            currentNumLength = len(currentNum)  
            return ('0' * (targetLength  - currentNumLength) + currentNum)[::-1]
        
        else:                           
            try:                        ##if all above is not matched， try coding in 10-coded return success
                currentNum = str(bin(int(speString, 2)))[2:]
                currentNumLength = len(currentNum)
                return ('0' * (targetLength  - currentNumLength) + currentNum)[::-1]
            except:                    ## raise a error if failed 
                raise Exception("SPE Value Error")
            # return speString.upper()[:targetLength]
class ParseOneSheet(object):
    def __init__(self, excel, sheetName, speType):

        self.__sheetName = sheetName
        self.__speType = speType
        self.__table = excel.sheet_by_name(self.__sheetName)
        self.__label = self.__table.row_values(0)

        self.__speValue = SpeValue()
        self.__initValue =self.__speValue.initValue

        keyWordSit = KeyWordSit(self.__label)
        self.regOffsetSite = keyWordSit.getSite("Reg_Offset")
        self.regBitSite  = keyWordSit.getSite("Reg_Bit")
        self.keywordValueSite = keyWordSit.getSite(self.__speType)
        
        self.__minOffset = self.minOffset
        self.__register = self.createInitTable 
        
        for row in range(self.rowsLength):
            self.handleOneRow(row)

    def __str__(self):
        return self.__sheetName

    def keywordValueTable(self, rowValue):
        return rowValue[self.keywordValueSite]

    @property
    def rowsLength(self):
        return self.__table.nrows 

    @property
    def colsLength(self):
        return self.__table.ncols

    @property
    def createInitTable(self): # create a table for the function
        return [self.__initValue] * ((self.maxOffset - self.__minOffset + 1) * 8)

    @property
    def registerValue(self):
        return ''.join(self.__register)

    @property
    def maxOffset(self):
        _regOffsetList = self.__table.col_values(self.regOffsetSite)
        _regOffsetList = '\n'.join(_regOffsetList).strip().split('\n')  
        _maxRegOffset, _ = self.regOffsetValue(_regOffsetList[-1])
        return int(_maxRegOffset, 16)
    
    @property
    def minOffset(self):
        _regOffsetList = self.__table.col_values(self.regOffsetSite)[1:]
        _regOffsetList = '\n'.join(_regOffsetList).strip().split('\n')  
        _, _minRegOffset = self.regOffsetValue(_regOffsetList[0])
        return int(_minRegOffset, 16)
        
    def regOffsetValue(self, offset):
        register = re.findall(r'[0-9a-fA-F]+', offset)
        if len(register) > 0:
            return register[0], register[-1]  # max register, min register
        return None, None

    def bitOffet(self, offset):
        bitNmuberList = re.findall(r'\d+', offset)
        if len(bitNmuberList) == 2 or len(bitNmuberList) == 1:
            return bitNmuberList # max bit number, min bit number
        else:
            raise Exception("Bit error")

    def handleOneRow(self, row):
        rowValue = self.__table.row_values(row)
        maxRegister, minRegister = self.regOffsetValue(rowValue[self.regOffsetSite])

        if 'bit' in rowValue[self.regBitSite]:
            bitList = self.bitOffet(rowValue[self.regBitSite])
            bitLength = int(bitList[0]) - int(bitList[-1]) + 1
            offset = int(minRegister, 16) * 8 + int(bitList[-1]) - self.__minOffset
            debug.debug("Sheet Name: {}, Offset: {}, BIT: {}, Length: {}, {} is: {}".format(
                         self.__sheetName,
                         rowValue[self.regOffsetSite], 
                         rowValue[self.regBitSite],
                         bitLength,
                         self.__speType,
                         self.keywordValueTable(rowValue)))
            self.__register[offset : offset + bitLength] = list(self.__speValue.speValue(self.keywordValueTable(rowValue), bitList))
            
            if type(self.keywordValueTable(rowValue)) == type('string') and 'DIP' in self.keywordValueTable(rowValue).upper():
                warning.warning("Sheet Name: {}, Offset: {}, BIT: {}, Length: {}, {} is: {}".format(
                         self.__sheetName,
                         rowValue[self.regOffsetSite], 
                         rowValue[self.regBitSite],
                         bitLength,
                         self.__speType,
                         self.keywordValueTable(rowValue)))

                         
class ParseSPEExcel(object):
    def __init__(self, excelName):
        self.__excelName = excelName
        self.__excel = xlrd.open_workbook(self.__excelName)
        self.__sheets = self.__excel.sheets()
        self.__sheetNames = self.__excel.sheet_names()
        self.__excleTable = []
        
    def __str__(self):
        return self.__excelName
    
    @property
    def tableValue(self):
        return __excleTable

    def sheetsValue(self, value):
        print(value + ' Mode')
        for name in self.__sheetNames:
            if '@' in name:
                continue
            table = ParseOneSheet(self.__excel, name, value)
            self.__excleTable.append([table, table.minOffset, table.registerValue])
    
    @property
    def smallEndTable(self):
        sheets = []
        for table in self.__excleTable:
            [name, offset, sheetTables] = table
            sheetTable = re.findall('.{8}', sheetTables)
            
            sheetTable = [item[::-1] for item in sheetTable]
            sheets.append([name, offset, sheetTable])
        return sheets

    def showSmallEndTable(self):
        for sheet in self.smallEndTable:
            [name, offset, sheetTable] = sheet
            print("#Name, Offset, Length: {}, {}, {}".format(name, offset, len(sheetTable) * 8))
            i = 0
            for item in sheetTable:
                i += 1
                print(item + ' ', end = '')
                if i % 16 == 0:
                    print(' ')
            print(' ')


if __name__ == "__main__":
    import sys
    import os
    import logging
    
    if os.path.exists('myapp.log'):
	    os.remove('myapp.log')
    if os.path.exists('warning.log'):
        os.remove('warning.log')
    
    debug = Debug('Log', 'myapp.log', logging.DEBUG)
    warning = Debug('Dip Warning', 'warning.log', logging.WARNING)

    excelName = sys.argv[1]
    excel = ParseSPEExcel(excelName)
    print(excel)

    excel.sheetsValue("SW_S")
    excel.showSmallEndTable()

    excel.sheetsValue("SW_P")
    excel.showSmallEndTable()

    excel.sheetsValue("SW_E")
    excel.showSmallEndTable()

    excel.sheetsValue("Default Value")
    excel.showSmallEndTable()

    

