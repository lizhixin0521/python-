#!/usr/bin/env python3
import filecmp
import sys
a=sys.argv[1]
b=sys.argv[2]
#单个文件比对
result=filecmp.cmp(a,b)
#文件比对是不是同一个，ture|false
print(result)
