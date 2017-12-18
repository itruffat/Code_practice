input_lines = """6 3
1 1 1 0 1 0"""

recibir = True
i__l = -1

def get_input():
	global i__l
	if not recibir:
		i__l += 1
		return input_lines.splitlines()[i__l]
	return raw_input()

def mirror(c,y):
	return 2 * c - y

def inRange(c,y, group):
	return mirror(c,y) >= 0 and  mirror(c,y) < len(group)

c, start = map(int,get_input().split())
start -= 1
criminals = list(map(int,get_input().split()))

found = True

i = criminals[start]

ranges = reversed(range(0,start))
if(start <= c/2):
	ranges = range(start+1, c)
	
for x in ranges:
	if  (criminals[x]) == 1:
		if inRange(start,x,criminals):
			if criminals[mirror(start,x)] == 1:
				i+=2
		else:
			i+=1
	
	 
print i


			
