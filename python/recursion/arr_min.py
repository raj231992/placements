def find_min(A):
	if len(A)==1:
		return A[0]
	min = find_min(A[0:len(A)-1]) if find_min(A[0:len(A)-1]) < A[len(A)-1] else A[len(A)-1]
	return min

A=[2,4,1,5,3,6,8,9,7]
print(find_min(A))