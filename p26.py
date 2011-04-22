def cycle(n):
	if n == 1:
		return 0

	visited = []
	div = 1

	while not div in visited:
		visited.append(div)
		div *= 10
		while div < n: 
			div *= 10
			visited.append(div)

		div = div % n 
		if div == 0:
			return 0

	return len(visited[visited.index(div):])


i = -1
m = 1
for n in xrange(1,1000):
	c = cycle(n)
	if c > m:
		i = n
		m = c
print i
