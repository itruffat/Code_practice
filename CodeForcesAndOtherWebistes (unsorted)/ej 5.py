n = int(raw_input())

for x in range(n):
	cnd, eat = map(lambda x:int(x),raw_input().split())
	quantity = list(map(lambda x:int(x),raw_input().split()))
	i = 0
	for x in quantity:
		i += x/eat
	print i
