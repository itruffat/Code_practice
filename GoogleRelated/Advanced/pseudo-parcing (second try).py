def parse(string):
	stringList = list(string)
	text = [[]]
	quantity = []
	i = 0

	for x in range(len(stringList)):
		letter = stringList[x]
		
		if (unicode(letter,'utf-8').isnumeric()):
			i *= 10
			i += int(letter)
		elif letter == "[":
			text.append([])
			quantity.append(i)
			i = 0
		elif letter == "]":
			text[-1] += text.pop(-1) * (quantity.pop(-1)-1)
		else:
			text[-1].append(letter)	

	text = ''.join(list(map(lambda x: ''.join(x) , text)))
	return text

s = "2[3[a]b]"

print parse(s)
