from simpleIO import get_input_generator, to_file
import sys

sys.setrecursionlimit(5000)

test0 = """3
****
It
Shakes*e
S*speare
Shakes*e
*peare"""

input_line = get_input_generator("=INFILE=", test0)
input_line = get_input_generator("B-small-practice.in")
input_line = get_input_generator("B-large-practice.in")

array = []
books = [[],[]]
def dynamic(book1, book2, p1, p2, skip1allowed, skip2allowed):
	global array
	global books
	if array[p1][p2] == -1:
		if(len(book1) == p1 or len(book2) == p2):
			only_wild_cards = (set(book1[p1:]+book2[p2:]+["*"]) == set("*"))
			array[p1][p2] = only_wild_cards
			
		elif book1[p1] != "*" and book2[p2] != "*":
			the_same = (book1[p1] == book2[p2])
			array[p1][p2] = the_same and dynamic(book1, book2, p1+1, p2+1, True, True)
		else:
			used_first, used_second, used_both = [False, False, False]
			if book1[p1] == "*":
				used_first  = dynamic(book1, book2, p1+1, p2  , True, True) 
			if book2[p2] == "*" and not used_first:
				used_second = dynamic(book1, book2, p1  , p2+1, True, True)
			if not used_first and not used_second:
				used_both   = dynamic(book1, book2, p1+1, p2+1, book1[p1] != "*", book2[p2] != "*")
			array[p1][p2] = used_first or used_second or used_both		
	return(array[p1][p2])
			

#@to_file
def main_algorithm():
	global array
	global books
	cases_number = int(next(input_line))
	for current_case in range(cases_number):
		books = [[],[]]
		for x in range(2): 
			for l in list(next(input_line)):
				if l == "*":
					books[x]+= ["*"]*3
				books[x].append(l)
		
		array = [[-1 for _ in range(len(books[1])+1)] for _ in range(len(books[0])+1)]
		#for x in range(min(len(books[0]),len(books[1]))-1,0,-1):
		#	dynamic(books[0], books[1], x, x, True, True)

		#t = 0 if len(books[1]) < len(books[0]) else 1
		#d = 0
		#while d!=2:
		#	
		#	if t == 0:
		#		for x in range(len(books[0])-1,len(books[1])-1,-1):
		#			dynamic(books[0], books[1], x, len(books[1])-1, True, True)
		#		d+=1
		#	elif t==1:
		#		for x in range(len(books[0])-1,len(books[1])-1,-1):
		#			dynamic(books[0], books[1], x, len(books[1])-1, True, True)
		#		d+=1
				
		#	t = 1 - t	
		answer = 0
		answer = dynamic(books[0], books[1], 0, 0, True, True)
		print("Case #{}: {}".format(current_case + 1, (str(answer)).upper()) )

main_algorithm()
