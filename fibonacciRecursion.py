def fibonacci(x):
	if x == 0:
		return 0
	if x <= 2:
		return 1
	else:
		return fibonacci(x - 1) + fibonacci(x - 2)

print fibonacci(0), fibonacci(2), fibonacci(2),\
	  fibonacci(3), fibonacci(4), fibonacci(5)