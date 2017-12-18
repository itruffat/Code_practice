from math import sqrt

solo = 0
primero_ocupado = 1
segundo_ocupado = 8
ultimo_ocupado = 2
anteultimo_ocupado = 4

def ccc_aux(n):
	assert n%2 == 0
	if n==0:
		return 0
	n/= 2
	n+=1
	return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))


def contar_combinaciones_coleccion2(n):
	global solo
	global primer_ocupado
	global ultimo_ocupado
	global anteultimo_ocupado
	combinaciones = [0 for x in range(8)]
	if n%2 == 0:
			combinaciones[solo] = ccc_aux(n)
			combinaciones[primero_ocupado+ultimo_ocupado] = ccc_aux(n - 2)
			combinaciones[primero_ocupado+anteultimo_ocupado] = combinaciones[primero_ocupado+ultimo_ocupado]
			combinaciones[ultimo_ocupado+anteultimo_ocupado] = combinaciones[primero_ocupado+ultimo_ocupado]
	elif n%2 == 1:
			combinaciones[primero_ocupado] = ccc_aux(n - 1)
			combinaciones[ultimo_ocupado] = combinaciones[primero_ocupado]
			combinaciones[anteultimo_ocupado] = combinaciones[primero_ocupado]
			if n > 3:
				combinaciones[primero_ocupado+ultimo_ocupado+anteultimo_ocupado] = ccc_aux(n - 3)
	return combinaciones


def contar_combinaciones_coleccion3(n):
	global solo
	global primer_ocupado
	global ultimo_ocupado
	combinaciones = [0 for x in range(4)]
	if n%2 == 0:
			combinaciones[solo] = ccc_aux(n)
			combinaciones[primero_ocupado+ultimo_ocupado] = ccc_aux(n - 2)
	elif n%2 == 1:
			combinaciones[primero_ocupado] = ccc_aux(n - 1)
			combinaciones[ultimo_ocupado] = combinaciones[primero_ocupado]
	return combinaciones

def contar_combinaciones_coleccion(n):
	global solo
	global primer_ocupado
	global segundo_ocupado
	global ultimo_ocupado
	global anteultimo_ocupado
	combinaciones = [0 for x in range(16)]
	if n%2 == 0:
			combinaciones[solo] = ccc_aux(n)
			
			answer_2 = ccc_aux(n - 2)
			answer_4 = ccc_aux(n - 4)
			combinaciones[primero_ocupado+segundo_ocupado] = answer_2
			combinaciones[primero_ocupado+anteultimo_ocupado] = answer_2
			combinaciones[primero_ocupado+ultimo_ocupado] = answer_2	
			
			
			combinaciones[segundo_ocupado+anteultimo_ocupado] = answer_2
			combinaciones[segundo_ocupado+ultimo_ocupado] = answer_2
			
			combinaciones[anteultimo_ocupado+ultimo_ocupado] = answer_2
			if n > 4:
				combinaciones[primero_ocupado+segundo_ocupado+anteultimo_ocupado+ultimo_ocupado] = answer_4
				
	elif n%2 == 1:
			answer_1 = ccc_aux(n - 1)
			answer_3 = ccc_aux(n - 3)
			combinaciones[primero_ocupado] = answer_1
			combinaciones[segundo_ocupado] = answer_1
			combinaciones[ultimo_ocupado] = answer_1
			combinaciones[anteultimo_ocupado] = answer_1
			if n > 3:
				combinaciones[primero_ocupado+ultimo_ocupado+anteultimo_ocupado] = answer_3
				combinaciones[primero_ocupado+segundo_ocupado+anteultimo_ocupado] = answer_3
				combinaciones[primero_ocupado+segundo_ocupado+ultimo_ocupado] = answer_3
				combinaciones[segundo_ocupado+ultimo_ocupado+anteultimo_ocupado] = answer_3
				
	return combinaciones


#for x in range(0,15,2):
	#print contar_combinaciones_coleccion(x)

print "----"

#for x in range(1,15,2):
	#print contar_combinaciones_coleccion(x)


"""def contar_combinaciones_coleccion(n):
	i1, i2 = contar_combinaciones_coleccion_aux(n)
	return i1 + i2

def contar_combinaciones_coleccion_aux(n):
	assert n%2 == 0
	if n == 0:
		return 0,0
	if n == 2:
		return  1,0
	i1,i2= contar_combinaciones_coleccion_aux(n-2)
	return i1+i2, i1

for x in range(0,15,2):	
	print contar_combinaciones_coleccion(x)	"""



