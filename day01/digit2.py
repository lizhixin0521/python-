#!/usr/bin/env python3

#折半查找
val=int(input(">>>"))
if val>=1000:
	if val>=10000:
		print("五位")
	else:
		print("四位")
else:
	if val>=100:
		print("三位")
	elif val>=10:
		print("二位")
	else:
		print("一位")
