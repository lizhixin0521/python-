#!/usr/bin/env python3
#质数
num=int(input("请输入一个你要判断的数："))
for i in range(2,num):
	if num%i==0:
		print("该数不是质数！")
		break
else:
	print("该数是质数")
