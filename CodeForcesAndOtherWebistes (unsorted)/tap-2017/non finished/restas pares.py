import math
inpt_c = 0

isZero = -1

def inpt():
	global inpt_c
	if inpt_c == 0:
		inpt_c +=1
		return "3"
	elif inpt_c > 0:
		inpt_c +=1
		return "9 8 1 1"
	return raw_input()

def primer0(i2):
	t = (i2+1)&~(i2)
	return -1 if (t==0) else (int(math.log(t,2)))
	
	
def primer0_segundo0(i2):
	t1 = (i2+1)&~(i2)
	i2t1 = i2+t1
	t2 = (i2t1+1) & ~(i2t1) 
	c = []
	c.append(-1 if (t1==0) else (int(math.log(t1,2))))
	c.append(-1 if (t2==0) else (int(math.log(t2,2))))
	return c
	
def int2map(a):
	return primer0_segundo0(int(a))
	

inpt()
entradas = sorted(list(map(int2map, inpt().split())))
print entradas

rep = 0
x = 0
limit= len(entradas)

while x < limit:
	v =entradas[x][0]
	if v != isZero:
		if limit - x > v:
			rep  += (v + 1)
			limit-= (v)
			entradas[x][0] = entradas[x][1] - entradas[x][0] 
		else:
		
	limit = 0
			
			if entradas[0][0] == isZero:
				rep += (limit - x)
			
			else:
				rep += 5
	x+=1
							
