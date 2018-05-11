# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=1881

###
### Config data
###

import os
from math import floor, ceil, log, sqrt

example_test= """7
19
10
6
0"""

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
	deck = [x+1 for x in range(n)]
	while len(deck) > 1:
		deck.pop(0)
		deck.append(deck.pop(0))
	return(deck[0])

###
### Solution
###

def resolve(n):
	answer = n
	if n > 1:
		answer -= pow(2,int(log(n-1,2)))	# Distance to the previous power of 2
		answer *= 2 						# Meassured in units of 2
	return answer
	
###
### Oracle Confirmation
###

if check_with_oracle:
	for x in range(1, 500000 + 1):
		if resolve(x) != oracle_generate_answer(x):
			print("\nValue:{}\n~~~~~~\nExpected:  {}\n--------- \n Result :  {}".format(x,oracle_generate_answer(x),resolve(x)))
			break
###
### Run
###
next_value = int(next(line))

while next_value != 0:
	answer = resolve(next_value)
	print(answer, end = pend)
	next_value = int(next(line))
