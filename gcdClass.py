class Gcd:
	def run(self, m, n):
		if(m > n):
			t = m
			m = n
			n = t
		while m > 0:
			t = n % m
			n = m
			m = t
		print n

attempt = Gcd()
attempt.run(10, 21) # Answer = 1
attempt.run(21, 10) # Answer = 1
attempt.run(6, 15) # Answer = 3
attempt.run(15, 6) # Answer = 3
attempt.run(120, 700) # Answer = 20
attempt.run(700, 120) # Answer = 20
attempt.run(9, 0) # Answer = 9
attempt.run(6, 6) # Answer = 6