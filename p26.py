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


print reduce( lambda x, y: x if x[1] > y[1] else y,\
			[(n,cycle(n)) for n in range(1,1000)] )[0]

