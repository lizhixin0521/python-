#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
HOST='smtp.163.com'
SUBJECT='流量数据报表'
FROM='18298067196@163.com'
TO='2960183352@qq.com'
Text='''
<html>
<head>
</head>
<body>
        <table border=1px>
                <tr>
                        <th>name</th>
                        <th>hobby</th>
                </tr>
                <tr>
                        <td>李志新</td>
                        <td>音乐</td>
                </tr>
                <tr>
                        <td>韩长看</td>
                        <td>电影</td>
                </tr>
                <tr>
                        <td>王忠旭</td>
                        <td>王者</td>
                </tr>
                <tr>
                        <td>汤俊杰</td>
                        <td>英雄联盟</td>
                </tr>
        </table>
</body>
</html>
'''
msg=MIMEText(Text,'html')
msg['Subject']=SUBJECT
msg['From']=FROM
msg['To']=TO
try:
	server=smtplib.SMTP(HOST)
	server.login('18298067196@163.com','lizhixin0521')
	server.sendmail(FROM,[TO,'1351162894@qq.com','384400195@qq.com','1574320833@qq.com'],msg.as_string())
	server.quit()
	print("send ok")
except Exception as e:
	print("Fail"+str(e))
