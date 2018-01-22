import tushare as ts

myStockData = ts.get_realtime_quotes("300445")

ts.get_tick_data("600096",date= "2017-06-26")
#
# some thing that is really useful
# 


data = ts.get_hist_data("600096",start = '2017-06-23',end="2017-06-26")
# return type
# date：日期
# open：开盘价
# high：最高价
# close：收盘价
# low：最低价
# volume：成交量
# price_change：价格变动
# p_change：涨跌幅
# ma5：5日均价
# ma10：10日均价
# ma20:20日均价
# v_ma5:5日均量
# v_ma10:10日均量
# v_ma20:20日均量
# turnover:换手率[注：指数无此项]

#print myStockData.value
for key in myStockData:
	print(myStockData[key])