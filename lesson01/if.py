#!/usr/bin/env python
name=raw_input('name:')
age=int(raw_input('age:'))
job=raw_input('job:')
print("------------------\n")
if age<28:
	print("you are a young")
else:
	print("old")
msy='''
	\tname:%s
	\tage:%d
	\tjob:%s
''' %(name,age,job)

print(msy)
