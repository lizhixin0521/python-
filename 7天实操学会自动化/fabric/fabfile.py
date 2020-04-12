#!/usr/bin/env python3

from fabric.api import run
from fabric.colors import *
print(blue('lizhixin'))
def host_type():
	run('uname -s')

