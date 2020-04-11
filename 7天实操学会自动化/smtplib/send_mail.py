#!/usr/bin/env python3
import smtplib
import string

HOST='smtp.163.com'
SUBJECT='Test email from Python Day3 exec' #主题
FROM='18298067196@163.com'
TO='2960183352@qq.com'

Text='python alert'
Body='\r\n'.join(
	(
		"From:%s"%FROM,
		"To:%s"%TO,
		"Subject:%s"%SUBJECT,
		"",Text
	)
)

server=smtplib.SMTP(HOST)
server.login('18298067196@163.com','lizhixin0521')
server.sendmail(FROM,[TO],Body) #收件人可以为多个，用列表表示
server.quit()
