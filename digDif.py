N = input() # defines a NxN matrix
num = 0 # initialize num to 0
digOne = [] # create empty array for the first diagonal
digTwo = [] # create empty array for the second diagonal

for i in range(N):
	row = map(int, raw_input().split()) # ith row of matrix stored
	digOne.append(row[num - N]) # desired integer stored from ith row
	digTwo.append(row[N - num-1]) # desired integer stored from ith row
	num += 1 # update num

sumOne = sum(digOne) # sum first diagonal
sumTwo = sum(digTwo) # sum second diagonal

print abs(sumOne - sumTwo) # print absolute difference
