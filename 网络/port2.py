#!/usr/bin/env python3

from __future__  import print_function
import  telnetlib
def conn_scan(ip,port):
	t=telnetlib.Telnet()
	try:
		t.open(ip,port,timeout=1)
		print(ip,port,"is avaliable")
	except Exception as e:
		print(ip,port,"is not avaliable")
	finally:
		t.close()

def main():
	ip="192.168.162.22"
	for port in range(20,100):
		conn_scan(ip,port)

if __name__=="__main__":
	main()
