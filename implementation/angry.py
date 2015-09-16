T = input() # number of test cases
cancel = [] # empty array cancel to later store responses

for i in range(T): # for however many test cases

	N = map(int, raw_input().split()) # store two space-separated integers
	limit = N[1] # store how many students it takes to keep the professor from canceling class
	arrivals = map(int, raw_input().split()) # arrivals of students on time (a_i <= 0) or late (a_i > 0) 
	count = 0 # intialize count to 0
	
	for j in arrivals: # for every studnet arrival
		if j <= 0: # if the student is on time
			count += 1 # count the number of ontime students

	if count >= limit: # case where professor doesn't cancel class 
		cancel.append('NO') # update response to cancel

	else: # case where professor does cancel class
		cancel.append('YES') # update response to cancel

for k in cancel: # for every response in cancel
	print k # prnit each response on a new line without ""
