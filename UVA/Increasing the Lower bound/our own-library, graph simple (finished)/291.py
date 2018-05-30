# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=132&page=show_problem&problem=227

# This is an incredibly weird excercise that requires you to brute force your way into an Eulerian Path

class node():
	def __init__(self,n):
		self.number = n
		self.edges = []

class edge():
	def __init__(self, node_tree, nodes):
		self.nodes = nodes
		self.visited = False
		node_tree[nodes[0]].edges.append(self)
		node_tree[nodes[1]].edges.append(self)
	

tree = [node(n + 1) for n in range(5)]
configuration = [[0,1],[0,2],[0,4],[1,2],[1,4],[2,3],[2,4],[3,4]]
		
for e in  configuration:
	edge(tree, e)


def iterative_call(node_tree, tree_configuration, legacy = [0]):
	
	cnode = legacy[-1]
	
	for e in node_tree[cnode].edges:
		if not e.visited:
			e.visited = True
			direction = 1 if e.nodes[0] == cnode else 0
			legacy.append(e.nodes[direction])
			iterative_call(node_tree, tree_configuration, legacy)
			e.visited = False
			legacy.pop()
	
	if len(legacy) == len(tree_configuration) + 1:
		print("".join(map(lambda x: str(x + 1),legacy)))

iterative_call(tree, configuration)
