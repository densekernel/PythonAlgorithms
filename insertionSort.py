def insertionSort(A):
	for j in range (1,len(A)):
		temp = A[j]
		i = j - 1
		while i >= 0 and A[i] > temp:
			A[i + 1] = A[i]
			i = i - 1
		A[i + 1] = temp
	return A

myList = [5,2,4,6,1,3]
longList = [5,2,4,6,1,3,23,21,14,3]
compList = [52,23,48,68,164,3323]

print insertionSort(myList)
print insertionSort(longList)
print insertionSort(compList)