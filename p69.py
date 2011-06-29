from eulerlib import sieve, cmpf

N = 1000000
prime_factors = [[],[(1,1)]] + [[] for n in xrange(N-1)]
phi = [0,1] + [-1 for n in xrange(N-1)]
all_primes = sieve(N)
sub_primes = [p for p in all_primes if p <= N/2]

#calculate prime factors
for p in sub_primes:
	n = p
	while n <= N:
		m = n
		s = 0
		while m % p == 0:
			s += 1
			m /= p

		
		prime_factors[n].append((p,s))
		n += p

#calculate Euler Phi function
for p in all_primes:
	n = p
	prev = phi[1]
	while n <= N:
		phi[n] = n - n/p
		prev = n
		n *= p

def euler_phi(n):
	if phi[n] < 0:
		phi[n] = 1
		for f in prime_factors[n]:
			phi[n] *= phi[f[0]**f[1]]
	return phi[n]

ratios = [(n,euler_phi(n)) for n in xrange(1,N+1)]
print reduce(lambda r1, r2: r1 if cmpf(r1,r2) > 0 else r2, ratios)[0]
