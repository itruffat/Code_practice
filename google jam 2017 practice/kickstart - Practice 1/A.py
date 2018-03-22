from simpleIO import get_input_generator, to_file

test0 = """"""

input_line = get_input_generator("=INFILE=", test0)
input_line = get_input_generator("A-small-practice.in")

cases_number = int(next(inp))

@to_file
def main_function():
for current_case in range(cases_number):
	print(printable = "Case #{}: {}".format(current_case + 1, )) 
