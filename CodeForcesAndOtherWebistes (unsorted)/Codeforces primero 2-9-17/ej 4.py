t,c = (map(lambda x: int(x),raw_input().split()))
numbers = list(map(lambda x: int(x),raw_input().split()))
n = t * 2 + 1
input_points = []

for x in range(n):
    input_points.append(numbers[x])


def esTopeDistante(array, x):
	return array[x] > (max(array[x-1],array[x+1]) + 1)

potential = []
while(c>0):
	for x in range(1,n,2):
		if esTopeDistante(input_points, x):
			potential.append(x)
	while(c>0 and potential != []):
		p = potential.pop()
		c-= 1
		input_points[p]-=1

print (str(input_points)[1:-1]).replace(",","")
