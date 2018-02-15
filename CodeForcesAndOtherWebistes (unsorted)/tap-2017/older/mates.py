import copy
c = 0
i = 0

def determinante(matriz):
	if len(matriz) == 2:
		return matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]

	value = 0
	molde = matriz[1:]

	for y in range(len(molde[0])):
		new = copy.deepcopy(molde)
		for x in range(len(molde)): 
			new[x].pop(y)
		value += determinante(new)
		del new
	
	return value


def get_inp():
	global c
	global i
	if c == -1:
		return raw_input()
	i+=1
	if c==0:
		answer = """5 3
		13 15 14 6 3"""
	if c==1:
		answer = """3 2
		2 3 7"""
	if c==2:
		answer = """5 2
		1 1 1 1 1"""
	return answer.splitlines()[i - 1]

n,k = (map(int,get_inp().split()))

valores = list(map(int,get_inp().split()))

matriz = []
for x in range(n):
	y = [0 for z in range(n)]
	
	i =  0
	while i < k:
		 #y[x - i] = valores[x - i]
		 y[x - i] = 1.0
		 i +=1
	matriz.append(y)


#print determinante(matriz)

i = 0
for m in range(len(matriz)):
	matriz[m].append(valores[m] * 1.0) 

for x in matriz:
	print x


z = 0

def restar(fila1, fila2, columna):
	cociente = fila2[columna] / fila1[columna]
	for x in range(columna, len(fila2)):
		fila2[x]-= cociente*fila1[x]

for y in range(0, len(matriz)-1):
	for x in range(y + 1, len(matriz)):
		restar(matriz[y],matriz[x],y)

print " "
print "-----"
print " "
for x in matriz:
	print x
