#!/usr/bin/env python3
num=[]
for i in range(3):
	num.append(int(input('第{}个数:'.format(i+1))))
num.sort(reverse=False)
