def getval(A,r,c,max_r,max_c):
	if r<0 or c<0 or r>=max_r or c>=max_c:
		return 0
	else:
		return A[r][c]

def Check_Next(A,r,c,max_r,max_c,size):
	global cntr
	global max_size
	if r>max_r or c>max_c:
		return
	next_dir = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
	size += 1
	cntr[r][c] = 1
	if size>max_size:
		max_size = size
	for direc in next_dir:
		next_r = r + direc[0]
		next_c = c + direc[1]
		val = getval(A,next_r,next_c,max_r,max_c)
		if val>0 and cntr[next_r][next_c]!=1:
			Check_Next(A,next_r,next_c,max_r,max_c,size)
	cntr[r][c] = 0

def Get_Max_Chain(A,max_r,max_c):
	global max_size
	for i in range(max_r):
		for j in range(max_c):
			if A[i][j]!=0:
				Check_Next(A,i,j,max_r,max_c,0)
	print max_size
A = [[1,1,0,0,0],[0,1,1,0,1],[0,0,0,1,1],[1,0,0,1,1],[0,1,0,1,1]]
max_r = 5
max_c = 5
cntr=max_r*[max_c*[0]]
max_size = 0
Get_Max_Chain(A,max_r,max_c)