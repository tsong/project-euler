from math import factorial

N = 1000000
chains = {}

def get_distance(n):
	if n not in chains:
		m = sum([factorial(int(d)) for d in str(n)])
		chains[n] = [n]
		if n != m:
			subchain = get_distance(m)
			end = len(subchain)
			for i in xrange(end):
				if subchain[i] == n:
					end = i
					break

			chains[n].extend(subchain[:end])

	return chains[n]

s = 0
for n in xrange(1,N):
	if len(get_distance(n)) == 60:
		s += 1
print s
