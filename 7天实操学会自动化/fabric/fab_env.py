#!/usr/bin/env python3
from fabric.api import run
from fabric.api import env
import os
dir=os.getcwd() #当前工作目录
env.hosts=['192.168.162.22']
env.user='root'
env.port='22'
env.password='123456'

def hostname():
	run('hostname')

def ls(path=dir):
	run('ls {}'.format(path))


def tail(path='/etc/passwd',line=10):
	run('tail -n {0} {1}'.format(line,path))
