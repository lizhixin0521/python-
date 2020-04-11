#/usr/bin/env python3
import psutil
#cpu个数
print(psutil.cpu_count())
#内存
print(psutil.virtual_memory())
#内存的使用率
print(psutil.virtual_memory().percent)
#内存总大小
print(str(psutil.virtual_memory().total/1024/1024/1024)+'G')

#磁盘分区
print(psutil.disk_partitions())
#磁盘利用率
print(psutil.disk_usage('/').percent)



