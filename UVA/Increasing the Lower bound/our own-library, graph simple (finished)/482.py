# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=124&page=show_problem&problem=423

###
### Config data
###

import os
from math import floor, ceil, log

example_test= """1

3 1 2
32.0 54.7 -2"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()


fobject = None
pend = None

check_with_oracle = False


###
### Run
###
test_cases = int(next(line))

for tc in range(test_cases):
	next(line)
	
	permutations = list(map(lambda x: int(x) - 1,next(line).split()))
	floats =  next(line).split()
	copyfloats = [x for x in floats]
	
	for p in range(len(permutations)):
		floats[permutations[p]]   = copyfloats[p]
	
	if tc != 0:
		print("")	
	for x in floats:
		print(x)
