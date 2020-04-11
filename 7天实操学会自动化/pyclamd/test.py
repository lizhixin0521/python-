#!/usr/bin/env python3

import pyclamd

ips=["192.168.162.22"]
for ip in ips:
	cd=pyclamd.ClamdNetworkSocket(ip,3310)
	if cd.ping():
		print(ip+"is alive")
		print(cd.scan_file('/home/lizhixin'))
	else:
		print(ip+"error")
