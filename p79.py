P = [ [int(d) for d in l.strip()] for l in open('data/p79.in') ]
N = [ [n,set(),False] for n in xrange(10) ]
S = set() #set of used values

for p in P:
	d0 = p[0]
	S.add(d0)
	for d in p[1:]:
		S.add(d)
		n = N[d]
		n[1].add(d0)
		d0 = d 

''' topological sort '''

#remove from S, all nodes with incoming edges
for n in N:
	for e in n[1]:
		if e in S: S.remove(e)
L = []

def dfs(n):
	if not n[2]:
		n[2] = True
		for e in n[1]:
			dfs(N[e])
		L.append(n[0])

for i in S:
	dfs(N[i])
	

print ''.join([str(d) for d in L])
