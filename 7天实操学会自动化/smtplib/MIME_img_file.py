#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

HOST='smtp.163.com'
SUBJECT=u'肖像'
FROM='18298067196@163.com'
TO='2960183352@qq.com'

def addimg(src,imgid):
	fp=open(src,'rb')
	magImage=MIMEImage(fp.read())
	fp.close()
	magImage.add_header('Content-ID',imgid)
	return magImage

msg=MIMEMultipart('related')#大的容器，等放入内容进去
msg['Subject']=SUBJECT
msg['From']=FROM
msg['To']=TO

msgtext=MIMEText(
"""
<table>
	<tr>
		<td><img src="cid:wangzhongxu" width="400px" height="500px"></td>
		<td><img src="cid:hanchangkan" width="400px" height="500px"></td>
		<td><img src="cid:tangjunjie" width="400px" height="500px"></td>
	</tr>
	<tr>
		<td>傻子1</td>
		<td>傻子2</td>
		<td>傻子3</td>
	</tr>
</table>
""",'html')

msg.attach(msgtext)#第一个内容放进去
msg.attach(addimg('wangzhongxu.jpg','wangzhongxu'))#第二个放进去
msg.attach(addimg('hanchangkan.jpg','hanchangkan'))
msg.attach(addimg('tangjunjie.jpg','tangjunjie'))

#附件
file=MIMEText(open("access_log.txt",'r').read(),"base64")
file["Content-Type"]="application/octet-stream"
#file["Content-Disposition"]="attachment;filename='access_log'"
msg.attach(file)

try:
        server=smtplib.SMTP(HOST)
        server.login('18298067196@163.com','lizhixin0521')
	#server.sendmail(FROM,[TO,'1351162894@qq.com','384400195@qq.com','1574320833@qq.com'],msg.as_string())
        server.sendmail(FROM,[TO],msg.as_string())
        server.quit()
        print("send ok")
except Exception as e:
        print("Fail"+str(e))
