#!/usr/bin/env python3
from IPy import IP
#查看ip类型返回4或6
print(IP('192.168.162.21').version())

#网段ip地址个数(必须是网段)
count=IP('192.168.162.20/30')
#print(list(count)[0])
print(count.len())
for i in count:
	print(i)


#ip计算
#ip是否在指定网段里
if '192.168.0.34' in IP('192.168.0.0/24'):
	print('TRUE')

#交互式运行测试ip是否在网段内
ip_s=input('Input ip address:')
ip_s=IP(ip_s)
if len(ip_s) > 1:
	print(ip_s.net())   #网络地址
	print(ip_s.broadcast())  #广播地址
	print(ip_s.netmask())  #子网掩码
else:
	print(ip_s)
	print(ip_s.strBin())  #二进制格式



#网络监测
#判断是公网地址还是私网地址
ip=input('Input ip address:')
ip=IP(ip)
print(ip.iptype()) #共有还是私有地址

