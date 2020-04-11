#!/usr/bin/env python3
import difflib
import sys


try:
	textfile1=sys.argv[1]
	textfile2=sys.argv[2]
except:
	print("Error  argv")
	sys.exit()


def readfile(f):
	fileopen=open(f,'rb')
	text=fileopen.read().decode("utf-8").splitlines()
	fileopen.close()
	return text


text1=readfile(textfile1)
text2=readfile(textfile2)

d=difflib.Differ()
diff=d.compare(text1,text2)
#print(type(f))
print('\n'.join(diff))
