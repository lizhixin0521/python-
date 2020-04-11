#!/usr/bin/env python3
triangle=[]
n=6
for i in range(n):
	row=[1]
	triangle.append(row)
	if i==0:
		continue
	for j in range(i-1):
		row.append(triangle[i-1][j]+triangle[i-1][j+1])
	row.append(1)
print(triangle)
