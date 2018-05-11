filename = __file__[:-3]
__script_dir__ = os.path.realpath(__file__)
__script_path__ = os.path.dirname(__script_dir__) + os.sep

def input_iter(has_finish_flag = False, flag = ""):
	while True:
		try: # Instead of using a conditional, we use a try/except to catch other exceptions
			 # created by input finishing.
			i = input()
			assert(not(has_finish_flag and i==flag))
		except:
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
