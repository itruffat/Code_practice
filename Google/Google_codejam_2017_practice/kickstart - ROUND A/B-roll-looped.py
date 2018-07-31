from simpleIO import get_input_generator, to_file
import sys

sys.setrecursionlimit(5000)

test0 = """3
****
 n
 It
Shakes*e
S*speare
Shakes*e
*peare"""

input_line = get_input_generator("=INFILE=", test0)
#input_line = get_input_generator("B-small-practice.in")
#input_line = get_input_generator("B-large-practice.in")

array = []

books = [[],[]]

def dynamic(p1, p2):
	global array
	global books
	if array[p1][p2] == -1:
		if(len(books[0]) == p1 or len(books[1]) == p2):
			array[p1][p2] = (set(books[0][p1:]+books[1][p2:]+["*"]) == set("*"))
		elif books[0][p1] != "*" and books[1][p2] != "*":
			array[p1][p2] = (books[0][p1] == books[1][p2]) and dynamic(p1+1, p2+1)
		else:
			if books[0][p1] == "*": #First 
				array[p1][p2] = dynamic(p1+1, p2)
			if books[1][p2] == "*" and array[p1][p2] in [False, -1]: #Second
				array[p1][p2] = dynamic(p1  , p2+1)
			if array[p1][p2]  in [False, -1]: #Third:
				array[p1][p2] = dynamic(p1+1, p2+1)
	return array[p1][p2]

def dynamic_loop(p1, p2):
	global array
	global books
	queue = [(p1,p2)]
	backwards = False
	i = 0
	while queue != []:
		p1,p2  = queue[-1]
		
		if array[p1][p2] == -1 or backwards:
			
			if(len(books[0]) == p1 or len(books[1]) == p2): #If we have reached the end of any of the stringss	
				queue.pop(-1)
				array[p1][p2] = (set(books[0][p1:]+books[1][p2:]+["*"]) == set("*"))
				
			elif books[0][p1] != "*" and books[1][p2] != "*": #If none of the current is a wildcard
				if array[p1+1][p2+1] == -1:
					queue.append((p1+1,p2+1))
				else:
					queue.pop(-1)
					array[p1][p2] = (books[0][p1] == books[1][p2]) and array[p1+1][p2+1]
			else:	
				if books[0][p1] == "*": #First 
					if array[p1+1][p2] == -1:
						print("X")
						queue.append((p1+1,p2))
						print(queue)
					else:
						array[p1][p2] = array[p1+1][p2]

				if books[1][p2] == "*" and array[p1+1][p2] == False: #Second
					#print("X")
					if array[p1][p2+1] == -1:
						queue.append((p1,p2+1))
					else:
						array[p1][p2] = array[p1][p2+1]
				
				if array[p1+1][p2] == False and array[p1][p2+1] == False:
					if array[p1+1][p2+1] == -1:
						queue.append((p1+1,p2+1))
					else:
						array[p1][p2] = array[p1+1][p2]
			
				if array[p1][p2] == True or (array[p1+1][p2] == False and array[p1][p2+1] == False and array[p1+1][p2+1] == False):
						#print(array[p1+1][p2] == True or array[p1][p2+1] == True or array[p1+1][p2+1] == True)
						
						#print("x")
						backwards = True
						queue.pop(-1)			
				#if array[p1][p2]  in [False, -1]: #Third:
				#	array[p1][p2] = dynamic(p1+1, p2+1)


#@to_file
def main_algorithm():
	global array
	global books
	cases_number = int(next(input_line))
	for current_case in range(cases_number):
		
		books[0] = []
		books[1] = []
		del array[:]
		
		for book in books: 
			for l in list(next(input_line)):
				if l == "*":
					book+= ["*"]*3
				book.append(l)
				
		for _ in range(len(books[0])+1):
			array.append([-1 for _ in range(len(books[1])+1)])
		if current_case == 0:
			dynamic_loop(0, 0)
		answer = array[0][0]
		print("Case #{}: {}".format(current_case + 1, (str(answer)).upper()) )

main_algorithm()
