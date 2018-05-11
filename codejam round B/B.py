import os

filename = __file__[:-3]
__script_dir__ = os.path.realpath(__file__)
__script_path__ = os.path.dirname(__script_dir__) + "\\"

example_test= """2
3 1 2
2 2 1
4 3 1
1 2 1
2 3 1
3 4 1
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
line = file_iter("B-small-attempt1.in")

fobject = None
fobject = open(__script_path__ + filename + 'output.txt', 'w')

T = int(next(line))			
	
for case in range(T):
	N,K,P = map(int,next(line).split())
	answer  = [ 0 for x in range(N)]
	freedom = [ x for x in range(N)]
	for _ in range(K):
		A,B,C = map(int,next(line).split())
		A-= 1
		answer[A]  = C
		freedom[A] = -1
	freedom = [x for x in freedom if x != -1]
	P = '{}0:0{}b{}'.format('{',len(freedom),'}').format(P-1)
	for f in range(len(freedom)):
		answer[freedom[f]] = P[f]
	 
	print( "Case #{}: {}".format(case+1, ''.join(map(str,answer))),file = fobject)
