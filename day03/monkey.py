#!/usr/bin/env python3
def monkey(num=1,day=9):
	num=(num+1)*2
	if day==1:
		return num
	return monkey(num,day-1)
#num=1
#for i in range(9,0,-1):
#	num=(num+1)*2
#print(num)
print(monkey())
