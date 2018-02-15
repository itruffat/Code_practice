from math import log

#
#
# |||| PRINT ||||
#
#

c = 0 #..If c value is -1 then we are ready for launch
#.........Otherwise we are running the test case number c

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

VOID = -1

#
# |||| ALGORITHM ||||
#
#

def getSwitches(m, resultingLights, operationsRequired):
	for x in range(m):
		input_array = list(map(int,get_inp().split()))
		bit_switch = 0
		pos = 1
		for switch in input_array:
			bit_switch += switch * (pos)
			pos *=2
		operationsRequired[bit_switch] = 1
		resultingLights[2**x]     = bit_switch

def bruteForce(firstNonReachableSwitch,resultingLights, operationsRequired):
	it = 1
	while it < firstNonReachableSwitch:
		last_bit 	= furthest_bit(it) 
		other_bits 	= it - last_bit
			
		lastLights  = resultingLights[last_bit]
		otherLights = resultingLights[other_bits]
		
		lightResult = lastLights ^ otherLights
		resultingLights[it] = lightResult
	
		operationResult = operationsRequired[lastLights] + operationsRequired[otherLights]
		if(operationsRequired[lightResult] == VOID or operationResult < operationsRequired[lightResult]):
			operationsRequired[lightResult] = operationResult
		
		it += 1

def constrainedBruteForce(firstNonReachableSwitch,resultingLights, operationsRequired, smallestSwitch):

	it = smallestSwitch
	meetInMiddle = (it != 1)
	allSwitches = firstNonReachableSwitch - 1

	if meetInMiddle:
		print("SV: " + str(it))
	
	while it < firstNonReachableSwitch:
		print("enter")
		last_bit 	= furthest_bit(it) 
		other_bits 	= it - last_bit
			
		lastLights  = resultingLights[last_bit]
		otherLights = resultingLights[other_bits]
		
		lightResult = lastLights ^ otherLights
		
		resultingLights[it] = lightResult
	
		operationResult = operationsRequired[lastLights] + operationsRequired[otherLights]
		
		if(operationsRequired[lightResult] == VOID or operationResult < operationsRequired[lightResult]):
			print(lightResult)
			operationsRequired[lightResult] = operationResult
			if meetInMiddles:
					assert(allSwitches > lightResult)
					otherOperationResult = operationsRequired[allSwitches ^ lightResult]
					if(otherOperationResult != VOID):
						newOperationsAllSwitches = otherOperationResult & operationResult 
						if( operationsRequired[allSwitches] > newOperationsAllSwitches):
							operationsRequired[allSwitches] = newOperationsAllSwitches
			   
		it += smallestSwitch

#
#
# |||| MAIN RUN ||||
#
#

cases= int(get_inp())

for current_case in range(cases):
	
	n, m = (map(int, get_inp().split()))
	
	AllSwitches = (2**n)-1
	
	operationsRequired      = [VOID for _ in range(AllSwitches+1)]
	resultingLights 		= [VOID for _ in range(AllSwitches+1)]	

	operationsRequired[0] = 0
	resultingLights[0] = 0	
	
	getSwitches(m, resultingLights, operationsRequired)	
	#bruteForce(AllSwitches + 1, resultingLights, operationsRequired)
	#constrainedBruteForce(AllSwitches + 1, resultingLights, operationsRequired,1)
	cutValue = int(2**((n)/2))
	print(cutValue)
	constrainedBruteForce(cutValue, resultingLights, operationsRequired,1)
	print(operationsRequired)
	constrainedBruteForce(AllSwitches + 1, resultingLights, operationsRequired,cutValue)
	print(operationsRequired)
	p = operationsRequired[AllSwitches]
		
	put_out((str(p) if p != -1 else "IMPOSSIBLE"), current_case)
		
		
if(c != -1):
	print("--end of output--")	
