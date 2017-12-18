n = int(raw_input())
i = 0
for x in range(n):
	a,b,c = map(lambda x:int(x),raw_input().split())
	if a + b + c > 1:
		i +=1

print i
