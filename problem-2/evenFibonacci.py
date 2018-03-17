fourMillion = 4000000

one = 1
two = 2

latest_fib_term = 0

list_of_fib_terms = list()
list_of_fib_terms.append(1)
list_of_fib_terms.append(2)

sum_of_even_fib_terms = 0

while True:
	if list_of_fib_terms[len(list_of_fib_terms) - 1] > fourMillion:
		for counter in range(0, len(list_of_fib_terms)):
			if(list_of_fib_terms[counter]%2 == 0):
				sum_of_even_fib_terms += list_of_fib_terms[counter]
		print(sum_of_even_fib_terms)		 
		break
	else:
		list_of_fib_terms.append(list_of_fib_terms[len(list_of_fib_terms) - 1] + list_of_fib_terms[len(list_of_fib_terms) - 2])


