def inpt():
	return "99 99 99 99"
	#return "4 4 4 4"
	#return ""
	return raw_input()

l,o,s,t = map(int, inpt().split() )

#Para LS2T
leftovers_ls = (l%2 + s%2)/2

l/=2
o/=2
s/=2
t/=2

smaller = min(l,o)
bigger = max(l,o)
s_usage = min(bigger, s)
bigger -= s_usage
leftovers_lo = (smaller%2) + (bigger%2)

answer= (t/2) + (smaller/2) + (s_usage) + (bigger/2) + (leftovers_lo/2) + (t%2 * leftovers_ls)

print answer
