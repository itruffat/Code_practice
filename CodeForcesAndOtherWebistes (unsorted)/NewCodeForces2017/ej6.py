input_lines = """1 3"""

recibir = True
i__l = -1

def get_input():
	global i__l
	if not recibir:
		i__l += 1
		return input_lines.splitlines()[i__l]
	return raw_input()

a, b = map(int,get_input().split())

#maximo = max(a,b) - 1

#total = 6
#results = total - maximo

results =  6 - max(a,b)
	
numerador =   [1,1,1,2,5,1]	
denominador = [6,3,2,3,6,1]

print str(numerador[results]) + "/" + str(denominador[results])
