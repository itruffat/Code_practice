class tree_node():
	def __init__(self, value = None, parent = None):
		self.children = []
		self.properties = {}
		self.value = value
		self.parent = parent
		
	def __iter__(self):
		return iter(self.children)
	
	def __next__(self):
		raise Exception("")
	
	@staticmethod
	def create(value = None, *children, parent = None):
		base = tree_node(value = value, parent = parent)
		if len(children):
			for a in children:
				base.children.append(tree_node.create(a[0], *a[1:],parent = base))
		return base

def bfs(node):
	yield node
	pile = [node]
	while pile:
		for c in pile.pop(0):
			yield c
			pile.append(c)

def dfs(node):
	yield node
	pile = [iter(node)]
	while pile:
		try: 
			c = next(pile[-1])
			if len(c.children) > 0:
				pile.append(iter(c))
			yield c
		except StopIteration:
			pile.pop()
		except Exception as e:
			raise e

def binary_insert(tree, element):
	

a = tree_node.create(1
						,[2
							,[3
								,[9
									,[10]
									]
								]
							,[4]
							]
						,[5
							,[6]
							]
						,[7
							]
					)

for x in dfs(a):
	print(x)
	print (x.value)
