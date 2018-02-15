from math import log

#
#
# |||| PRINT ||||
#
#

#If c value is -1 then we are ready for launch
#Otherwise we are running the test case #c
c = -1
i = -1
		
def get_inp():
	global c
	global i
	if c==-1:
		return input()
	i+=1
	if c==0:
		return """2
2 2
0 1
1 0
3 2
1 0 1
1 1 0""".splitlines()[i]
	if c==1:
		return """1
5 5
1 1 1 1 0
1 0 0 0 0
0 0 1 0 0
0 0 0 0 1
0 0 0 0 0""".splitlines()[i]
		
def put_out(p,x):
	global c
	if c>-1:
		print("---Original")
	print("Case "+str(x+1) + ": " + p)
	if c>-1:
		print("...Expected")
	if c==0:
		print("""Case 1: 2
Case 2: IMPOSSIBLE""".splitlines()[x])
	if c==1:
		print("""Case 1: 2""")

#
#
# |||| AUX ||||
#
#

def furthest_bit(x):
	return(2**int(log(x,2)))

#
#
# |||| ALGORITHM ||||
#
#

def fuerza_bruta(n,m):
	pass


#
#
# |||| MAIN RUN ||||
#
#

cases= int(get_inp())

for current_case in range(cases):
	
	n, m = (map(int, get_inp().split()))
	
	AllSwitches = (2**n)-1
	
	operationsRequired      = [-1 for _ in range(AllSwitches+1)]
	resultingLights 		= [-1 for _ in range(AllSwitches+1)]	

	operationsRequired[0] = 0
	resultingLights[0] = 0	
		
	for x in range(m):
		bit_switch = 0
		pos = 1
		input_array = list(map(int,get_inp().split()))
		for switch in input_array:
			bit_switch += switch * (pos)
			pos *=2
		operationsRequired[bit_switch] = 1
		resultingLights[2**x]     = bit_switch
	it = 1
	
	while it <= AllSwitches:
		last_bit = furthest_bit(it) 
		other_bits = it - last_bit
			
		lastLights  = resultingLights[last_bit]
		otherLights = resultingLights[other_bits]
		
		lightResult = lastLights ^ otherLights
		resultingLights[it] = lightResult
	
		operationResult = operationsRequired[lastLights] + operationsRequired[otherLights]
		operationsRequired[lightResult] = operationResult if operationsRequired[lightResult] == -1 \
										   else  min(operationsRequired[lightResult], operationResult)
		it += 1
	
	p = operationsRequired[AllSwitches]
		
	put_out((str(p) if p != -1 else "IMPOSSIBLE"), current_case)
		
if(c != -1):
	print("--end of output--")	
	
