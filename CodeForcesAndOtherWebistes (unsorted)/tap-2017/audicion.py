letras = ["DO","DO#", "RE", "RE#","MI","FA", "FA#","SOL","SOL#","LA", "LA#","SI"]
letras_inv = list(reversed(letras))
dic = {}
for x in range(len(letras)):
	dic[letras_inv[x]] = x

num, note = raw_input().split()
num = int(num)

print letras_inv[(dic[note] + num)%len(dic)]
