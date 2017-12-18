def function(a):
	n, m = map(int, a.split(" "))

	puntaje = [1 for x in range(n)]
	allows_list = [[] for x in range(n)]  
	
	for _ in range(m):
		x,y = map(lambda z: int(z) - 1, input().split(" "))
		allows_list[x].append(y)
		puntaje[y] += 1
	
	materias = list(map(lambda z: int(z) - 1, input().split(" ")))
	
	score = 0
	for p in materias:
		score += completar(p, allows_list, puntaje)
		print(score)

def completar(x, allows_list, puntaje):
	c_score = 0
	puntaje[x] -= 1	
	if puntaje[x] == 0:
		c_score += 1
		for y in allows_list[x]:
			c_score += completar(y, allows_list, puntaje)
	return c_score


while True:
	try:
		i = input()
		if len(i) > 2 and " " in i:
			function(i)
		else:
			break
	except:
		break
