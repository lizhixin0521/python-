#!/usr/bin/env python3
import subprocess
import threading
def is_reacheable(ip):
	if subprocess.call(["ping","-c","1",ip]):
		print("{0}is alive".format(ip))
	else:
		print("{0}is unreacheable".format(ip))


def main():
	with open("ip.txt","r") as f:
		lines=f.readlines()
		thread=[]
		for line in lines:
			thr=threading.Thread(target=is_reacheable,args=(line,))
			thr.start()
			thread.append(thr)
		for thr in thread:
			thr.join()

if  __name__=='__main__':
	main()



