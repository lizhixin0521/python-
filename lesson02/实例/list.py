#!/usr/bin/env python3
f=open("shops.txt",'r')
products=[]
prices=[]
for line in f.readlines():
        new_line=line.split()
        products.append(new_line[0])
        prices.append(new_line[1])
#products=['apple','banana','pea','desk','tv']
#prices=[345,   400,  500,  600,3300]
shop_list=[]
salary=int(input("Please input your salary:"))
while True:
	print("Things have in the shop,please choose one to buy:")
	for p in products:
		print(p,prices[products.index(p)])
	choice=input("please input one item to buy:")
	f_choice=choice.strip()
	if f_choice in products:
		product_price_index=products.index(f_choice)
		product_price=int(prices[product_price_index])
		print(f_choice,product_price)
		if salary > product_price:
			shop_list.append(f_choice)
			print("add %s into your shop list"%f_choice)
			salary=salary-product_price
			print("salary left:",salary)
		else:
			if salary<int(min(prices)):
				print("sorry,rest of your salary cannot buy amything!88")
				print("you have bought these things:%s"%shop_list)
				break
			else:
				print("sorry,you cannot afford this product,please try other ones!")
				
	else:
		print("sorry,not have!")
		
