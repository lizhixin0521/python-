#!/usr/bin/env python3

#折半查找
val=int(input(">>>"))
if val>=1000:
	if val>=10000:
		print("五位")
		a=val//10000
		b=(val%10000)//1000
		c=(val%10000%1000)//100
		d=(val%10000%1000%100)//10
		e=(val%10000%1000%100%10)//1
		print(a,b,c,d,e)
	else:
		print("四位")
		print("个十百千")
		for i in range(4):
			print(val%10)
			val=val//10
else:
	if val>=100:
		print("三位")
		j=100
		for i in range(3):
			print(val//j)
			val=val%j
			j//=10
	elif val>=10:
		print("二位")
		pre=0
		for i in range(2,0,-1):
			cur=val//(10**(i-1))
			print(cur-pre*10)
			pre=cur
	else:
		print("一位")
		print(val)
