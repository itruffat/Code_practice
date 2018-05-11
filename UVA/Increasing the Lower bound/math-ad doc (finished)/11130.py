# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=2071

###
### Config data
###-

import os
from math import *

example_test= """100 50 10 90 10
100 50 10 0 40
100 100 10 45 15
100 50 10 1 200
100 50 10 89 200
100 50 10 45 1000
100 100 10 30 200
0 0 0 0 0"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()

fobject = None
pend = None

check_with_oracle = False

###
### Oracle Definition
###


def quadratic_formula(a,b,c):
	answers = []
	root = pow(b,2) - (4*a*c)				
	if root > 0:
		if root == 0:
			answers.append((-1/2) * (b/a))
		else:
			answer.append((-b + root) / (2 * a))
			answer.append((-b - root) / (2 * a))
	return answers			

def positive_quadratic_formula(a,b,c):
	return list(filter(lambda x: x > 0, quadratic_formula(a,b,c)))
	
def oracle_generate_answer(horizontal,vertical,velocity,angle,time):
	horizontal_bounce, vertical_bounce = 0,0
	x, y = map(lambda x: x/2, [horizontal, vertical])
	acceleration = velocity / time
	
	#
	# I may want to define the oracle just for fun sake
	#
	
	return [horizontal_bounce, vertical_bounce]


###
### Solution
###

	
def resolve(length,height,speed,angle,time):	
	accel = (-1) * speed / time
	angle = radians(angle)
	
	horizontal = {'speed':cos(angle)*speed,'accel':cos(angle)*accel, 'size': length}
	vertical   = {'speed':sin(angle)*speed,'accel':sin(angle)*accel, 'size': height}
	
	answer = []
	for d in [horizontal, vertical]:
		final_p  = (d['size']/2 + d['speed'] * time + (1/2) * d['accel'] * pow(time,2))
		answer.append(int(final_p//d['size']))
	
	return answer
	
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
	print("{} {}".format(*answer), end = pend)
	inputs = list(map(int,next(line).split()))
