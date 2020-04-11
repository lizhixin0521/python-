#!/usr/bin/env python3
#write()写字符串到文件中，并返回写入的字符数
f=open("data2.txt",'a')
f.write("lizhixin\n")
#writelines()写一个字符串列表到文件中
f.writelines(["hanchangkan\n","wangzhongxu\n","tangjunjie"])
f.close()

