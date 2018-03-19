from itertools import count

def numDigits(inputNum):
	for placeValue in count(1):
		inputNum = inputNum/10
		if inputNum < 1:
			return placeValue

print(numDigits(603))	
