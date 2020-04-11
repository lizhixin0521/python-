#!/usr/bin/env python3
#拆分路径

#split:返回一个二元组，包括文件的路径与文件名
#dirname:返回文件的路径
#basename:返回文件的文件名
#splitext:返回一个去除文件扩展名的部分和扩展名的二元组

import os
path="/var/log/redis/redis.log"

print(os.path.split(path))

print(os.path.dirname(path))

print(os.path.basename(path))


print(os.path.splitext(path))
