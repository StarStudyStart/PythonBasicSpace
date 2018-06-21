#HanoiMethod.py
def hanoi(n,a,b,c):
	if n == 1:
		print(a+"-->"+c)
	else:
		hanoi(n-1,a,c,b)#将n-1个圆盘移动到b柱上
		hanoi(1,a,b,c)#将最后一个大圆盘移动到c柱上
		hanoi(n-1,b,a,c)#将n-1个圆盘偶从b柱移动到c柱上
hanoi(4,'A','B','C')
