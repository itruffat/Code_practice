# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=2172

###
### Config data
###-

import os
from math import *

example_test= """8 8 0
8 8 1
9 9 1
40000 39999 0
0 0 0"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()
#line = file_iter("A-small-attempt0.in")

fobject = None
#fobject = open(__script_path__ + filename + 'output.txt', 'w')
pend = None
#pend = ''

check_with_oracle = False

###
### Oracle Definition
###
	
def oracle_generate_answer(n,m,c):
	return None


###
### Solution
###

	
def resolve(n,m,c):	
	n -= 7
	m -= 7
	c  = 1 - (c if (n+m)%2 else 1 - c)
	even_rows =   ceil(n/2) * ceil((m - 1 + c)/2)
	odd_rows  =  floor(n/2) * ceil((m + 0 - c)/2)
	return even_rows + odd_rows 
	
###
### Oracle Confirmation
###

if check_with_oracle:
	pass

###
### Run
###

inputs = list(map(int,next(line).split()))

while inputs[0] != 0:
	answer = resolve(*inputs)
	print("{}".format(answer), end = pend)
	inputs = list(map(int,next(line).split()))
