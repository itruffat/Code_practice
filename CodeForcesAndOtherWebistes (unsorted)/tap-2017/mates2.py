# Hacemos eliminacion gaussiana.
# Si los valores no son enteros positivos, no hay solucion


import copy
c = 2
i = 0


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

n,k 	= 		map(int,get_inp().split())

valores =  list(map(int,get_inp().split()))

matriz = []

# Creo la matriz, con uno en los lugares correspondientes
for x in range(n):
	y = [0 for z in range(n)]
	i =  0
	while i < k:
		 y[x - i] = 1.0
		 i +=1
	matriz.append(y)

#Agrego el valor al final de la columan para tener la matriz extendida
# [a1 a2 a3 | valor_1]
# [b1 b2 b3 | valor_2]
# [c1 c2 c3 | valor_3]
for m in range(len(matriz)):
	matriz[m].append(valores[m] * 1.0) 

def restarFilaTriangulada(fila1, fila2, columna):
	cociente = fila2[columna] / fila1[columna]
	for x in range(columna, len(fila2)):
		fila2[x]-= cociente*fila1[x]

def despejarValor(fila, columna):
	return fila[-1]/fila[columna]

def restarValor(fila, columna, multiplicador):
	fila[-1] -= fila[columna] * multiplicador
	fila[columna] = 0

# Triangulo la matriz
for y in range(0, len(matriz)-1):
	for x in range(y + 1, len(matriz)):
		restarFilaTriangulada(matriz[y],matriz[x],y)

# Con la matriz triangulada, despejo los x
valid = True
for y in range(1, len(matriz) + 1):
	valid = False
	val =  despejarValor(matriz[-y], len(matriz) - y)
	if val < 0 or int(val) != val:
		break #Si algun x despejado no es positivo entero, el resultado es falso
	valid = True # Llegar a este punto garantia que es valido
	for x in range(y, len(matriz) + 1):
		restarValor(matriz[-x], len(matriz) - y, val)

print "S" if valid else "N"
