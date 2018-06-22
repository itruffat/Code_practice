import os
from math import floor, ceil, log

filename = __file__[:-3]
__script_dir__ = os.path.realpath(__file__)
__script_path__ = os.path.dirname(__script_dir__) + "\\"

example_test= """3
4 1 1 4 1 1 4 2 4 5
6 3 1 1 0 1 0 1 0 9
3 7 24 34 11 17 31 15 40 50
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
line = file_iter("C-small-attempt0.in")

fobject = None
fobject = open(__script_path__ + filename + 'output.txt', 'w')

T = int(next(line))

for case in range(T):
	N, V, H, A, B, C, D, E, F, M = map(int,next(line).split())
	Bars = [(V,H)]
	for _ in range(1,N):
		V = ((A * Bars[-1][0] + B * Bars[-1][1] + C)%M)
		H = ((D * Bars[-1][0] + E * Bars[-1][1] + F)%M)
		Bars.append((V,H))
	answer = 0	
	for x in range(len(Bars) - 2):
		b1 = Bars[x]
		for y in range(x+1,len(Bars) - 1):
			b2 = Bars[y]
			if(b1[0] == b2[0] or b1[1] == b2[1]):
				answer += len(Bars) - y - 1
			else:
				
				direction_h = (b1[0] - b2[0]) / abs(b1[0] - b2[0])
				direction_v = (b1[1] - b2[1]) / abs(b1[1] - b2[1])
				
				for z in range(y+1, len(Bars)): 
					b3 = Bars[z]
					if b1[0] == b3[0] or b1[1] == b3[1]:
						answer +=1
					else:
						direction_h3 = (b1[0] - b3[0]) / abs(b1[0] - b3[0])
						direction_v3 = (b1[1] - b3[1]) / abs(b1[1] - b3[1])
						if direction_h3 == direction_h or direction_v3 == direction_v: 	
							answer +=1
					
	print( "Case #{}: {}".format(case+1,answer),file = fobject)
