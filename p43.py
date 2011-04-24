#D = divisors
D = [2,3,5,7,11,13,17]

#T = valid triplets
T = ["%03d" % n for n in xrange(1000) if len("%03d"%n) == len(set("%03d"%n))] 

#N = valid triplets satisfiying each divisibility property
N = [ [n for n in T if int(n,10)%i==0] for i in D ]

#backtrack and stitch together triplets
pandigitals = []
def stitch(curr,N,i):
	#verify pandigital property
	if len(curr) != len(set(curr)):
		return

	#add to results if all triplets have bene stitched
	if i >= len(N):
		pandigitals.append(int(curr))
		return

	#try to stitch all potentially valid triplets
	triplets = N[i]
	for t in triplets:
		if curr[len(curr)-2] == t[0] and curr[len(curr)-1] == t[1]:
			stitch(curr + t[2], N, i+1)

#backtrack begginning at each valid initial triplet
for t in N[0]: 
	stitch(str(t), N, 1)

#add first digit to each pandigital
#first digit is remaining unused digit in the pandigital 
P = []
for p in pandigitals:
	remaining = set(str('1234567890')).difference(set(str(p)))
	P.append(int(remaining.pop() + str(p)))
print sum(P)
