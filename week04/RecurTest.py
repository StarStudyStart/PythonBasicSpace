#RecurTest.py
def rvs(s):
	if s == "":
		return s
	else:
		return rvs(s[1:])+s[0]
print(rvs("sun"))
'''斐波那契函数'''
def pbnqlist(n):
	if n==1 or n == 2:
		return 1
	else:
	 return pbnqlist(n-1)+pbnqlist(n-2)
print(pbnqlist(5))
# 汉诺塔实现
count = 0
def hanoi(n,src,dst,mid):
	global count
	if n == 1:
		print("{}:{}-->{}".format(n,src,dst))
		count += 1
	else:
		hanoi(n-1,src,mid,dst)
		print("{}:{}-->{}".format(n,src,dst))
		count += 1
		# hanoi(1,src,dst)
		hanoi(n-1,mid,dst,src)
hanoi(3,'A','C','B')
print(count)
