T = input() # number of test cases
x = [] # create empty array for sums
num = 0 # initialize num to 0
for i in range(T):
	t = map(int, raw_input().split()) # create array fo integers given to sum
	num += sum(t) # update num
	x.append(num) # store sum in x array
	num = 0
for i in range(len(x)):
	print x[i] # print respective sums
