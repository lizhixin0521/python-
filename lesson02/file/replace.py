#!/usr/bin/env python3

import fileinput
for line in fileinput.input('hh.txt',backup='.bak',inplace=1):
	line=line.replace("gggg","eeee")
	print(line)
