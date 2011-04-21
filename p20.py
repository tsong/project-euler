fact = 1
for n in range(1,101):
	fact *= n

s = str(fact)
print sum( [int(d) for d in s] )
