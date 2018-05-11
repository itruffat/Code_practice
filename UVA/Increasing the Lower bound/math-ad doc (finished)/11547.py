# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=2542

###
### Config data
###-

import os
from math import *

example_test= """2
637
-120"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()

fobject = None
pend = None

def resolve(n):
	n *= 567
	n /= 9
	n += 7492
	n *= 235
	n /= 47
	n -= 498
	n  = abs(n)%100
	n /= 10
	return int(n)

###
### Run
###

inputs = int(next(line))

for _ in range(inputs):
	print(resolve(int(next(line))), end = pend)
