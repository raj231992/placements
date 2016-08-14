def gen_list(k):
	res =[]
	for i in range(k):
		res.append(str(i))
	return res

def n_ary(n,k):
	if n==0:
		return []
	elif n==1:
		return gen_list(k)
	else:
		return [digit+string for digit in n_ary(1,k) for string in n_ary(n-1,k)]

print n_ary(4,3)