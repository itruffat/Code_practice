# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=29&page=show_problem&problem=36

###
### Config data
###

import os
from math import floor, ceil, log

example_test= """1 10
100 200
201 210
900 1000"""

example_test= """1 10"""

exec(open("../../../_auxiliary/input_iterators.py").read())

#line = input_iter()
line = string_iter()

fobject = None
pend = None


###
### Solution
###

def resolve(v1,v2):
	answer = 1
	truth = [False for _ in range(v1,v2+1)]
	uncovered = len(truth)
	x = 1
	while uncovered != 0:
		if (x-1)%3 == 0 and ((x-1)/3)%2 != 0:
			x = (x-1)//3 
		else:
			x *= 2
		
		if v1 <= x and x <= v2:
			if truth[x-v1] == False:
				uncovered -= 1
				print(uncovered)
				truth[x-v1] = True
		answer += 1
	return answer			


def oracle(v1,v2):
	answer = 0
	for x in range(v1, v2+1):
		t_answer = 1
		tx = x
		while tx != 1:
			if (tx%2) == 0:
				tx= (tx//2)
			else:
				tx = (tx * 3)  + 1
			t_answer += 1	
		answer = max(answer, t_answer)
	return answer
	
###
### Run
###

while True:
	try:
		value1, value2 = list(map(int,next(line).split()))
	except:
		break
	answer = resolve(value1, value2)
	answer2 = oracle(value1, value2)
	assert(answer == answer2)
	print("{} {} {}".format(value1, value2, answer), end = pend)
