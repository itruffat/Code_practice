###
### Config data
###

import os
from math import *
from copy import deepcopy

example_test= """2
5
1 2
2 3
3 4
2 4
5 3
3
1 2
3 2
1 3"""

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
#line = file_iter("A-small-attempt4.in")
line = file_iter("A-large.in")

#fobject = None
fobject = open(__script_path__ + filename[-1] + 'output.txt', 'w')
pend = None

check_with_oracle = False

		
			
### Run
###

T = int(next(line))
	
for case in range(T):
	planets = int(next(line))
	tubes = [[] for _ in range(planets)]

	for x in range(planets):
		p1, p2 = map(lambda x:int(x) - 1, next(line).split())
		tubes[p1].append(p2)
		tubes[p2].append(p1)
	
	queue = []	
	
	def bds(tubes,depth,stop):
		ctube = 0
		cdepth = 0
		while True:
			if len(queue) == 0 or queue[-1] != ctube:
				depth[ctube] = cdepth
				queue.append(ctube)
			if len(tubes[ctube]) != 0:
				x = tubes[ctube].pop()
				if depth[x] == -1:
					ctube = x
					cdepth += 1
				elif depth[x] < cdepth - 1:
					if stop:
						return cdepth - depth[x] + 1
			else:
				queue.pop()
				cdepth -= 1
				
	depth = [-1 for _ in range(planets)]
	length = bds(deepcopy(tubes), depth, True)
	circle = queue[-length:]
	
	depth = [-1 for _ in range(planets)]
	
	for x in circle:
		depth[x] = 0
		
	for x in circle:
		bds(tubes,depth, False)
	
	answer = depth
	
	print( "Case #{}: {}".format(case+1," ".join(map(str,answer))),file = fobject)
