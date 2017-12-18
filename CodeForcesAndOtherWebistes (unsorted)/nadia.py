prittyPrint = {True:"YES", False:"NO"}
n = int(raw_input())

for x in range(n):
	line = list(raw_input())
	nadia = list("nadia")
	while line != [] and nadia != []:
		l = line.pop(0)
		if l == nadia[0]:
			nadia.pop(0)
	print prittyPrint[nadia == []]
