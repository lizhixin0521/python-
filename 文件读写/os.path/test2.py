#!/usr/bin/env python3
#拆分路径

#expanduser:展开用户的home目录，如~，~username
#abspath:得到文件或路径的绝对路径
#join:根据不同的操作系统平台，使用不同的路径分割符拼接路径
import os


print(os.path.expanduser('~'))
print(os.path.expanduser('~lizhixin'))

print(os.path.expanduser('~lizhixin/fstab'))


print(os.path.abspath('.'))

print(os.path.join("/etc","passwd"))
