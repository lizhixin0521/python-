#!/usr/bin/env python3
#输入一位数判断是几位数
#打印每一位数字及其重复的次数，打印顺序个、十、百

while True:
	num=input("请输入数字：")
	if num.isdigit():
		break
print("该数字是{}位数".format(len(num)))
a=[]
for i in num:
	a.append(i)
a.reverse()
for j in a:
	print("{} 数字出现{}".format(j,a.count(j)))
