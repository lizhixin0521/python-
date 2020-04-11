#!/usr/bin/env python3
#打印最常用的linux命令
import os
from collections import Counter
c=Counter()
with open(os.path.expanduser('~/.bash_history')) as f:
	for line in f:
		cmd=line.strip().split()
		if cmd:
			c[cmd[0]]+=1
print(c.most_common(10))
