#/usr/bin/env python3
from subprocess import PIPE
import psutil
#执行的命令
p=psutil.Popen(['/usr/local/bin/python3','-c',"print('lizhixin')"])
print(p.name())
print(p.username())
print(p.cpu_times)

