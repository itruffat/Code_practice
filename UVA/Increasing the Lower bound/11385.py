# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=204&page=show_problem&problem=2380

###
### Config data
###-

import os
from math import *
from copy import deepcopy

example_test= """2
11
13 2 89 377 8 3 233 34 144 21 1
OH, LAME SAINT!
15
34 21 13 144 1597 3 987 610 8 5 89 2 377 2584 1
O, DRACONIAN DEVIL!"""

exec(open("../../_auxiliary/input_iterators.py").read())

#line = input_iter()
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

def expandFibonachi(fibo):
	fibo.append(fibo[-1] + fibo[-2])
					
def resolve(numbers,letter):
	ordered_numbers = list(enumerate(numbers))
	ordered_numbers.sort(key = lambda x: x[1] ) 
	answer = []
	fibo = [0,1]
	for original_position,number in ordered_numbers:
		expandFibonachi(fibo)
		while fibo[-1] < number:
			expandFibonachi(fibo)
			answer.append(" ")
		answer.append(letter[original_position])
	return ''.join(answer)	
		
###
### Oracle Confirmation
###


if check_with_oracle:
	pass
			
### Run
###

is_letter = lambda x:ord(x) >= ord('A') and ord(x) <= ord('Z')
to_number = int

test_cases = int(next(line))

for _ in range(test_cases):
	next(line)
	numbers = list(map   (to_number, next(line).split()))
	letters = list(filter(is_letter, list(next(line))))
	answer = resolve(numbers,letters)
	print(answer)
