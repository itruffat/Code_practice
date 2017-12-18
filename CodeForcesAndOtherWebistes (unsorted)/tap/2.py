def function(a):
  n, e, s = map(int, a.split(""))
  for xy in range(n):
    x,y = map(int, input().split(""))

while True:
	try:
		i = input()  
		print(function(i))
	except:
		break