from simpleIO import get_input_generator, to_file

test0 = """3
4
4 8 15 16 23 42
8 6 7 5 30 9
1 2 3 4 55 6
2 10 18 36 54 86
2
1 2 3 4 5 6
60 50 40 30 20 10
3
1 2 3 4 5 6
1 2 3 4 5 6
1 4 2 6 5 3"""

input_line = get_input_generator("=INFILE=", test0)
#input_line = get_input_generator("A-small-practice.in")
#input_line = get_input_generator("A-large-practice.in")

cases_number = int(next(inp))
tdone = 0


def generate_clusters():
	dice = int(next(inp))
	
	#Put dices in Dice space
	dice_space = [ [] for x in range(0,pow(10,6) + 1)]
	while dice > 0:
		for side in list(map(int,next(inp).split())):
				dice_space[side].append(dice)
		dice -= 1
	
	#Trim Dice Space into Clusters
	clusters = []
	current_cluster = []
	for cell in dice_space:
		if cell != []:
			current_cluster.append(cell)
		elif current_cluster != []:
			clusters.append([current_cluster, -1])
			current_cluster = []
	if current_cluster != []:
		print(clusters)
		clusters.append([current_cluster, -1])
	
	#Rename dices in the same cluster			
	for current_cluster in clusters:
		dice_renames = {}
		for cell in current_cluster[0]:
			for element_number in range(len(cell)):
				element = cell[element_number] 
				new_name = dice_renames.get(element)		 
				if new_name is None:
					new_name = len(dice_renames) + 1
					dice_renames[element] = new_name
				cell[element_number] = new_name
		current_cluster[1] = len(dice_renames)
	
	return(clusters)	

def brute_force(cluster, dices):
	full_mask = pow(2,dices+1) - 1
	library = {}	# The library saves the progress done so far
					# It is saved as "Available:dices"
	library[full_mask] = 0
	bfmax = 0
	cluster.append([])
	for cell in cluster:
		itmax, library = cell_call(cell, library, full_mask)
		bfmax = max(bfmax, itmax)
	return bfmax
	
def cell_call(vals, old_library, full_mask):
	masked_vals = [pow(2,v) for v in vals]
	current_mask = sum(masked_vals)
	new_library = {}
	itmax = 0
	
	for key, value in old_library.items():
		matches = key&current_mask
		if matches == 0:
			itmax = max(itmax,value)
		while(matches != 0):
			match = matches
			matches = (matches & (matches-1))
			match -= matches
			
			new_key = match ^ key
			new_value = max(new_library.get(new_key,0),value + 1)
			
			new_library[new_key] = new_value
	new_library[full_mask] = 0
	return [itmax,new_library]

@to_file
for current_case in range(1,cases_number+1):
	cmax = 0	
	clusters_n_dices  = generate_clusters()	
	for cluster, dices in clusters_n_dices:
		cmax = max(cmax, brute_force(cluster, dices)) 
	print(printable = "Case #{}: {}".format(current_case, cmax)) 
