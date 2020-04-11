#!/usr/bin/env python3
import paramiko

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname="192.168.162.22",username='root',password='123456')
#stdin,stdout,stderr=ssh_client.exec_command('ls -lh')
#print(stdout.read().decode())
#print("#"*30)
#stdin,stdout,stderr=ssh_client.exec_command('free -m')
#print(stdout.read().decode())

#如果要输入值才能进行的话
stdin,stdout,stderr=ssh_client.exec_command('ssh lizhixin@localhost')
stdin.write('123456\n')
ssh_client.close()
