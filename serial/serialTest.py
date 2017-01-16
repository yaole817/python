
#!/usr/bin/env python
import serial
import time
import thread

class MSerialPort:
	message=''
	def __init__(self,port,buand):
		self.port=serial.Serial(port,buand)
		if not self.port.isOpen():
			self.port.open()
	def port_open(self):
		if not self.port.isOpen():
			self.port.open()
	def port_close(self):
		self.port.close()
	def send_data(self,data):
		number=self.write(data)
		return number
	def read_data(self):
		data=''
		while True:
			data=self.port.readline()
			self.message+=data
if __name__=='__main__':
	mSerial=MSerialPort('com5',115200)
	thread.start_new_thread(mSerial.read_data,())
	outputList=[]
	with open('output.txt','w')as f:
		while True:
			time.sleep(0.1)
			receiveMessage= mSerial.message
			if(receiveMessage!=''):
				f.write(receiveMessage)
				#outputList.append()
				print(receiveMessage.strip())





