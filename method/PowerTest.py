#PowerTest
def power(x,n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = x*s
	return s
print(power(3))
