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
	for y in range(0 + (n%2),roof(n/2.0), 2):
		if (y==0):
				i += iteraciones_conjunto(n) * 2
		elif(y==1):
				belleza = n - 1
				i += n * (iteraciones_conjunto((n-1)) +  iteraciones_intraconjunto(n)) * belleza * 2
		else:
			for x in range(1, n - y):
				grupo = (n - y- 1)
				resto = y - 1
				i += medir_iterativo(0,grupo,resto)
	return i

	
def medir_iterativo(grupo1,grupo2,resto):
	grupo = grupo1 + grupo2
	
	if grupo1 > 1:
			pass
		
	print str(grupo1) + " " + str(grupo2) + "--" + str(resto)
	return 0
		

def medir_iterativo_aux(grupo1,grupo2,resto):
	return 0


print medir(int(raw_input()))

#print iteraciones_conjunto(2)

#print iteraciones_intraconjunto(3)



#def contarIteraciones(n):
#	if n >0:
#		return contarIteraciones(n - 2) + contarIteraciones(n - 4)
#	elif n == 0:
#		return 1
#	else:
#		return 0

#for x in range(15):
	#print str(x) + ": " + str(contarIteraciones(x))
	#print str(x) + ": " + str(iteraciones_conjunto(x))
	#print str(x) + ": " + str(iteraciones_intraconjunto(x))



