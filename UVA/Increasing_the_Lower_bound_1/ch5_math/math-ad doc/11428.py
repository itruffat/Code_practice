# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=2423

###
### Config data
###-

import os
from math import *

example_test= """7
37
12
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
	cubicroot_n = int(pow(n,1/3))
	answer = ['No', 'Solution'] 
	found = False
	for i in range(1,n+1):
		for p in range(1, n+1):
			if n == (pow(p,3) - pow(i,3)):
				answer[0] = p
				answer[1] = i
				found = True
			if found:
				break
		if found:
			break
	return answer



###
### Solution
###

def resolve(n):	
	answer = ['No', 'solution'] 
	cube_root   = (n ** (1/3))
	square_root = (n ** (1/2))
	
	for x in range(floor(cube_root) + 1, floor(square_root) + 1):
		target_y_cube = (x**3 - n)
		for y in range(1,x):
			current_y_cube = y**3
			if target_y_cube == current_y_cube:
				answer[0] = x
				answer[1] = y
			if target_y_cube <= current_y_cube:
				break 
		if answer[0] != "No":
			break
	return answer
	
###
### Oracle Confirmation
###


if check_with_oracle:
	for x in range(1,10000):
		oga = oracle_generate_answer(x)
		rga   =  resolve(x)
		if oga != rga:
			print("{}: {} - {}".format(x,oga,rga))
###		
### Run
###

inputs = int(next(line))

while inputs != 0:
	answer = resolve(inputs)
	print("{} {}".format(*answer), end = pend)
	inputs = int(next(line))
