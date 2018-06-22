###
### Config data
###

import os
from math import *

example_test= """5
6
0 1 0 0 0 0
1 0 1 0 0 0
0 1 0 1 0 0
0 0 1 0 1 0
0 0 0 1 0 1
0 0 0 0 1 0
6
0 2 0 0 0 0
2 0 0 0 0 0
0 0 0 3 0 0
0 0 3 0 0 0
0 0 0 0 0 4
0 0 0 0 4 0
6
0 1 0 0 0 0
1 0 0 0 0 0
0 0 0 2 0 0
0 0 2 0 0 0
0 0 0 0 0 4
0 0 0 0 4 0
6
0 1 1 1 1 1
1 0 0 0 0 0
1 0 0 0 0 0
1 0 0 0 0 0
1 0 0 0 0 0
1 0 0 0 0 0
8
0 5 0 0 0 0 0 0
5 0 0 0 0 0 0 0
0 0 0 5 0 0 0 0
0 0 5 0 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 5 0 0 0
0 0 0 0 0 0 0 5
0 0 0 0 0 0 5 0"""

exec(open("../_auxiliary/input_iterators.py").read())

line = string_iter()
#line = file_iter("B-small-attempt0.in")
#line = file_iter(filename[-1] +"-large-attempt1.in")

#fobject = None
fobject = open(__script_path__ + filename[-1] + 'output.txt', 'w')
pend = None

check_with_oracle = False

		
			
### Run
###

T = int(next(line))

		
for case in range(T):
	elements = int(next(line))
	tree = [list(map(int, next(line).split())) for _ in range(elements)]
	#print(tree)
	for t in tree:
		print(t)
	print("")
	answer = ""
	print( "Case #{}: {}".format(case+1,str(answer)),file = fobject)
