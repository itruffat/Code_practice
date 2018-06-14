#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=1287

###
### Config data
###

import os
from math import floor, ceil, log

example_test= """4 3
10 3
100 5"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()

fobject = None
pend = None


###
### Solution
###

def resolve(c_quantity,h_required):
	answer = 0
	while c_quantity//h_required > 0:
		left_overs =  c_quantity % h_required
		answer    +=  c_quantity - left_overs
		c_quantity =  left_overs + (c_quantity//h_required)
	
	answer += c_quantity
	
	return answer
	
###
### Run
###

while True:
	try:
		value1, value2 = list(map(int,next(line).split()))
	except:
		break
	answer = resolve(value1, value2)
	print("{}".format(answer), end = pend)
