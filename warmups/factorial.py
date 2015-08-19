def factorial(x): # create the factorial function with parameter x

	if x == 0: # case where x is 0

		return 1 # function returns 1 because 0! = 1



	else: # remaining cases

		return x * factorial(x-1) # calls function until x-1 = 0, returns desired product

N = input() # takes an integer from the user

print factorial(N) # print the desired result
