n = int(input())
a = 1
while n != 0:
	vals = list(map(int, input().split(" ")))
	i= sum(vals)/n
	r = int(sum([x-i for x in vals if x > i]))
	#print("Set #" + str(a))
	#print("The minimum number of moves is " + str(r) + ".")
	print ("""Set #%i
	The minimum number of moves is %i.
	"""%format(a,r), end + "")
	a+=1
	n = int(input())
