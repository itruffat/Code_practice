n = int(raw_input())

for x in range(n):
	words = list(map(lambda x:int(x) - 1,raw_input().split(" "))).inverse()
	
	gotFirst = colors[0] == first
	gotLast =  colors[ballons] == last
	
	
	if gotFirst and gotLast:
		print "BOTH"
	elif gotFirst:
		print "EASY"
	elif gotLast:
		print "HARD"
	else:
		print "OKAY"	
	
	
	
