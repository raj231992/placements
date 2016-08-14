def inversions(a):
	if len(a)<=1:
		return a,0
	l = len(a)/2 
	a1,invs1 = inversions(a[0:l])
	a2,invs2 = inversions(a[l:])
	return merge(a1,a2,invs1+invs2)

def merge(a,b,invs):
	cura = 0
	curb = 0
	s = []
	while cura<len(a) and curb<len(b):
		if a[cura]<b[curb]:
			s.append(a[cura])
			cura+=1
		else:
			s.append(b[curb])
			invs+=len(a[cura:])
			curb+=1
	if cura==len(a):
		while curb<len(b):
			s.append(b[curb])
			curb+=1
	else:
		while cura<len(a):
			s.append(a[cura])
			cura+=1
	return s,invs

a = [5,4,3,2,1]
print inversions(a)