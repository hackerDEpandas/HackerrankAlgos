N = input() # gets a size of the array from user
arr = map(int, raw_input().split()) # takes array of numbers from user
length = float(len(arr)) # stores the length of arr as a float

zero = 0.0 # initialize zero to 0.0
pos = 0.0 # initialize pos to 0.0
neg = 0.0 # initialize neg to 0.0

for i in range(len(arr)):
	if arr[i] == 0: 
		zero += 1.0 # counts how many zeros
	elif arr[i] > 0:
		pos += 1.0 # counts how many positives
	else:
		neg += 1.0 # counts how many negatives

fracPos = round((pos/length), 3) # computes positive fraction & rounds
fracNeg = round((neg/length), 3) # computes negative fraction & rounds
fracZero = round((zero/length), 3) # computes zero fraction & rounds

print '%r\n%r\n%r' %(fracPos, fracNeg, fracZero) # displays results each on their own line
