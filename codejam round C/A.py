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

exec(open("../_auxiliary/input_iterators.py").read())

#line = string_iter()
#line = file_iter(filename[-1] +"-small-attempt1.in")
line = file_iter("A-small-attempt4.in")
#line = file_iter("A-large-practice.in")

#fobject = None
fobject = open(__script_path__ + filename[-1] + 'output.txt', 'w')
pend = None

		
		
def resolve_with_calls(planets, tubes):
	
	depth, queue, stop = [None, None, None]
	
	def dfs(ctube):
		queue.append(ctube)
		for x in tubes[ctube]:
			if depth[x] == -1:
				depth[x] = depth[ctube] + 1
				previous_answer = dfs(x)
				if previous_answer != -1:
					return previous_answer
			elif depth[x] < depth[ctube] - 1 and stop:
				return depth[ctube] - depth[x] + 1
		queue.pop()
		return -1
	
	#prepare		
	depth = [-1 for _ in range(planets)]
	for x in [0]: depth[x] = 0
	queue = []
	stop = True
	#run
	distance = dfs(0)
	circle = queue[-distance:]
	
	#prepare
	depth = [-1 for _ in range(planets)]
	for x in circle: depth[x] = 0
	queue = []
	stop = False
	#run	
	for x in circle: dfs(x)
	
	return depth		
			
			
def resolve_without_calls(planets, tubes):
	depth = []
	start_points = [0]
	for times in range(2):
		depth = [(0 if p in start_points else -1) for p in range(planets)]
		queue = []
		for start_point in start_points:
			ctubes = deepcopy(tubes)
			ctube  = start_point
			while True: #This is a DFS
				if 0 < len(ctubes[ctube]):
					ntube = ctubes[ctube].pop()
					if depth[ntube] == -1:
						queue.append(ctube)
						depth[ntube] = depth[ctube] + 1
						ctube = ntube
					elif depth[ntube] + 1 < depth[ctube] and times == 0: #This is our stop condition for the first iteration
						queue.append(ctube)
						distance = depth[ctube] - depth[ntube] + 1
						start_points = queue[-distance:]
						break
				elif len(queue) == 0 and times == 1: #This is our stop condition for the second iteration
						break
				else:
					ctube = queue.pop()
	return depth
			
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
	
	answer = resolve_without_calls(planets, tubes)
	
	try:
		answer_resolve_with_calls = resolve_with_calls(planets, tubes)
		assert(answer == answer_resolve_with_calls)
	except AssertionError:
		raise e
	except Exception as e:
		print("resolve_with_calls did not finish")
	
	print( "Case #{}: {}".format(case+1," ".join(map(str,answer))),file = fobject)
	
