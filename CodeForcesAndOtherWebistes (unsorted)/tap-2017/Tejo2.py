import copy
c=2
def get_inp():
	if c==-1:
		return raw_input()
	if c==0:
		return "3 2 2 2"
	if c==1:
		return "3 2 3 3"
	if c==2:
		return "5 12 3 2"
	if c==3:
		return "5 12 5 3"
		
def put_out(i):
	print i
	if c>-1:
		print "Expected:"
	if c==0:
		print 12
	if c==1:
		print 0
	if c==2:
		print 200

n,m,p1,p2 = list(map(int,get_inp().split()))

mem_dim_fila = [-1 for x in range(max(p1,p2))]
mem__dim     = [copy.deepcopy(mem_dim_fila) for x in range(n)]


def factorial(x):
	i = 1
	for n in range(2,x+1):
		i *= n
	return i
	
def binomial(n,k):
	return (factorial(n))/( factorial(k) * factorial(n-k))
	#return (factorial(n) * 1.0)/( factorial(k) * factorial(n-k) * 1.0)

#print binomial(5,2)
#print binomial(3,2)
#print binomial(0,2)

def conseguir_mul(n,m,p):
	global mem__dim
	
	if(n==1):
		i = 1 if (p<=m) else 0
	elif(n>p):
		i = 0
	else:
		i = 0
		limite= min(m + 1, p)
		for next_p in map(lambda x: p - x,range(1, limite)):
			if mem__dim[n-2][next_p-1] == -1:
				conseguir_mul(n-1,m,next_p)
			i += mem__dim[n-2][next_p-1]	
	mem__dim[n-1][p-1] = i

for tmp_n in range(1,n+1):
	conseguir_mul(tmp_n,m,max(p1,p2))	

print mem__dim

sumas = []
s = 0
for tmp_n in range(n):
	s= mem__dim[tmp_n][max(p1,p2)-1]
	sumas.append(s)

print sumas
