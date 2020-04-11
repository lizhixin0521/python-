#/usr/bin/env python3
import psutil

#总共进程数
print(len(psutil.pids()))
#获取进程的信息
print(psutil.Process(6943))
#获取该进程的执行命令
print(psutil.Process(6943).exe())
#获取该进程的连接信息（远程连接ip等）
print(psutil.Process(6943).connections())
