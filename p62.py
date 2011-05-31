N = 1000000
cubes = [n**3 for n in xrange(N)]
buckets = {}
for n in cubes:
	key = tuple(sorted(str(n)))
	if key not in buckets:
		buckets[key] = []
	buckets[key].append(n)

lenfive = [li for li in buckets.itervalues() if len(li) == 5]

m = min( sum(lenfive, []) )

