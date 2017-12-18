coins = {"A":0, "B":1, "C":2}
coins_inv = {0:"A", 1:"B", 2:"C"}
comparison = {"<":-1, ">":1}

weights = []
for x in range(3):
	weights.append(0)

for x in range(3):
	c1,s,c2 = list(raw_input())
	weights[coins[c1]]+= comparison[s]
	weights[coins[c2]]-= comparison[s]

result = ""
position = -1
for x in range(3):
	if weights[x] == -2:
		position = x
		
if position == -1:
	print "Impossible"
else:
	result += coins_inv[position]
	position = -1
	for x in range(3):
		if weights[x] == 0:
			position = x
	if position == - 1:
		print "Impossible"
	else:
		result += coins_inv[position]
		position = -1
		for x in range(3):
			if weights[x] == 2:
				position = x
		result += coins_inv[position]
		
print result

