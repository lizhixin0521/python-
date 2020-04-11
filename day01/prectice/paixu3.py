#!/usr/bin/env python3
num_list=[1,8,5,6,4,3,9,2,7]
nums=len(num_list)
#flag=False
for i in range(nums):#多少次全部比较出大小（循环一次比较出一个）
	flag=False
	for j in range(nums-i-1):
		if num_list[j]>num_list[j+1]:
			tmp=num_list[j]
			num_list[j]=num_list[j+1]
			num_list[j+1]=tmp
			flag=True
	if not flag:
		break
print(num_list)
