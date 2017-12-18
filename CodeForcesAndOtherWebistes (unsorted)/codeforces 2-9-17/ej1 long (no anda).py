prittyAnswer = {True:"Yes", False:"No"}
n = int(raw_input())
numbers = list(map(lambda x: int(x),raw_input().split()))

dynamicArray = []
dynamicArrayWasDefined = []

for x in range(n):
    dynamicArray.append([False, False])
    dynamicArrayWasDefined.append([False, False])

def searchForGroups(startAt, endsBefore, needsUneven):
        numAt = numbers[startAt]
        if (numAt % 2 == 0) or (numbers[endsBefore - 1] % 2 == 0):
            dynamicArrayWasDefined[startAt][needsUneven] = True
            dynamicArray[startAt][needsUneven] = False
        elif ((needsUneven) and (((endsBefore - 1) - startAt)%2 == 0)):
            dynamicArrayWasDefined[startAt][1] = True
            dynamicArray[startAt][1] = True
        else:
            for x in range(startAt + 1, endsBefore - 1):
                if((startAt - x < 2) or (startAt - x)%2 == 0 ) and ((numAt - numbers[x]) % 2 == 0) and (numbers[x] % 2 == 1):
                    if not dynamicArrayWasDefined[x][int(needsUneven)]:
                        if (numbers[x-1] % 2 == 0):
                            dynamicArrayWasDefined[x][0] = True
                            dynamicArray[x][0] = False
                            dynamicArrayWasDefined[x][1] = True
                            dynamicArray[x][1] = False
                        else:
                            searchForGroups(x, endsBefore, not(needsUneven))

                    resultIsEven =     ((not(needsUneven) or numAt == numbers[x])  and dynamicArrayWasDefined[x][1] and dynamicArray[x][1])
                    resultIsUneven = (      (needsUneven)                          and dynamicArrayWasDefined[x][0] and dynamicArray[x][0])


                    if resultIsEven and resultIsUneven:
                        dynamicArray[startAt][0] = True
                        dynamicArrayWasDefined[x][0] = True
                        dynamicArray[startAt][1] = True
                        dynamicArrayWasDefined[startAt][1] = True
                        return True

                    elif resultIsEven:
                        dynamicArray[startAt][0] = True
                        dynamicArrayWasDefined[startAt][0] = True

                    elif resultIsUneven:
                        dynamicArray[startAt][1] = True
                        dynamicArrayWasDefined[startAt][1] = True

        return dynamicArray[startAt][int((needsUneven))]

print prittyAnswer[searchForGroups(0,n, True)]
