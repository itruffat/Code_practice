def tokenize_string(stringer):
	print stringer
	stringList = list(stringer)
	pureString = [[]]
	tokens = []
	quantity = []
	i = 0

	for x in range(len(stringList)):
		notJustOpened = True
		notJustClosed = True
		letter = (stringList[x])
		
		if letter == "[":
			if i == 0:
				notJustOpened = False
				number = []
				while(pureString[-1] and unicode(pureString[-1][-1],'utf-8').isnumeric()):
					number.insert(0,pureString[-1].pop(-1))
				number = int(''.join(number))
				quantity.append(number)
				pureString.append([])
				tokens.append([])
			i+=1

		elif letter == "]":
			notJustClosed = False
			i-=1

		if i == 0 and notJustClosed:
			pureString[-1].append(letter)
		elif i != 0 and notJustOpened:
			tokens[-1].append(letter)

	return pureString, tokens, quantity

def processTokensAndText(text,tokens,quantity):
	pstring =  ''.join(text[0])
	for x in range(len(tokens)):
		tkTxt, tkTk, tkQt = tokenize_string(''.join(tokens[x]))
		if(len(tkTxt) > 1):
			tokens[x] = processTokensAndText(tkTxt, tkTk, tkQt)
		pstring += (quantity[x] * ''.join(tokens[x])) + ''.join(text[x + 1])
	return pstring


def processText(text):
	txt, tk, qt = tokenize_string(text)
	#print txt
	#print tk
	#print qt
	return processTokensAndText(txt, tk, qt)

s = "2[3[a]b]"

print processText(s)
