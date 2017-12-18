n = int(raw_input())

dynamo_0 = []
dynamo_1 = []
dynamo_2 = []

def uninitiated(z):
	return z == []

for x in range(n):
	dynamo_0.append(-1)
	dynamo_1.append(-1)
	dynamo_2.append(-1)

def first_call(n):
	if n ==0:
		return 0
	elif n==1:
		return 0
	elif n==2:
		return 4
	else:
		result = 0
		#2 backwards/fowards
		result+= iteration(n-2, True, False) * 2
		#1 backward/fowards
		result+= iteration(n-2, True, True ) * 2
		#0 steps
		result+= iteration(n-1, False, True) * 1

def iteration(n, step0_allowed, step1_allowed):
	result = 0
	if step0_allowed and n>=0:
		if uninitiated(dynamo_0[n-1]):
			iteration(n-1, False, True)
		result += dynamo_0[n-1]
	
	if step1_allowed and n > 0:
		if uninitiated(dynamo_1[n-1]):
			iteration(n-2, True, True)
		result += dynamo_1[n-2]
		
	if n > 1:
		if uninitiated(dynamo_2[n-1]):
			iteration(n-2, step0_allowed, False)
		result += dynamo_1[n-2]
	
