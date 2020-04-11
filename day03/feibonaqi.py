#!/usr/bin/env python3
def fib(n):
	a=0
	b=1
	count=0
	while True:
		a,b=b,a+b
		count+=1
		if count==n:
			 yield a
c=fib(4)
print(next(c))
