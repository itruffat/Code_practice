n1,n2 = (map(lambda x: int(x),raw_input().split()))


i = 0
while n1 <= n2:
	n1= n1 * 3
	n2= n2 * 2
	i+=1

print i
