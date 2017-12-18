import sys
c_char = 0
for inp_l in sys.stdin.read():
	if inp_l != '':
		new_inp = ""
		for x in inp_l:
			if x == '"':
				x = ["``", "''"][c_char]
				c_char = 1 - c_char
			new_inp = new_inp + x
		print(new_inp, end="" )
