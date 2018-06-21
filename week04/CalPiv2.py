#CalPiv2.py 蒙特卡罗方法求解圆周率
from random import random
from time import perf_counter
hits = 0.0
DARTS = 1000 * 1000 * 10
start = perf_counter()
for dot in range(1,DARTS+1):
	x,y = random(),random()
	dist = pow(x**2+y**2,0.5)
	if(dist < 1.0):
		hits+=1
end = perf_counter()
pi = 4*(hits/DARTS)
print("计算运周率PI为：{}".format(pi))
print("运行时间为：{:.2f}".format(end-start))
