coins = {"A":0, "B":1, "C":2}
comparison = {"<":1, ">":-1}

weights = []
for x in range(3):
#	weights.append([])
#	for y in range(3):
#		weights[x].append(0)	
	weights.append(0)

for x in range(3):
	c1,s,c2 = (raw_input().split())
	#weights[coins[c1]][coins[c2]] = comparison[s]
	#weights[coins[c2]][coins[c1]] = comparison[s] * -1
	weights[coins[c1]]+= comparison[s]
	weights[coins[c2]]-= comparison[s]


