import pandas as pd

s = pd.Series([1,2,3],index = ['a','b','c']) # create a series

d = pd.DataFrame([[1,2,3],[4,5,6]],columns = ['a','b','c']) # create a table

d2 = pd.DataFrame(s)
print s

print d.head()

print d.describe()

excel  = pd.read_excel('data.xlsx')

print excel

csv = pd.read_csv('data.csv',encoding = 'utf-8')

print csv