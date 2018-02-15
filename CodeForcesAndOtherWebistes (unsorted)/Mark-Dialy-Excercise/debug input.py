#If c value is -1 then we are ready for launch
#Otherwise we are running the test case #c
c= 0
i = -1

# Normal get input (use in most cases)
def get_inp():
	return get_real_inp()

# Forced exception get input 
# (use when you need an exeption to tell you when input is over)
#more_input = True
#last_input = ""

#def get_inp():
#	global more_input
#	global last_input
	
#	if i == -1:
#		last_input = get_real_inp()
		
#	input_buffer = last_input	
#	try:
#		last_input = get_real_inp()
#	except:
#		more_input = False	
#	return input_buffer

def get_real_inp():
	global given_false
	global c
	global i
	if c==-1:
		return input()
	i+=1
	if c==0:
		return """5
2 3
1 3 4
1 2 5
2 5
3 4
6
1 2 3 4 5
1 2 5
2 4
1 3 4
1 4 5
3 4 5""".splitlines()[i]

		
def put_out(p,x,last_x):
	global c
	print(p)
	if c>-1:
		print("Expected:")
	if c==0:
		print("""yes
		yes
		no
		yes
		yes
		no""".splitline()[x])

n = int(get_inp())

grafo = [[y for y in list(map(lambda k: int(k) - 1,get_inp().split())) if y > x] for x in range(n - 1)]
get_inp()

cases = get_inp()

for _ in range(cases):
	
		
if(c != -1):
	print("--end of output--")
