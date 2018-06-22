import re
import sys
import os

def get_input_generator(input_method, parameters = ""):
	if re.match(".*\.(txt|in)",input_method):
		ofile = open(input_method, 'r')
		line_buffer = ofile.readline()
		for line in ofile:
			yield line_buffer
			line_buffer = line
		ofile.close()
		yield line_buffer
		raise EOFError
	elif re.match("=COMMAND=",input_method):
		while True:
			yield input()
	elif re.match("=INFILE=",input_method):
		if parameters  != "":
			testnumber = 0
			input_text = parameters.split("\n")	
			while True:
				yield input_text[testnumber]
				testnumber+=1
		raise Exception('Infile Input Handler needs an string')
	raise Exception('Incorrect Input Handler')

def to_file(decorated):
	def function_with_fileoutput():
		orig_stdout = sys.stdout
		f = open('out.txt', 'w')
		sys.stdout = f
		decorated()
		sys.stdout = orig_stdout
		f.close()
	return function_with_fileoutput
