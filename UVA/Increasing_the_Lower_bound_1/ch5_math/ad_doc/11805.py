# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=2905

###
### Config data
###-

import os
from math import *

example_test= """3
5 2 5
6 3 5
4 1 3"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()

fobject = None
pend = None

def resolve(n,k,p):
	answer = (k+p)%n 
	return (answer if answer != 0 else n)

###
### Run
###

inputs = int(next(line))

for p in range(inputs):
	answer = resolve(*list(map(int,next(line).split())))
	print("Case {}: {}".format(p+1, answer), end = pend)
