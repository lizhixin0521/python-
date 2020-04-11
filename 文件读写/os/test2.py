#!/usr/bin/env python3
#找到目录下最大的十个文件

import os
import fnmatch
def is_file_match(filename,patterns):
	for pattern in patterns:
		if fnmatch.fnmatch(filename,pattern):
			return True
	return False


def find_specific_files(root,patterns=['*'],exclude_dirs=[]):
	for root,dirnames,filenames in os.walk(root):
		for filename in filenames:
			if is_file_match(filename,patterns):
				yield os.path.join(root,filename)
		for d in exclude_dirs:
			if d in dirnames:
				dirnames.remove(d)


#查找目录下所有文件
print(next(find_specific_files(".")))
for i in find_specific_files("."):
	print(i)


#查找目录下所有txt文件

patterns=['*.py']
for i in find_specific_files(".",patterns):
        print(i)


#查找排除ww 目录以外的文件
exclude_dirs=['ww']
for i in find_specific_files(".",patterns,exclude_dirs):
        print(i)
