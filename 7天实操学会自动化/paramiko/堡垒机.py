#!/usr/bin/env python3
import paramiko
import sys
blip='192.168.162.22'
bluser='root'
blpasswd='123456'

rel_ip='192.168.162.23'
rel_user='root'
rel_pass='123456'

#日志保存
paramiko.util.log_to_file('paramiko.log')


ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname=blip,username=bluser,password=blpasswd)
print("连上了堡垒机")

channel=ssh.invoke_shell()
channel.settimeout(10)
buff=''
resp=''
passinfo="password: "   #连接时返回的信息包含的内容
channel.send('ssh  '+rel_user+'@'+rel_ip)
while not str(buff).endswith(passinfo):
#while not passinfo in buff:
	try:
		resp = channel.recv(9999)   #一直等拿到所有数据
		print(resp)
	except Exception as e:
		print('error1')
		channel.close()
		ssh.close()
		sys.exit()
	buff += str(resp)
	print(buff)
channel.send(rel_pass+'\n')
print(buff)
buff=''
channel.send('ip addr')
buff=''
try:
	while buff.find('#') == -1:
		resp=channel.recv(9999)
		buff = buff + str(resp)
except Exception as e:
	print('error2')
print(buff)
channel.close()
