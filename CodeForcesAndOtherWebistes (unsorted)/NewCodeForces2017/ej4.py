input_lines = """ViP"""
recibir = True
i__l = -1

def get_input():
	global i__l
	if not recibir:
		i__l += 1
		return input_lines.splitlines()[i__l]
	return raw_input()


def isUpper(c):
	return c == c.upper()

word = get_input()
mayusculas = [1 for x in word if isUpper(x)]

print word.upper() if 2 * len(mayusculas) > len(word) else word.lower()
