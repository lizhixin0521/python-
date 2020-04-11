#!/usr/bin/env python3
def sayHi(name):
	print("hi %s"%name)
with open("./user_info.txt",'r')as f:
	for i in f.readlines():
		i=i.split()[1]
		sayHi(i)
	f.close()
