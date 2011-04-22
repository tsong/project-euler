import itertools

i = 0
for p in itertools.permutations(range(10)):
	i += 1
	if i == 1000000:
		print ''.join([str(n) for n in p])
		break
