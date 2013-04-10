def fibonacci2(n):
	i = 1
	j = 0
	for k in range(n):
		j = i + j
		i = j - i
	return j

print fibonacci2(5)
print fibonacci2(53)