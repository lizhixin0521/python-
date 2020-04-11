#!/usr/bin/env python3
#将文件中所有单词的首字母改成大写‘


with open("data2.txt",'r')as f,open("data3.txt",'w')as g:
	for line in f:
		#print(*[word.capitalize() for word in line.split()],file=g)
		g.write(" ".join([word.capitalize() for word in line.split()]))
		g.write("\n")
