class Fibonacci:
	def run(self, n):
		i = 1
		j = 0
		for k in range(n):
			j = i + j
			i = j - i
		print j
		return j

# Test Algorithm
testObject = Fibonacci()
fibonacciList = [] #empty list to store values from our algorithm
for i in range(10):
	j = testObject.run(i)
	fibonacciList.append(j);
print fibonacciList