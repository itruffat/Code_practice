import re
import sys
import os
import os.path as path
import pyperclip

def main():
	if len(sys.argv) >= 3:
		output,pyfile, pydir = sys.argv[1:3+1]
	else:
		pyfile,pydir = [__file__, ""]

	string_file = get_string(pyfile, pydir) 

	if output == "0":
		print(string_file)
	elif output == "1":
		pyperclip.copy(string_file)
	elif output == "2":
		output_dir = path.join(pydir, "_RFEFL_" + pyfile)
		with open(output_dir,"w") as output_file:
			output_file.write(string_file)

	
def get_string(file_name, file_path):
	with open(file_name, "r") as open_file:	
		string_file = str(open_file.read())

	re.MULTILINE = True
	execreg = re.compile("exec\(open\((?P<fileresult>(\"[^\"]*\")|(\'[^\']*\'))\)\.read\(\)\)")
	

	for result in execreg.finditer(string_file):
		file_name = path.join(file_path,result.group("fileresult")[1:-1])
		with open( file_name, "r") as open_file:
			string_file = string_file.replace(result[0], open_file.read())
	return string_file		

if __name__ == "__main__":
	main()
