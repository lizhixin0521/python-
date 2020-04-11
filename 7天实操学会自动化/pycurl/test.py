#!/usr/bin/env python3
import os
import sys
import pycurl

URL="http://www.baidu.com"
c=pycurl.Curl()#生成curl浏览器
c.setopt(pycurl.URL,URL)#请求的网址

#连接时间超时
c.setopt(pycurl.TIMEOUT,5)#连接网站的超时时间
c.setopt(pycurl.CONNECTTIMEOUT,5)#请求某个操作时的超时时间
c.setopt(pycurl.FORBID_REUSE,1)#完成交互后断开连接，不重用
c.setopt(pycurl.NOPROGRESS,1)#是否屏蔽下载进度条，非0则屏蔽

indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
#os.path.dirname()返回文件路径，原样返回
#os.path.realpath()返回文件的绝对路径
#os.path.join()把目录和文件名合成一个路径

c.setopt(pycurl.WRITEHEADER,indexfile)  #将返回的HTTP HEADER定向到indexfile文件
c.setopt(pycurl.WRITEDATA,indexfile)    #将返回的HTML内容定向到indexfile文件

try:
	c.perform()#开始连接
except Exception as e:
	print("连接不上")
	c.close()#关闭连接
	sys.exit()#退出程序

#HTTP 状态
print("HTTP状态码：%s"%(c.getinfo(c.HTTP_CODE)))
print("建立连接时间：%.2f ms"%(c.getinfo(c.CONNECT_TIME)))
print("平均下载速度：%d bytes/s"%(c.getinfo(c.SPEED_DOWNLOAD)))
print("DNS解析时间：%2f"%(c.getinfo(c.NAMELOOKUP_TIME)))
print("准备传输时间：%2f"%(c.getinfo(c.PRETRANSFER_TIME))) 
print("传输开始时间：%2f"%(c.getinfo(c.STARTTRANSFER_TIME)))
print("传输结束总时间：%2f"%(c.getinfo(c.TOTAL_TIME)))
print("下载数据包大小：%d bytes/s"%(c.getinfo(c.SIZE_DOWNLOAD)))
print("HTTP头部大小：%d bytes/s"%(c.getinfo(c.HEADER_SIZE)))
c.close()
