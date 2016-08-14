def bin_gen(n):
	if n == 0:
		return []
	elif n == 1:
		return ['0','1']
	return [digits+string for digits in bin_gen(1) for string in bin_gen(n-1)]
print bin_gen(4)