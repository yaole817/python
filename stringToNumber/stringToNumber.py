import string
a='C00|88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 '
c=a.replace('|',' ')
b=c.split(' ')
bb=string.atoi(b[3])>>3

decodeWithHex = int('0x88',16) # decode 0x88 with base16, and return base10
print('0x88 decodeWithHex = %d'%decodeWithHex) # print 136

stringToDec = int('88',10)  #return 88 
print('88 transferToDec = %d'%stringToDec) # print 88

numberToHex = hex(456)  #the par can only be number,and return 0x1c8
print('456 numberToHex = %s'%numberToHex) # print 0x1c8

numToBinary = bin(456)  #the parameter can only be number,return 0b111001000
print('456 numToBinary = %s'%numToBinary) # print 0b111001000
