from math import sqrt

#
# Esto me permite calcular las iteraciones concretas de una iteracion
#
def iteraciones_conjunto(n):
	assert n%2 == 0
	if n%2 == 1 or n<=0:
		return 0
 	n/= 2 
	n+=1
	return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
	
#
# Esto me permite calcular las iteraciones concretas de un circulo no conectado
#
def iteraciones_intraconjunto(n):	
	assert n%2 == 1
	n1 = n - 1
	if n > 3:
		n1 -= 2	
	return iteraciones_conjunto(n1)
	

def roof(n):
	summ = int(n)
	if n - int(n) != 0:
		summ += 1
	return summ
	
def medir(n):
	i = 0
	for fence in range(0 + (n%2),roof(n/2.0), 2):
		if (fence==0):
				i += iteraciones_conjunto(n) * 2
		elif(fence==1):
				belleza = n - 1
				i += n * (iteraciones_conjunto((n-1)) +  iteraciones_intraconjunto(n)) * belleza * 2
		else:
			for x in range(2, (n) - (fence - 2)* 2):
				grupo = ((n -1))
				resto = n - x - 1
				repeticion = n
				if grupo == resto:
					repeticion /= 2	
				if n%==0:
					i += repeticion * medir_iterativo(grupo,resto - 0, x - 2, False, False)
					i += repeticion * medir_iterativo(grupo,resto - 2, x - 2,  True,  True)
				else:
					i += repeticion * medir_iterativo(grupo,resto - 1, x - 2,  True, False)
					i += repeticion * medir_iterativo(grupo,resto - 1, x - 2, False,  True)
	return i

	
def medir_iterativo(grupo, resto, fences, skipFirst, skipLast):
	i = 0
	for x in range(grupo+resto+1, n):		
		i += medir_iterativo(grupo, x - resto, fences - 1, False, skipLast)
		print str(grupo1) + " " + str(grupo2) + "--" + str(resto)
	return 0
		


print medir(int(raw_input()))

#print iteraciones_conjunto(2)

#print iteraciones_intraconjunto(3)
