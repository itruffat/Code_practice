c = -1
i = 0

def m_p(i):
	return i%(10**9 + 7)

def get_inp():
	global c
	global i
	if c==-1:
		return raw_input()
	i +=1
	if i== 1:
		return ""
	if c==0:
		if i == 2:
			return "2 2"
		if i == 3:
			return "1 100000000"
	if c==1:
		if i == 2:
			return "2 1 3"
		if i == 3:
			return "3 2 4"
	if c==2:
		if i == 2:
			return "1 1 1 1 1 1 1 1 1 1 1 1 1"
		if i == 3:
			return "1 1 1 1 1 1 1 1 1 1 1 1 1"
	if c==3:
		if i == 2:
			return "50 100 150"
		if i == 3:
			return "70 80 10"


def sent_out(out):
	global c
	print m_p(out)
	if c>-1:
		print "Expected:"
	if c==0:
		print "0" 
	if c==1:
		print"4"
	if c==2:
		print "227020758"
	if c==3:
		print "NO IDEA"
		
get_inp()

pirata = sorted(list(map(int,get_inp().split())))
lastp = -1

pirata2 = []
for cp in pirata:
	if cp > lastp:
		lastp = cp
		pirata2.append([cp,0])
	pirata2[-1][1]+=1
	
score = [0 for x in range(len(pirata2))]

def busqueda_binaria(lista, searchval):
	first = 0
	last = len(lista)
	return_val = busqueda_binaria_it(lista, searchval, first,last, -1)	
	return return_val
	
def busqueda_binaria_it(lista, searchval, first,last, candidate):
	if(first + 1 == last):
		if lista[first][0] <= searchval:
			candidate = max(candidate, first)
		return candidate
	
	mid = first + (last-first)/2
	if lista[mid][0] == searchval:
		return mid
		if lista[mid][0] > searchval:
		if(first == mid):
			return busqueda_binaria_it(lista, searchval, first, mid+1,candidate)
		return busqueda_binaria_it(lista, searchval, first, mid,candidate) 
	if lista[mid][0] < searchval:
		if(mid + 1 == last):
			return busqueda_binaria_it(lista, searchval, mid, last, mid)
		return busqueda_binaria_it(lista, searchval, mid+1, last, mid)



for t in map(int, get_inp().split()):
	p = busqueda_binaria(pirata2, t)
	if p != -1:
		score[p]+=1
	
	#### FORMA SIN BUSQUEDA binaria
	#p = 0
	#while p < len(pirata2) and pirata2[p][0] <= t:
	#	p+=1
		
	#if p > 0 and p <= len(pirata2):
	#	score[p-1] += 1
	

final_score = 1
ascore = 0

for s in range(len(score) - 1, 0 - 1, -1):
	ascore += score[s]
	for y in range(pirata2[s][1]):
		final_score *= ascore
		ascore -= 1

sent_out(final_score)
