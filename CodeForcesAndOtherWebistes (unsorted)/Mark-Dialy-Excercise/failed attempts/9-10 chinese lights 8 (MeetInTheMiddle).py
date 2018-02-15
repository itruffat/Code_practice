from math import log

#
#
# |||| PRINT ||||
#
#

c = -1 	# If c value is -1 then we are ready for launch
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
# We must think of switches as a mask. A single number represents multiple instances. 
#
# Resulting lights: the lights that are on after pressing all the switches in the mask.
# Operations Required: the least ammount of flips required to get that light configuration.
#

def getSwitches(resultingLights, operationsRequired, m):
	for x in range(m):
		bit_switch = 0
		pos = 1
		for switch in map(int,get_inp().split()):
			pass
			bit_switch += switch * (pos)
			pos *=2
		operationsRequired[bit_switch] = 1 if(bit_switch !=0) else 0
		resultingLights[2**x]     = bit_switch

def bruteForce(resLight, opReq, switchEnd, allLig, additionalProcessing):
	it = 1

	while it < switchEnd:
		last_bit 	= (2**int(log(it,2)))
		#Tecnicamente esto podemos sacarlo
		#al estar recorriendo en orden el algoritmo daria bien
		#aun sin esto, solo nos basta con multiplicar por dos el anterior
		other_bits 	= it - last_bit
		
		lastLights  = resLight[last_bit]
		otherLights = resLight[other_bits]
	
		lightResult = lastLights ^ otherLights
	
		resLight[it] = lightResult

		operationResult = opReq[lastLights] + opReq[otherLights]
	
		if(opReq[lightResult] == VOID or operationResult < opReq[lightResult]):
			opReq[lightResult] = operationResult
		
		additionalProcessing(opReq, lightResult, operationResult, allLig)
		   
		it += 1

def doNothing(opReq, lightResult, operationResult, allLights):
	pass

def doMeetInTheMiddle(opReq, lightResult, operationResult, allLights):
	if opReq[lightResult] == operationResult:
		complementConfigurationReq = opReq[allLights ^ lightResult]
		if(complementConfigurationReq != VOID):
			operationToGetAllLights = complementConfigurationReq + operationResult 
			if( operationsRequired[allLights] == VOID or operationToGetAllLights < operationsRequired[allLights]):
				operationsRequired[allLights] = operationToGetAllLights	
#
#
# |||| MAIN RUN ||||
#
#

cases= int(get_inp())

for current_case in range(cases):
	
	n, m = (map(int, get_inp().split()))
	allLights   = (2**n)-1
	halfm = int((m)/2)
	switchesFirstHalf      = (2**     halfm )
	switchesSecondHalf     = (2**(m - halfm))
	
	operationsRequired      = [-1 for a in range(allLights+1)]
	operationsRequired[0]   = 0
	
	resultingLights = [0 for _ in range(switchesFirstHalf+1)]	
	getSwitches(resultingLights, operationsRequired, halfm)	
	bruteForce(resultingLights, operationsRequired, switchesFirstHalf, allLights, doNothing) 
	
	resultingLights = [0 for _ in range(switchesSecondHalf+1)]	
	getSwitches(resultingLights, operationsRequired, m - halfm)	
	bruteForce(resultingLights, operationsRequired, switchesSecondHalf, allLights, doMeetInTheMiddle)
	
	
	p = operationsRequired[allLights]	
	put_out((str(p) if p != -1 else "IMPOSSIBLE"), current_case)
		
		
if(c != -1):
	print("--end of output--")	
