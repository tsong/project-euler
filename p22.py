def score_word(word):
	return sum( [ord(c) - ord('a') + 1 for c in word] )


names = [ w.strip('" ').lower() for \
		w in open('data/p22.in').readline().split(',')]
names.sort()

print sum( [(i+1)*score_word(names[i]) for i in xrange(len(names))] ) 
