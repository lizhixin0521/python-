#!/usr/bin/env  python3
#sum=1 #用不到此变量  作用域问题
def jc(n,sum=1):
	sum=sum*n
	#print("sum:",sum)
	if n==1:
		return sum
	return jc(n-1,sum)
c=jc(4)
print(c)
