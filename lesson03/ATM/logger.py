#!/usr/bin/env python3
import time
logfile='account.log'
def record_log(account,expense,description,interest=0):#数额 花费 描述 利息
	date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
	record_line="%s  %s  '%s'   %s     %s\n"  %(date,account,description,expense,interest)
	f=open(logfile,'a')
	f.write(record_line)
	f.flush()
	f.close()
