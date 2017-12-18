def mainF(n):
	
    suma = 0
    
    hayDobleMayorA2 = False
    hayFirstD = False
    hayLastR  = False

    firstR_and_lastD_count = 0
    firstR_count = 0
    lastD_count  = 0
	singleD_count = 0
	singleR_count = 0

    for x in range(n):
        a = [z for z in (input()).upper() if z=='D' or z=='R']
        a = [a[z] for z in range(len(a))  if (z == 0) or (a[z] != a[z-1]) ]
        
        if a!= "":
			firstR = a[ 0]=='R'
			hayFirstD = hayFirstD or not firstR
	
			lastD  = a[-1]=='D'
			hayLastR  = hayLastR  or not lastD
			
			if(len(a) == 1):
					singleD_count += 1 if lastD else 0
					singleR_count += 1 if firstR else 0
							
			suma  += int(len(a)/2) - (1 if (firstR and lastD) else 0)
			 
			if firstR and lastD:
				firstR_and_lastD_count += 1
				hayDobleMayorA2 = hayDobleMayorA2 or (len(a) > 2)
			elif         firstR:
				firstR_count           += 1
			elif          lastD:
				lastD_count            += 1  
			
    if not hayFirstD:
		if (firstR_count > 0) and (firstR_count > singleR_count):
			firstR_count  -= 1
			hayFirstD = True
		elif firstR_and_lastD_count > 0:
			firstR_and_lastD_count -= 1
			lastD_count   += 1
			singleD_count += 1 if not hayDobleMayorA2 else 0
			hayFirstD = True
	
	if not hayLastR:
		if (lastD_count > 0) and (lastD_count > singleD_count):
			lastD_count  -= 1
			hayLastR = True
		elif firstR_and_lastD_count > 0:
			firstR_and_lastD_count -= 1
			firstR_count += 1
			hayLast = True
	
	combinaciones_r_d = min(lastD_count, firstR_count) 
	resto_combinaciones_r_d = abs(lastD_count - firstR_count)
	combinaciones_dobles = min(firstR_and_lastD_count, resto_combinaciones_r_d)
	resto_combinaciones_dobles = abs(firstR_and_lastD_count - resto_combinaciones_r_d)
	
	suma += combinaciones_r_d
	suma += combinaciones_dobles
	suma += resto_combinaciones_dobles if ((firstR_and_lastD_count - combinaciones_dobles) > 0) else 0 
	
	if not hayFirstD or not hayLastR:
		print(0)
	else:
		print(suma)


while True:
    try:
        n = int(input())
        mainF(n)
    except:
        break
