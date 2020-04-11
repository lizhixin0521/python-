#!/usr/bin/env python3
import json
from fabric.api import run,sudo
from fabric.api import env

env.hosts=['192.168.162.22']
env.port=22
env.user='root'

def hostname():
	run('hostname')

def ls(path='.'):
	run('ls {}'.format(path))

def tail(path='/etc/passwd',line=5):
	sudo('tail -n {0} {1}'.format(path,line))


print(json.dumps(env,indent=4))
def hello(name="world"):
	print("hello {}".format(name))
