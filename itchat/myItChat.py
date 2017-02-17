import time
import itchat
import datetime
import tushare as ts

stock_symbol = 'SZ300104'

def login():
	itchat.auto_login()
def stock():
	time = datetime.datetime.now()
	print(time)
	now	 = time.strftime('%H:%M:%S')
	print(now)
	data = ts.get_realtime_quotes(stock_symbol)
def text_reply(msg):
    itchat.send(msg['Text'], msg['FromUserName'])
if __name__ == '__main__':
	login()
	itchat.run()
	