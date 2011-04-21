triangle = [ [[int(n),-1] for n in l.strip().split()]\
			for l in open('data/p67.in') ]
triangle[0][0][1] = triangle[0][0][0]

for r in xrange(len(triangle)-1):
	for i in xrange(len(triangle[r])):
		curr = triangle[r][i][1]
		adj = triangle[r+1][i][0]
		triangle[r+1][i][1] = max( triangle[r+1][i][1], curr + adj )

		if i+1 <= r+1:
			adj = triangle[r+1][i+1][0]
			triangle[r+1][i+1][1] = max(triangle[r+1][i+1][1], curr+adj)
		
print max([r[1] for r in triangle[len(triangle)-1]])

