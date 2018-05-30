###
### Config data
###

import os
from math import *

example_test= """2
2 3 1 2 1 2 1 1 9
10 10 10001 10002 10003 10004 10005 10006 89273
"""

exec(open("../_auxiliary/input_iterators.py").read())

line = string_iter()
#line = file_iter("B-small-attempt0.in")
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

def resolve(A,K):
	return 0
			
### Run
###

T = int(next(line))

		
for case in range(T):
	input_list = list(map(int, next(line).split()))
	A = generate_A(*input_list)
	
	answer = resolve(A, input_list[1])
	
	#print( "Case #{}: {}".format(case+1,str(answer%1000000007)),file = fobject)
	print( "Case #{}: {}".format(case+1,str(answer%1000000007)))
