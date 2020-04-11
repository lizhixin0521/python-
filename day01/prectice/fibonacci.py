#!/usr/bin/env python3
#斐波那契数列
a,b,c=0,0,1
max=10
while a<max:
	print(c)
	b,c=c,c+b
	#b=c
	a+=1
