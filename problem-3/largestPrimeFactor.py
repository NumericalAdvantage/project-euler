import math
from itertools import count

def primeFactors(inputNum):
	factorsList = []
	for divisor in count(2):
		while(inputNum%divisor == 0):
			factorsList.append(divisor)
			inputNum = inputNum/divisor
		if divisor > inputNum:
		    return factorsList

print(primeFactors(600851475143))
