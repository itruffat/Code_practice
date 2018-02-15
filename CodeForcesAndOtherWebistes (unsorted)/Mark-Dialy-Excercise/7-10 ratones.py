#If c value is -1 then we are ready for launch
#Otherwise we are running the test case #c
c= -1
i = -1

def get_inp():
	global c
	global i
	if c==-1:
		return input()
	i+=1
	if c==0:
		return """1
		
		4
		2
		1
		8
		1 2 1
		1 3 1
		2 1 1
		2 4 1
		3 1 1
		3 4 1
		4 2 1
		4 3 1""".splitlines()[i]
	if c == 1:
		return """2
		
		4
		2
		0
		8
		1 2 1
		1 3 1
		2 1 1
		2 4 1
		3 1 1
		3 4 1
		4 2 1
		4 3 1
		
		4
		1
		6
		3
		2 1 2
		3 2 2
		4 3 2""".splitlines()[i]
		
def put_out(p,x,last_x):
	global c
	print(p)
	if c>-1:
		print("Expected:")
	if c==0:
		print(3)
	if c==1:
		if x==0:
			print(1)
		if x==1:
			print(4)
	if x < last_x -1:
		print("")

#These functions take -1 as infinity
def smaller(x,y):
	if x==-1:
		return False
	if y == -1:
		return True
	return x < y

def smaller_equal(x,y):
	return x == y or smaller(x,y)

def min2(x,y):
	if smaller(x,y):
		return x
	return y


repeticiones = int(get_inp())

for rep in range(repeticiones):
	get_inp()
	n = int(get_inp())
	e = int(get_inp()) - 1
	t = int(get_inp())
	m = int(get_inp())
	
	grafo = [[] for x in range(n)]
	distancias = [(-1 if x!=e else 0) for x in range(n)]
	no_visitados =  [x for x in range(n)]
	
	#We create a graph, but with the nodes pointing the other way around
	for x in range(m):
		source, destiny, value = map(int,get_inp().split())
		grafo[destiny - 1].append([source - 1, value])		
		
	#This is pretty much dijkstra, without taking into consideration the "previous node" slot.
	while no_visitados != []:
		c_mark = -1
		c_dist = -1
		# Select the "non-visited" node with the smallest distance
		for x in range(len(no_visitados)):
			node_x = no_visitados[x]
			dist_x = distancias[node_x]
			if smaller(dist_x, c_dist):
				c_mark = x
				c_dist = dist_x
		#if all nodes are unreachable, end algorithm
		if c_mark == -1:
			no_visitados = []
		else:
			c_node = no_visitados[c_mark]	
			no_visitados.pop(c_mark)
			for apunta in grafo[c_node]:
				x_nodo = apunta[0]
				x_dist = apunta[1]
				distancias[x_nodo] = min2(distancias[x_nodo], c_dist+x_dist) 
	put_out(sum([1 for x in range(n) if smaller_equal(distancias[x], t)]),rep, repeticiones)


if(c != -1):
	print("--end of output--")
