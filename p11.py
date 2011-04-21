grid = [ [int(n) for n in l.strip().split()] for l in open('data/p11.in') ]
D = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

m = 0 
for i in xrange(len(grid)):
	for j in xrange(len(grid[i])):
		for (dx,dy) in D:
			p = 1
			for k in xrange(4):
				x = i+k*dx
				y = j+k*dy
				if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[i]):
					p *= grid[x][y]

			m = max(m, p)

print m



