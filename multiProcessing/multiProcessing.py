import os
#print("process (%s) start"%os.getpid())
#pid = os.fork()
#if pid == 0:
#	print('i am child process (%s) and parent is %s.'%(os.getpid(),os.getppid()))

from multiprocessing import Process
def run_proc(name):
	print("Run child process %s (%s)"%(name,os.getpid()))

if __name__ == '__main__':
	print("start multiprocessing...")
	print("Parant process %s."%os.getpid())
	p	= Process(target=run_proc,args=('test',))
	print('child process will start')
	p.start()
	p.join()
	print("child process end")
	print("end multiprocessing...")