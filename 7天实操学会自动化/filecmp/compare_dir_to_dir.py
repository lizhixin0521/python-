#!/usr/bin/env python3
import filecmp
a='testdir1'
b='testdir2'
#目录之间比较
result=filecmp.dircmp(a,b)
print(result.report())

print("="*10)

#第一个目录中所有的文件
print(result.left_list)   #right_list

print("="*10)
#第一个目录中独有的文件
print(result.left_only)


print('='*20)
#目录中是否有相同的目录名
print(result.common_dirs)


print('='*20)
#目录中是否有相同的文件名
print(result.common_files)



