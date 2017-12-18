import math

primos = [2,3]
answer = ['no', 'yes']

def _primo(numero):
	while len(primos) <= numero:
		x = primos[-1]
		notDivisible = False
		while not notDivisible:
			x += 2
			i2 = 1
			i2_limit = math.sqrt(x)
			notDivisible = True
			while(notDivisible and i2 < len(primos) and primos[i2] <= i2_limit):
				if (x%primos[i2] ==0):
				  notDivisible = False 
				i2 += 1 	
		primos.append(x)
	return primos[numero]

n = int(input())

while n != 0:
	i = 1
	p = 0
	primo = _primo(p)
	n_limit = math.sqrt(n)
	
	while(n >= primo and (n_limit >= primo)):
		p += 1
		if(n%primo == 0):
		  i_loop = 2
		  n/= primo
		  while n%primo == 0:
		  	i_loop += 1
		  	n/=primo 	

		  i*= i_loop
		  n_limit = math.sqrt(n)
		  if n == 1:
		    p = 0
		primo = _primo(p)
	
	if(n > 1):
		i *= 2
	
	print (answer[i%2], end = "")
	n = int(input())
