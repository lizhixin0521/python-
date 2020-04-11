#!/usr/bin/env python3
#打印正方形
n=input("正方形的边长：")
n=int(n)
for i in range(n):
	if i==0 or i==n-1:
		for j in range(n):
			print("x",end='')
	#elif i==n-1:
	#	for j in range(n):
	#		print("x",end='')
	else:
		print("x"+(' '*(n-2))+"x",end='')
	print('')
