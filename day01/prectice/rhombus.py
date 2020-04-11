#!/usr/bin/env python3
#菱形
for i in range(-3,4):
	if i<0:
		prespace=-i
	else:
		prespace=i
	print(' '*prespace+'*'*(7-prespace*2))
