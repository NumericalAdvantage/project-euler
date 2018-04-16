

sumofnums = 0
sumofsquares = 0

for num in range(1, 101):
	print(num)
	sumofnums = sumofnums + num
	sumofsquares = sumofsquares + num**2

print(sumofnums**2, " ", sumofsquares)
print(sumofnums**2 - sumofsquares)