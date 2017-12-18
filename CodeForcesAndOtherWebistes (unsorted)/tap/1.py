def function(a):
  for x in a:
    if x=="i":
      return 'N'
  return 'S'
  

while True:
	try:
		i = input()  
		print(function(i))
	except:
		break