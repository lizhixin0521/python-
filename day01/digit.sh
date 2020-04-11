#!/bin/bash
read -p "请输入判断的数：" num
if [ $num -gt 1000 ];then
	if [ $num -gt 10000 ];then
		echo "5"
	else
		echo "4"
	fi
else
	if [ $num -gt 100 ];then
		echo "3"
	elif [ $num -gt 10 ];then
		echo "2"
	else
		echo "1"
	fi
fi
		
