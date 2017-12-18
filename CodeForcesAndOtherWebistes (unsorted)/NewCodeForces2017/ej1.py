input_lines = """74 99"""
recibir = True
i__l = -1

def get_input():
	global i__l
	if not recibir:
		i__l += 1
		return input_lines.splitlines()[i__l]
	return raw_input()
	


zero,uno = map(int,get_input().split())

returner = ""

#print uno
#print zero

while(((uno) >= zero) and uno>1 and zero>0):
	returner += "110"
	uno-=2
	zero-=1
	
#print uno
#print zero
	
while(uno>0 and zero>0):
	returner += "10"
	uno-=1
	zero-=1

#print uno
#print zero

if(uno>0):
	returner += "1"
	uno-=1
	
if(uno>0):
	returner += "1"
	uno-=1

if(zero>0):
	returner = "0" + returner	
	zero -= 1

#print uno
#print zero
print returner if uno==0 and zero==0 else "-1"
