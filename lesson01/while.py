#!/usr/bin/env python3
while True:
	user=input("Please input your username:")
	if user=='lizhixin':
		password=input("password:")
		p='123'
		while True:
			if password == p:
				print("welcome login to beijing!")
				break
			else:
				print("password error!")
				password=input("password:")
		break
	else:
		print("sorry,user %snot found"%user)
		
