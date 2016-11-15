from random import randint
from collections import deque

num = randint(1,100)
history = deque([],5)

def guess(k):
    if k == num:
	print 'Bingo!'
	return True
    if k < num:
        print '%s is small!' % k
    else:
	print '%s is big!' % k     
    return False

while True:
    line = raw_input('Please input a number: ')
    if line.isdigit():
        k = int(line)
        history.append(k)		
        if guess(k):
            break    
    elif line == 'history' or line == 'h?':
	print list(history)