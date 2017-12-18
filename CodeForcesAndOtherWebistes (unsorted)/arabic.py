n = int(raw_input())

for x in range(n):
	n2 = int(raw_input())
	result = (list(raw_input().split(" ")))
	value = -1
	for x in range(n2):
		if result[x][0] != "#": 
			value  = x
	
	if value != -1:
		result = result[value+1:n2] + [result[value]] + result[0:value]
		
	print ' '.join(result)
			

	
	
	
