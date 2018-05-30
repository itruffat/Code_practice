import os
from math import floor, ceil, log

filename = __file__[:-3]
__script_dir__ = os.path.realpath(__file__)
__script_path__ = os.path.dirname(__script_dir__) + "\\"

example_test= """2
16 26
88 102
"""

def input_iter(finish_flag = True, flag = ""):
    while True:
        i = input()
        if finish_flag and i ==flag:
           break
        yield(i)

def string_iter(string=example_test):
    for i in string.split("\n"):
        yield(i)

def file_iter(filepath = "input.txt"):
    _file = open(__script_path__ + filepath, "r")
    i_buffer = _file.readline()
    for i in _file.readlines():
        yield(i_buffer[:-1])
        i_buffer = i
    _file.close()
    yield(i_buffer)

#line = input_iter()
line = string_iter()
#line = file_iter("A-small-attempt0.in")
#line = file_iter("A-largesmall-attempt0.in")

fobject = None
fobject = open(__script_path__ + filename + 'output.txt', 'w')

T = int(next(line))

for case in range(T):
	F,L = next(line).split()
	first_f = 0	
	F,L = map(int,[F,L]) 
	digits = floor(log(F,10))
	i = [1]
	for x in range(1,digits):
		i.append(10 ** x + i[-1] * 9 )
	print(i)
	#print(pow(10,digits))
	answer = 0
	#   10
	#             1
	#  100
	# 1-100
	# 
	#        10 + 9 = 10 + 9*(1)
	#1.000
	# 100 + 90 + 81 = 100 + 9 * (10 + 9)
	#10.000
	# 1000 +        = 1000 + 9 * 
	print( "Case #{}: {}".format(case+1,answer),file = fobject)
