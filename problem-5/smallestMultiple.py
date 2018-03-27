from itertools import count 

limit = 20

for num in count (0, limit):
	isEvenlyDivisibleForAll = True
	for divisor in count(limit -1, -1):
		if divisor < 3:
			break

		if num%divisor != 0:
			isEvenlyDivisibleForAll = False
			break

	if isEvenlyDivisibleForAll == True and num > 0:
		print(num, " is evenly divisible by all numbers from 1 to ", limit)
		break