def kruskals(N, E):
	E = sort(E)
	C = [[u] for u in N]
	T = []
	n = len(N)
	for e in E:
		u = e[1]
		v = e[2]
		ucomp = find(u, C)
		vcomp = find(v, C)
		print ucomp, vcomp
		print ucomp[0], vcomp[0]
		if(ucomp != vcomp):
			C = merge(ucomp[0], vcomp[0], C)
			T.append((u,v))
			if(len(T) == (n-1)):
				break
	print T
	return T

def sort(A):
	for j in range(1,len(A)):
		t = A[j]
		i = j - 1
		while(i >= 0 and A[i] > t):
			A[i + 1] = A[i]
			i = i - 1
		A[i + 1] = t
	return A

def find(u, C):
	j = 0
	for c in C:
		if u in c:
			return (c, j)
		j += 1

def merge(ucomp, vcomp, C):
	comp = [ucomp + vcomp]
	newer = []
	for item in comp:
		for c in C:
			if(c[0] not in item):
				newer.append(c)
	newer = comp + newer
	newer[0].sort()
	return newer

#Simple Test
NSimp = ['A','B','C']
ESimp = [[5, 'A', 'B'], [4, 'B', 'C'], [3, 'A', 'C']]
kruskals(NSimp,ESimp)

#Complex Test
N = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
E = [[2, 'A', 'B'], [5, 'A', 'C'], [8, 'A', 'D'], \
	 [1, 'A', 'G'], [5, 'A', 'H'], [3, 'B', 'C'], \
	 [2, 'B', 'F'], [4, 'B', 'G'], [6, 'C', 'D'], \
	 [6, 'C', 'E'], [1, 'C', 'H'], [1, 'D', 'E'], \
	 [1, 'D', 'F'], [2, 'E', 'F'], [3, 'F', 'G'], \
	 [6, 'G', 'H']]
kruskals(N, E)