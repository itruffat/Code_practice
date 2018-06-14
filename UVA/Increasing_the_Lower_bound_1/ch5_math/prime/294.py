# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=188&page=show_problem&problem=230

###
### Config data
###-

import os
from math import *
from copy import deepcopy

example_test= """3
1 10
1000 1000
999999900 1000000000"""

exec(open("../../_auxiliary/input_iterators.py").read())

line = input_iter()
line = string_iter()

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

def expandPrimes(primes):
	next_value = primes[-1]
	found_divisor = True
	while found_divisor:
		next_value += 1
		next_value_root = next_value ** (1/2)
		found_divisor = False
		for p in primes:
			if (next_value%p) == 0:
				found_divisor = True
				break
			if p > next_value_root:
				break
	primes.append(next_value)		
	
					
def resolve(l,u):	
	primes = [2]
	while primes[-1] < u:
		expandPrimes(primes)
	
	return x
	
###
### Oracle Confirmation
###


if check_with_oracle:
	pass
			
### Run
###

test_cases = int(next(line))

#for _ in range(test_cases):
#	inputs = map(int,next(line).split())
#	answer = resolve(*inputs)
#	print("between {1} and {2}, {0} has a maximum of {} divisors.".format(answer, *inputs), end = pend)
