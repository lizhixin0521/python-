#!/usr/bin/env python3
#import tab
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory #输入的内容保存在文件中，通过上下键查找
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
f=open("user_info.txt",'r')
contact_dir = {}
for line in f.readlines():
	name=line.split()[1]
	contact_dir[name]=line
for n,p in contact_dir.items():
	print(n,p,end="")

'''for i in contact_dir:
	print(i,contact_dir[i])
'''
while True:
	user=prompt("Please input the staff name:",
			history=FileHistory('history.txt'),
			auto_suggest=AutoSuggestFromHistory(),
).strip()
	#print(type(user))
	if len(user)==0:continue
	if user in contact_dir:
		print(contact_dir[user])
	else:
		print("sorry,no staff name found!")
