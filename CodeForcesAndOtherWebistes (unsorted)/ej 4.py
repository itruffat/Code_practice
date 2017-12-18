n = int(raw_input())
cards = list(map(lambda x:int(x),raw_input().split()))

zeros = 0
cincos = 0
for x in cards:
	if x ==5:
		cincos += 1
	else:
		zeros  += 1

if cincos < 3:
	if zeros == 0:
		print -1
	else:
		print 0
else:
	new_text = ""
	for x in range(cincos):
		new_text += "5"
	for x in range(zeros):
		new_text += "0"	
	print new_text
