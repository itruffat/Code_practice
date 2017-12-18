n = int(raw_input())
i = 0

new_text = ""

for x in text_in:
	if not x in vowels:
		new_text += "."
		new_text += x
		
#for v in vowels:
#	text_in.replace(v,".")

print new_text

