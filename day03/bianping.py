#!/usr/bin/env python3
#扁平化
c=dict()
di={'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}

#方法一
#for i,j in di.items():
#	for k,h in j.items():
#		if not isinstance(h,dict):
#			c.update({i+"."+k:h})
#		else:
#			for w,e in h.items():
#				c.update({i+"."+k+"."+w:e})
#print(c)



#方法二
def flatmap(src,dst=None,prefix=''):
	if dst is None:
		dst={}
	for k,v in src.items():
		if isinstance(v,dict):
			flatmap(v,dst,prefix+k+'.')
		else:
			dst[prefix+k]=v
	return dst
print(flatmap(di))
