c = 2
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
tesoro = sorted(list(map(int,get_inp().split())))

lastp = -1
pirata2 = []
for cp in pirata:
	if cp > lastp:
		lastp = cp
		pirata2.append([cp,0])
	pirata2[-1][1]+=1

score = [0 for x in range(len(pirata2))]

cp = 0

for ct in tesoro:
	while (cp+1 < len(pirata2)) and (pirata2[cp+1][0] <= ct):
		cp +=1
	if pirata2[cp][0] <=ct:
		score[cp] += 1

final_score = 1
ascore = 0

for s in range(len(score) - 1, 0 - 1, -1):
	ascore += score[s]
	for y in range(pirata2[s][1]):
		final_score *= ascore
		ascore -= 1

sent_out(final_score)
