# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=2288

###
### Config data
###-

import os
from math import *

example_test= """3
3 2
4 3
4 4"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()

fobject = None
pend = None

def resolve(n,m):
	n -= 1
	m -= 1
	answer = n/m
	if answer == int(answer):
		answer = int(answer)
	else:
		answer = "cannot do this"
	return answer

###
### Run
###

inputs = int(next(line))

for _ in range(inputs):
	print(resolve(*list(map(int,next(line).split()))), end = pend)
