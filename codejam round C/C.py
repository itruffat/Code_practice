import os
from math import *

example_test= """2
2 3 1 2 1 2 1 1 9
10 10 10001 10002 10003 10004 10005 10006 89273
"""

exec(open("../_auxiliary/input_iterators.py").read())

line = string_iter()
#line = file_iter("C-small-practice.in")
line = file_iter("C-large-practice.in")
#line = file_iter(filename[-1] +"-large-attempt1.in")

#fobject = None
fobject = open(__script_path__ + filename[-1] + 'output.txt', 'w')
pend = None
	
def resolve(genA,N,K):
	answer = 0
	multipliers = 0
	for x in range(N):
		power_mult = 1
		for y in range(K):
			power_mult  *= (x+1)
			multipliers += power_mult
		answer += next(genA) * (N - x) * multipliers
	return int(answer)
	

def oracle(genA,N,K):
	A = [next(genA) for _ in range(N)]
	answer = 0
	for power in range(1,K+1):
		for x in range(N):
			current_answer = 0
			for y in range(N-x):
				current_answer += A[x+y] * ((y+1)**power) 
				answer += current_answer  		
	return answer

def A_generator(x, y, C, D, E1, E2, F):		
	while True:
		yield ((x + y)%F)
		x0, y0 = [x,y] 
		x = C*x0 + D*y0 + E1
		y = D*x0 + C*y0 + E2

### Run		
###

T = int(next(line))
		
for case in range(T):
	print(case)
	input_list = list(map(int, next(line).split()))
	genA  = A_generator(*input_list[2:])
	N,K = input_list[:2] 
	answer  = resolve(genA, N, K)
	print( "Case #{}: {}".format(case+1,str(answer%1000000007)),file = fobject)


# 	* Explanation
#	-------------
# When one looks at the formula it's very easy to see a pattern
#
# Example: A = [a,b,c],N = 3, K = 5
#
# Everything that will be multiplied by powers of the base 1 
# a * n		b * (n-1)	c * (n-2)	#power 1
# a * n		b * (n-1)	c * (n-2)	#power 2
# a * n		b * (n-1)	c * (n-2) 	#power 3
# a * n		b * (n-1)	c * (n-2) 	#power 4
# a * n		b * (n-1)	c * (n-2) 	#power 5
#
# Everything that will be multiplied by powers of the base 2
# b * (n-1) * 2		c * (n-2) * 2	#power 1
# b * (n-1) * 4		c * (n-2) * 4	#power 2
# b * (n-1) * 8		c * (n-2) * 8	#power 3
# b * (n-1) * 16	c * (n-2) * 16	#power 4
# b * (n-1) * 32	c * (n-2) * 32	#power 5
#
# Everything that will be multiplied by powers of the base 3
# c * (n-2) * 3						#power 1
# c * (n-2) * 9						#power 2
# c * (n-2) * 27					#power 3
# c * (n-2) * 81					#power 4
# c * (n-2) * 243					#power 5
#
# If we compress each table into a single line, we get
# a * (n-0) * (1+1+1+1+1+1) + b * (n-1) * (1+1+1+1+1+1) + c * (n-2) * (1+1+1+1+1+1) 	#powers of base 1
# b * (n-1) * (2+4+8+16+32) + c * (n-2) * (2+4+8+16+32)									#powers of base 2
# c * (n-2) * (3+9+27+81+243)															#powers of base 3
#
# Finally we reshuffle a little and we get this, which is far more useful
# a * (n-0) * ((1+1+1+1+1+1))+
# b * (n-1) * ((1+1+1+1+1+1) + (2+4+8+16+32))+
# c * (n-2) * ((1+1+1+1+1+1) + (2+4+8+16+32) + (3+9+27+81+243))
#
# Finally, we add a few renames to those additions
# a * (n-0) * (multipliers(0))+
# b * (n-1) * (multipliers(0) + multipliers(1))+
# c * (n-2) * (multipliers(0) + multipliers(1) + multipliers(2))
#
# So, for each original number we have the following formula:
# number * (n-position) * sum(multipliers from [0] to [position])
