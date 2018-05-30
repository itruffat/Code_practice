# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=132&page=show_problem&problem=1869

###
### Config data
###

import os
from math import floor, ceil, log

example_test= """2
3
2
1 3
2 1

4
2
3
1 4 2
2 1 3"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()


fobject = None
pend = None

check_with_oracle = False

###
### Oracle Definition
###

def oracle_generate_answer(n):
	return None

###
### Solution
###

def resolve(n):
	return None
			
###
### Oracle Confirmation
###

if check_with_oracle:
	pass

###
### Run
###
test_cases = int(next(line))

for tc in range(test_cases):
	if tc != 0:
		next(line)
	
	p = int(next(line))
	answer = []
	cmin = p + 1
	
	for n in range(p):
		x = next(line).count(" ") + 1
		if x < cmin:
			answer = []
			cmin = x
		if x == cmin:
			answer.append(str(n+1))
	print(" ".join(answer))
