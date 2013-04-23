class PrintPairs(object):
	def __init__(self, x):
		self.x = x

	def run(self):
		n = 0
		m = 0
		while n <= self.x:
			while m <= self.x:
				print (n, m)
				print 
				m += 1
			n += 1
			m = 0

attempt = PrintPairs(3)
attempt.run()

attempt = PrintPairs(4)
attempt.run()

attempt = PrintPairs(5)
attempt.run()