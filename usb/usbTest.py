#!/usr/bin/python
#-*-coding:utf-8 -*-

import pywinusb.hid as hid

class hidHelper(object):
    def __init__(self, vid=0x046D, pid=0xC077):
		self.alive	= False
		self.device = None
		self.report = None
		self.vid 	= vid
		self.pid 	= pid
    def start(self):
        _filter = hid.HidDeviceFilter(vendor_id = self.vid, product_id = self.pid)
        hid_device = _filter.get_devices()
        if len(hid_device) > 0:
			print("success")
			self.device = hid_device[0]
			self.device.open()
			self.report = self.device.find_output_reports()
			self.alive = True
    def stop(self):
        self.alive = False
        if self.device:
			self.device.close()
    def setcallback(self):
        '''
        设置接收数据回调函数
        '''
        if self.device:
			self.device.set_raw_data_handler(self.read)
    def read(self, data):
        '''
        接收数据回调函数
        '''
        print([hex(item).upper() for item in data[1:]]) 
    def write(self, send_list):
        '''
        向HID设备发送数据
        '''
        if self.device:
            if self.report:
                self.report[0].set_raw_data(send_list)
                bytes_num = self.report[0].send()
                return bytes_num
if __name__ == '__main__':
	myhid = hidHelper()
	myhid.start()
	if myhid.alive:
		hid.setcallback()
		send_list = [0x00 for i in range(65)]
		myhid.write(send_list)
        import time
        time.sleep(0.5)
        myhid.stop()