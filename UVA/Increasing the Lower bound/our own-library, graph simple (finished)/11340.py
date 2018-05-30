# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=124&page=show_problem&problem=2315

###
### Config data
###

import os
from math import floor, ceil, log

example_test= """1
7
a 3
W 10
A 100
, 10
k 7
. 3
I 13
7
ACM International Collegiate Programming Contest (abbreviated
as ACM-ICPC or just ICPC) is an annual multi-tiered competition
among the universities of the world. The ICPC challenges students
to set ever higher standards of excellence for themselves
through competition that rewards team work, problem analysis,
and rapid software development.
From Wikipedia."""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()


fobject = None
pend = None



###
### Run
###

test_cases = int(next(line))

for tc in range(test_cases):

	prices = [0 for _ in range(256)]
	loops =  int(next(line))
	for _ in range(loops):
		keyvalue = next(line) 
		key, value = keyvalue[0], keyvalue[2:]
		prices[ord(key)] = int(value)
	
	price = 0	
	loops =  int(next(line))
	for _ in range(loops):
		for l in next(line):
			price += prices[ord(l)]
			

	fprice = str(price).zfill(3)	

	print (f'{fprice[:-2]}.{fprice[-2:]}$')

		
