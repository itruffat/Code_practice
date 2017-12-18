def function(a):
  n, m = map(int, a.split(" "))
  
  needs_map =  []
  needs_list = []
  puntaje = []
  genero_puntaje_ajeno = []
  allows_list = []
  complete = []
  
  for x in range(n):
    puntaje.append(1)
    genero_puntaje_ajeno.append(False)
    needs_map.append([])
    allows_list.append([])
    needs_list.append([])
    allows_list[x].append(x)
    complete.append(False)
    for y in range(n):
      needs_map[x].append(0)
  
      
  for _ in range(m):
    x,y = map(lambda x: int(x) - 1, input().split(" "))
    needs_map[y][x] = 1
    needs_list[y].append(x)
    allows_list[x].append(y)
    puntaje[y] += 1
    genero_puntaje_ajeno[y] = True

  raices = []
  for x in range(n):
    if puntaje[x] == 1:
      complete[x] = True
    elif not genero_puntaje_ajeno:
      raices.append(x)

  for x in raices:
    completarN(x, complete, needs_list, allows_list, needs_map, puntaje)

  materias = list(map(lambda x: int(x) - 1, input().split(" ")))

  score = 0
  for p in materias:
    for x in allows_list[p]:
      puntaje[x] -= 1
      if puntaje[x] == 0:
        score +=1
    print(score)

def completarN(n, complete_list, needs_list, allows_list, needs_map, puntaje):
  if not complete_list[n]:
    complete_list[n] = True
    for x in needs_list[n]:
      completarN(x, complete_list, needs_list,allows_list, needs_map, puntaje)
      for y in needs_list[x]:
        if needs_map[y][n] == 0:
          needs_map[y][n] = 1
          #needs_list[n].append(y)
          allows_list[y].append(n)
          puntaje[n]+=1

while True:
  try:
    i = input()
    function(i)
  except:
    break
	