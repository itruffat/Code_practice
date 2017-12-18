a = raw_input()
b = []
i = 0
for x in a:
	if not(x in b):
		b.append(x)
		i = 1 - i  
print "CHAT WITH HER!" if i==0 else "IGNORE HIM!"
