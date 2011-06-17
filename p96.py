
def gethoriz(grid,i):
	assert len(grid[i]) == 9
	return set([n for n in grid[i] if n != 0])

def getvert(grid,j):
	assert len(grid) == 9
	vert = set()
	for i in xrange(9):
		if grid[i][j] != 0:
			vert.add(grid[i][j])
	return vert

def getblock(grid,i,j):
	ii = i / 3
	jj = j / 3

	block = set()
	for i in xrange(ii*3, ii*3+3):
		for j in xrange(jj*3, jj*3+3):
			if grid[i][j] != 0:
				block.add(grid[i][j])

	return block




def backtrack(grid, i, j):
	if j >= 9:
		j = 0
		i += 1
	if i >= 9: 
		return True

	if grid[i][j] != 0:
		return backtrack(grid, i, j+1)
	else:
		horiz = gethoriz(grid,i)
		vert = getvert(grid,j)
		block = getblock(grid,i,j)

		for n in xrange(1,10):
			if n not in horiz and n not in vert and n not in block:
				grid[i][j] = n
				if backtrack(grid, i, j+1):
					return True
				grid[i][j] = 0

	return False


			

def solve(grid):
	res = backtrack(grid, 0, 0)	
	assert res == True

f = open('data/p96.in')
lines = f.readlines()
gridLines = [lines[i].strip() for i in xrange(len(lines)) if i % 10 != 0]
grids = [gridLines[i:i+9] for i in xrange(0, len(gridLines), 9)]
grids = [[[int(d) for d in row] for row in grid] for grid in grids]

s = 0
for grid in grids:
	solve(grid)
	s += int(''.join([str(n) for n in grid[0][:3]]))

print s
