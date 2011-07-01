f = open('data/p83.in')
M = [ [ int(n.strip()) for n in l.split(',')] for l in f]
directions = [(1,0), (-1,0), (0,1), (0,-1)]

INF = 999999
def djikstra(M, start, dst):
	vertices = set([ start ])
	distances = { start : M[start[0]][start[1]] }
	parent = {start : None}

	#get vertices with minimum distance	
	def next_vertex():
		dist = INF
		v = (-1,-1)
		for u in vertices:
			if u in distances and distances[u] < dist:
				v = u
				dist = distances[u]
		return v

	while len(vertices) > 0:
		u = next_vertex()
		assert (u in distances)
		vertices.remove(u)

		for d in directions:
			v = (u[0] + d[0], u[1] + d[1])
			if v[0] >= 0 and v[0] < len(M) and v[1] >= 0 and v[1] < len(M):
				dist = distances[v] if v in distances else INF
				if dist == INF:
					assert(v not in vertices)
					vertices.add(v)
					distances[v] = dist

				#relax
				if distances[u] + M[v[0]][v[1]] < dist:
					distances[v] = distances[u] + M[v[0]][v[1]]
					parent[v] = u

	def path(v):
		if v not in parent:
			return []
		return path(parent[v]) + [v]

	return path(dst), distances[dst]


(path, dist) = djikstra(M, (0,0), (len(M)-1, len(M)-1))
print dist
