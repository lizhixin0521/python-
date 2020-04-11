import yagmail
with yagmail.SMTP(user="18298067196@163.com",password="lizhixin0521",host='smtp.163.com',port=465) as yag:
	yag.send("2960183352@qq.com","监控信息")
