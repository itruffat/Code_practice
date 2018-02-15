from collections import deque

# |||| PRINT ||||

c = -1 	# If c value is -1 then we are ready for launch
		# Otherwise run test case number c
i = -1 	# This value always has to be 0
		
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

# |||| ALGORITHM ||||

def getSwitches(unseen, switches, m):
	for _ in range(m):
		bit_switch = 0
		pos = 1
		for switch in map(int,get_inp().split()):
			bit_switch += switch * (pos)
			pos *=2
		if(unseen[bit_switch]):
			unseen[bit_switch] = False
			switches.append(bit_switch)


cases= int(get_inp())

for current_case in range(cases):
	n, m = (map(int, get_inp().split()))
	allLights   = (2**n)-1
	
	unseen      = [True for a in range(allLights+1)]
	unseen[0]   = False
	
	switches = []
	getSwitches(unseen, switches, m)

	nodeQueue = deque(switches)	
	nodesInDepth = 0
	depth = 1
		
	while len(nodeQueue) != 0 and unseen[allLights]:
		if nodesInDepth == 0:
			nodesInDepth = len(nodeQueue)
			depth += 1
		nodesInDepth -= 1
		
		cnode = nodeQueue.popleft()
		
		for switch in switches:
			fnode = cnode ^ switch
			if(unseen[fnode]):
				nodeQueue.append(fnode)
				unseen[fnode] = False
			
			if(fnode == allLights):
				break

	put_out("IMPOSSIBLE" if unseen[allLights] else str(depth), current_case)
		
		
if(c != -1):
	print("--end of output--")	
