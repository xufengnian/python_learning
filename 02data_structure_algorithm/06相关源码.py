from random import randint
from time import time
from collections import OrderedDict

d = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in range(8):
	raw_input()	
	p = players.pop(randint(0,7-i))
	end = time()
	print i+1,p,end - start,	//逗号是因为防止用户以回车键输入造成换行
	d[p] = (p,end - start)

print	//配合print i+1,p,end - start,最后的逗号
print '-' * 20	

	
for k in d:
	print k,d[k]