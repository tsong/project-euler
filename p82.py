f = open('data/p82.in')
M = [ [int(t) for t in l.strip().split(',')] for l in f]
N = len(M)

INF = 99999999
lookup = {}
def minpath(cell, prev):
	(i,j) = cell

	if i < 0 or j < 0 or i >= N or j >= N:
		return INF
	elif j == N-1:
		return M[i][j] 

	index = (i,j,prev[0],prev[1])
	if index not in lookup:
		D =	[d for d in [(i,j+1),(i-1,j),(i+1,j)] if d != prev]
		lookup[index] = min([M[i][j] + minpath(d,(i,j)) for d in D])

	return lookup[index]

m = min([minpath((i,0), (i,-1)) for i in xrange(N)])
print m
