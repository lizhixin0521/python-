#!/usr/bin/env python3
#输入五个数，打印每位数的位数，将这些数字排序打印，要求升序打印
print("请输入5个数")
nums=[]
for i in range(5):
	num=input("输入第{}位数：".format(i+1)).strip().lstrip()
	nums.append(num)
nums.sort()
for j in nums:
	print("{},{}位数".format(j,len(j)))
