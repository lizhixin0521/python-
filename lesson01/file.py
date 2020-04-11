#!/usr/bin/env python3
while True:
	user=input("Please input username:")
	p=123
	if user=='lizhixin':
		while True:
			password=int(input("Please input password:"))
			if password==p:
				print("welcome to login")
				break
			else:
				print("password error!")
		#info=open("user_info.txt",'r')
		while True:
			match_yes=0
			info=open("user_info.txt",'r')
			keyword=input("what's your search?")
			while True:
				data=info.readline()
				if len(data)==0:break
				if keyword in data:
					print(data)
					match_yes=1
			if match_yes==0:
				print("sorry don't have")
			info.close()	
	else:
		print("username error!")
