def is_sorted(a):
	if len(a) == 1 :
		return True
	else:
		return a[0]<a[1] and is_sorted(a[1:])

print (is_sorted([1,2,4,3]))