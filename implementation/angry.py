T = input()
arr = []
for i in range(T):
	N = map(int, raw_input().split())
	limit = N[1]
	arrivals = map(int, raw_input().split())
	count = 0
	for j in arrivals:
		if j <= 0:
			count += 1

	if count >= limit:
		arr.append('No')

	else:
		arr.append('Yes')

for k in arr:
	print k
