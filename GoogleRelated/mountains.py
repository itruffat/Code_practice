inputs =  [1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]

currentmax = -1
acumulated =  0
n = 0
totalval = 0


for a in inputs:
	if a >= currentmax:
		totalval += min(a,currentmax) * n - acumulated 
		currentmax = a
		n = 0
		acumulated = 0
	else:
		acumulated += a
		n+=1

previousmax = currentmax

currentmax = 0
acumulated = 0

for a in reversed(inputs):
	if currentmax < previousmax:
		if a >= currentmax:
			totalval += min(a,currentmax)*n - acumulated 
			currentmax = a
			n = 0
			acumulated = 0
		else:
			acumulated += a
			n+=1
			
print(totalval)
