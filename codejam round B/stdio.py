import os

filename = __file__[:-3]
print(filename)
__script_dir__ = os.path.realpath(__file__)
__script_path__ = os.path.dirname(__script_dir__) + "\\"

example_test= """7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE
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
line = file_iter()

fobject = None
fobject = open(__script_path__ + filename + 'output.txt', 'w')

T = int(next(line))

for x in iter(line):
	print( x,file = fobject)
