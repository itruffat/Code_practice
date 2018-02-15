#If c value is -1 then we are ready for launch
#Otherwise we are running the test case #c
c = -1
i = -1
		

def get_inp():
	global c
	global i
	if c==-1:
		return input()
	i+=1
	if c==0:
		return """2
2 2
0 1
1 0
3 2
1 0 1
1 1 0""".splitlines()[i]

		
def put_out(p,x,last_x):
	global c
	print("Case "+str(x+1) + ": " + p)
	if c>-1:
		print("Expected:")
	if c==0:
		print("""Case 1: 2
Case 2: IMPOSSIBLE""".splitlines()[x])
	if x < last_x -1:
		pass

cases= int(get_inp())

for current_case in range(cases):
	n, m = (map(int, get_inp().split()))
	matriz = [[] for _ in range(n)]
	for x in range(m):
		pos = 0
		for switch in map(int,get_inp().split()):
			matriz[pos].append(switch)
			pos +=1
			
	for x in range(len(matriz)):
		matriz[x].append(1)
	
	
	invalid_cell = [(1 if x == m else 0) for x in range(m+1)]
	finished_cell = [0 for x in range(m+1)]
	
	for x in range(0, len(matriz)):
		if matriz[x][x] == 0:
			for y in range(x+1, len(matriz)):
				if matriz[y][x] == 1:
					t = matriz[x]
					matriz[x] = matriz[y]
					matriz[y] = t
		if matriz[x][x] == 1:
			for y in range(x+1, len(matriz)):
				if matriz[y][x] == 1:
					for z in range(x,len(matriz[0])):
						matriz[y][z] = matriz[y][z] ^ matriz[x][z]
			
	p = 0
	valid = True
	for x in range(len(matriz)):
		if valid:
			if matriz[x] != finished_cell:
				p+=1
			if matriz[x] == invalid_cell:
				p = -1
				valid = False 
	
	put_out((str(p) if p != -1 else "IMPOSSIBLE"), current_case, cases)
		
if(c != -1):
	print("--end of output--")
