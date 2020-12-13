def distance(strand_a, strand_b):
	if len(strand_a) == len(strand_b):
	    return len([1 for a, b in zip(strand_a, strand_b) if  a != b])
	raise ValueError('Unequal strands')
