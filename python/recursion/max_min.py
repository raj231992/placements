def max_min(A):
	if len(A)==2:
		min = A[0]
		max = A[1]
		if A[0]>A[1]:
			min , max = max , min
		return max,min
	last = len(A) - 1
	max1 , min1 = max_min(A[0:last-1])
	max2 , min2 = max_min(A[last-1:])
	max , min = 0, 0 
	max = max1 if max1>max2 else max2
	min = min1 if min1<min2 else min2
	return max,min

A = [5,1,2,3,4,6]
print(max_min(A))