import tushare as ts

myStockData = ts.get_realtime_quotes("600096")
#print myStockData

#print myStockData.value
for key in myStockData:
	print myStockData[key]