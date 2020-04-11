#!/usr/bin/env python3
import dns.resolver

#A记录查询
A=dns.resolver.query('www.lizhixin.net','A')
#print(A.response.answer)
for i in A.response.answer:
	print(i)

#邮件服务器
B=dns.resolver.query('lizhixin.net','MX')
for i in B.response.answer:
	print(i)


#CNAME别名
C=dns.resolver.query('ftp.lizhixin.net','CNAME')
for i in C.response.answer:
	print(i)

