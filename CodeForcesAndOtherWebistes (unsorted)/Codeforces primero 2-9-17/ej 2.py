prittyPrint = {1:"Anton",-1:"Danik",0:"Friendship"}
n = int(raw_input())
letters = raw_input()

result = 0
for l in letters:
	if l == "A":
		result +=1
	else:
		result -=1

if result != 0:
	result = result / abs(result)		

print prittyPrint[result]
