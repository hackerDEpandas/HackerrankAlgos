N = input() # height of the staircase as given by user

for i in range(N):
	print ' ' * (N-i-1) + '#' * (i+1) # prints each line of the staircase with N-1 'spaces' that precede i+1 '#'
