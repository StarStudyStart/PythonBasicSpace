#MethodCal
def product(*argus):
	pro = 1
	for item in argus:
		pro = item*pro
	return pro
print(product(5,6,7))
