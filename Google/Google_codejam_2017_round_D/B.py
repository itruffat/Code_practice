###
### Config data
###

import os
from math import *
from copy import deepcopy
#import geometria_linea

example_test= """2
3 2
1 4 1 1 0 11
4 1 1 1 8 11
2 5 0 0 0 11
4 1 0 0 0 11
5 5
2 4 1 0 1 13
4 4 0 1 12 13
1 4 1 1 0 13
3 5 1 1 7 13"""

exec(open("../_auxiliary/input_iterators.py").read())


#line = string_iter()
#line = file_iter(filename[-1] +"-small-attempt1.in")
#line = file_iter("B-small-attempt3.in")
#line = file_iter("A-large-practice.in")

fobject = None
#fobject = open(__script_path__ + filename[-1] + 'output.txt', 'w')
pend = None

			
### Run
###



T = int(next(line))
	
for case in range(T):
	N,K = map(int,next(line).split())
	
	p,h,x,y 	= [[0,0] for _ in range(4)]
	A,B,C,M		= [[0,0,0,0] for _ in range(4)]
			
	if True:
		for num, g in enumerate([p,h,x,y]):
			g[0],g[1],A[num],B[num],C[num],M[num]	 = map(int,next(line).split())	

	if True:
		for limit, num,g in zip([N,N,K,K],range(4),[p,h,x,y]):
			for i in range(2, limit):
				g.append(((A[num] * g[i-1]) + (B[num] * g[i-2]) + C[num])%(M[num]) + 1)

	eliminated = [False for _ in range(len(y))] 
	 
	for _h in range(len(h)):
		for b in range(len(y)): 
			distance_x = abs(p[_h] - x[b])
			if (distance_x + y[b] <= h[_h]):
				eliminated[b] = True
	
	answer = sum([1 for x in eliminated if x])
	print("Case #{}: {}".format(case+1,answer), file= fobject)
	
