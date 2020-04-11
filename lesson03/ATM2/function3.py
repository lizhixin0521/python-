#!/usr/bin/env python3

#余额
balance ={"money":0}
#登录状态
state={"state":False}
#log日志
def w_log(operation):
    with open("consume_log.txt","a",encoding="utf-8") as f:
        f.write("执行操作: "+operation+"\n")
 
 
#登录账号信息
user={"egon":"111","alex":"222","wusir":"333","somebody":"444"}
# 登录验证
def login():
    name =input("===>user_name:").strip()
    passwd = input("===>user_password:").strip()
    str = "login==>name={}   password={}-----".format(name,passwd)
    if name in user and passwd == user[name]:
        str1 = "login  successful"
        state["state"]=True
        print(str1)
    else:
        str1="login failed   please enter again"
        print(str1)
    str = str + str1
    w_log(str)
 
 
#装饰器
def wrapper(func):
    def inner(*args,**kwargs):
        while not state["state"]:
            login()
        ret = func(*args,**kwargs)
        return ret
    return inner
 
 
#查询余额
@wrapper
def check_balance():
    str = "check_balance==>当前余额为:{}".format(balance["money"])
    print(str)
    print("查询余额操作完成！\n")
    w_log(str)#操作写入日志
 
 
#提现取款  提现手续费5% 额度 10000或自定义
@wrapper
def draw_money(poundage=0.05,quota=10000):
    str="darw_money==>当前余额为:{}  限超出额度:{}  手续费率:{}".format(balance["money"],quota,poundage)
    print(str)
    money= int(input("Please enter the amount of money you withdraw:").strip())
    if balance["money"] -money >= -quota:
        balance["money"] = balance["money"] - money -money*poundage     #扣除取款 扣除手续费
        str1="------扣除手续费:{}   取款余额:{}   剩余余额（已扣手续费）:{}".format(money*poundage,money,balance["money"])
        str=str+str1
    else:
        str1="------超出限额 , 取款失败!"
        str = str+str1
 
 
    print(str1)
    print("取款操作完成！\n")
    w_log(str)
 
 
#转账
@wrapper
def transfer_accounts():
    str = "transfer_accounts==>当前余额为:{}".format(balance["money"])
    print(str)
    #输入转账对象信息
    name=input("Please enter the name of the transfer person:").strip()
    car_number=input("enter  car number:").strip()
    t_money=int(input("enter transfer money:").strip())
    balance["money"]-=t_money
    str1 = "-----转账对象 姓名={}   卡号={}   转钱数={}   剩余余额={}".format(name,car_number,t_money,balance["money"])
    str = str +str1
 
 
    print(str1)
    print("转账完成！\n")
    w_log(str)
 
 
#查看本月消费 消费和日常操作等内容以字符串的形式记录到文件中
@wrapper
def check_consume(filename="consume_log.txt"):
    with open(filename,encoding="utf-8") as f:
        for x in f:
            print(x,end="")
    print("查看本月消费完成!\n")
 
 
#命令界面
info ='''\t\t信用卡程序功能
\tcb   -----查询余额
\tdm   -----提现取款
\tta   -----转账
\tcc   -----查看本月消费
\texit -----退出
'''
 
 
#被装饰后的函数字典
func_dict={"cb":check_balance,"dm":draw_money,"ta":transfer_accounts,"cc":check_consume,"exit":exit}
 
 
while True:
    print(info)
    cmd =input("Please enter the command above:").strip()
    if cmd in func_dict:
        func_dict[cmd]()
    else:
     print("error,please enter again")
