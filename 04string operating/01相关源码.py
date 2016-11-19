'''
def myString(s,ds):
	res=s
	for d in ds:
		res=','.join(res.split(d))	
	res=res.split(',')
	return [x for x in res if x]
	
s='ab;;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
print myString(s,';|\t,')
'''

import re

s='ab;;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

print re.split(r'[;|\t,]+',s)