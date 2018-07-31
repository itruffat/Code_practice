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
#line = file_iter(filename[-1] +"-small-attempt1.in")
line = file_iter("B-large.in")
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
	
	answer = sum([1 for _x in eliminated if _x])
	print("Case #{}: {}".format(case+1,answer), file= fobject)
	
