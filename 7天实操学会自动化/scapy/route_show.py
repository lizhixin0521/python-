#!/usr/bin/env python3
from scapy.all import traceroute
import subprocess
domains=input("Please input one or more IP/domain:")
target=domains.split(' ')
dport=[80]
if len(target) >= 1 and target[0] != '':
	res,unans=traceroute(target,dport=dport)
	res.graph(target=">test.svg")#生成svg矢量图形
	time.sleep(1)
	subprocess.Popen('/usr/bin/convert test.svg test.png', shell=True)#svg转png格式
	print("路由追踪完成")
else:
	print("域名异常！")
