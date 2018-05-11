import re
import sys
import os
import os.path as path

##
## Sometimes I need to move files from folder to folder.
## To maintain congruence with this folder, I scan all of them and
## replace them for the current distance

	
def rewrite_file(full_file_path, distance):
	with open(full_file_path, "r") as open_file:	
		old_string_file = str(open_file.read())

	
	execreg = re.compile("exec\(open\((?P<fileresult>(\"[^\"]*\")|(\'[^\']*\'))\)\.read\(\)\)")  
	dotsreg = re.compile("(\.\.\/)*")
	auxreg = re.compile("_auxiliary\/")
	
	execmatch = execreg.search(old_string_file)
	
	if execmatch is not None:
		if auxreg.search(execmatch[0]) is not None:		
			old_file_path = execmatch.group("fileresult")[1:-1]
			
			old_dots = dotsreg.search(old_file_path)[0]		
			new_dots = "../" * distance
			
			new_file_path = old_file_path.replace(old_dots, new_dots)
			new_string_file = old_string_file.replace(old_file_path, new_file_path)
			
			with open(full_file_path + ".bkp", "w") as open_file:	
				open_file.write(old_string_file)
			
			with open(full_file_path, "w") as open_file:	
				open_file.write(new_string_file)
			
			os.remove(full_file_path + ".bkp")
		
def start_full_walk():
	__script_dir__  = path.realpath(__file__)
	cpath = path.join(path.dirname(__script_dir__), "..")
	isfolder = (lambda _path: not path.isfile(path.join(cpath,_path)))
	listdir = (os.listdir(cpath))
	folders = [d for d in listdir if isfolder(d) and d != "_auxiliary" and d!= ".git"]
	folders = ["UVA"]
	for cfolder in folders:
		continue_walk(path.join(cpath,cfolder),1)
		
def continue_walk(cfolder, depth):
	for f in os.listdir(cfolder):
		fpath = path.join(cfolder,f)
		if path.isfile(fpath):
			rewrite_file(fpath,depth)
		else:
			continue_walk(fpath,depth + 1)
	
def main():
	start_full_walk()

if __name__ == "__main__":
	main()
	pass
