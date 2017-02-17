import string
a='C00|88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 88 '
c=a.replace('|',' ')
b=c.split(' ')
bb=string.atoi(b[3])>>3