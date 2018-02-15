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
		
get_inp()
pirata = sorted(list(map(int,get_inp().split())))
score = [x for x in range(-1 * len(pirata) + 1, 1)]

lastp = -1
pirata2 = []
for cp in range(len(pirata)):
	if cp < p:
		if cp != -1:
			pirata2.append([cp,i])
		i = 1	
		cp = p
	else:
		pirata2[-1]+=1
		#i+=1

for t in map(int, get_inp().split()):
	p = 0
	while p < len(pirata) and pirata[p] <= t:
		score[p]+=1
		p+=1

final_score = 1
for x in score:
	final_score *= x

sent_out(final_score)
