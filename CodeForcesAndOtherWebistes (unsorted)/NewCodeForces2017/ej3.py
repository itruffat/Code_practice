input_lines = """8
1 -1 1 -1 -1 1 1 1"""
recibir = True
i__l = -1

def get_input():
	global i__l
	if not recibir:
		i__l += 1
		return input_lines.splitlines()[i__l]
	return raw_input()
		
get_input()
crime = list(map(int,get_input().split()))
r = 0
c = 0

for x in crime:
	r += x
	if r<0:
		c += (-1 * r) 
		r = 0
	
print c
