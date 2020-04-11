#!/usr/bin/env python3
for i in range(1,10):
	for j in range(1,10):
		if i>j:
			print("%s %s %s"%('','','')+'\t',end='')
		else:
			print("%dx%d=%d"%(j,i,j*i)+'\t',end='')
	print("")
