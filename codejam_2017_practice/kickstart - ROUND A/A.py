from simpleIO import get_input_generator, to_file
from math import ceil

test0 = """4
2 4
3 4
4 4
1000 500"""

input_line = get_input_generator("=INFILE=", test0)
#input_line = get_input_generator("A-small-practice.in")

#@to_file
def main_algorithm():
	cases_number = int(next(input_line))
	for current_case in range(cases_number):
		R,D =  list(map(int,next(input_line).split()))
		B = max(R,D)
		S = min(R,D)
		
		a = 0
		for n in range(1,S):
				sn = S - n
				bn = B - n
				a += sn * bn
		for Y in range(1, B//2 +1): #decide middle y 
			for X in range(0, S-1):	#decide middle x
				X_leftover = (S-X)
				Y_leftover = (B-Y)
				max_space = min(X_leftover//2, Y_leftover ) 
				for Z in range(0, max_space+1):
					a+=0
					if current_case == 0:
						print("{},{}".format(X,Y))
		#	for n in range(1,S):
		#		sn = S - n
		#		bn = b2 - n
		#		a += sn * bn


		
		print(("Case #{}: {}".format(current_case + 1, a)) )

main_algorithm()
