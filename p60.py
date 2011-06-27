from eulerlib import sieve

N = 10000
M = 100000000
primes = sieve(N)
prime_set = set(sieve(M))

def concat(a,b):
	return int(str(a)+str(b))

def get_concat_sets(n):
	if n == 0:
		return []
	elif n == 1:
		return [[n] for n in primes]

	concat_sets = []
	prev_sets = get_concat_sets(n-1)
	for s in prev_sets:
		for p1 in primes[primes.index(max(s))+1:]:
			found = True
			for p2 in s:
				if concat(p1,p2) not in prime_set or concat(p2,p1) not in prime_set:
					found = False
					break
			if found:
				concat_sets.append(s + [p1])

	return concat_sets


sets = get_concat_sets(5)
min_set = sets[0]
for s in sets:
	if sum(s) < sum(min_set):
		min_set = s
print sum(min_set)
