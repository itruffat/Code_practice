from math import log

#
#
# |||| PRINT ||||
#
#

c =  0 	# If c value is -1 then we are ready for launch
		# Otherwise run test case number c

i = -1 #This value always has to be 0
		
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
	if c==2:
		return """1
2 2
0 1
1 0""".splitlines()[i]
	if c==3:
		return """2
1 1
1
1 1
0""".splitlines()[i]	

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
	if c==2:
		print("""Case 1: 2""")
	if c==3:
		print("""Case 1: 1
Case 2: IMPOSSIBLE""".splitlines()[x])


VOID = -1

#
# |||| ALGORITHM ||||
#
# We must think of switches as a mask. A single number represents multiple inst ances. 
#
# Resulting lights: the lights that are on after pressing all the switches in the mask.
# Operations Required: the least ammount of flips required to get that light configuration.
#

def furthest_bit(x):
	return(2**int(log(x,2)))

def getSwitches(resultingLights, operationsRequired, m):
	for x in range(m):
		input_array = list(map(int,get_inp().split()))
		bit_switch = 0
		pos = 1
		for switch in input_array:
			bit_switch += switch * (pos)
			pos *=2
		operationsRequired[bit_switch] = 1 if(bit_switch !=0) else 0
		resultingLights[2**x]     = bit_switch

def bruteForce(resultingLights, operationsRequired, switchesEnd):
	it = 1
	while it < switchesEnd:
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

def constrainedBruteForce(resultingLights, operationsRequired, switchesEnd, allLights, smallestSwitch):

	it = smallestSwitch
	meetInMiddle = (it != 1)
	
	while it < switchesEnd:
		last_bit 	= furthest_bit(it) 
		other_bits 	= it - last_bit
			
		lastLights  = resultingLights[last_bit]
		otherLights = resultingLights[other_bits]
		
		lightResult = lastLights ^ otherLights
		
		resultingLights[it] = lightResult
	
		operationResult = operationsRequired[lastLights] + operationsRequired[otherLights]
		
		if(operationsRequired[lightResult] == VOID or operationResult < operationsRequired[lightResult]):
			operationsRequired[lightResult] = operationResult
		
		if meetInMiddle and operationsRequired[lightResult] == operationResult:
				otherOperationResult = operationsRequired[allLights ^ lightResult]
				if(otherOperationResult != VOID):
					operationToGetAllLights = otherOperationResult + operationResult 
					if( operationsRequired[allLights] == VOID or operationToGetAllLights < operationsRequired[allLights]):
						operationsRequired[allLights] = operationToGetAllLights
			   
		it += smallestSwitch

def meetInTheMiddle(resultingLights, operationsRequired, AllSwitches, middle):
	constrainedBruteForce(resultingLights, operationsRequired,         middle,      1)
	constrainedBruteForce(resultingLights, operationsRequired,AllSwitches + 1, middle)
	
#
#
# |||| MAIN RUN ||||
#
#

cases= int(get_inp())

for current_case in range(cases):
	
	n, m = (map(int, get_inp().split()))
	AllLights   = (2**n)-1
	AllSwitches = (2**m)-1
	middle      = (2**int((m)/2))
	first__half      = (2**int((m)/2))
	second_half      = m - (2**int((m)/2))
	
	operationsRequired      = [-1 for a in range(AllLights+1)]
	operationsRequired[0]   = 0
	resultingLights 		= [0 for a in range(AllSwitches+1)]	
	
	getSwitches(resultingLights, operationsRequired, m)	
	meetInTheMiddle(resultingLights, operationsRequired, AllSwitches, middle)
	
	p = operationsRequired[AllLights]	
	put_out((str(p) if p != -1 else "IMPOSSIBLE"), current_case)
		
		
if(c != -1):
	print("--end of output--")	
