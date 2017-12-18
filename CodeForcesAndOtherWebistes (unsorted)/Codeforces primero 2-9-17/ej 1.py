n,h = (map(lambda x: int(x),raw_input().split()))
numbers = list(map(lambda x: int(x),raw_input().split()))
input_points = []


width = n
for x in range(n):
	if (numbers[x] > (h)):
		width += 1

print width
