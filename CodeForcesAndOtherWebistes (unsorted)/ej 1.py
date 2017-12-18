text_in = (raw_input()).lower()

#vowels = ["A", "O", "Y", "E", "U", "I"]
vowels = ['a', 'o', 'y', 'e', 'u', 'i']
n = len(vowels)

new_text = ""

for x in text_in:
	if x in vowels:
		new_text += "."
	else:
		new_text += x
		
#for v in vowels:
#	text_in.replace(v,".")

print new_text
