#If c value is -1 then we are ready for launch
#Otherwise we are running the test case #c
c = -1
i = -1
		

def get_inp():
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
	if c==1:
		return"""1

1
1""".splitlines()[i]

		
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
no""".splitlines()[x])
	if c==1:
		print("""yes""")
	if x < last_x -1:
		pass
		#print("")

###
### PROGRAM STARTS
###

n = int(get_inp())
#We use a bitmap mask because it's very cheap to update
#and we know the number of cases to be something python 
#can effortlessly handle (40 cases max)
target_geode_nodes = (2**n)-1

#grafo = [list(map(lambda k: int(k) - 1,get_inp().split())) for x in range(n )]
grafo = []
for _ in range(n):
	grafo.append(list(map(lambda k: int(k) - 1,get_inp().split())))

cases= int(get_inp())

for current_case in range(cases):
	inputs = list(map(lambda k: int(k) - 1,get_inp().split()))
	is_input = [False for x in range(n)]
	for x in inputs:
		is_input[x] = True
		
	nodes_in_geodes = 0
	
	#For each element in the query subset we do a BFS.
	#This guarantees that we will first find each node at its shortest distance.
	for c_n in inputs:
		geodes = [2**x for x in range(n)]
		depth = [0 for x in range(n)]
		
		depth[c_n] = 1
		current_depth = 2
		pile_1 = [c_n]
		
		while pile_1 != []:
			
			pile_2 = []
			while pile_1 != []:
				p1_e = pile_1.pop()	
				#If we have arrived at some of the vectors in the input V
				#then we check all of the nodes we could have passed through to get
				#here and add them to the  final list
				if is_input[p1_e]:
					nodes_in_geodes = nodes_in_geodes|geodes[p1_e]
			
				
				for x in grafo[p1_e]:
					#If the vector has never been visited
					if depth[x] == 0:
						depth[x] = current_depth
						pile_2.append(x)
					
					#If the vector has been visited IN THIS DEPTH
					#(otherwise nothing would guarantee it's at its smallest distance)	
					if depth[x] == current_depth:
						geodes[x] = geodes[x]|geodes[p1_e]
				
							
			pile_1 = pile_2
			current_depth +=1
	
	put_out("yes" if nodes_in_geodes == target_geode_nodes else "no", current_case, cases)
		
if(c != -1):
	print("--end of output--")
