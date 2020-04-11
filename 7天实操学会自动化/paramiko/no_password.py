#!/usr/bin/env python3
import paramiko

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#免密码登录：需要本地的id_rsa文件内容
privateKey='./id_rsa'
pkey=paramiko.RSAKey.from_private_key_file(privateKey)

ssh_client.connect(hostname="192.168.162.22",username='root',pkey=pkey)

stdin,stdout,stderr=ssh_client.exec_command('ls -lh')
print(stdout.read().decode())
ssh_client.close()
