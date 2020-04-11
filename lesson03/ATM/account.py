#!/usr/bin/env python3
import json
account_info={"123456":['lizhixin',15000,15000],
	      "654321":['heihei',9000,9000]
		}
f=open("account.pkl",'w')
b=json.dump(account_info,f)
#print(type(b))
#print(b)
#f.write(b)
f.close()
