def get_inp():
	return input()

def put_out(p,x):
	print("Case "+str(x+1) + ": " + p)

VOID = -1

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

cases= int(get_inp())

for current_case in range(cases):
	
	n, m = (map(int, get_inp().split()))
	AllLights   = (2**n)-1
	AllSwitches = (2**m)-1
	middle      = (2**int((m)/2))
	
	operationsRequired      = [-1 for a in range(AllLights+1)]
	operationsRequired[0]   = 0
	resultingLights 		= [0 for a in range(AllSwitches+1)]	
	
	getSwitches(resultingLights, operationsRequired, m)	
	
	p = operationsRequired[AllLights]	
	put_out((str(p) if p != -1 else "IMPOSSIBLE"), current_case)
