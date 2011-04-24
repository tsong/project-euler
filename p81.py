M = [ [int(n) for n in l] for l in \
		[l.strip().split(',') for l in open('data/p81.in')] ]

INF = 9999999
lookup = {(0,0):M[0][0]}
def minpath(i,j):
	if i < 0 or j < 0:
		return INF

	if (i,j) not in lookup.keys():
		m = min( minpath(i-1,j), minpath(i,j-1) )
		lookup[(i,j)] = m + M[i][j]

	return lookup[(i,j)]

print minpath(79,79)
