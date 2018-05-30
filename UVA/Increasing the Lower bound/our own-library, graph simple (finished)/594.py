# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=124&page=show_problem&problem=535

###
### Config data
###

import os
from math import floor, ceil, log

example_test= """123456789
-123456789
1
16777216
20034556"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()


fobject = None
pend = None

###
### Solution
###

def resolve(n):
	n += 2**32 if n < 0 else 0
	b = (bin(n)[2:].zfill(32))
	byte_pockets = [b[x:x+8] for x in range(0,32,8)][::-1]
	b = f'0b{"".join(byte_pockets)}'
	answer = int(b,2)
	answer -= 0 if answer < (2**31) else 2**32
	return(answer)


###
### Run
###


while True:
	try:
		i = int(next(line))
	except StopIteration:
		break	
	print("{} converts to {}".format(i,resolve(i)))



