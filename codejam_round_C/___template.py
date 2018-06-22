###
### Config data
###

import os
from math import *

example_test= """2
falar talk
compor compose
andar walk"""

exec(open("../_auxiliary/input_iterators.py").read())

line = string_iter()
line = file_iter(filename +"-small-attempt0.in")
#line = file_iter(filename +"-large-attempt0.in")

fobject = None
#fobject = open(__script_path__ + filename + 'output.txt', 'w')
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

def resolve(port,eng):

	return answer 
		
			
### Run
###

T = int(next(line))

for case in range(T):
	answer = next(line)
	print( "Case #{}: {}".format(case+1,answer),file = fobject)
