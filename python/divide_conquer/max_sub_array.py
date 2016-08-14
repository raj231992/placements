m = []
s = []
def max_s_a(a):
	global m
	global s
	if len(a)==1:
		m = a[0]
 		s = a
		return a,a[0]
	max_a , max_s = max_s_a(a[0:len(a)-1])
	if a[len(a)-1]<(max_s+a[len(a)-1]):
		if m<(max_s+a[len(a)-1]):
			m = (max_s+a[len(a)-1])
			s = a
		return a,max_s+a[len(a)-1]
	else:
		if m<(a[len(a)-1]):
			m = (a[len(a)-1])
			s = a[len(a)-1:]
		return a[len(a)-1:],(a[len(a)-1])
a=[5,-1,3,3,-4]
max_s_a(a)
print s

