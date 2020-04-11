#!/usr/bin/env python3 
#阶乘
num=int(input("请输入您要的阶乘："))
sum=1
j=0
for i in range(1,num+1):
	sum*=i
	j+=sum
print(j)
