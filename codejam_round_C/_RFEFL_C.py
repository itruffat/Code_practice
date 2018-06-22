###
### Config data
###

import os
from math import *

example_test= """2
2 3 1 2 1 2 1 1 9
10 10 10001 10002 10003 10004 10005 10006 89273
"""

filename = __file__[:-3]
__script_dir__ = os.path.realpath(__file__)
__script_path__ = os.path.dirname(__script_dir__) + os.sep

def input_iter(has_finish_flag = False, flag = ""):
	while True:
		try: # Instead of using a conditional, we use a try/except to catch other exceptions
			 # created by input finishing.
			i = input()
			assert(not(has_finish_flag and i==flag))
		except:
			break
		yield(i)

def string_iter(string=example_test):
    for i in string.split("\n"):
        yield(i)

def file_iter(filepath = "input.txt"):
    _file = open(__script_path__ + filepath, "r")
    i_buffer = _file.readline()
    for i in _file.readlines():
        yield(i_buffer[:-1])
        i_buffer = i
    _file.close()
    yield(i_buffer)


#line = string_iter()
line = file_iter("C-small-practice.in")
#line = file_iter(filename[-1] +"-large-attempt1.in")

#fobject = None
fobject = open(__script_path__ + filename[-1] + 'output.txt', 'w')
pend = None

check_with_oracle = False

def generate_A(N, K, x, y, C, D, E1, E2, F):		
	A = [(x + y)%F]
	for p in range(1,N):
		x0, y0 = [x,y]
		x = C*x0 + D*y0 + E1
		y = D*x0 + C*y0 + E2
		A.append((x + y)%F)
	return A


	# Explanation
	#
	# When one looks at the formula it's very easy to see a pattern
	#
	# Example: N = 3 ([a,b,c]), K = 5
	#
	# everything that will be multiplied by powers of 1 
	# a * n		b * (n-1)	c * (n-2)
	# a * n		b * (n-1)	c * (n-2)	
	# a * n		b * (n-1)	c * (n-2)
	# a * n		b * (n-1)	c * (n-2)
	# a * n		b * (n-1)	c * (n-2)
	# everything that will be multiplied by powers of 2
	# b * (n-1) * 2		c * (n-2) * 2
	# b * (n-1) * 4		c * (n-2) * 4
	# b * (n-1) * 8		c * (n-2) * 8
	# b * (n-1) * 16	c * (n-2) * 16
	# b * (n-1) * 32	c * (n-2) * 32
	# everything that will be multiplied by powers of 3
	# c * (n-2) * 3
	# c * (n-2) * 9
	# c * (n-2) * 27
	# c * (n-2) * 81
	# c * (n-2) * 243
	#
	# If we compress each table into a single line, we get
	# a * (n-0) * (1+1+1+1+1+1) + b * (n-1) * (1+1+1+1+1+1) + c * (n-2) * (1+1+1+1+1+1) 	#powers of 1
	# b * (n-1) * (2+4+8+16+32) + c * (n-2) * (2+4+8+16+32)									#powers of 2
	# c * (n-2) * (3+9+27+81+243)															#powers of 3
	#
	# Finally we reshuffle a little and we get
	# a * (n-0) * ((1+1+1+1+1+1))
	# b * (n-1) * ((1+1+1+1+1+1) + (2+4+8+16+32))
	# c * (n-2) * ((1+1+1+1+1+1) + (2+4+8+16+32)+(3+9+27+81+243))
	#
	# We add renames
	# a * (n-0) * multipliers(0)
	# b * (n-1) * multipliers(0) + multipliers(1)
	# c * (n-2) * multipliers(0) + multipliers(1) + multipliers(2)
	#
	# So, for each original number we have:
	# number * (n-position) * sum(multipliers from [0] to [position])
	#
	# Finally, if we add a temporal variable we can do the following:
	# VARt <- multipliers(0)
	# a * (n-0) * VARt
	# VARt <- multipliers(1) + VARt
	# b * (n-1) * VARt
	# VARt <- multipliers(2) + VARt
	# c * (n-2) * VARt
	
def resolve(A,N,K):
	answer = 0
	multipliers = 0
	for x in range(N):
		repetitions = (N - x)
		multipliers += sum((pow(x+1,y) for y in range(1,K+1)))
		value = A[x] * repetitions * multipliers
		answer += value 
	return int(answer)
			
### Run
###

T = int(next(line))

		
for case in range(T):
	input_list = list(map(int, next(line).split()))
	A = generate_A(*input_list)
	
	answer = resolve(A, input_list[0], input_list[1])
	
	
	
	print( "Case #{}: {}".format(case+1,str(answer%1000000007)),file = fobject)
	#print( "Case #{}: {}".format(case+1,str(answer%1000000007)))
