def mainF(n2):
	print mainF_it(0, n2)


de mainF_it(i, maxis, leftoverR, leftoverD):
    suma = 0
    if i < maxis:
		a = [z for z in (input()).upper() if z=='D' or z=='R']
		a = [a[z] for z in range(len(a))  if (z == 0) or (a[z] != a[z-1]) ]
		if a!= []:
			suma+= len(a)/2 + (-1 if a[0]=='R' and a[-1]=='D' else 0)
			
			if a[0]=='R':
				leftoverR +=1
			if a[1]=='D':
				leftoverD +=1
			suma+= mainF_it(i + 1, maxis, leftoverR, leftoverD)	
    else:
		suma += min(leftoverR, leftoverD)
    return suma      

while True:
    try:
        n = int(input())
        mainF(n)
    except:
        break
