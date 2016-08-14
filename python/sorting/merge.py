def sort(a):
	if len(a)<=1:
		return a
	l = len(a)/2 
	a1 = sort(a[0:l])
	a2 = sort(a[l:])
	return merge(a1,a2)

def merge(a,b):
	cura = 0
	curb = 0
	s = []
	while cura<len(a) and curb<len(b):
		if a[cura]<b[curb]:
			s.append(a[cura])
			cura+=1
		else:
			s.append(b[curb])
			curb+=1
	if cura==len(a):
		while curb<len(b):
			s.append(b[curb])
			curb+=1
	else:
		while cura<len(a):
			s.append(a[cura])
			cura+=1
	return s

a = [5,2,4,1,3]
print sort(a)

