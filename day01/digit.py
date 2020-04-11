#!/usr/bin/env python3
num=int(input("请输入你要判断的整数:"))
a=num%10
if a==num:
	print("一位数")
else:
	if 10<=num<=99:
		print("二位数")
	elif 100<=num<=999:
		print("三位数")
	else:
		print("四位以上")
