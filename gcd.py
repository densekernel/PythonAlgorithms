def gcd(m,n):
	print "**GCD Python Algorithm**"
	print "Input: %d, %d" % (m, n)
	while m > 0:
		t = n % m
		n = m
		m = t
		print "t :%d n: %d n: %d" % (t, n, m)
	return n

print gcd(6,15)
print gcd(120,700)
print gcd(9,0)
print gcd(10,21)