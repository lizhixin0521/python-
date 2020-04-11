#!/usr/bin/env python3
import http.client
import dns.resolver

A=dns.resolver.query('www.lizhixin.net','A')
for i in A.response.answer:
	ip=i.items[0].address
	print(ip)
	conn=http.client.HTTPConnection(ip)
	try:
		conn.request('GET','/monitor.html')
		r=conn.getresponse()
		print(r.read(6).decode("utf-8"))
		if r.read(6).decode("utf-8")=='<html>':
			print("web ok")
	except:
		print('web down')
		
