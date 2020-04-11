#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
import socket
from datetime import datetime
import jinja2
import yagmail
import psutil


EMAIL_USER='18298067196@163.com'
EMAIL_PASSWORD='lizhixin0521'
RECIPIENTS=['2960183352@qq.com','1351162894@qq.com']


#jinja2将信息写入html中
def render(tpl_path,**kwargs):
	path,filename=os.path.split(tpl_path)
	return jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(**kwargs)



#便于读大小
def bytes2human(n):
	symbols=('K','M','G','T','P','E','Z','Y')
	prefix={}
	for i,s in enumerate(symbols):
		prefix[s]=1 << (i+1) * 10
	for s in reversed(symbols):
		if n>prefix[s]:
			value=float(n) / prefix[s]
			return '%.f%s'%(value,s)
	return '%sB'%n


def get_cpu_info():
	cpu_count=psutil.cpu_count()   #cpu个数
	cpu_percent=psutil.cpu_percent(interval=1)  #cpu利用路
	return dict(cpu_count=cpu_count,cpu_percent=cpu_percent)


def get_memory_info():
	virtual_mem=psutil.virtual_memory()
	mem_total=bytes2human(virtual_mem.total) #内存总量
	mem_percent=virtual_mem.percent#内存利用率
	mem_free=bytes2human(virtual_mem.free + virtual_mem.buffers + virtual_mem.cached) #内存剩余
	mem_used=bytes2human(virtual_mem.total * virtual_mem.percent / 100)#内存使用
	return dict(mem_total=mem_total,mem_percent=mem_percent,mem_free=mem_free,mem_used=mem_used)


def get_disk_info():
	disk_usage=psutil.disk_usage('/')
	disk_total=bytes2human(disk_usage.total)
	disk_percent=disk_usage.percent  #利用率
	disk_free=bytes2human(disk_usage.free)  #剩余
	disk_used=bytes2human(disk_usage.used)  #使用
	return dict(disk_total=disk_total,disk_percent=disk_percent,disk_free=disk_free,disk_used=disk_used)

def get_boot_info():
	boot_time=datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
	return dict(boot_time=boot_time)


def collect_monitor_data():
	data={}
	data.update(get_cpu_info())
	data.update(get_memory_info())
	data.update(get_disk_info())
	data.update(get_boot_info())
	return data



def main():
	hostname=socket.gethostname()
	data=collect_monitor_data()
	data.update(dict(hostname=hostname))
	#print(data)
	content=render('/var/www/html/monitor.html',**data)
	
	with yagmail.SMTP(user=EMAIL_USER,password=EMAIL_PASSWORD,host='smtp.163.com',port=465) as yag:
		for recipient in RECIPIENTS:
			yag.send(recipient,"监控信息",content)


if __name__ == '__main__':
	main()
