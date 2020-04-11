#!/usr/bin/env python3
import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect('192.168.162.22',22,'root','123456')
stdin,stdout,stderr=ssh.exec_command('df')
print(stdout.read().decode())
ssh.close()

transport=paramiko.Transport('192.168.162.22',22)
transport.connect(username='root',password='123456')
sftp=paramiko.SFTPClient.from_transport(transport)
sftp.get('/etc/fstab','fstab') #从服务器上拿取文件
sftp.put('sshclient.py','/home/lizhixin/sshclient.py') #把本地的文件，推到服务器上
sftp.close()

