#!/usr/bin/env python3
import nmap

def nmap_ping_scan(np,ps):
	nm=nmap.PortScanner()
	ping_result=nm.scan(hosts=np,arguments='-v -sS -p '+ps)
	print(ping_result)
	for host in nm.all_hosts():
		print("Host:%s (%s)"%(host,nm[host].hostname()))
		print("State:%s"%(nm[host].state()))

if __name__=='__main__':
	nmap_ping_scan("192.168.162.0/24",'22')
