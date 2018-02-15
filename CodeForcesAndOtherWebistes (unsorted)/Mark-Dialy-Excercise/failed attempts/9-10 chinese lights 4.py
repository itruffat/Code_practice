from bisect import insort

# 1 1 true
# 0 1 false
# 1 0 false
# 0 0 true

#If c value is -1 then we are ready for launch
#Otherwise we are running the test case #c
c = 1
i = -1
		

def get_inp():
	global c
	global i
	if c==-1:
		return input()
	i+=1
	if c==0:
		return """2
2 2
0 1
1 0
3 2
1 0 1
1 1 0""".splitlines()[i]
	if c==1:
		return """1
5 5
1 1 1 1 0
1 0 0 0 0
0 0 1 0 0
0 0 0 0 1
0 0 0 0 0""".splitlines()[i]
		
def put_out(p,x,last_x):
	global c
	print("Case "+str(x+1) + ": " + p)
	if c>-1:
		print("Expected:")
	if c==0:
		print("""Case 1: 2
Case 2: IMPOSSIBLE""".splitlines()[x])
	if c==1:
		print("""Case 1: 2""")
	if x < last_x -1:
		pass

def ultimo(i):
	return ((i|~i)+1)>>1

def bin2(i):
	return bin(i)[2:]

ka = 50
print(bin2(ka))
print(bin2(ultimo(ka)))
print(ultimo(ka))
print(bin(not(50)))

cases= int(get_inp())

for current_case in range(cases):
	
	n, m = (map(int, get_inp().split()))
	
	target_switches = (2**n)-1
	
	founds_values = [-1 for _ in range(target_switches+1)]
	
	switches = [-1 for x in range(m)]	
		
	for x in range(m):
		pos = 0
		bit_switch = 0
		for switch in map(int,get_inp().split()):
			bit_switch += switch * (2**pos)
			pos +=1
		switches[x] = bit_switch
	
	p= -1
	

		
	put_out((str(p) if p != -1 else "IMPOSSIBLE"), current_case, cases)
		
if(c != -1):
	print("--end of output--")



a = [1,2,3,4,5,6,15]

insort(a,9)
print(a)
