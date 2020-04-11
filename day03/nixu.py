#!/usr/bin/env python3
#将一个数逆序放入列表中，例如1234=》[4,3,2,1]
li=[]
def a(num):
	m,n=divmod(num,10)
	#m,n=divmod(num,10) m=num//10  n=num%10
	#n=num%10
	li.append(n)
	if m==0:
		return li
	return a(m)
c=a(1234)
print(c)



#方法二
data=str(1234)
c=list(map(int,reversed(data)))
print(c)


#方法三
target=[]
def revert(data):
	target.append(data[-1])
	if len(data)==1:
		return target
	return revert(data[:-1])
print(list(map(int,revert("1234"))))
#print(revert("1234"))


#方法四
#如果target一开始none,定义一个列表，如果不为空，在其基础上上追加
def revert(data,target=None):
	if target is None:
		target=list()
	target.append(data[-1])
	if len(data) == 1:
                return target
	
	return revert(data[:-1],target)
print(revert('abcd',[100,102]))
#print(list(map(int,revert("1234"))))
