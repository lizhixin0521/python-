#!/usr/bin/env python3
#编写一个函数，接受一个参数n,n是整数，打印数字三角
def san(n,num=""):
	for i in range(1,n+1):
		c="   "*(n-i)
		if i>=10:
			num=str(i)+" "+num
		else:
			num=str(i)+"  "+num
		print(c+num)
san(12)
