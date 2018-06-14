# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=2823

###
### Config data
###-

import os
from math import *

example_test= """8 5
100 2
0 0"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()

fobject = None
pend = None

###
### Solution
###

	
def resolve(r,n):
	answer = ceil(r / n) - 1 	
	if answer > 26:
		answer = "impossible"
	return answer 

###
### Run
###

i = 0
inputs = list(map(int,next(line).split()))

while inputs[0] != 0:
	answer = resolve(*inputs)
	i += 1
	print("Case {}: {}".format(i,answer), end = pend)
	inputs = list(map(int,next(line).split()))
	
