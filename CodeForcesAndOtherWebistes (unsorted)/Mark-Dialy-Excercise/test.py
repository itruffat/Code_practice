testN = -1
testCases = []
testResults = []

testCases.append("""1
1 1
1""") 

testCases.append("""---
...
11111
ññññ
123131""")


moreInput = True

def getinput(infinite = False):
	global testN
	global testCases
	global moreInput
	value = input()
	if value != "$test":
		while True:
			yield value
			try:
				value = input()
			except:
				moreInput = False
				if infinite:
					value = "0"
				else:
					break
				
	else:
		testN = int(input("Eliga un test del 0 al "+str(len(testCases)-1) + ": "))
		testStringLines = testCases[testN].splitlines() 
		call = 0
		while call < len(testStringLines):
			yield testStringLines[call]
			call +=1
		moreInput = False	
		if infinite:
			while True:
				yield "0"

def printRes(result, number):
	global testN
	global testResults
	if testN == -1:
		print(result)
		#print("Case " + str(number+1) + ":" + str(result))
	else:
		print("Result ("+str(number)+"):")
		print(result)
		testresult = testResults[testN].splitlines[number]
		if(testresult != result):
			print("Expected:")
			print(testresult)
		

inp = getinput()

for x in inp:
	print(x)
