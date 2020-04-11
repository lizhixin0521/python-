#!/usr/bin/env python3

from __future__  import print_function
from socket import *
def conn_scan(ip,port):
	conn=socket(AF_INET,SOCK_STREAM)
	try:
		conn.connect((ip,port))
		print(ip,port,"is avaliable")
	except Exception as e:
		print(ip,port,"is not avaliable")
	finally:
		conn.close()

def main():
	ip="192.168.162.22"
	for port in range(20,100):
		conn_scan(ip,port)

if __name__=="__main__":
	main()
