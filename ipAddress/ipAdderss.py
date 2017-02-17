import socket
def getIp():
	hostname=socket.gethostname()
	ip = socket.gethostbyname(hostname)
	return ip
if __name__ == '__main__':
	print(getIp())