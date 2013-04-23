class InsertionSort():
	def sort(self, A):
		for j in range(1,len(A)):
			t = A[j]
			i = j - 1
			while(i >= 0 and A[i] > t):
				A[i + 1] = A[i]
				i = i - 1
			A[i + 1] = t
		print A
		return A

attempt = InsertionSort()
testArray = [12,1,4,23,7,0,12]
attempt.sort(testArray)