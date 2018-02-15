from collections import deque


MEET_IN_THE_MIDDLE = False
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

def getSwitches(switches, opReq, m):
	for _ in range(m):
		bit_switch = 0
		pos = 1
		for switch in map(int,get_inp().split()):
			bit_switch += switch * (pos)
			pos *=2
		
		if (opReq[bit_switch] != 1) and (bit_switch != 0):
			opReq[bit_switch] = 1
			switches.append(bit_switch)
		
def bruteForce(switches, opReq, allLig, additionalProcessing):
	queue = deque(switches)
	
	for switch in switches:
		additionalProcessing(opReq, switch, opReq[switch], allLig)
		
	while len(queue) != 0:
		it = queue.popleft()
		for sw in switches:
				
			lightResult = it ^ sw
			operationResult = opReq[sw] + opReq[it]
			
			if(opReq[lightResult] == VOID or operationResult < opReq[lightResult]):
				if(opReq[lightResult] == VOID):
					queue.append(lightResult)
				opReq[lightResult] = operationResult
				
			additionalProcessing(opReq, lightResult, operationResult, allLig)

def doNothing(opReq, lightResult, operationResult, allLights):
	pass

def doMeetInTheMiddle(opReq, lightResult, operationResult, allLights):
	if opReq[lightResult] == operationResult:
		complementOpResult = opReq[allLights ^ lightResult]
		if(complementOpResult != VOID):
			allLightsResult = complementOpResult + operationResult 
			if( opReq[allLights] == VOID or allLightsResult < opReq[allLights]):
				opReq[allLights] = allLightsResult	
#
#
# |||| MAIN RUN ||||
#
#

cases= int(get_inp())

for current_case in range(cases):
	
	n, m = (map(int, get_inp().split()))
	allLights   = (2**n)-1
	half_m = int((m)/2)
	operationsRequired      = [VOID for a in range(allLights+1)]
	operationsRequired[0]   = 0
	
	
	switches = []
	getSwitches(switches, operationsRequired, half_m )	
	bruteForce(switches, operationsRequired, allLights, doNothing) 
	
	switches = []
	getSwitches(switches, operationsRequired, m - half_m)	
	bruteForce(switches, operationsRequired, allLights, doMeetInTheMiddle)

	
	p = operationsRequired[allLights]	
	put_out(("IMPOSSIBLE" if p == VOID else str(p)), current_case)
		
		
if(c != -1):
	print("--end of output--")	
