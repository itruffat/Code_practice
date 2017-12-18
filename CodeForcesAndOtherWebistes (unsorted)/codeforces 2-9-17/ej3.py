prittyAnswer = {True:"Yes", False:"No"}
n = int(raw_input())

current_letra = 97
resta = 0
answer = ""

numero = n

while(numero > 0):
	assert numero > 0
	numero -= resta
	answer += chr(current_letra)
	resta +=1 
	if resta > numero:
		current_letra +=1
		resta = 0
	assert numero >= 0

if answer == "":
	answer = "p"
		
print answer
