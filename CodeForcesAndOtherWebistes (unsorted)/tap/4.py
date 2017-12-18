def mainF(n):
    suma = 0
    hayFirstD = False

    firstR_and_lastD_count = 0
    firstR_count = 0
    lastD_count  = 0

    for x in range(n):
        a = (input()).upper()
        i = 0
      
        while i < len(a) and a[i] != 'D' and a[i] != 'R':
            i+=1
        if i != len(a):   
            firstR = (a[i] == 'R')
            lastD  = (a[i] == 'D')
            foundD = lastD
          
            while i < len(a):
                if a[i] == 'D' and not lastD:
                    lastD  = True
                    foundD = lastD
                
                if a[i] == 'R' and lastD:
                    lastD = False
                    suma+= 1  
                i +=1
            
            
            if foundD and not firstR: 
                hayFirstD = True
            
            if firstR and lastD:
                firstR_and_lastD_count += 1
            if firstR:
                firstR_count += 1
            elif lastD:
                lastD_count += 1
                
        i = i+1

    if not hayFirstD:
        hayFirstD = True
        if firstR_count > 0:
            firstR_count -= 1
        elif firstR_and_lastD_count > 0:
            firstR_and_lastD_count -=1
            lastD_count += 1
        else:
            hayFirstD = False
    
    if hayFirstD:
        suma += min(firstR_count, lastD_count)
        resto = abs(firstR_count - lastD_count)        
        
        suma += min(firstR_and_lastD_count , resto)
        resto = (firstR_and_lastD_count - resto)    
        
        if resto>0:
            suma += resto
        
    print(suma)

while True:
    try:
        n = int(input())
        mainF(n)
    except:
        break
