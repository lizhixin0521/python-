#!/usr/bin/env python3
import json
import time
import logger
import sys
pkl_file=open("account.pkl",'r')

account_list=json.load(pkl_file)
#print(type(account_list))
pkl_file.close()

def recon(account,cost_amount,expense_type):
	pkl_file=open("account.pkl",'w')
	old_position=account_list[account][2]
	if old_position < cost_amount:
		print("no enought money!")
		json.dump(account_list,pkl_file)
		pkl_file.close()
		sys.exit()
	global intrest
	intrest=0
	if expense_type == 'withdraw':
		intrest=cost_amount * 0.05
		new_position=old_position-cost_amount-intrest
	else:
		new_position=old_position-cost_amount
	account_list[account][2]=new_position
	json.dump(account_list,pkl_file)
	pkl_file.close()
print(account_list)
recon("123456",16000,'withdraw')
#logger.record_log('123456',500,'phone')#花费
logger.record_log('123456',16000,'withdraw',intrest)#取款
