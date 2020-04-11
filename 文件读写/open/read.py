#!/usr/bin/env python3

#read()读取文件中的所有行
f=open("data.txt",'r')
print(f.read())
print("---------------------------------")
#readline()一次读取一行
f.seek(0)
print(f.readline())
print("---------------------------------")
f.seek(0)
print(f.readlines())
f.close()
#readlines()将文件的内容存到列表中，列表中每一行对应文件的一行

