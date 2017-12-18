prittyAnswer = {True:"Yes", False:"No"}

n = int(raw_input())
numbers = list(map(lambda x: int(x),raw_input().split()))
print prittyAnswer[n%2 == 1 and numbers[0]%2 == 1 and numbers[n-1]%2 == 1]
