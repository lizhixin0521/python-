#!/usr/bin/env python3
import subprocess
import threading
from queue import Queue
from queue import Empty

def call_ping(ip):
	if subprocess.call(["ping","-c","1",ip]):
		print("{0}is alive".format(ip))
	else:
		print("{0}is unreacheable".format(ip))


def is_reacheable(q):
	try:
		while True:
			ip=q.get_nowait()
			call_ping(ip)
	except Empty:
		pass

def main():
	q=Queue()
	with open("ip.txt","r") as f:
		for line in f:
			q.put(line)
	threads=[]
	for i in range(10):
		thr=threading.Thread(target=is_reacheable,args=(q,))
		thr.start()
		threads.append(thr)
		for thr in threads:
			thr.join()

if  __name__=='__main__':
	main()

