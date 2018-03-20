from itertools import count

def numDigits(inputNum):
	for placeValue in count(1):
		inputNum = inputNum/10
		if inputNum < 1:
			return placeValue

def isPalindrome(pNum):
	
	nDigits = numDigits(pNum)
	digits = []
	
	for num in range(1, nDigits + 1):
		digits.append(int((pNum%10**num)/10**(num -1)))

	for i in range(0, len(digits)):
		if digits[i] != digits[(len(digits) -1) - i]:
			return False

	return True

def bruteForceThruCombinations():
	allPalindromes = [] 

	for LHS in count(999, -1):
		if LHS < 100:
			break

		for RHS in count(999, -1):
			if RHS < 100 :
				break
			product = LHS*RHS
			if(isPalindrome(product)):
				allPalindromes.append(product)

	return allPalindromes			

allPalindromes = bruteForceThruCombinations()

print(max(allPalindromes))

	