N = 10000
F = [lambda n: n*(n+1)/2, lambda n: n*n, lambda n: n*(3*n-1)/2,
	lambda n: n*(2*n-1), lambda n: n*(5*n-3)/2, lambda n: n*(3*n-2)]

figurate_numbers = [[f(n) for n in xrange(N) if f(n) < 10000 and f(n) > 999]\
					for f in F]


def get_cyclic_sets(n):
	if n == 0:
		return []
	if n == 1:
		return [ [(n,i)] for i in xrange(len(figurate_numbers)) \
						for n in figurate_numbers[i] ]

	curr_sets = []
	prev_sets = get_cyclic_sets(n-1)

	total = set(range(len(figurate_numbers)))
	for prev_set in prev_sets:
		unused = total.difference(set([t[1] for t in prev_set]))
		for i in unused:
			for n in figurate_numbers[i]:
				d = str(n)
				assert(len(d) == 4)
				if d[:2] == str(prev_set[-1][0])[2:]:
					curr_sets.append(prev_set + [(n,i)])
				if d[2:] == str(prev_set[0][0])[:2]:
					curr_sets.append([(n,i)] + prev_set)
	return curr_sets

sets = [ [t[0] for t in s] for s in get_cyclic_sets(6)]
cyclic = [l for l in sets if str(l[-1])[2:] == str(l[0])[:2]]
assert(len( [l for l in cyclic if set(l) != set(cyclic[0])] ) == 0)
print sum(cyclic[0])
