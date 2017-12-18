n = int(raw_input())

for x1 in range(n):
	n2 = int(raw_input())
	result = list(map(lambda x: int(x) , (raw_input().split(" "))))
	i = 0
	for x in result:
		i+= x
	print "Case "+str(x1+1) +": " + str(i)
