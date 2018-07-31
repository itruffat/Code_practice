###
### Config data
###

import os
from math import *
from copy import deepcopy
#import geometria_linea

example_test= """5
6 1 1000000000000000
1 1 1 1 0 100 0
6 1 -100
1 1 1 1 0 100 0
10 1 8
4 3 4 1 5 20 -10
10 2 8
4 3 4 1 5 20 -10
10 1 8
4 3 4 1 5 20 -19"""

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
#line = file_iter("B-small-attempt3.in")
line = file_iter("A-small-practice.in")

#fobject = None
fobject = open(__script_path__ + filename[-1] + 'output.txt', 'w')
pend = None

			
### Run
###

T = int(next(line))
	
for case in range(T):

	answer = "IMPOSSIBLE"

	N,O,D,x = *map(int,next(line).split()), [0,0]
	x[0], x[1], A, B, C, M, L = map(int,next(line).split())
	minimum = min(x[0] + L,x[1] + L)
	for i in range(2, N): 
		x.append(((A * x[i-1]) + (B * x[i-2]) + C)%(M))
		#minimum = min(minimum, x[-1] + L) 
	
	for i in range(len(x)):
			x[i] += L
	
	treshold = lambda c_d, c_o: (c_d > D or c_o > O)	
	
	p1 = 0 
	p2 = 0
	smallest = min(*x)
	largest = smallest - 1
	odds = 0
	tsum = 0
	while p1 < len(x) and p2 <len(x):
		tsum += x[p2]
		odds += 1 if x[p2] % 2 == 1 else 0

		while (treshold(tsum, odds)) and p1 <= p2:
			tsum -= x[p1]
			odds -= 1 if x[p1] % 2 == 1 else 0
			p1 += 1
		
		if(not treshold(tsum, odds)):
			largest = max(largest, tsum)
		
		p2 += 1
	
	if largest >= smallest:
		answer = largest
			
	print("Case #{}: {}".format(case+1,answer), file= None)
	print("Case #{}: {}".format(case+1,answer), file= fobject)
	
