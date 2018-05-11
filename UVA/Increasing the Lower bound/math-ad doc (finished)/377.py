#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=162&page=show_problem&problem=313

###
### Config data
###

import os
import operator
from math import floor, ceil, log

example_test= """5 
VVVVU\nVVVVU\nA\nA\nA\nVVVVVVUV
VVCCV\nVVDCC\nL\nR\nA\nVVVVUCVC
VVCCV\nVVDCC\nR\nL\nA\nVVVVUCVV
VVUUU\nVVVVU\nA\nN\nN\nVVVVVUCU
DDDDD\nVVVVU\nA\nL\nL\nUVVVVVVV"""

exec(open("../../../_auxiliary/input_iterators.py").read())

line = input_iter()
#line = string_iter()

fobject = None
pend = None

###
### Solution
###

numbers = {'V':'0', 'U':'1', 'C':'2', 'D':'3'}
operations = {'A': (operator.add), 'R': (lambda x,y: x//4), 'L': (lambda x,y: x*4), 'N':(lambda x,y: x)}

def resolve(N1,N2,A1,A2,A3,answer):
	
	for key,value in numbers.items():
		N1     = N1.replace(key,value)
		N2     = N2.replace(key,value)
		answer = answer.replace(key,value)
	
	N1     = int(    N1, 4)
	N2     = int(    N2, 4)
	answer = int(answer, 4)

	for A in [A1,A2,A3]:
		N2 = operations[A](N2,N1)
			 
	return (answer == N2)

###
### Run
###

answer_map = {True:'YES', False:'NO'}

print("COWCULATIONS OUTPUT", end = pend)

T = int(next(line))
for x in range(T):
	
	input_table = [next(line) for _  in range(6)]
	answer = resolve(*input_table)
	
	print(answer_map[answer], end = pend)

print("END OF OUTPUT", end = pend)
